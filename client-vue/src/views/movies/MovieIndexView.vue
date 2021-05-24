<template>
  <div>
    <h1>
    Movie Index
    </h1>

    <h1>Top Rated</h1>
    <ul>
      <li v-for="movie in fetchTopRated" :key="`${movie.id}`">
        <img src="" alt="">
        {{ movie.title }} // {{ movie.vote_average }}
      </li>
    </ul>

    <h1>Popularity</h1>
    <ul>
      <li v-for="movie in fetchPopularity" :key="`${movie.id}`">
        <img src="" alt="">
        {{ movie.title }} // {{ movie.popularity }}
      </li>
    </ul>

    <h1> 한국 영화 </h1>
    <ul>
      <li v-for="movie in fetchKorean" :key="`${movie.id}`">
        <img src="" alt="">
        {{ movie.title }} // {{ movie.vote_average }}
      </li>
    </ul>

    <h1> 1970-1980 년대 영화 </h1>
    <ul>
      <li v-for="movie in fetchClassic" :key="`${movie.id}`">
        <img src="" alt="">
        {{ movie.title }} // {{ movie.release_date }}
      </li>
    </ul>

  </div>
</template>

<script>

import {mapActions, mapGetters} from "vuex";

export default {
  name: "MovieIndex",

  methods: {
    ...mapActions(['fetchMovies'])
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