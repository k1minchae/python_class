<template>
  <div class="mainContainer">
    <h1>가수 정보 페이지에 오신 것을 환영합니다</h1>
    <p>여러분이 좋아하는 가수와 아티스트에 대한 정보를 탐색해보세요.</p>
    <img style="width: 200px;" src="@/assets/microphone.jpg" alt="">
    <SingerList />
  </div>
</template>

<script setup>
import SingerList from '@/components/SingerList.vue';
</script>

<style scoped>
.mainContainer {
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}
</style>