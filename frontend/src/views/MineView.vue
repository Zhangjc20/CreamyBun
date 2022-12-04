<template>
  <el-container class="container">
    <el-header class="header-style">
      <NavBar
        :login="true"
        activeItem="4"
        :username="username"
        :imageUrl="image.src"
      ></NavBar>
    </el-header>
    <el-container>
      <el-aside class="left-menu-area">
        <el-menu
          active-text-color="#FBE484"
          background-color="#FFFFFF"
          class="el-menu-vertical-demo"
          :default-active="defaultActive"
          text-color="#4E5969"
        >
          <el-menu-item index="1" @click="clickLeftMenu(1)">
            <el-icon><Menu /></el-icon>
            <span>个人信息</span>
          </el-menu-item>
          <el-menu-item index="2" @click="clickLeftMenu(2)">
            <el-icon><document /></el-icon>
            <span>领取列表</span>
          </el-menu-item>
          <el-menu-item index="3" @click="clickLeftMenu(3)">
            <el-icon><document /></el-icon>
            <span>发布列表</span>
          </el-menu-item>
          <el-menu-item index="4" @click="clickLeftMenu(4)">
            <el-icon><Shop /></el-icon>
            <span>奖励中心</span>
          </el-menu-item>
          <el-menu-item index="5" @click="clickLeftMenu(5)">
            <el-icon><Flag /></el-icon>
            <span>活动中心</span>
          </el-menu-item>
          <el-menu-item index="6" @click="clickLeftMenu(6)">
            <el-icon><setting /></el-icon>
            <span>设置</span>
          </el-menu-item>
        </el-menu>
      </el-aside>
      <el-main class="main-style">
          <component
            :is="showContent"
            :key="showContent"
            :username="username"
            :imageSrc="image.src"
            :type="showTaskType"
            ref="coreComponent"
            @changeUsername="changeUsername"
            @changeAvatar="changeAvatar"
          ></component>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import MineInfoView from "@/components/MineInfoView.vue";
import NavBar from "@/components/NavBar.vue";
import GiftCenter from "@/components/GiftCenter.vue";
import SettingView from "@/components/SettingView.vue";
import TaskPage from "@/components/TaskPage.vue";
import ActivityCenter from "@/components/ActivityCenter.vue";
import axios from "axios";
export default {
  name: "MineView",
  components: {
    MineInfoView,
    NavBar,
    GiftCenter,
    SettingView,
    TaskPage,
    ActivityCenter,
  },
  data() {
    return {
      image: {
        src: "",
        type: "",
      },
      showContent: "MineInfoView",
      total: 4,
      showTaskType:1,
      username: "",
      defaultActive:"1",
    };
  },
  methods: {
    changeAvatar(src) {
      this.image.src = src;
    },
    changeUsername(newUsername) {
      this.username = newUsername;
    },
    clickLeftMenu(number) {
      switch (number) {
        case 1:
          this.showContent = "MineInfoView";
          break;
        case 2:
          this.showContent = "TaskPage";
          this.showTaskType = 1;
          break;
        case 3:
          this.showContent = "TaskPage";
          this.showTaskType = 2;
          break;
        case 4:
          this.showContent = "GiftCenter";
          break;
        case 5:
          this.showContent = "ActivityCenter";
          break;
        case 6:
          this.showContent = "SettingView";
          break;
        default:
      }
    },
  },
  mounted() {
    if (localStorage.getItem('username')) {
      this.username = localStorage.getItem('username');
    }
    if(!localStorage.getItem('avatar')){
      axios.get('/get_avatar',{
        params:{
          username:this.username
        }
      })
      .then((res)=>{
        if(res.data['status']==='ok'){
          if(res.data['avatar']){
              this.image.src = "data:image/png;base64," + res.data["avatar"];
              localStorage.setItem("avatar", this.image.src);
            }
        }
      })
    }
    else{
      this.image.src = localStorage.getItem('avatar');
    }
    if (this.$route.query.defaultActive) {
      this.defaultActive = this.$route.query.defaultActive;
      this.clickLeftMenu(Number(this.defaultActive));
    }
  },
};
</script>

<style scoped>
.container {
  margin: 0;
  height: 100%;
}
.left-menu-area {
  padding-top: 100px;
  padding-left: 10px;
  padding-right: 10px;
}
.el-aside .el-menu {
  border-right: 0;
}
.el-aside {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 5px 0 rgba(0, 0, 0, 0.19);
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
.el-button--primary {
  background: #fbe484 !important;
  border-color: #fbe484 !important;
  color: #6c6c6c;
}
.el-button--medium {
  width: 80px;
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
.logo {
  width: 45px;
  height: 40px;
  margin-top: 10px;
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
  width: 470px;
  overflow: hidden;
  border-radius: 40px;
  margin-top: 10px;
  display: flex;
}
.main-style {
  background-color: transparent;
}
.el-nav-menu {
  width: 480px;
  padding-left: 46px;
}
.el-menu {
  border-radius: 0;
}
.el-menu-item {
  height: 50px;
  font-size: 16px;
  padding-top: 4px;
}
.el-menu--horizontal .el-menu-item:not(.is-disabled):focus {
  background-color: transparent;
}
.el-menu--horizontal .el-menu-item:not(.is-disabled):hover {
  background-color: #f8f8f8;
}
</style>
