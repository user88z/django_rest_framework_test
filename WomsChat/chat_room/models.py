from django.db import models
# from djoser.urls.base import User
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    # Модель комнаты чата
    creator = models.ForeignKey(User, verbose_name="Создатель", on_delete=models.CASCADE)
    invited = models.ManyToManyField(User, verbose_name="Участники", related_name='invited_user')
    date = models.DateField("Дата создания", auto_now=True)
    

    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("Room_detail", kwargs={"pk": self.pk})

class Chat(models.Model):
    room = models.ForeignKey(Room, verbose_name="Комната чата", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    text = models.TextField('Сообщение', max_length=500)
    date = models.DateField("Дата отправки", auto_now=True)
    

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("Chat_detail", kwargs={"pk": self.pk})
