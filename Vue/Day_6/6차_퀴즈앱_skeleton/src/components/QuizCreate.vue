<template>
  <div class="quiz-card">
    <h3>퀴즈 생성</h3>
    <form @submit.prevent="createQuizFunc(question, answer)">
      <label for="question">문제</label>
      <p style="margin: 3px;"></p>
      <input class="input-box" type="text" id="question" v-model="question" required style="height: 100px;">
      <p></p>
      <label for="answer">답안</label>
      <p style="margin: 3px;"></p>
      <input class="input-box" type="text" id="answer" v-model="answer" required style="height: 27px;">
      <p></p>
      <button value="submit" class="button">퀴즈 생성</button>
    </form>
  </div>
</template>

<script setup>
import {ref} from 'vue'
const question = ref('')
const answer = ref('')
const emit = defineEmits(['createQuiz'])
const createQuizFunc = function (q, a) {
  emit('createQuiz', q, a)
  question.value = ''
  answer.value=''
}
</script>

<style scoped>
.quiz-card {
  width: 60%;
  margin: 10px;
  background-color: rgb(247, 247, 247);
  padding-bottom: 20px;
  padding-left: 15px;
  padding-right: 15px;
  padding-top: 5px;
  border-radius: 10px;
  box-shadow: 0 1px 1px rgb(207, 207, 207);
}
.input-box {
  border: rgb(202, 202, 202) 1px solid;
  border-radius: 4px;
  width: 100%;
}
.button {
  border-radius: 4px;
  background-color: rgb(29, 119, 255);
  color: white;
  border: rgb(29, 119, 255) 1px solid;
  width: 100%;
  height: 40px;
  font-size: 14px;
}
</style>