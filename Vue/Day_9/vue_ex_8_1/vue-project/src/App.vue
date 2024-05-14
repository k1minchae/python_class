<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'TodoView' }">Home </RouterLink>|
      <RouterLink :to="{ name: 'DetailView', params: { id: todoId } }"
        >Detail </RouterLink
      >|
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from "vue-router";
import { ref } from "vue";
const todoId = ref(1);
</script>

<style scoped></style>
