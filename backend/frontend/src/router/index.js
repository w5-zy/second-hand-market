import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Home from '../views/Home.vue'
import Publish from '../views/Publish.vue'
import MyGoods from '../views/MyGoods.vue'

const routes = [
  {path:'/',component:Home},
  {path:'/login',component:Login},
  {path:'/publish',component:Publish},
  {path:'/mygoods',component:MyGoods}
]

const router = createRouter({
  history: createWebHistory(),
  routes
})
export default router
