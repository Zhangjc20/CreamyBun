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
        <div class="jump-active">
          <div style="position: absolute; bottom: 20px;left: 0px;width: 20px;height: 150px;">
            <div style="position: absolute; bottom: 0px;border-top: 20px solid #5EABBF;border-left: 20px solid transparent;"></div>
            <div style="background-color:#5EABBF;position: absolute; bottom: 20px;width: 20px;height: 110px;"></div>
            <div style="position: absolute; bottom: 130px;border-bottom: 20px solid #5EABBF;border-left: 20px solid transparent;"></div>
          </div>
          <div style="position: absolute; bottom: 10px;left: 40px;width: 25px;height: 200px;">
            <div style="position: absolute; bottom: 0px;border-top: 25px solid #FBE484;border-right: 25px solid transparent;"></div>
            <div style="background-color:#FBE484;position: absolute; bottom: 25px;width: 25px;height: 150px;"></div>
            <div style="position: absolute; bottom: 175px;border-bottom: 25px solid #FBE484;border-right: 25px solid transparent;"></div>
          </div>
          <div style="position: absolute; bottom: 65px;left: 200px;width: 10px;height: 80px;">
            <div style="position: absolute; bottom: 0px;border-top: 10px solid #5EABBF;border-right: 10px solid transparent;"></div>
            <div style="background-color:#5EABBF;position: absolute; bottom: 10px;width: 10px; height: 60px;"></div>
            <div style="position: absolute; bottom: 70px;border-bottom: 10px solid #5EABBF;border-right: 10px solid transparent;"></div>
          </div>
          <div style="position: absolute; bottom: 20px;left: 230px;width: 20px;height: 150px;">
            <div style="position: absolute; bottom: 0px;border-top: 20px solid #FBE484;border-left: 20px solid transparent;"></div>
            <div style="background-color:#FBE484;position: absolute; bottom: 20px;width: 20px;height: 110px;"></div>
            <div style="position: absolute; bottom: 130px;border-bottom: 20px solid #FBE484;border-left: 20px solid transparent;"></div>
          </div>
          <div style="position: absolute; bottom: 140px;left: 170px;width: 15px;height: 30px;">
            <div style="position: absolute; bottom: 0px;border-top: 15px solid #FBE484;border-left: 15px solid transparent;"></div>
            <div style="position: absolute; bottom: 15px;border-bottom: 15px solid #FBE484;border-left: 15px solid transparent;"></div>
          </div>
          <div style="position: absolute; bottom: 150px;left: 90px;width: 15px;height: 30px;">
            <div style="position: absolute; bottom: 0px;border-top: 15px solid #5EABBF;border-right: 15px solid transparent;"></div>
            <div style="position: absolute; bottom: 15px;border-bottom: 15px solid #5EABBF;border-right: 15px solid transparent;"></div>
          </div>
          <div style="position: absolute; bottom: 20px;left: 90px;width: 250px;height: 250px;">
            <div style="flex-direction: column;position:absolute;bottom: 0px;margin-left: auto;margin-right: auto;text-align:center ">
              <el-image
                style="width: 88px; height: 80px"
                fit="cover"
                :src="require('@/assets/images/logo_small.png')"
                class="jump-logo"
              ></el-image>
              <div class="jump-shadow"></div>
            </div>
          </div>
        </div>
      </el-aside>
      <el-main class="main-style">
        <div class="right-part">
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
        </div>
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
    const choices = ['MineInfoView','TaskPage','TaskPage','GiftCenter','ActivityCenter','SettingView'];
    return {
      image: {
        src: "",
        type: "",
      },
      showContent: localStorage.getItem('defaultMine')?choices[Number(localStorage.getItem('defaultMine'))-1]:choices[0],
      total: 4,
      showTaskType:localStorage.getItem('defaultMine')=='2'?1:2,
      username: "",
      defaultActive:localStorage.getItem('defaultMine')?localStorage.getItem('defaultMine'):"1",
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
      axios.get('http://101.42.118.80:8000/get_avatar/',{
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
@media (min-width: 0px) and (max-width:768px) {
  .el-aside{
    width:40%;
  }
  .jump-active{
    display:none;
  }
  .main-style {
    background-color: transparent;
  }
  .right-part{
    width:1000px;
  }
}
@media (min-width: 768px) {
  .jump-active{
    position: fixed; 
    bottom: 0px;
    left: 20px;
    width: 250px;
    height: 250px;
  }
  .main-style {
    background-color: transparent;
  }
}
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
.jump-logo {
  z-index: 2;
  animation: jump-logo 1s infinite;
  animation-timing-function: ease;
}
.jump-shadow {
  z-index: 1;
  width: 100px;
  height: 5px;
  background: #eaeaea;
  border-radius: 100%;
  animation: shadow 1s infinite;
  animation-timing-function: ease;
  margin-left: auto;
  margin-right: auto;
}
@keyframes jump-logo {
  0% {
    margin-bottom: 0px;
  }

  50% {
    margin-bottom: 30px;
  }

  100% {
    margin-bottom: 0px;
  }
}
@keyframes shadow {
  0% {
    width: 85px;
  }

  50% {
    width: 65px;
  }

  100% {
    width: 85px;
  }
}
</style>
