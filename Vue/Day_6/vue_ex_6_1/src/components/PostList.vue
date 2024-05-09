<template>
  <div>
    <h3> {{ $route.params.username }} 이 작성한 게시글</h3>
    <PostListItem 
      v-for="post in posts"
      :key="post.id"
      :post="post"
    />
    <hr>
    <PostDetail 
      :posts="posts"
    />
  </div>
  
</template>

<script setup>
import { ref } from 'vue'
import PostListItem from '@/components/PostListItem.vue';
import PostDetail from '@/components/PostDetail.vue';
const posts = ref([
  {id: 1, title: 'post1', content: 'content1'},
  {id: 2, title: 'post2', content: 'content2'},
  {id: 3, title: 'post3', content: 'content3'},
])
</script>

<style scoped>

</style>