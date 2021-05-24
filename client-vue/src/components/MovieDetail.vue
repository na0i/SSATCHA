<template>
  <div>
    <h1> Movie Detail </h1>
    {{ this.movies.selectedMovie }}
    <div>
      구매: {{ this.movies.selectedMovieProviders.buy }}
    </div>
    <div>
     스트리밍: {{ this.movies.selectedMovieProviders.flatrate }}
    </div>
    <div>
      대여: {{ this.movies.selectedMovieProviders.rent }}
    </div>
  </div>
</template>

<script>
import {mapState} from "vuex";

export default {
  name: "MovieDetail",
  actions:{
  },
  computed: {
    ...mapState(['movies'])
  },
}
</script>

<style scoped>

</style>