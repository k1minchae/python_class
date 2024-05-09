<template>
  <div class="quiz-card">
    <p><b>{{props.quiz.pk}}번 문제. {{ props.quiz.question }}</b></p>
    <p class="small-font">정답 입력</p>
    <input class="input-box" type="text" v-model="myAnswer" @keydown.enter.prevent="enterAnswerFunc(myAnswer, props.quiz.pk, props.quiz.answer)">
  </div>
</template>

<script setup>

import { useRouter } from 'vue-router'
const props = defineProps({
  quiz: Object
})

const router = useRouter()
const enterAnswerFunc = function(input, id, ans) {
  router.push({name: 'answer', params: {'pk':id, 'answer':ans}, query: {input}})
  myAnswer.value = ''
}

</script>

<style scoped>
.small-font {
  font-size: 13px;
}

.quiz-card {
  width: 70%;
  margin: 10px;
  border: rgb(175, 175, 175) 1px solid;
  background-color: rgb(247, 247, 247);
  
  padding-bottom: 20px;
  padding-left: 15px;
  padding-right: 15px;
  padding-top: 5px;
  border-radius: 10px;
  box-shadow: 0 1px 1px rgb(155, 155, 155);
}

.input-box {
  width: 100%; 
  height: 30px;
  border-radius: 5px;
  border: rgb(175, 175, 175) 1px solid;
}
</style>