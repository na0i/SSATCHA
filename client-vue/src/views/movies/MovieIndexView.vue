<template>
  <div>
    <h1>
    Movie Index
    </h1>

    <h1>Top Rated</h1>
    <ul>
        <li>
          <MovieListItem v-for="movie in fetchTopRated" :key="`${movie.id}`" :movie="movie"/>
        </li>
    </ul>

    <h1>Popularity</h1>
    <ul>
      <li v-for="movie in fetchPopularity" :key="`${movie.id}`">
        <MovieListItem :movie="movie"/> {{ movie.popularity }}
      </li>
    </ul>

    <h1> 한국 영화 </h1>
    <ul>
      <li v-for="movie in fetchKorean" :key="`${movie.id}`">
        <MovieListItem :movie="movie"/> {{ movie.vote_average }}
      </li>
    </ul>

    <h1> 1970-1980 년대 영화 </h1>
    <ul>
      <li v-for="movie in fetchClassic" :key="`${movie.id}`">
        <MovieListItem :movie="movie"/> {{ movie.release_date }}
      </li>
    </ul>

  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";
import MovieListItem from "@/components/MovieListItem";
// import MovieDetail from "@/components/MovieDetail";

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

</style>