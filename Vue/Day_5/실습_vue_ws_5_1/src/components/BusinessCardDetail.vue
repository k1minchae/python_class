<template>
  <div class="business-card">
    <b>이름 : {{ card.name }}</b>
    <br>
    <p>직함 : {{ card.title }}</p>
    <!-- 1. 전역 emit 객체 활용하기 -->
    <!-- 전역 변수는 권장사항인가 ? -->
    <!-- <button @click="$emit('deleteCardEvent')">명함 삭제</button> -->

    <!-- 2. 함수 쓰기 -->
    <button @click="deleteCardFunc(card)">명함 삭제</button>
  </div>
</template>

<script setup>
defineProps({
  card: Object
})

// 부모의 이벤트를 받아와서 사용할 수 있도록 등록하는 기능
const emit = defineEmits(['deleteCardEvent'])

const deleteCardFunc = function (card) {
  emit('deleteCardEvent', card)
  
  // 아래는 옛날 코드 방식! 이제는 안쓴다!
  // 다른 코드 참고 시 주의하시기 바랍니다.
  // this.$emit('deleteCardEvent', card)
}

</script>

<style scoped>
.business-card {
  width: 30%;
  border: 1px solid #ccc;
  background-color: #f9f9f9;
  padding: 20px;
  margin: 20px;
}
</style>