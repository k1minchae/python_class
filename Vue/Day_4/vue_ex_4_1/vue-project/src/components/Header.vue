<template>
  <header class="fixed-top bg-success-subtle">
    <h1 class="fw-semibold">{{title}}</h1>
  </header>
</template>

<script setup>
import {ref} from 'vue'
const title = ref('My Gallery')
</script>

<style scoped>
header {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 70px;
}
</style>