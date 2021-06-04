<template>
  <div id="app">
    <nav class="nav navbar navbar-expand-lg container-fluid d-flex justify-content-between align-items-end m-2">
      <!--<div class="container-fluid d-flex justify-content-between align-items-end m-2">-->
        <div class="d-inline-flex align-items-end">

        <a class="navbar-brand ms-2 d-block" href="/">
          <img src="@/assets/LOGO_KOR.png" alt="LOGO_KOR" width="168" height="35" class="ms-1 align-self-center">
        </a>

          <div class="d-inline-block mx-5">
            <span v-if="!isLoggedIn">
              <RouterLink :to="{ name: 'Signup' }">SIGNUP</RouterLink>
            </span>
            <span v-if="!isLoggedIn" class="ms-5">
              <RouterLink :to="{ name: 'Login' }">LOGIN</RouterLink>
            </span>
            <span v-if="isLoggedIn">
              <RouterLink :to="{ name: 'Profile' }">PROFILE </RouterLink>
            </span>
            <span v-if="isLoggedIn" class="ms-5">
              <RouterLink :to="{ name: 'Logout' }">LOGOUT </RouterLink>
            </span>
          </div>
        </div>
        <div class="w-50">
          <SearchBar/>
        </div>
      <!--</div>-->
    </nav>
    <div id="wrapper">
      <RouterView/>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import SearchBar from "@/components/SearchBar"

export default {
  name: 'App',
  components: {
    SearchBar
  },
  computed: {
    ...mapGetters(['isLoggedIn', ]),
    ...mapActions(['fetchInitialDatum'])
  },
  created() {
    this.fetchInitialDatum
  }
}
</script>

<style scoped>
.nav {
  position: absolute;
  z-index: 100;
  width: 100%;
  vertical-align: middle;
}

.nav a {
  color: #b7d1eb;
  text-decoration: none;
  /*font-weight: bolder;*/
  font-size: 18px;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased; 
  /* 텍스트가 렌더링될 때 부드럽게 표현 */
  -moz-osx-font-smoothing: grayscale; 
}

</style>
