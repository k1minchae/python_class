<template>
  <div class="albumCard">
    <h3>앨범 제목</h3>
    <p class="singlistText">노래 목록1</p>
    <p class="singlistText">노래 목록2</p>
    <p class="singlistText">노래 목록3</p>
  </div>
</template>

<script setup>

</script>

<style scoped>
.albumCard {
  border: 1px solid rgb(190, 190, 190);
  border-radius: 10%;
  width: 40%;
  background-color: rgb(240, 240, 240);
  margin-bottom: 20px;
  box-shadow: 5px 5px 5px rgb(185, 185, 185);
}

.singlistText {
  color: orangered;
}
</style>