import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue';
import MineView from '../views/MineView.vue';
import ReleaseView from '../views/ReleaseView.vue';
import LogupView from '@/views/LogupView.vue';
import LogresetView from "@/views/LogresetView.vue";
import TaskCenterView from "@/views/TaskCenterView.vue";
import HelpView from '@/views/HelpView.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: "/login",
    name: "login",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/LoginView.vue"),
  },
  {
    path: "/logup",
    name: "logup",
    component: LogupView,
  },
  {
    path: "/logreset",
    name: "logreset",
    component: LogresetView,
  },
  {
    path: "/help",
    name: "help",
    component: HelpView,
  },
  {
    path: "/mine",
    name: "mine",
    component: MineView
  },
  {
    path: "/Release",
    name: "release",
    component: ReleaseView
  },
  {
    path: "/taskcenter",
    name: "taskcenter",
    component: TaskCenterView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
