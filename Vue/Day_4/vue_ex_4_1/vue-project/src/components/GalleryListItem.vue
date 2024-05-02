<template>
<div class="container">
    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
    <div v-for="_ in numberOfitems">
        <div class="card" >
          <img src="@/assets/sample.png" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
            <GalleryListItemButton />
            </div>
          </div>
        </div>

    </div>
  </div>
</template>

<script setup>
import {ref} from 'vue'
const numberOfitems = 4;
import GalleryListItemButton from '@/components/GalleryListItemButton.vue';
</script>

<style scoped>

</style>