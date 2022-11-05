<template>
  <el-container class="logup">
    <div class="logup-box">
      <div class="logup-title">
        <span class="log-account-font">注册账号</span>
        <el-link type="primary" class="login-link" @click="clickLogin"
          >已有账号，立即登录</el-link
        >
      </div>
      <el-form class="form-box" label-width="120px" status-icon>
        <el-form-item label="" required>
          <el-input
            clearable
            v-model="form.username"
            placeholder="设置用户名称"
          >
            <template #prefix>
              <svg class="icon" aria-hidden="true">
                <use xlink:href="#icon-user"></use>
              </svg>
            </template>
          </el-input>
        </el-form-item>
        <el-form-item label="" required>
          <el-input
            clearable
            v-model="form.password"
            show-password
            placeholder="设置6-18位登录密码"
          >
            <template #prefix>
              <svg class="icon icon-lock-change" aria-hidden="true">
                <use xlink:href="#icon-lock"></use>
              </svg>
            </template>
          </el-input>
        </el-form-item>
        <el-form-item label="" required>
          <el-input
            clearable
            v-model="form.passwordAgain"
            show-password
            placeholder="再次输入登录密码"
          >
            <template #prefix>
              <svg class="icon icon-lock-change" aria-hidden="true">
                <use xlink:href="#icon-lock"></use>
              </svg>
            </template>
          </el-input>
        </el-form-item>
        <el-form-item label="">
          <el-input
            clearable
            v-model="form.email"
            required
            placeholder="输入邮箱"
          >
            <template #prefix>
              <svg class="icon" aria-hidden="true">
                <use xlink:href="#icon-email-fill"></use>
              </svg>
            </template>
          </el-input>
        </el-form-item>
        <el-form-item label="" required class="verify-button">
          <el-col :span="14"
            ><el-input
              clearable
              v-model="form.verifyCode"
              placeholder="输入验证码"
            >
              <template #prefix>
                <span
                  class="iconfont icon-verify-fill icon-verify-change"
                ></span>
              </template> </el-input
          ></el-col>
          <el-col :span="10"
            ><el-button class="get-verify">获取验证码</el-button></el-col
          >
        </el-form-item>
        <el-form-item class="logup-outer">
          <el-button class="logup-button" @click="clickLogup">注册</el-button>
        </el-form-item>
      </el-form>
    </div>
  </el-container>
</template>

<script>
import axios from "axios";
import { ElMessage } from 'element-plus';
export default {
  name: "LogupView",
  data() {
    return {
      form: {
        username: "",
        password: "",
        passwordAgain: "",
        email: "",
        verifyCode: "",
      },
    };
  },
  methods: {
    clickLogin() {
      this.$router.push({
        name: "login",
      });
    },
    clickLogup(){
      if(this.password!=this.passwordAgain){
        ElMessage({
            type: 'error',
            message: '两次输入的密码不一致',
          })
      }
      axios.get('http://localhost:8000/log_up',{
        username:this.username,
        password:this.password,
        email:this.email,
        verifyCode:this.verifyCode
      })
      .then(function(res){
        console.log(res);
        this.$router.push({
          name: "login",
        });
      })
      .catch(function(err){
        console.log(err);
      });
    }
  },
};
</script>

<style scoped lang="scss">
.el-form-item {
  margin-bottom: 26px;
}
.logup-button {
  color: #ffffff;
  width: 100%;
  font-size: 18px;
  background-color: #fbe484;
  border-color: #fbe484;
  height: 36px;
}
.logup-button:hover,
.logup-outer .el-button:focus {
  background-color: #e8d173;
  color: #ffffff;
  border-color: #e8d173;
}
.el-button--active {
  background-color: #e8d173;
  border-color: #e8d173;
}
.icon {
  width: 1em;
  height: 1em;
  vertical-align: -0.15em;
  fill: currentColor;
  overflow: hidden;
}
.icon-verify-change {
  font-size: 14px;
}
.icon-lock-change {
  width: 1.2em;
  height: 1.2em;
}
.get-verify {
  background-color: #5eabbf;
  color: #ffffff;
  margin-left: 10px;
}
.get-verify:hover,
.verify-button .el-button:focus {
  background-color: #7ec3d4;
  color: #ffffff;
}
.login-link {
  font-size: 15px;
  float: right;
  position: relative;
  right: 4%;
}
.log-account-font {
  line-height: 22px;
  float: left;
  position: relative;
  left: 8%;
  font-size: 24px;
  font-family: YouSheBlack;
}
.form-box {
  padding-right: 70px;
  padding-left: 0px;
}
.logup-title {
  margin-top: 40px;
  padding: 10px;
  padding-right: 20px;
  height: 30px;
  margin-bottom: 30px;
}
.logup-box {
  width: 36%;
  height: 64%;
  margin-left: 32%;
  margin-top: 8%;
  border-radius: 20px;
  background-color: #ffffff;
}
.logup {
  width: 100%;
  height: 100%;
  position: absolute;
  background: url(@/assets/images/background.png);
  background-size: 100% 100%;
}
::v-deep .el-form-item__content {
  margin-left: 86px !important;
}
</style>
