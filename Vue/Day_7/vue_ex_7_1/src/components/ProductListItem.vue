<template>
  <div>
    <li>
      <span>
        {{ props.product.id }} - {{ props.product.title }} - {{ props.product.body }}
      </span>
      <button @click="store.deleteProduct(props.product.id)">Delete</button>
    </li>
  </div>
</template>

<script setup>
import { useProductStore } from '@/stores/product';
const store = useProductStore()
const props = defineProps({
  product: Object
})
</script>

<style scope>

</style>