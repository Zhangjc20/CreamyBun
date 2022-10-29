<template>
    <el-container class="container">
      <el-header class="header-style">
        <NavBar :login="true" activeItem="4"></NavBar>
      </el-header>
      <el-container>
        <el-aside class="left-menu-area">
            <el-menu
              active-text-color="#FBE484"
              background-color="#FFFFFF"
              class="el-menu-vertical-demo"
              default-active="1"
              text-color="#4E5969"
              @open="handleOpen"
              @close="handleClose"
            >
              <el-menu-item index="1" @click="clickLeftMenu(1)">
                <el-icon><icon-menu /></el-icon>
                <span>个人信息</span>
              </el-menu-item>
              <el-menu-item index="2" @click="clickLeftMenu(2)">
                <el-icon><icon-menu /></el-icon>
                <span>已领取任务</span>
              </el-menu-item>
              <el-menu-item index="3" @click="clickLeftMenu(3)">
                <el-icon><document /></el-icon>
                <span>已发布任务</span>
              </el-menu-item>
              <el-menu-item index="4" @click="clickLeftMenu(4)">
                <el-icon><setting /></el-icon>
                <span>奖励中心</span>
              </el-menu-item>
              <el-menu-item index="5" @click="clickLeftMenu(5)">
                <el-icon><setting /></el-icon>
                <span>设置</span>
              </el-menu-item>
            </el-menu>
        </el-aside>
        <el-main class="main-style">
          <component :is="show_content"></component>
        </el-main>
      </el-container>
    </el-container>
  </el-container>
</template>

  <script>
  import MineInfoView from '@/components/MineInfoView.vue';
  import NavBar from '@/components/NavBar.vue';
  import GiftCenter from '@/components/GiftCenter.vue';
  import SettingView from '@/components/SettingView.vue';
  export default{
    name: 'MineView',
    components:{
      MineInfoView,
      NavBar,
      GiftCenter,
      SettingView
    },
    data(){
      return {
        show_content:"MineInfoView",
      }
    },
    methods:{
      clickLeftMenu(number){
        switch(number){
          case 1:
            this.show_content = "MineInfoView";
            break;
          case 4:
            this.show_content = "GiftCenter";
            break;
          case 5:
            this.show_content = "SettingView";
            break;
          default:
        }
      }
    }
  }
  </script>
  
  <style scoped>
  .container {
    margin:0;
    height:100%;
  }
  .left-menu-area {
    padding-top: 100px;
    padding-left: 10px;
    padding-right: 10px;
  }
  .el-aside .el-menu {
    border-right: 0;
  }
  .el-aside .el-menu .el-menu-item {
    border-radius: 20px;
  }
  .el-aside .el-menu .el-menu-item:hover {
    background-color: #F2F2F2;
  }
  .el-aside .el-menu .el-menu-item.is-active {
    background-color: #5EABBF;
  }
  .el-button--primary {
    background: #FBE484 !important;
    border-color: #FBE484 !important;
    color:#6C6C6C;
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
    color: #5EABBF;
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
    width:470px;
    overflow: hidden;
    border-radius: 40px;
    margin-top: 10px;
    display: flex;
  }
  .main-style {
    background-color:transparent;
  }
  .el-nav-menu {
    width:480px;
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
  .el-menu--horizontal .el-menu-item:not(.is-disabled):focus{
    background-color: transparent;
  }
  .el-menu--horizontal .el-menu-item:not(.is-disabled):hover{
    background-color: #f8f8f8;
  }
  </style>