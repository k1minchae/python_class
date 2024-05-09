<template>
  <div class="card-container">
    <div class="card-body">
      <p style="margin:0px">{{ $route.params.pk }}번 문제</p>
      <p class="answer"><b>정답 확인</b></p>
      <div>
        <p v-if="$route.query.input !== $route.params.answer">오답입니다.</p>
        <p v-if="$route.query.input === $route.params.answer">정답입니다.</p>
        <p>나의 제출 답안 : {{ $route.query.input }}</p>
        <p>정답 : {{ $route.params.answer }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>
.card-container {
  margin: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.answer {
  font-size: 20px;
  margin-top: 3px;
  text-align: center;
}
.card-body {
  border: 1px lightgray solid;
  width: 60%;
  padding: 20px;
}
</style>