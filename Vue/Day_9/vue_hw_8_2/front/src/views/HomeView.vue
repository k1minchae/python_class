<template>
  <div>
    <ArticleList :articles="store.articles" />
  </div>
</template>

<script setup>
import ArticleList from "../components/ArticleList.vue";
import { useArticleStore } from "@/stores/articles";
const store = useArticleStore();
import { onMounted } from "vue";
onMounted(() => {
  store.getArticles();
});
</script>

<style lang="scss" scoped></style>
