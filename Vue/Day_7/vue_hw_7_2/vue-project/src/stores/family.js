import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useFamilyStore = defineStore('counter', () => {
  const familyInfo = ref([
    {
      familyName: '메디치',
      father: '로도비코 데 메디치',
      mother: '마리아 살비아티',
      children: [
                  {name: '자녀1'},
                  {name: '자녀2'},
                ]
    },
    {
      familyName: '전주 이씨',
      father: '이도',
      mother: '소헌왕후',
      children: [
                  {name: '이향'},
                  {name: '이유'},
                ]
    },
  ])

  return { familyInfo }
})
