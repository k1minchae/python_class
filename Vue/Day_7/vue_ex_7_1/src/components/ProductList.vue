<template>
  <div>
    <h1>ProductList</h1>
    <ProductListItem
      v-for="product in store.products"
      :key="product.id"
      :product="product"
    />
  </div>
</template>
<script setup>
import ProductListItem from '@/components/ProductListItem.vue'
import { useProductStore } from '@/stores/product';
const store = useProductStore()
// 1. 그냥 setup 에 넣어주기
store.fetchProducts()
</script>
<style scoped>
</style>