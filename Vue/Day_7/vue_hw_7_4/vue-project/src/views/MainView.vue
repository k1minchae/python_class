<template>
  <div>
    <h1>메인 페이지</h1>
    <div v-for="balance in store.balances">
      <p>이름 : {{ balance.name }}</p>
      <p>잔고 : {{ balance.balances }}</p>
      <button>
        <RouterLink :to="{name:'update', params:{name:balance.name}}">
          updateBalance
        </RouterLink>
      </button>
      <hr>
    </div>
  </div>
</template>

<script setup>
import {useBalanceStore} from '@/stores/balance'
const store = useBalanceStore()

</script>

<style scoped>

</style>