<template>
  <el-container class="logreset">
    <div class="logreset-box">
      <div class="logreset-title">
        <span class="log-account-font">重置密码</span>
        <el-link type="primary" class="login-link" @click="clickLogin"
          >立即登录</el-link
        >
      </div>
      <el-form
        class="form-box"
        ref="ruleFormRef"
        status-icon
        :rules="rules"
        :model="form"
      >
        <el-form-item label="重置方式" prop="isUsername">
          <el-radio v-model="form.isUsername" :label="true">用户名</el-radio>
          <el-radio v-model="form.isUsername" :label="false">邮箱</el-radio>
        </el-form-item>

        <div v-if="form.isUsername">
          <el-form-item required prop="username">
            <el-input
              clearable
              v-model="form.username"
              placeholder="请输入用户名"
            >
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
        <el-form-item required class="verify-button" prop="verifyCode">
          <el-col :span="14"
            ><el-input
              placeholder="请输入验证码"
              clearable
              v-model="form.verifyCode"
            >
              <template #prefix>
                <span
                  class="iconfont icon-verify-fill icon-verify-change"
                ></span>
              </template> </el-input
          ></el-col>
          <el-col :span="10"
            ><el-button class="get-verify" @click="clickGetCode"
              >获取验证码</el-button
            ></el-col
          >
        </el-form-item>
        <el-form-item required prop="password">
          <el-input
            clearable
            v-model="form.password"
            show-password
            placeholder="请输入想要重置的密码"
          >
            <template #prefix>
              <svg class="icon icon-lock-change" aria-hidden="true">
                <use xlink:href="#icon-lock"></use>
              </svg>
            </template>
          </el-input>
        </el-form-item>
        <el-form-item required prop="passwordAgain">
          <el-input
            clearable
            v-model="form.passwordAgain"
            show-password
            placeholder="请确认密码"
          >
            <template #prefix>
              <svg class="icon icon-lock-change" aria-hidden="true">
                <use xlink:href="#icon-lock"></use>
              </svg>
            </template>
          </el-input>
        </el-form-item>

        <el-form-item class="logreset-outer">
          <el-button class="logreset-button" @click="clickLogreset"
            >重置密码</el-button
          >
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
      } else if (value.search(/[a-z\d]{5,12}/g) == -1) {
        this.usernameRight = false;
        callback(new Error("请输入5-12位字母和数字的组合"));
      } else {
        this.usernameRight = true;
        callback();
      }
    };
    const validatePassword = (rule, value, callback) => {
      if (value === "") {
        this.passwordRight = false;
        callback(new Error("密码不能为空"));
      } else if (value.search(/[a-z\d]{6,18}/g) == -1) {
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
        value.search(
          /[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+/
        ) == -1
      ) {
        this.emailRight = false;
        callback(new Error("邮箱格式不合法"));
      } else {
        this.emailRight = true;
        callback();
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
        verifyCode: "",
        isUsername: true,
      },
      correctCode: "",
      usernameRight: false,
      passwordRight: false,
      passwordAgainRight: false,
      emailRight: false,
      verifyCodeRight: false,
      emailing: false,
      codeEmail: "", //发来的验证码对应的email
      codeUsername: "", //发来验证码对应的username
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
    clickLogin() {
      this.$router.push({
        name: "login",
      });
    },
    clickGetCode() {
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
      this.codeUsername = this.form.username;
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
      if (this.form.isUsername) {
        axios
          .get("/log_reset", {
            params: {
              type: "getVerifyCode",
              resetWay: "username",
              username: this.codeUsername,
            },
          })
          .then((res) => {
            if (res.data["status"] === "ok") {
              this.correctCode = res.data["verifyCode"];
              let realEmail = res.data["email"];
              ElMessage({
                type: "success",
                message: `验证码发送成功，请在${this.blurEmail(realEmail)}查收`,
              });
              console.log(this.correctCode);
              return;
            } else if (res.data["status"] === "wrong") {
              ElMessage({
                type: "error",
                message: "验证码发送失败",
              });
              this.emailing = false;
              this.emailingSeconds = 0;
              clearTimeout(timerT);
              clearInterval(timerI);
            }
            console.log("error");
          })
          .catch(function (err) {
            console.log(err);
          });
      } else {
        axios
          .get("/log_reset", {
            params: {
              type: "getVerifyCode",
              resetWay: "email",
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
              console.log(this.correctCode);
              return;
            } else if (res.data["status"] === "wrong") {
              ElMessage({
                type: "error",
                message: "验证码发送失败",
              });
              this.emailing = false;
              this.emailingSeconds = 0;
              clearTimeout(timerT);
              clearInterval(timerI);
            }
            console.log("error");
          })
          .catch(function (err) {
            console.log(err);
          });
      }
    },
    clickLogreset() {
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
      if (this.form.email != this.codeEmail) {
        ElMessage({
          type: "warning",
          message: "填写邮箱与发送验证码时对应邮箱不匹配",
        });
        return;
      }
      if (this.form.username != this.codeUsername) {
        ElMessage({
          type: "warning",
          message: "填写用户名与发送验证码时对应用户名不匹配",
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
      if (this.isUsername) {
        axios
          .get("/log_reset", {
            params: {
              type: "resetPassword",
              resetWay: "username",
              username: this.codeUsername,
              password: this.form.password
            },
          })
          .then((res) => {
            if (res.data["status"] === "ok") {
              ElMessage({
                type: "success",
                message: "重置密码成功",
              });
              this.$router.push({
                name: "login",
              });
              return;
            } else {
                ElMessage({
                  type: "error",
                  message: "重置失败",
                });
            }
          })
          .catch(function (err) {
            console.log(err);
          });
      }
      else{
        axios
          .get("/log_reset", {
            params: {
              type: "resetPassword",
              resetWay: "email",
              email: this.codeEmail,
              password: this.form.password
            },
          })
          .then((res) => {
            if (res.data["status"] === "ok") {
              ElMessage({
                type: "success",
                message: "重置密码成功",
              });
              this.$router.push({
                name: "login",
                query: {
                  username: this.form.username,
                },
              });
              return;
            } else {
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
      }
    },
    blurEmail(email) {
      var [front, end] = email.split("@");
      if (front.length <= 1) {
        return email;
      } else if (front.length <= 4) {
        return front.slice(0, 2) + "*" * (front.length - 2) + end;
      } else {
        return "**" + front.slice(2, -2) + "**" + end;
      }
    },
  },
};
</script>

<style scoped lang="scss">
.el-form-item {
  margin-bottom: 26px;
}
.logreset-button {
  color: #ffffff;
  width: 100%;
  font-size: 18px;
  background-color: #fbe484;
  border-color: #fbe484;
  height: 36px;
}
.logreset-button:hover,
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
