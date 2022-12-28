<template>
  <el-container class="logup">
    <div class="logup-box">
      <div class="logup-title">
        <span class="log-account-font">注册账号</span>
        <el-link type="primary" class="login-link" @click="clickLogin"
          >已有账号，立即登录</el-link
        >
      </div>
      <el-form
        :model="form"
        class="form-box"
        label-width="120px"
        status-icon
        :rules="rules"
      >
        <el-form-item label="" prop="username">
          <el-input
            clearable
            v-model="form.username"
            placeholder="设置5-12位用户名"
            maxlength="12"
          >
            <template #prefix>
              <svg class="icon" aria-hidden="true">
                <use xlink:href="#icon-user"></use>
              </svg>
            </template>
          </el-input>
        </el-form-item>
        <el-form-item label="" required prop="password">
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
        <el-form-item label="" required prop="passwordAgain">
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
        <el-form-item label="" prop="email">
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
        <el-form-item label="" required class="verify-button" prop="verifyCode">
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
            ><el-button class="get-verify" @click="getVerifyCode"
              >获取验证码</el-button
            ></el-col
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
import { ElMessage } from "element-plus";
export default {
  name: "LogupView",
  data() {
    const validateUsername = (rule, value, callback) => {
      if (value === "") {
        this.usernameRight = false;
        callback(new Error("用户名不能为空"));
      } else if (value.match(/[a-zA-z\d]{5,12}/g)) {
        this.usernameRight = true;
        callback();
      } else {
        this.usernameRight = false;
        callback(new Error("请输入5-12位字母和数字的组合"));
      }
    };
    const validatePassword = (rule, value, callback) => {
      if (value === "") {
        this.passwordRight = false;
        callback(new Error("密码不能为空"));
      } else if (value.search(/^[a-zA-Z\d]{6,18}$/g) == -1) {
        this.passwordRight = false;
        callback(new Error("请输入6-18位字母和数字的组合"));
      } else {
        this.passwordRight = true;
        callback();
      }
    };
    const validatePasswordAgain = (rule, value, callback) => {
      if (value != this.form.password) {
        this.passwordAgainRight = false;
        callback(new Error("两次输入的密码不一致"));
      } else {
        this.passwordAgainRight = true;
        callback();
      }
    };
    const validateEmail = (rule, value, callback) => {
      if (
        value.match(/[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+/g)
      ) {
        this.emailRight = true;
        callback();
      } else {
        this.emailRight = false;
        callback(new Error("邮箱格式不合法"));
      }
    };
    const validateVerifyCode = (rule, value, callback) => {
      if (!Number.isInteger(value) && value.length != 6) {
        this.verifyCodeRight = false;
        callback(new Error("请输入六位数字验证码"));
      } else {
        this.verifyCodeRight = true;
        callback();
      }
    };
    return {
      form: {
        username: "",
        password: "",
        passwordAgain: "",
        email: "",
        verifyCode: "", //仅为点击验证码时的验证码
      },
      correctCode: "",
      usernameRight: false,
      passwordRight: false,
      passwordAgainRight: false,
      emailRight: false,
      verifyCodeRight: false,
      emailing: false,
      codeEmail: "", //发来的验证码对应的email
      emailingSeconds: 0,
      rules: {
        username: [
          {
            validator: validateUsername,
            required: true,
            trigger: ["blur", "change"],
          },
        ],
        password: [
          {
            validator: validatePassword,
            required: true,
            trigger: ["blur", "change"],
          },
        ],
        passwordAgain: [
          {
            validator: validatePasswordAgain,
            required: true,
            trigger: ["blur", "change"],
          },
        ],
        email: [
          {
            validator: validateEmail,
            required: true,
            trigger: ["blur", "change"],
          },
        ],
        verifyCode: [
          {
            validator: validateVerifyCode,
            required: true,
            trigger: ["blur", "change"],
          },
        ],
      },
    };
  },
  methods: {
    getVerifyCode() {
      if (!this.emailRight) {
        ElMessage({
          type: "error",
          message: "邮箱格式错误，请进行修改",
        });
        return;
      }
      if (this.emailing) {
        ElMessage({
          type: "warning",
          message: `验证码已发送，${60 - this.emailingSeconds}s后可以重新发送`,
        });
        return;
      }
      this.codeEmail = this.form.email;
      this.emailing = true;
      this.emailingSeconds = 0;
      let timerI = setInterval(() => {
        this.emailingSeconds += 1;
      }, 1000);
      let timerT = setTimeout(() => {
        this.emailing = false;
        clearTimeout(timerT);
        clearInterval(timerI);
      }, 60000);
      axios
        .get("http://101.42.118.80:8000/log_up/", {
          params: {
            type: "getVerifyCode",
            email: this.codeEmail,
          },
        })
        .then((res) => {
          if (res.data["status"] === "ok") {
            this.correctCode = res.data["verifyCode"];
            ElMessage({
              type: "success",
              message: "验证码发送成功，请在对应邮箱查收",
            });
            return;
          } else if (res.data["status"] === "wrong") {
            if (res.data["type"] === "sameEmail") {
              ElMessage({
                type: "error",
                message: "该邮箱已被注册",
              });
              this.emailing = false;
              this.emailingSeconds = 0;
              clearTimeout(timerT);
              clearInterval(timerI);
            }
          }
        })
        .catch(function (err) {
          console.log(err);
        });
    },
    clickLogin() {
      this.$router.push({
        name: "login",
      });
    },
    clickLogup() {
      if (
        !(
          this.usernameRight &&
          this.passwordRight &&
          this.passwordAgainRight &&
          this.emailRight &&
          this.verifyCodeRight
        )
      ) {
        ElMessage({
          type: "error",
          message: "填写信息格式错误，请进行修改",
        });
        return;
      }
      if(this.form.email != this.codeEmail){
        ElMessage({
          type: "warning",
          message: "填写邮箱与发送验证码时对应邮箱不匹配",
        });
        return;
      }
      if (this.form.verifyCode != this.correctCode) {
        ElMessage({
          type: "error",
          message: "验证码错误",
        });
        return;
      }
      axios
        .get("http://101.42.118.80:8000/log_up/", {
          params: {
            type: "logUp",
            username: this.form.username,
            password: this.form.password,
            email: this.form.email,
            verifyCode: this.form.verifyCode,
          },
        })
        .then((res) => {
          if (res.data["status"] === "ok") {
            ElMessage({
              type: "success",
              message: "注册成功",
            });
            this.$router.push({
              name: "login",
              query: {
                username: this.form.username,
              },
            });
            return;
          } else {
            console.log(res)
            if (res.data["type"] === "sameName") {
              ElMessage({
                type: "error",
                message: "该用户名已注册，请选择其他用户名",
              });
            }
          }
        })
        .catch(function (err) {
          console.log(err);
        });
    },
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
:deep .el-form-item__content {
  margin-left: 86px !important;
}
</style>
