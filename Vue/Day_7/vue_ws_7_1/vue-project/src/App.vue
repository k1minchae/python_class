<template>
  <div>
    <nav class="nav">
      <RouterLink class="link" :to="{name:'home'}">Home&nbsp;</RouterLink> | 
      <RouterLink class="link" :to="{name:'products'}">&nbsp;Products&nbsp; </RouterLink> | 
      <RouterLink class="link" :to="{name:'favorite'}">&nbsp;Favorite&nbsp;</RouterLink> 
      <button class="button" v-if="store.countFavorite">{{ store.countFavorite }}</button>
    </nav>
    <RouterView />
  </div>
</template>

<script setup>
import {useProductStore} from '@/stores/products';
const store = useProductStore()

</script>

<style scoped>
  .nav {
    background-color: rgb(61, 61, 61);
    height: 45px;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .link {
    text-decoration: none;
    color: white
  }

  .button {
    background-color: red;
    border: 1px solid red;
    color: white;
    border-radius: 50%;
  }
</style>
