import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    }
  ]
})

// import Login from '@/components/Login'
//,
    // {
    //   path: '/login',
    //   name: 'login',
    //   component: Login
    // }