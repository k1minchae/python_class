<template>
  <div class="card-container">
    <h3>{{ props.product.name }}</h3>
    <img class="image" :src="props.product.imagePath" alt="">
    <p style="margin-bottom: 0px;">\ {{ props.product.price }}</p>
    <p style="margin-bottom:40px" v-if="!props.product.isFavorite" @click="store.favoriteFunc(props.product.name)">🤍</p>
    <p style="margin-bottom:40px" v-if="props.product.isFavorite" @click="store.favoriteFunc(props.product.name)">❤️</p>
  </div>
</template>

<script setup>
import {useProductStore} from '@/stores/products'
const store = useProductStore()
const props = defineProps({
  product:Object
})

</script>

<style scoped>
  .image {
    width: 80%;
    ;
  }

  .card-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    border: 1px solid rgb(228, 228, 228);
    width: 30%;
    margin: 10px;
  }
</style>