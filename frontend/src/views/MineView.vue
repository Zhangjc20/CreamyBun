<template>
    <el-container class="container">
      <el-header class="header-style">
        <div class="nav-title">
          <el-image 
            :src="require('@/assets/images/logo.png')"
            class="logo"
          >
          </el-image>
          <span class="nav-title-font">奶黄包</span>
        </div>
        <div class="menu-out">
          <el-menu
            default-active="1"
            class="el-nav-menu"
            mode="horizontal"
            background-color="#ffffff"
            text-color="#6C6C6C"
            active-text-color="#5EABBF">
            <el-menu-item index="1">首页</el-menu-item>
            <el-menu-item index="2">任务</el-menu-item>
            <el-menu-item index="3">发布</el-menu-item>
            <el-menu-item index="4">我的</el-menu-item>
            <el-menu-item index="5">帮助</el-menu-item>
          </el-menu>
        </div>
        <el-avatar :src="require('@/assets/images/avatar.jpeg')" class="avatar"></el-avatar>
        <span class="user-area">
            <span class="user-center" @click="clickUser">个人中心</span>
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
              @open="handleOpen"
              @close="handleClose"
            >
              <el-menu-item index="1">
                <el-icon><icon-menu /></el-icon>
                <span>个人信息</span>
              </el-menu-item>
              <el-menu-item index="2">
                <el-icon><icon-menu /></el-icon>
                <span>已领取任务</span>
              </el-menu-item>
              <el-menu-item index="3">
                <el-icon><document /></el-icon>
                <span>已发布任务</span>
              </el-menu-item>
              <el-menu-item index="4">
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
  </template>
  
  <script>
  import MineInfoView from '@/components/MineInfoView.vue';
  export default{
    name: 'MineView',
    components:{
      MineInfoView
    },
    data(){
      return {
        show_content:"MineInfoView",
      }
    },
    methods:{
        clickUser(){
            this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
            }).then(() => {
                this.$message({
                    type: 'success',
                    message: '删除成功!'
                });
            }).catch(() => {
                this.$message({
                    type: 'info',
                    message: '已取消删除'
                });          
                });
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
  .user-area {
    float: right;
    position: absolute;
    top:0;
    right: 0;
    height: 60px;
    margin-right: 90px;
  }
  .avatar {
    float: right;
    position: absolute;
    top:0;
    right: 0;
    margin-right: 180px;
    margin-top: 10px;
  }
  .user-center {
    line-height: 60px;
    margin-bottom: 20px;
    font-size: 22px;
    color:#f8f8f8;
    font-family: YouSheBlack;
    cursor: pointer;
  }
  .user-center:hover {
    opacity: 0.6;
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