import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useProductStore = defineStore('counter', () => {
  const products = ref(
    [{
      name: '상품 1',
      imagePath: 'src/assets/product1.png',
      price: 10000,
      isFavorite: false
      },
      {
      name: '상품 2',
      imagePath: 'src/assets/product2.png',
      price: 20000,
      isFavorite: false
      },
      {
      name: '상품 3',
      imagePath: 'src/assets/product3.png',
      price: 30000,
      isFavorite: false
      },
      {
      name: '상품 4',
      imagePath: 'src/assets/product4.png',
      price: 40000,
      isFavorite: false
      },]
  )
  const favoriteFunc = function(name) {
    const index = products.value.findIndex((pro) => pro.name === name)
    products.value[index].isFavorite = !products.value[index].isFavorite
  }

  const countFavorite = computed(() => {
    return products.value.filter((pro) => pro.isFavorite).length
  })

  const carts = function() {
    return products.value.filter(pro => pro.isFavorite=== true)
  }

  return { products, favoriteFunc, countFavorite, carts }
}, {persist:true})
