import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import MineView from "../views/MineView.vue";
import ReleaseView from "../views/ReleaseView.vue";
import PerformView from "../views/PerformView.vue";
import LogupView from "@/views/LogupView.vue";
import LogresetView from "@/views/LogresetView.vue";
import TaskCenterView from "@/views/TaskCenterView.vue";
import HelpView from "@/views/HelpView.vue";
import TaskDetailView from '@/views/TaskDetailView.vue';
import AdminView from "@/views/AdminView.vue";
import FeedbackManagerView from "@/views/FeedbackManagerView.vue";

const routes = [
  {
    meta: {
      global: true,
      requireUsername: true,
      requireAvatar: true,
    },
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
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
    path: "/feedbackmanager",
    name: "feedbackmanager",
    component: FeedbackManagerView,
  },
  {
    //元数据
    meta: {
      // 必须登录才可以查看
      requireAuth: true,
    },
    path: "/mine",
    name: "mine",
    component: MineView,
  },
  {
    //元数据
    meta: {
      // 必须管理员登录才可以查看
      requireAdminAuth:true
    },
    path: "/admin",
    name: "admin",
    component: AdminView,
  },
  {
    meta: {
      // 必须登录才可以查看
      requireAuth: true,
    },
    path: "/Release",
    name: "release",
    component: ReleaseView,
  },
  {
    meta: {
      // 必须登录才可以查看
      requireAuth: true,
    },
    path: "/Perform",
    name: "perform",
    component: PerformView,
  },
  {
    meta: {
      // 必须登录才可以查看
      requireAuth: true,
    },
    path: "/taskcenter",
    name: "taskcenter",
    component: TaskCenterView,
  },
  {
    meta:{
      // 必须登录才可以查看
      requireAuth: true
    },
    path: "/taskdetail",
    name: "taskdetail",
    component: TaskDetailView
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

// 登录之后才能访问
router.beforeEach((to, from, next) => {
  //to:即将要进入的目标路由对象；
  //2、from:当前导航即将要离开的路由对象；
  //3、next ：调用该方法后，才能进入下一个钩子函数(afterEach)。 next()
  //直接进to 所指路由 next(false)
  //中断当前路由 next('route')
  //跳转指定路由 next('error')
  if(to.meta.requireAdminAuth){
    if(sessionStorage.getItem("adminAuth")){
      next()
    }else{
      next({name:"login"})
    }
  }
  if (to.meta.requireAuth) {
    // 判断该路由是否需要登录权限
    if (sessionStorage.getItem("logined") == "true") {
      // 判断本地是否存在token
      next();
    } else {
      // 未登录,跳转到登陆页面
      next({
        path: "/login",
      });
    }
  } else {
    next();
  }
});

export default router;
