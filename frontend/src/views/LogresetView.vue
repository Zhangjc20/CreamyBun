<template>
    <el-container class="logreset">
        <div class="logreset-box">
            <div class="logreset-title">
                <span class="log-account-font">重置密码</span>
                <el-link type="primary" class="login-link" @click="clickLogin">立即登录</el-link>
            </div>
            <el-form
                class="form-box"
                ref="ruleFormRef"
                status-icon
            >
                
                <el-form-item label="重置方式" prop="isUsername">
                    <el-radio v-model="form.isUsername" :label="true">用户名</el-radio>
                    <el-radio v-model="form.isUsername" :label="false">邮箱</el-radio>
                </el-form-item>

                <div v-if="form.isUsername">
                <el-form-item required>
                    <el-input clearable v-model="form.username" placeholder="请输入用户名">
                        <template #prefix>
                            <svg class="icon" aria-hidden="true">
                                <use xlink:href="#icon-user"></use>
                            </svg>
                        </template>
                    </el-input>
                </el-form-item>
                </div>
                <div v-else>
                <el-form-item required>
                    <el-input clearable v-model="form.email" placeholder="请输入邮箱">
                        <template #prefix>
                            <svg class="icon" aria-hidden="true">
                                <use xlink:href="#icon-email-fill"></use>
                            </svg>
                        </template>
                    </el-input>
                </el-form-item>
                </div>
                <el-form-item required class="verify-button">
                    <el-col :span="14"><el-input placeholder="请输入验证码" clearable v-model="form.verifyCode">
                        <template #prefix>
                            <span class="iconfont icon-verify-fill icon-verify-change"></span>
                        </template>
                    </el-input ></el-col>
                    <el-col :span="10"><el-button class="get-verify">获取验证码</el-button></el-col>
                </el-form-item>
                <el-form-item required>
                    <el-input clearable v-model="form.password" show-password placeholder="请输入想要重置的密码">
                        <template #prefix>
                            <svg class="icon icon-lock-change" aria-hidden="true" >
                                <use xlink:href="#icon-lock"></use>
                            </svg>
                        </template>
                    </el-input>
                </el-form-item>
                <el-form-item required>
                    <el-input clearable v-model="form.passwordAgain" show-password placeholder="请确认密码">
                        <template #prefix>
                            <svg class="icon icon-lock-change" aria-hidden="true">
                                <use xlink:href="#icon-lock"></use>
                            </svg>
                        </template>
                    </el-input>
                </el-form-item>
                
                <el-form-item class="logreset-outer">
                    <el-button class="logreset-button"
                        >注册</el-button
                    >
                </el-form-item>
                
        </el-form>
        </div>
    </el-container>
  </template>
  
  <script>
    export default {
        name:'LogupView',
        data(){
            return {
                form:{
                    username:"",
                    password:"",
                    passwordAgain:"",
                    email:"",
                    verifyCode:"",
                    isUsername:false,
                }
            }
        },
        methods:{
            clickLogin(){
                this.$router
            }
        }
    }
</script>

  <style scoped lang="scss">
    .el-form-item{
        margin-bottom: 26px;
    }
  .logreset-button {
    color:#ffffff;
    width: 100%;
    font-size: 18px;
    background-color: #FBE484;
    border-color: #FBE484;
    height: 36px;
  }
  .logreset-button:hover,.logup-outer .el-button:focus {
    background-color: #e8d173;
    color:#ffffff;
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
    background-color: #5EABBF;
    color:#ffffff;
    margin-left: 10px;
  }
  .get-verify:hover, .verify-button .el-button:focus {
    background-color: #7ec3d4;
    color:#ffffff;
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
    font-size:24px;
    font-family: YouSheBlack;
  }
  .form-box {
    margin-left: 20%;
    margin-right: 20%;
  }
  .logreset-title {
    margin-top: 40px;
    padding: 10px;
    padding-right: 20px;
    height: 30px;
    margin-bottom: 30px;
  }
  .logreset-box {
    width: 36%;
    height: 64%;
    margin-left: 32%;
    margin-top: 8%;
    border-radius: 20px;
    background-color: #ffffff;
  }
  .logreset {
    width: 100%;
    height: 100%;
    position: absolute;
    background: url(@/assets/images/background.png);
    background-size: 100% 100%;
  }
  </style>
  