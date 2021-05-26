<template>
  <div class="main-container">
    <div class="movie-list">
      <div class="movie-card mb-5 ms-1 me-1" @click="setMovieDetail(movie)">
        <RouterLink :to="`/${movie.id}`" class="card-text movietitle">
          <img :src="fullpath" alt="movieposter"/>
          <div class="desc movietitle">
            {{ movie.title }}
            <p class="card-text movietitle">{{ movie.vote_average }}</p>
          </div>
        </RouterLink>
      </div>
    </div>
  </div>  
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: "MovieListItem",
  props: {
    movie: Object
  },
  computed: {
    fullpath(){
      return "https://image.tmdb.org/t/p/original/" + this.movie.poster_path
    }
  },
  methods: {
    ...mapActions(['setMovieDetail']),
    onClick() {
      this.$router.push(`/${this.movie.id}`)
    }
  },
}
</script>

<style scoped>
#bg-color {
  background-color: black;
}

/* font css 시작 */
@font-face {
  font-family: 'Noto Sans KR', sans-serif;
  src: url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@700&display=swap')
}

.movietitle {
  font-family: Noto Sans KR, sans-serif;
  font-size: 12px;
  color: #b7d1eb;
  text-decoration: none;
  text-align: left;
}
/* font css 끝 */

/* card css 시작 */
#card-bg {
  background-color: #b2d7fa;
}

* {
  box-sizing: border-box;
}

.main-container {
  background-color: black;
}

.movie-list {
  flex-wrap: nowrap;
  justify-content: center;
}

.movie-card {
  border-radius: 3px;
  box-shadow: -1px 1px 8px #111111, 1px -1px 8px #111111;
  transition-duration: 300ms;
  height: 200px;
}

.movie-card img {
  transition-duration: 300ms;
  border-radius: 3px 3px 0 0;
  width: 100%;
  height: 100%;
}
/* .movie-card .desc {
  padding: 0 1rem;
} */
/* card text에 padding 생김 */

.movie-card:hover {
  background-color: #363636;
  box-shadow: -1px 1px 10px 1px #363636, 1px -1px 10px 1px #363636;
}
.movie-card:hover img {
  filter: brightness(50%);
}
/* card css 끝 */
</style>