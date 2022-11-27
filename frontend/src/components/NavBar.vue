<template>
  <div class="nav-title">
    <el-image :src="require('@/assets/images/logo.png')" class="logo">
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
    <el-avatar
      :src="imageUrl ? imageUrl : require('@/assets/images/avatar.jpeg')"
      class="avatar"
    ></el-avatar>
    <span class="user-area">
      <span class="user-center" @click="clickUser">个人中心</span>
    </span>
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
        query: {
          username: this.username,
          imageSrc: this.imageUrl,
        },
      });
    },
    clickHelp() {
      this.$router.push({
        name: "help",
        query: {
          username: this.username,
          imageSrc: this.imageUrl,
        },
      });
    },
    clickTask() {
      this.$router.push({
        name: "taskcenter",
        query: {
          username: this.username,
          imageSrc: this.imageUrl,
        },
      });
    },
    clickLogin() {
      this.$router.push({
        name: "login",
        query: {
          username: this.username,
        },
      });
    },
    clickLogup() {
      this.$router.push({
        name: "logup",
        query: {
          username: this.username,
        },
      });
    },
    clickMine() {
      this.$router.push({
        name: "mine",
        query: {
          username: this.username,
          imageSrc: this.imageUrl,
        },
      });
    },
    clickRelease() {
      this.$router.push({
        name: "release",
        query: {
          username: this.username,
          imageSrc: this.imageUrl,
        },
      });
    },
  },
};
</script>

<style scoped>
.user-area {
  float: right;
  position: absolute;
  top: 0;
  right: 0;
  height: 60px;
  margin-right: 90px;
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
.user-center:hover {
  opacity: 0.6;
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
.menu-out {
  margin-left: 80px;
  background-color: #ffffff;
  width: 470px;
  overflow: hidden;
  border-radius: 40px;
  margin-top: 10px;
  display: flex;
}
.el-button--primary {
  background: #fbe484 !important;
  border-color: #fbe484 !important;
  color: #6c6c6c;
}
.el-button--medium {
  width: 80px;
}

.logo {
  width: 45px;
  height: 40px;
  margin-top: 10px;
}
.login-button {
  margin-right: 30px;
}

.log-buttons {
  float: right;
  position: absolute;
  top: 0;
  right: 0;
  line-height: 60px;
  margin-right: 100px;
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
