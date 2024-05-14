<template>
  <main v-if="store.todos">
    <h1>할 일 목록</h1>
    <TodoList :todos="store.todos" />
  </main>
</template>

<script setup>
import { useTodoStore } from "@/stores/todoStore";
import { onMounted } from "vue";
import TodoList from "@/components/TodoList.vue";

const store = useTodoStore();
onMounted(() => {
  store.getTodos();
});
</script>

<style></style>
