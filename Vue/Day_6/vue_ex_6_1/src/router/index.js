import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import AboutView from '@/views/AboutView.vue'
import UserView from '@/views/UserView.vue'
import Profile from '@/components/Profile.vue'
import PostList from '@/components/PostList.vue'
import PostDetail from '@/components/PostDetail.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView
    },
    {
      path: '/user/:username',
      name: 'user',
      component: UserView,
      beforeEnter: (to, from) => {
        const username = to.params.username
        if (username !== 'admin') {
          alert("잘못된 유저입니다.")
          return {name: 'home'}
        }
        console.log("진입성공")
      },
      children: [
        {
          path: 'profile',
          name: 'user-profile',
          component: Profile,
        },
        {
          path: 'posts',
          name: 'user-posts',
          component: PostList,
          children: [
            {
              path: ':id',
              name: 'post-detail',
              component: PostDetail,
            }
          ]
        }
      ]
    }
  ]
})

export default router
