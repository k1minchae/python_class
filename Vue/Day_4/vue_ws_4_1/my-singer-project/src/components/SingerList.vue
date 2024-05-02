<template>
  <h1>가수 목록</h1>
  <div style="display: flex; align-content: center; flex-wrap: wrap; justify-content: center;">
    <SingerDetail v-for="_ in singers"/>
  </div>
  
</template>

<script setup>
import SingerDetail from '@/components/SingerDetail.vue';
import { ref } from 'vue'
const singers = ref([
  {name: 'adele'},
  {name: 'marron 5'},
  {name: 'Dua Lipa'}
])
</script>

<style scoped>
h1 {
  color: red;
}


</style>