<template>
  <div v-if="store.todos">
    <h1>Detail</h1>
    <p>{{ todo.id }}번 째 할일</p>
    <p>{{ todo.work }} : {{ todo.content }}</p>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";
import { useTodoStore } from "@/stores/todoStore";
import { onMounted } from "vue";

const route = useRoute();
const store = useTodoStore();
const todo = ref(null);

const getDetail = function () {
  axios({
    url: `${store.BASE_URL}/api/v1/todos/${route.params.id}`,
    method: "get",
  }).then((res) => {
    console.log(res);
    todo.value = res.data;
  });
};

onMounted(() => {
  getDetail();
});
</script>

<style scoped></style>
