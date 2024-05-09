<template>
  <div class="product-container">
    <h2>상품 목록 페이지</h2>
    <div class="card-container">
      <ProductDetail 
        v-for="product in store.products"
        :key="product.name"
        :product="product"
      />
    </div>
  </div>
</template>

<script setup>
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