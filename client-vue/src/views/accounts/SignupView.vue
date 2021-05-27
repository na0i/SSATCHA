<template>
  <div>
    <h1>Signup</h1>
    <div>
      <label for="username">username:</label>
      <input v-model="signupData.username" id="username" type="text" />
    </div>
    <div>
      <label for="password1">password:</label>
      <input v-model="signupData.password1" id="password1" type="password" />
    </div>
    <div>
      <label for="password2">password:</label>
      <input v-model="signupData.password2" id="password2" type="password" />
    </div>
    <div>
      <label for="email">email:</label>
      <input v-model="signupData.email" id="email" type="text" />
    </div>
    <div>
      <label for="nickname">nickname:</label>
      <input v-model="signupData.nickname" id="nickname" type="text" />
    </div>
    <br>
      <SignupGenreSelect @like-genres="onSelect"/>
    <br>
    <div>
      <button @click="signup(signupData)">Signup</button>
    </div>
  </div>
</template>

<script>
import {mapActions, mapState} from 'vuex'
import SignupGenreSelect from "@/components/accounts/SignupGenreSelect";

export default {
  name: 'SignupView',
  components: {
    SignupGenreSelect
  },
  data() {
    return {
      signupData: {
        username: '',
        password1: '',
        password2: '',
        email: '',
        nickname: '',
        like_genres: [],
      }
    }
  },
  methods: {
    ...mapActions(['signup']),
    ...mapState({genreList: state => state.movies.genreList}), // ?? 왜 안대?
    onSelect(likeGenres) {
      this.signupData.like_genres = likeGenres
    }
  }
}
</script>

<style>

</style>