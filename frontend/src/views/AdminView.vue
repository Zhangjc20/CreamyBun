<template>
  <el-container class="container">
    <el-header class="header-style">
      <div class="nav-title">
        <el-image :src="require('@/assets/images/logo.png')" class="logo">
        </el-image>
        <span class="nav-title-font">奶黄包</span>
      </div>
      <div class="menu-out">首页</div>
      <span>
        <el-avatar
          :src="require('@/assets/images/avatar.jpeg')"
          class="avatar"
        ></el-avatar>
        <span class="user-area">
          <span class="user-center">管理员</span>
        </span>
      </span>
    </el-header>
    <el-container>
    <el-aside class="left-menu-area">
      <el-menu
        active-text-color="#FBE484"
        background-color="#FFFFFF"
        class="el-menu-vertical-demo"
        default-active="1"
        text-color="#4E5969"
      >
        <el-menu-item index="1" @click="clickLeftMenu(1)">
          <el-icon><Tickets /></el-icon>
          <span>审核任务</span>
        </el-menu-item>
        <el-menu-item index="2" @click="clickLeftMenu(2)">
          <el-icon><Reading /></el-icon>
          <span>处理反馈</span>
        </el-menu-item>
        <el-menu-item index="3" @click="clickLeftMenu(3)">
          <el-icon><SetUp /></el-icon>
          <span>参数调整</span>
        </el-menu-item>
        <el-menu-item index="4" @click="clickLeftMenu(4)">
          <el-icon><Setting /></el-icon>
          <span>设置</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <el-main class="main-style">
      <component :is="showContent" :type="3" :key="showContent" />
    </el-main>
    </el-container>
  </el-container>
</template>

<script>
import { componentSizes } from "element-plus";
import TaskPage from "@/components/TaskPage.vue";
import AdminSettings from "@/components/AdminSettings.vue";
import ChangeParams from "@/components/ChangeParams.vue";
// import { ElMessage, ElMessageBox } from "element-plus";

// @ is an alias to /src
export default {
  name: "AdminView",
  components: { componentSizes, TaskPage, AdminSettings,ChangeParams },
  data() {
    return {
      showContent: "TaskPage",
    };
  },
  methods: {
    clickLeftMenu(val) {
      switch(val){
        case 1:
            this.showContent = "TaskPage";
            break;
        case 2:
            break;
        case 3:
            this.showContent = "ChangeParams";
            break;
        case 4:
            this.showContent = "AdminSettings";
            break;
        default:
      }
    },
  },
  mounted() {
    if (this.$route.query.username) {
      this.username = this.$route.query.username;
      console.log(this.username);
    }
    if (this.$route.query.imageSrc) {
      this.image.src = this.$route.query.imageSrc;
    }
  },
};
</script>

<style scoped>
.container {
  margin: 0;
  height: 100%;
}
.el-aside .el-menu {
  border-right: 0;
}
.el-aside .el-menu .el-menu-item {
  border-radius: 20px;
}
.el-aside .el-menu .el-menu-item:hover {
  background-color: #f2f2f2;
}
.el-aside .el-menu .el-menu-item.is-active {
  background-color: #5eabbf;
}
.el-menu--horizontal .el-menu-item:not(.is-disabled):focus {
  background-color: transparent;
}
.el-menu--horizontal .el-menu-item:not(.is-disabled):hover {
  background-color: #f8f8f8;
}
.el-aside {
  /* border-right: 1px solid; */
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 5px 0 rgba(0, 0, 0, 0.19);
}
.left-menu-area {
  padding-top: 100px;
  padding-left: 10px;
  padding-right: 10px;
  height: 100%;
}
.user-area {
  float: right;
  position: absolute;
  top: 0;
  right: 0;
  height: 60px;
  margin-right: 100px;
}
.logo {
  width: 45px;
  height: 40px;
  margin-top: 10px;
}
.avatar {
  float: right;
  position: absolute;
  top: 0;
  right: 0;
  margin-right: 180px;
  margin-top: 10px;
}
.user-center {
  line-height: 60px;
  margin-bottom: 20px;
  font-size: 22px;
  color: #f8f8f8;
  font-family: YouSheBlack;
  cursor: pointer;
}
.main-style {
  background-color:transparent;
}
.header-style {
  background-image: url(@/assets/images/nav-background.png);
  background-size: cover;
  height: 60px;
  box-shadow: 0 0px 8px 0;
  display: flex;
}
.menu-out {
  margin-left: 80px;
  background-color: #ffffff;
  width: 100px;
  overflow: hidden;
  border-radius: 40px;
  margin-top: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #5eabbf;
}
.nav-title {
  float: left;
  height: 60px;
  font-family: YouSheRound;
  line-height: 50px;
  font-size: 28px;
  color: #5eabbf;
  margin-left: 80px;
  display: flex;
}
.nav-title-font {
  margin-left: 10px;
  line-height: 60px;
}
</style>
