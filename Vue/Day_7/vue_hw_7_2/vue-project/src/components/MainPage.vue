<template>
  <div>
    <h1>Pinia 연습하기</h1>
    <ParentPage 
      v-for="family in store.familyInfo"
      :family="family"
    />
  </div>
</template>

<script setup>
import ParentPage from '@/components/ParentPage.vue';
import {useFamilyStore} from '@/stores/family';
const store = useFamilyStore()
</script>

<style scoped>

</style>