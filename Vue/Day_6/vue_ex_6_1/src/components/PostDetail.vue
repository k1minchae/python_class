<template>
  <div v-if="postId >= 0">
    <p>번호 : {{ postId }}</p>
    <p>{{ filteredPosts }}</p>
  </div>
</template>

<script setup>
import { useRoute, onBeforeRouteUpdate } from 'vue-router';
import {ref, computed} from 'vue'
const props = defineProps({
  posts: Array
})
const route = useRoute()
const postId = ref(route.params.id)
onBeforeRouteUpdate((to, from) => {
  postId.value = to.params.id
})

const filteredPosts = props.posts.filter(post => post.id === postId)
</script>

<style scoped>

</style>