<template>
  <div>
    <div class="div-first">
      <span class="darkmode-title">暗色模式</span>
      <el-switch class="darkmode-switch" v-model="darkmode" />
    </div>
    <div class="logout-button-outer">
      <CustomButton title="退出登录" fontColor="#ffffff" normalColor="#5EABBF" focusColor="#4E98AB" hoverColor="#4E98AB" :clickBack="handleClickLogout"/>
    </div>
  </div>
</template>

<script>
import CustomButton from "@/components/CustomButton.vue";
import { ElMessage, ElMessageBox } from 'element-plus';
export default {
  name: "SettingView",
  components:{
    CustomButton
  },
  props: {},
  data() {
    return {
      darkmode: false,
    };
  },
  methods: {
    handleClickLogout(){//退出登录按钮触发函数
      ElMessageBox.confirm(
        '确定要退出登录吗？',
        '提示',
        {
          confirmButtonText: '确认',
          cancelButtonText: '取消',
          type: 'info',
        }
      )
        .then(() => {
          localStorage.setItem("logined", 'false');
          localStorage.removeItem("avatar");
          localStorage.removeItem("username");
          ElMessage({
            type: 'success',
            message: '退出登录成功',
          });
          this.$router.push({name:"home"});
        })
        .catch(() => {
          ElMessage({
            type: 'info',
            message: '取消',
          })
        })
    }
  },
};
</script>

<style scoped>
.div-first {
  margin: 40px 0 0 0;
  width: 100%;
}
.darkmode-title {
  float: left;
  margin-top: 4px;
  margin-left: 20px;
}
.darkmode-switch {
  float: left;
}
.logout-button {
  float: left;
}
.logout-button-outer {
  padding-top: 80px;
  padding-left: 40px;
}
.darkmode-title {
  margin-right: 20px;
}
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
