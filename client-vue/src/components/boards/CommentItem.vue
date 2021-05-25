<template>
  <div>
    {{ comment.content }}
    <span>
      <button @click="onClick" class="btn btn-warning"> 댓글 달기 </button>
    </span>
    <div v-if="isClicked">
      <input v-model="commentData.content" @keyup.enter="[createNestedComment(commentData), onSubmit()]">
      <button @click="[createNestedComment(commentData), onSubmit()]"> 등록 </button>
    </div>
  <div v-if="!!comment.replied_by.length" class="ms-5">
    <li v-for="(comment, idx) in comment.replied_by" :key="idx">
      <CommentItem :comment="comment"/>
    </li>
  </div>

  </div>
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: "CommentItem",
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
    },
    onSubmit() {
      this.isClicked = false
      this.commentData.content = ''
    }
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