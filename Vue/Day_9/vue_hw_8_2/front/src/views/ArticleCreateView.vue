<template>
  <div>
    <h1>게시글 생성 페이지</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model="title" />
      <label for="content">내용 : </label>
      <input type="text" id="content" v-model="content" />
      <input type="submit" value="create" />
    </form>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";
import { ref } from "vue";
import axios from "axios";
const title = ref(null);
const content = ref(null);
const router = useRouter();

const createArticle = function () {
  axios({
    url: "http://127.0.0.1:8000/api/v1/articles/",
    method: "post",
    data: {
      title: title.value,
      content: content.value,
    },
  }).then((res) => {
    console.log(res.data);
    router.push({ name: "home" });
  });
};
</script>

<style scoped></style>
