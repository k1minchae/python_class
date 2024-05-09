<template>
  <div>
    <h1>User Profile</h1>
    <p>Username : {{ $route.params.username }}</p>
    <RouterLink :to="{name: 'user-profile'}">상세 프로필</RouterLink>|
    <RouterLink :to="{name: 'user-posts'}">작성한 게시글</RouterLink>
  </div>
  <hr>
  <RouterView />
</template>

<script setup>

</script>

<style scoped>

</style>