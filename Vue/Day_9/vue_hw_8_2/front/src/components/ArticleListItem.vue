<template>
  <div>
    <h2>{{ index + 1 }}번 게시글</h2>
    <p>제목: {{ article.title }}</p>
    <p>내용: {{ article.content }}</p>
  </div>
</template>

<script setup>
defineProps({
  article: Object,
  index: Number,
});
</script>

<style scoped></style>
