import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useProductStore = defineStore('product', () => {
  let id = 0;
  const products = ref([
    // {id:++id,title: 'product1', body:'내용1'},
    // {id:++id,title: 'product2', body:'내용2'},
    // {id:++id,title: 'product3', body:'내용3'}
  ])

  const deleteProduct = function(productId) {
    // console.log(productId)
    const index = products.value.findIndex((product) => product.id === productId)
    products.value.splice(index, 1)
  }

  const productCount = computed(() => {
    return products.value.length
  })

  const fetchProducts = function () {
    axios({
      method:'get',
      url: 'https://jsonplaceholder.typicode.com/posts'
    })
    .then((response) => {
      products.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
  }


  return { products, deleteProduct, productCount, fetchProducts }
})
