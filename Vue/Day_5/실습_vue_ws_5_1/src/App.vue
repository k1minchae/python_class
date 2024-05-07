<script setup>
import { ref } from 'vue';
import BusinessCard from './components/BusinessCard.vue';
import CreateCardForm from './components/CreateCardForm.vue';

const newCardInfo = ref({})
const updateCard = function(cardInfo) {
  newCardInfo.value = cardInfo
  console.log('updateCard!! / ', cardInfo)
}
</script>

<template>
  <div class="app">
    <header class="header">
      <h1>명함 관리 페이지</h1>
    </header>
    <main class="main">
      <p>명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
    </main>
    <article class="article">
      <CreateCardForm @create-card-event="updateCard"/>
      <BusinessCard :new-card-info="newCardInfo"/>
    </article>
    <footer class="footer">
      &copy; 2024 My Business Cards
    </footer>
  </div>
</template>

<style scoped>
.app {
  text-align: center;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}

.header {
  background-color: rgb(26, 118, 204);
  color: white;
  padding: 20px;
}

.main {
  
}

.article {
  flex-grow: 1
}

.footer {
  background-color: hsl(0, 0%, 94%);
  width: 100%;
  padding: 10px;
}
</style>
