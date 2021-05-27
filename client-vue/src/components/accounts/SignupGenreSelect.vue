<template>
  <div>
    <div v-for="(genre, idx) in this.$store.state.movies.genreList" :key="idx">
      <input type="checkbox" v-model="likeGenres" :value="genre" @click="onChange(genre)"> {{ genre.name }}
    </div>
    {{likeGenres}}
  </div>

</template>

<script>
export default {
  name: "SignupGenreSelect",
  data() {
    return {
      likeGenres: [],
    }
  },
  methods: {
    // 아 진짜 이거 하나 만드는데 1시간반...
    onChange(justAdded) {
      let idx = this.likeGenres.indexOf(justAdded)
      let changed
      if (idx !== -1) {
        changed = this.likeGenres.splice(idx, 1)
      } else {
        changed = [...this.likeGenres, justAdded]
      }
      this.$emit('like-genres', changed)
    }
  },
  computed: {
  },
  // watch: {
  //   changed: function() {
  //     console.log('here')
  //     const handler = () => {console.log(this.likeGenres); return this.likeGenres}
  //     // 왜 여기서도 한개를 덜 잡아오죵...
  //     console.log('---', handler())
  //     console.log('changed')
  //     this.$emit('like-genre')}
  // }
}
</script>

<style scoped>

</style>