<template>
  <div>
    <card class="card">
    <div class="detail">
      <h1>가수 이름</h1>
      <img style="width: 200px; border-radius: 50%;" src="@/assets/singer.jpg" alt="">
      <p>가수 소개글</p>
      <SingerAlbum />
    </div>
  </card>
  </div>
</template>

<script setup>

  import SingerAlbum from '@/components/singers/SingerAlbum.vue'
</script>

<style scoped>
.detail {
  border: 1px solid black;
  margin: 30px;
  width: 100%;
  display: flex;
  
  flex-direction: column;
  align-items: center;
}
.card {
  display: flex;
  width: 30rem;
  margin: 20px;
}

</style>