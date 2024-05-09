<template>
  <div class="product-container">
    <h2>장바구니 페이지</h2>
    <div class="card-container">
      <ProductDetail 
        v-for="product in store.carts()"
        :key="product.name"
        :product="product"
      />
    </div>
  </div>
</template>

<script setup>
import ProductView from '@/views/ProductView.vue'
import ProductDetail from '@/components/ProductDetail.vue';
import {useProductStore} from '@/stores/products';
const store = useProductStore()
</script>

<style scoped>
  .product-container {
    margin: 40px;
  }

  .card-container {
    display: flex;
    flex-wrap: wrap;
  }
</style>