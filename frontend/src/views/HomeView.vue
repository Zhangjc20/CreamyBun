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
      <span class="log-buttons">
        <el-button type="primary" size="medium" round class="login-button">登录</el-button>
        <el-button type="primary" size="medium" round>注册</el-button>
      </span>
    </el-header>
    <el-main class="main-style">

    </el-main>
  </el-container>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'HomeView',
  components: {
  },
  data(){
    return {

    }
  }
}
</script>


<style scoped>
.container {
  margin:0;
  height:100%;
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
.login-button {
  margin-right: 30px;
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
.log-buttons {
  float: right;
  position: absolute;
  top:0;
  right: 0;
  line-height: 60px;
  margin-right: 100px;
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

