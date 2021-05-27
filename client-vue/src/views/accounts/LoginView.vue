<template>
  <div class="login container-fluid">
    <div class="row no-gutter">
        <!-- The image half -->
        <div class="col-md-6 d-none d-md-flex bg-image"></div>
          <!-- The content half -->
          <div class="col-md-6 bg-light">
              <div class="login d-flex align-items-center py-5">
                  <!-- Demo content-->
                  <div class="container">
                      <div class="row">
                          <div class="col-lg-10 col-xl-7 mx-auto">
                              <h4 class="display-4 fw-bold">SSATCHA</h4>
                              <h5 class="text-muted mb-4">LOGIN</h5>
                              <form class="accounts-form">
                                <div class="form-group mb-3">
                                    <input id="username" type="text" v-model="loginData.username" placeholder="username" required="" class="form-control rounded-pill border-0 shadow-sm px-4 text-primary">
                                </div>
                                <div class="form-group mb-3">
                                    <input id="password1" type="password" v-model="loginData.password1" placeholder="password" required="" class="form-control rounded-pill border-0 shadow-sm px-4 text-primary">
                                </div>
                                <div class="button-set">
                                  <SignupGenreSelect @like-genres="onSelect"/>
                                </div>
                                <button type="submit" @click="login(loginData)" class="btn btn-primary btn-block text-uppercase mb-2 rounded-pill shadow-sm">SIGN UP</button>
                              </form>
                          </div>
                      </div>
                  </div><!-- End -->
              </div>
          </div><!-- End -->
        </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'LoginView',
  data() {
    return {
      loginData: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    ...mapActions(['login'])
  }
}
</script>

<style scoped>
.bg-image {
  height: 100vh;
  background-image: url("../../assets/accounts_bg.jpg");
  background-size: cover;
  background-position: center;
}

.login {
  font-family: 'Noto Sans KR', sans-serif;
}
</style>
