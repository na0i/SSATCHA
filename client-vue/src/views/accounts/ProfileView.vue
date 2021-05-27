<template>
  <div>
    <h1>Profile</h1>

    <div v-if="isLoggedIn" class="profile">
      로그인 ok
        <h3>여기는 이제 프로필 다 만들었을 때 보이는 화면</h3>
        -> 닉네임이랑, 좋아요 누른 리뷰, 좋아요 누른 영화 목록 보여주고,
        -> 그거에 기반한 추천 대충 몇가지..
      <br>
      닉네임: {{ loginUser.nickname }}
      <br>
      username: {{ loginUser.username}}
      <hr>
      작성한 리뷰: {{ loginUser.my_reviews }}
      <hr>
      좋아한 영화 : {{ loginUser.like_movies }}
      <hr>
      좋아한 리뷰 : {{ loginUser.like_reviews }}
      <hr>
      <div class="container" >
      <h2 id="semititle" class="fw-bolder m-3">{{ loginUser.nickname }} 님이 좋아하실만한 영화를 추천해드려요!</h2>
        <li class="row row-cols-6">
          <MovieListItem v-for="movie in recByUser" :key="movie.id" :movie="movie"/>
        </li>
      </div>
    </div>


    <div v-else>
      로그인 안 함
    </div>


  </div>
</template>

<script>
import {mapActions, mapGetters, mapState} from 'vuex'
import MovieListItem from "@/components/movies/MovieListItem";

export default {
  name: 'ProfileView',
  components: {
    MovieListItem
  },
  methods: {
    ...mapActions(['profileSetting'])
  },
  computed: {
    ...mapGetters(['isLoggedIn', ]),
    ...mapState({
      loginUser: state => state.accounts.loginUser,
      recByUser: state => state.accounts.recByUser,
    })
  },
  created() {
    // 그냥 가지고만 있으면, 프로필 들어올 때마다 처음 받아본 데이터만 가지고 있네요
    // 매번 업데이트 해주겠습니다.
    this.profileSetting()
    // this.getLoginUser()
  }
}
</script>

<style scoped>
#semititle {
  /* font-family: Noto Sans KR, sans-serif; */
  font-size: 22px;
  color: white;
  text-align: left;
}

.profile {
  position: relative;
  z-index: 99;
}
</style>