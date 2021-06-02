import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"

import VueCookies from 'vue-cookies'
import ajax from 'vuejs-ajax'

Vue.config.productionTip = false

// vue-cookies
Vue.use(VueCookies)
Vue.use(ajax)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
