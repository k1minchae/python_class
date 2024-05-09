<template>
  <div>
    <li><RouterLink :to="{name:'post-detail', params: {'id': props.post.id}}">제목 : {{ props.post.title }}</RouterLink></li>  
  </div>
  
</template>

<script setup>
const props = defineProps({
  post : Object
})
</script>

<style scoped>

</style>