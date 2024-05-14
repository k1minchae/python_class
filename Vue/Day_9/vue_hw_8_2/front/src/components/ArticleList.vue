<template>
  <div>
    <h1>게시글 목록 페이지</h1>
    <button @click="goCreate">게시글 생성</button>
    <ArticleListItem
      v-for="(article, index) in store.articles"
      :key="article.id"
      :article="article"
      :index="index"
    />
  </div>
</template>
<script setup>
import ArticleListItem from "@/components/ArticleListItem.vue";
import { useRouter } from "vue-router";
import { useArticleStore } from "@/stores/articles";
const router = useRouter();
const store = useArticleStore();
defineProps({
  articles: Object,
});
const goCreate = function () {
  console.log("생성");
  router.push({ name: "create" });
};
</script>

<style lang="scss" scoped></style>
