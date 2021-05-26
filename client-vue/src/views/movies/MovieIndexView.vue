<template>
  <div id="bg-color">
    <div class="container">
      <p id="semititle" class="fw-bolder pt-1">TOP RATED</p>
      <div>
        <li class="row row-cols-6">
          <MovieListItem v-for="movie in fetchTopRated" :key="`${movie.id}`" :movie="movie"/>
        </li>
      </div>
    
      <p id="semititle" class="fw-bolder mt-5">POPULARITY</p>
      <div>
        <li class="row row-cols-6">
          <MovieListItem v-for="movie in fetchPopularity" :key="`${movie.id}`" :movie="movie"/>
          <!-- {{ movie.popularity }}  -->
        </li>
      </div>

      <p id="semititle" class="fw-bolder mt-5">KOREAN MOVIES</p>
      <div>
        <li class="row row-cols-6">
          <MovieListItem v-for="movie in fetchKorean" :key="`${movie.id}`" :movie="movie"/>
          <!-- {{ movie.vote_average }} -->
        </li>
      </div>

      <p id="semititle" class="fw-bolder mt-5">1970-80 MOVIES</p>
      <div>
        <li class="row row-cols-6">
          <MovieListItem v-for="movie in fetchClassic" :key="`${movie.id}`" :movie="movie"/>
          <!-- {{ movie.release_date }} -->
        </li>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";
import MovieListItem from "@/components/MovieListItem";

export default {
  name: "MovieIndex",
  components: {
    MovieListItem,
  },
  data() {
    return {
      movieId: '',
    }
  },
  methods: {
    ...mapActions(['fetchMovies']),
    onClick() {
      this.$router.push(`/${this.movieId}`)
    }
  },

  computed: {
    ...mapGetters(['fetchTopRated', 'fetchPopularity', 'fetchKorean', 'fetchClassic'])
  },
  created() {
    this.fetchMovies()
  }
}
</script>

<style scoped>
#title {
  /* font-family: Noto Sans KR, sans-serif; */
  font-size: 30px;
  color: #b7d1eb;
}

#semititle {
  /* font-family: Noto Sans KR, sans-serif; */
  font-size: 22px;
  color: white;
  text-align: left;
}

#bg-color {
  background-color: black;
}

.flux {
  font-family: neon;
  color: #3396f4;
  text-shadow: 0 0 0vw #07143f;
}

.flux {
  animation: flux 2s linear infinite;
  -moz-animation: flux 2s linear infinite;
  -webkit-animation: flux 2s linear infinite;
  -o-animation: flux 2s linear infinite;
}

@keyframes flux {
  0%,
  100% {
    text-shadow: 0 0 1vw #3396f4, 0 0 3vw #3396f4, 0 0 10vw #3396f4, 0 0 10vw #3396f4, 0 0 .4vw #242d35, .5vw .5vw .1vw #0d151d;
    color: #28D7FE;
  }
  50% {
    text-shadow: 0 0 .5vw #082180, 0 0 1.5vw #082180, 0 0 5vw #082180, 0 0 5vw #082180, 0 0 .2vw #082180, .5vw .5vw .1vw #0A3940;
    color: #146C80;
  }
}
</style>