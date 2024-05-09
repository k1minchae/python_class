<template>
  <header>
    <nav>
      <RouterLink :to="{name: 'home'}">Home</RouterLink>|
      <RouterLink :to="{name: 'about'}">About</RouterLink>|
      <RouterLink :to="{name: 'user', params: {username:username}}">user</RouterLink>
    </nav>
    <RouterView />
  </header>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { ref } from 'vue'
const username = ref('admin')

</script>

<style scoped>
</style>
