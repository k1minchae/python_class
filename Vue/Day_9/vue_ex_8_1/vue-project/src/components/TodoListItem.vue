<template>
  <div>{{ todo.id }} - {{ todo.work }} - {{ todo.content }}</div>
</template>

<script setup>
defineProps({ todo: Object });
</script>

<style scoped></style>
