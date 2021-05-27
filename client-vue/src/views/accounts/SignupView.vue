<template>
  <div class="container-fluid">
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
                            <p class="text-muted mb-4">CREATE ACCOUNT</p>
                            <form>
                                <div class="form-group mb-3">
                                    <input id="username" type="text" v-model="signupData.username" placeholder="USERNAME" required="" class="form-control rounded-pill border-0 shadow-sm px-4 text-primary">
                                </div>
                                <div class="form-group mb-3">
                                    <input id="inputEmail" type="email" placeholder="EMAIL" required="" autofocus="" class="form-control rounded-pill border-0 shadow-sm px-4">
                                </div>
                                <div class="form-group mb-3">
                                    <input id="password1" type="password" v-model="signupData.password1" placeholder="PASSWORD" required="" class="form-control rounded-pill border-0 shadow-sm px-4 text-primary">
                                </div>
                                <div class="form-group mb-3">
                                    <input id="password2" type="password" v-model="signupData.password2" placeholder="PASSWORD2" required="" class="form-control rounded-pill border-0 shadow-sm px-4 text-primary">
                                </div>
                                <button type="submit" @click="signup(signupData)" class="btn btn-primary btn-block text-uppercase mb-2 rounded-pill shadow-sm">SIGN UP</button>
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
  name: 'SignupView',
  data() {
    return {
      signupData: {
        username: null,
        password1: null,
        password2: null,
      }
    }
  },
  methods: {
    ...mapActions(['signup'])
  }
}
</script>

<style scoped>
.signup-ft {
  color: white;
  font-size: 23px;
}

.img-box {
  max-width: 100%;
}

.login,
.image {
  min-height: 100vh;
}

.bg-image {
  background-image: url('../assets/accounts_bg.jpg');
  background-size: cover;
  background-position: center;
}

</style>