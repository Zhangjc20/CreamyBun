<template>
  <div class="cloud-box">
    <div style="font-size: 28px; font-family: YouSheRound">设置</div>
    <div class="div-first">
      <span>我的页面 : 默认入口</span>
    </div>
    <div
      style="
        margin-top: 20px;
        padding-left: 6%;
        width: 100%;
        display: flex;
        justify-content: flex-start;
      "
    >
      <el-radio-group v-model="defaultMine" @change="handleRadio">
        <el-radio :label="1">个人信息</el-radio>
        <el-radio :label="2">领取列表</el-radio>
        <el-radio :label="3">发布列表</el-radio>
        <el-radio :label="4">奖励中心</el-radio>
        <el-radio :label="5">活动中心</el-radio>
        <el-radio :label="6">设置</el-radio>
      </el-radio-group>
    </div>
    <div class="logout-button-outer">
      <CustomButton
        title="退出登录"
        fontColor="#ffffff"
        normalColor="#5EABBF"
        focusColor="#4E98AB"
        hoverColor="#4E98AB"
        :clickBack="handleClickLogout"
      />
    </div>
  </div>
</template>

<script>
import CustomButton from "@/components/CustomButton.vue";
import { ElMessage, ElMessageBox } from "element-plus";
import axios from 'axios';
export default {
  name: "SettingView",
  components: {
    CustomButton,
  },
  data() {
    return {
      defaultMine: 1,
    };
  },
  methods: {
    handleRadio(val){
      localStorage.setItem('defaultMine',val);
    },
    handleClickLogout() {
      //退出登录按钮触发函数
      ElMessageBox.confirm("确定要退出登录吗？", "提示", {
        confirmButtonText: "确认",
        cancelButtonText: "取消",
        type: "info",
      })
        .then(() => {
          axios
        .get("http://101.42.118.80:8000/log_in/", {
          params: {
            username: localStorage.getItem("username"),
          },
        })
        .then((res)=>{
          if(res.data['status']=='ok'){
            localStorage.setItem("logined", "false");
            localStorage.removeItem("avatar");
            localStorage.removeItem("username");
            localStorage.removeItem("defaultMine");
            localStorage.removeItem("login_jwt");
            ElMessage({
              type: "success",
              message: "退出登录成功",
            });
            this.$router.push({ name: "home" });
          }
          else{
            ElMessage({
              type: "error",
              message: "退出登录失败",
            });
          }
        })
        })
        .catch(() => {
          ElMessage({
            type: "info",
            message: "取消",
          });
        });
    },
  },
  beforeMount(){
    if(localStorage.getItem('defaultMine')){
      this.defaultMine = Number(localStorage.getItem('defaultMine'));
    }
  }
};
</script>

<style scoped>
.div-first {
  padding: 40px 0 0 6%;
  width: 100%;
  display: flex;
  justify-content: flex-start;
}
.cloud-box {
  margin-top: 10px;
  padding: 20px 0 20px 0;
  box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
  border-radius: 10px;
}
.darkmode-switch {
  float: left;
}
.logout-button {
  float: left;
}
.logout-button-outer {
  padding-top: 30px;
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
