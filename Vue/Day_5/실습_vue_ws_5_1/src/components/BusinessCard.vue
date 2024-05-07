<template>
  <div>
    <h2>보유 명함 목록</h2>
    <div v-if="cardLength">
      <p>현재 보유중인 명함 수 : {{ cardLength }}</p>
      <div class="card-container">
        <BusinessCardDetail 
          v-for="businessCard in businessCards"
          :key="businessCard.id"
          :card="businessCard"
          @delete-card-event="deleteCard"
        />
      </div>
    </div>
    <p v-else>명함이 없습니다. 새로운 명함을 추가해주세요.</p>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import BusinessCardDetail from './BusinessCardDetail.vue';

const businessCards = ref([
  { id: 1, name: '일론 머스크', title: '테슬라 테크노킹'},
  { id: 2, name: '래리 엘리슨', title: '오라클 창업주'},
  { id: 3, name: '빌 게이츠', title: 'MS 공동창업주'},
  { id: 4, name: '래리 페이지', title: '구글 공동창업주'},
  { id: 5, name: '세르게이 브린', title: '구글 공동창업주'},
])

const props = defineProps({
  newCardInfo: Object
})


const deleteCard = function (card) {
  // console.log('businesscard 에서 호출!')
  // console.log('card = ', card)
  const findIdx = businessCards.value.findIndex(el => el.id === card.id)
  businessCards.value.splice(findIdx, 1)
}


// 왜 computed 를 썼을까 ?
// 캐시 기능 때문에 단순 계산은 제일 효율적
const cardLength = computed(() => {
  return businessCards.value.length
})

// watch ??
// 특정 변수의 변화에 따라 다른 변수를 수정하는 등 사이드 이펙트가 있을 때
watch(() => props.newCardInfo, (newCard) => {
  businessCards.value.push(newCard)
})

</script>

<style scoped>
.card-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
</style>