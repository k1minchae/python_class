import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useBalanceStore = defineStore('counter', () => {
  const balances = ref([
    {
      name: '김하나',
      balances: 100000
    }, 
    {
      name: '김두리',
      balances: 10000
    }, 
    {
      name: '김서이',
      balances: 100
    }, 
  ])

  const returnBalance = computed(() => (name) => {
    const account = balances.value.find(acc => acc.name === name)
    return account ? account.balances : '존재하지 않는 이름입니다.'
  })

  const moreBalance = function(name) {
    const index = balances.value.findIndex((acc) => acc.name === name)
    balances.value[index].balances += 1000;
    console.log(balances.value[index].balances)
  }

  return { balances, returnBalance, moreBalance }
})
