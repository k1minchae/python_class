<template>
  <div v-if="postId >= 0">
    <p>번호 : {{ $route.params.id }}</p>
    <p>제목 : {{ filteredPosts($route.params.id)[0].title }}</p>
    <p>내용 : {{ filteredPosts($route.params.id)[0].content }}</p>
  </div>
</template>

<script setup>
import { useRoute, onBeforeRouteUpdate } from 'vue-router';
import {ref, computed} from 'vue'
const props = defineProps({
  posts: Object
})
const route = useRoute()
const postId = ref(route.params.id)
onBeforeRouteUpdate((to, from) => {
  postId.value = to.params.id
})

const filteredPosts = function (pid) {
  console.log(pid)
  return props.posts.filter(post => post.id == pid)
}

</script>

<style scoped>

</style>