import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue';
import MineView from '../views/MineView.vue';
import ReleaseView from '../views/ReleaseView.vue';
import LogupView from '@/views/LogupView.vue';
import LogresetView from "@/views/LogresetView.vue";
import TaskCenterView from "@/views/TaskCenterView.vue";

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
    //元数据
    meta:{
        // 必须登录才可以查看
        requireAuth: true
    },
    path: "/mine",
    name: "mine",
    component: MineView
  },
  {
    meta:{
      // 必须登录才可以查看
      requireAuth: true
    },
    path: "/Release",
    name: "release",
    component: ReleaseView
  },
  {
    meta:{
      // 必须登录才可以查看
      requireAuth: true
  },
    path: "/taskcenter",
    name: "taskcenter",
    component: TaskCenterView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// 登录之后才能访问
router.beforeEach((to, from, next) => {
  //to:即将要进入的目标路由对象； 
  //2、from:当前导航即将要离开的路由对象； 
  //3、next ：调用该方法后，才能进入下一个钩子函数(afterEach)。 next()
  //直接进to 所指路由 next(false) 
  //中断当前路由 next('route') 
  //跳转指定路由 next('error') 
  if (to.meta.requireAuth) { // 判断该路由是否需要登录权限
    if (sessionStorage.getItem("token") == 'true') { // 判断本地是否存在token
      next()
    } else {
      // 未登录,跳转到登陆页面
      next({
        path: '/login'
      })
    }
  } else {
    next();
  }
});

export default router
