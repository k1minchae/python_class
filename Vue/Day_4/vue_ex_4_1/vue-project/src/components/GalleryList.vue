<template>
  <main class="py-3 align-middle">
    <GalleryListItem />
  </main>
</template>

<script setup>
import GalleryListItem from '@/components/GalleryListItem.vue';
import {ref} from 'vue'
const numberOfitems = ref(4)
</script>

<style scoped>
main {
  margin-top: 80px;
}
</style>