<template>
  <div>

    <div @click="setMovieDetail(movie)">
      <RouterLink :to="`/${movie.id}`">
        {{ movie.title }} // {{ movie.vote_average }}
      </RouterLink>
    </div>
  </div>

  <!--<div @click="[setMovieDetail(movie), onClick()]">-->
  <!--  <img src="" alt="">-->
  <!--  {{ movie.title }} // {{ movie.vote_average }}-->
  <!--</div>-->
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: "MovieListItem",
  props: {
    movie: Object
  },
  methods: {
    ...mapActions(['setMovieDetail']),
    onClick() {
      this.$router.push(`/${this.movie.id}`)
    }
  }
}
</script>

<style scoped>

</style>