<template>
  <div>
    <h1>
    Movie Index
    </h1>
    <ul v-for="(movie, idx) in movies" :key="idx">
      <li>
        {{ movie }}
      </li>
    </ul>


  </div>
</template>

<script>

import {mapActions, mapState} from "vuex";

export default {
  name: "MovieIndex",
  methods: {
    ...mapActions(['fetchMovies'])
  },
  computed: {
    ...mapState(['movies'])
  },
  created() {
    this.fetchMovies()
  }
}
</script>

<style scoped>

</style>