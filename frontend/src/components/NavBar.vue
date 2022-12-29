<template>
  <div class="nav-title">
    <el-image :src="require('@/assets/images/logo_small.png')" class="logo">
    </el-image>
    <span class="nav-title-font">奶黄包</span>
  </div>
  <div class="menu-out">
    <el-menu
      :default-active="activeItem"
      class="el-nav-menu"
      mode="horizontal"
      background-color="#ffffff"
      text-color="#6C6C6C"
      active-text-color="#5EABBF"
    >
      <el-menu-item index="1" @click="clickHome">首页</el-menu-item>
      <el-menu-item index="2" @click="clickTask">任务</el-menu-item>
      <el-menu-item index="3" @click="clickRelease">发布</el-menu-item>
      <el-menu-item index="4" @click="clickMine">我的</el-menu-item>
      <el-menu-item index="5" @click="clickHelp">帮助</el-menu-item>
    </el-menu>
  </div>
  <span v-if="login">
    <div class="nav-right">
    <el-avatar
      :src="imageUrl ? imageUrl : require('@/assets/images/avatar.jpeg')"
      class="avatar"
      @click="clickMine"
    ></el-avatar>
    <span class="user-area">
      <span class="user-center" @click="clickMine">个人中心</span>
    </span>
    </div>
  </span>
  <span class="log-buttons" v-else>
    <el-button
      @click="clickLogin"
      type="primary"
      size="default"
      round
      class="login-button"
      >登录</el-button
    >
    <el-button @click="clickLogup" type="primary" size="default" round
      >注册</el-button
    >
  </span>
</template>

<script>
export default {
  name: "NavBar",
  props: {
    login: Boolean,
    activeItem: String,
    username: {
      type: String,
      default: "",
    },
    imageUrl: {
      type: String,
      default: "",
    },
  },
  data() {
    return {};
  },
  methods: {
    clickHome() {
      this.$router.push({
        name: "home",
      });
    },
    clickHelp() {
      this.$router.push({
        name: "help",
      });
    },
    clickTask() {
      this.$router.push({
        name: "taskcenter",
      });
    },
    clickLogin() {
      this.$router.push({
        name: "login",
      });
    },
    clickLogup() {
      this.$router.push({
        name: "logup",
      });
    },
    clickMine() {
      this.$router.push({
        name: "mine",
      });
    },
    clickRelease() {
      this.$router.push({
        name: "release",
      });
    },
  },
};
</script>

<style scoped>
@media (min-width: 0px) and (max-width:768px) {
  .logo {
    width: 36px;
    height: 30px;
  }
  .nav-title-font {
    margin-left: 10px;
    line-height: 20px;
  }
  .nav-title {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 60px;
    font-family: YouSheRound;
    line-height: 60px;
    font-size: 1rem;
    color: #5eabbf;
  }
  .menu-out {
    margin-left: 6%;
    background-color: #ffffff;
    width: 50%;
    overflow: hidden;
    border-radius: 40px;
    margin-top: 10px;
    display: flex;
  }
  .el-nav-menu {
    width: 100%;
    padding-left: 10px;
  }
  .el-menu-item {
    height: 50px;
    font-size: 0.8em;
    padding-top: 4px;
  }
  .user-area {
    float: right;
    position: absolute;
    top: 0;
    right: 0;
    height: 0px;
    width:0;
    margin-right: 0px;
  }
  .avatar {
    float: right;
    position: absolute;
    top: 0;
    right: 0;
    margin-right: 20%;
    margin-top: 10px;
  }
  .avatar:hover {
    opacity: 0.4;
  }
  .log-buttons {
    line-height: 60px;
    margin-left: 4%;
    display: flex;
    flex-direction: column;
    height:100%;
  }
  .el-button--primary {
    height:23px;
    font-size: 0.6rem;
    background: #5eabbf !important;
    border-color: #5eabbf !important;
    color: #ffffff;
  }
  .login-button {
    margin-top: 12%;
    margin-bottom: 6%;
  }
  .el-button+.el-button{
    margin-left: 0;
  }
}
@media (min-width: 768px) {
  .logo {
    width: 45px;
    height: 40px;
    margin-top: 10px;
  }
  .nav-title-font {
    margin-left: 10px;
    line-height: 60px;
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
  .el-menu-item {
    height: 50px;
    font-size: 16px;
    padding-top: 4px;
  }
  .user-area {
    height: 60px;
    margin-right: 6%;
  }
  .avatar {
    margin-right: 8%;
    margin-top: 10px;
  }
  .avatar:hover {
    opacity: 0.4;
    cursor: pointer;
  }
  .log-buttons {
    position:absolute;
    right:0;
    float: right;
    line-height: 60px;
    margin-right: 4%;
  }
  .el-button--primary {
    background: #fbe484 !important;
    border-color: #fbe484 !important;
    color: #6c6c6c;
  }
  .login-button {
    margin-right: 2rem;
  }
}
.nav-right{
  position: absolute;
  top:0;
  right:0;
  display: flex;
  width:18%;
}
.user-center {
  line-height: 60px;
  margin-bottom: 20px;
  font-size: 22px;
  color: #f8f8f8;
  font-family: YouSheBlack;
  cursor: pointer;
}
.user-center:hover {
  opacity: 0.6;
}

.el-button--medium {
  width: 80px;
}





.el-menu {
  border-radius: 0;
}

.el-menu--horizontal .el-menu-item:not(.is-disabled):focus {
  background-color: transparent;
}
.el-menu--horizontal .el-menu-item:not(.is-disabled):hover {
  background-color: #f8f8f8;
}
</style>
