import Vue from 'vue'
import VueRouter from 'vue-router'

import SignupView from '@/views/accounts/SignupView.vue'
import LoginView from '@/views/accounts/LoginView.vue'
import LogoutView from '@/views/accounts/LogoutView.vue'

import MovieIndexView from "@/views/movies/MovieIndexView";
import MovieDetail from "@/components/MovieDetail";


Vue.use(VueRouter)

const routes = [
  // accounts
  { path: '/accounts/signup', name: 'Signup', component: SignupView },
  { path: '/accounts/login',  name: 'Login',  component: LoginView },
  { path: '/accounts/logout', name: 'Logout', component: LogoutView },

  // movies
  { path: '/', name: 'MovieIndex', component: MovieIndexView},
  { path: '/:id?', name: 'MovieDetail', component: MovieDetail},
]


const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
