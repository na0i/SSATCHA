<template>
  <div>
    {{ comment.content }}
    {{ comment.replied_by }}
    <span>
      <button @click="onClick" class="btn btn-warning"> 댓글 달기 </button>
    </span>
    <div v-if="isClicked">
      <input v-model="commentData.content" @keyup.enter="createNestedComment(commentData)">
      <button @click="createNestedComment(commentData)"> 등록 </button>
    </div>
  </div>
</template>

<script>
import {mapActions} from "vuex";
import CommentItem from

export default {
  name: "CommentItem",
  components: {
    CommentItem,
  },
  props: {
    comment: Object
  },
  data() {
    return {
      isClicked: false,
      commentData: {
        movie: '',
        review: '',
        reply_to: '',
        content: '',
      },
    }
  },
  methods: {
    ...mapActions(['createNestedComment']),
    onClick() {
      this.isClicked = !this.isClicked
    }
  },
  computed: {

  },
  mounted() {
    this.commentData.movie = this.$route.params.movie_id
    this.commentData.review = this.$route.params.review_id
    this.commentData.reply_to = this.comment.id
  },
}
</script>

<style scoped>

</style>