import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '/src/views/HomeView.vue';
import QuizView from '@/views/QuizView.vue';
import AnswerView from '@/views/AnswerView.vue';


const router = createRouter({
  // 해시모드
  // 히스토리모드 : 슬래시로 구분하는
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/quiz',
      name: 'quiz',
      component: QuizView,
    },
    {
      path: '/answer/:pk/:answer',
      name: 'answer',
      component: AnswerView,
    },
  ]
})

export default router
