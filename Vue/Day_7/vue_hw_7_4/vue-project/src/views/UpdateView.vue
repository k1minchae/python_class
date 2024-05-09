<template>
  <div>
    <h1>데이터 수정 페이지</h1>
    <p>이름 : {{ $route.params.name }}</p>
    <p>잔고 : {{ getBalance($route.params.name) }}</p>
    <button @click="store.moreBalance($route.params.name)">증가</button>
  </div>
</template>

<script setup>
import {ref} from 'vue'
import {useBalanceStore} from '@/stores/balance'
const store = useBalanceStore()
// import {useRoute} from 'vue-router'
// const route = useRoute()
// const userName = ref(route.params.name)

const getBalance = function (name) {
  return store.returnBalance(name)
}
</script>

<style scoped>

</style>