<template>
  <div>
    <form>
      <label for="name">이름</label>
      <input type="text" id="name" v-model="name">
      <label for="name">직함</label>
      <input type="text" id="name" v-model="title">
      <button @click.prevent="createCardFunc">명함 추가</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
const name = ref('')
const title = ref('')

const emit = defineEmits(['createCardEvent'])

const createCardFunc = function() {
  const cardInfo = {
    id: Date.now(),
    name: name.value,
    title: title.value
  }
  
  emit('createCardEvent', cardInfo)
  name.value = ''
  title.value = ''
}
</script>

<style scoped>

</style>