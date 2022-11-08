<template>
  <el-container>
      <div class="background-box">
          <div class="main-box">
              <div class="logo"></div>
                <el-form
                class="login-form"
                ref="ruleFormRef"
                status-icon
            >
                <el-form-item required>
                    <el-input clearable v-model="form.username" placeholder="请输入用户名">
                        <template #prefix>
                            <svg class="icon" aria-hidden="true">
                                <use xlink:href="#icon-user"></use>
                            </svg>
                        </template>
                    </el-input>
                </el-form-item>
                <el-form-item required>
                    <el-input clearable v-model="form.password" show-password placeholder="请输入密码">
                        <template #prefix>
                            <svg class="icon icon-lock-change" aria-hidden="true">
                                <use xlink:href="#icon-lock"></use>
                            </svg>
                        </template>
                    </el-input>
                </el-form-item>
                <el-form-item required>
                  <div class="link-box">
                    <el-link type="primary" class="logup-link" @click="clickLogup">没有账号？立即注册</el-link>
                    <el-link type="primary" class="logreset-link" @click="clickLogreset">忘记密码</el-link>
                  </div>
                </el-form-item>
                <el-form-item>
                    <el-button class="login-button" @click="clickLogin"
                        >登录</el-button
                    >
                </el-form-item>
              </el-form>
          </div>
      </div>
  </el-container>
</template>

<script>
import axios from 'axios';
import { ElMessage } from 'element-plus';
export default {
  name: 'MineInfoView',
  props: {
  },
  data(){
      return {
          form:{
              username: '',
              password: '',
          }
      }
  },
  methods:{
    clickLogup(){
      this.$router.push({
            name: 'logup',
        });
    },
    clickLogreset(){
      this.$router.push({
            name: 'logreset',
        });
    },
    clickLogin(){
      sessionStorage.setItem("token", 'true');
      axios.get('/log_in',{
        params:{
          username:this.username,
          password:this.password
        }
      })
      .then(res=>{
        if(res.data['status']==='wrong'){
          if(res.data['type']==='noUser'){
            ElMessage({
              type: 'error',
              message: "用户不存在",
            })
          }
          else if(res.data['type']==='wrongPassword'){
            ElMessage({
              type: 'error',
              message: "密码错误",
            })
          }
          else{
            ElMessage({
              type: 'error',
              message: "登录失败，请稍后再试",
            })
          }
        }
        else if(res.data['status']==='ok'){
          ElMessage({
              type: 'success',
              message: "登录成功",
          });
          this.$router.push({
              name: 'home',
              query:{
                username:this.form.username
              },
          });
        }
      })
      .catch(function(err){
        console.log(err);
      });
    },
  },
  mounted(){
    if(this.$route.query.username){
      this.form.username = this.$route.query.username;
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.el-container {
  height: 100%;
}
.main-box{
  width: 450px;
  height: 400px;
  background-color: white;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  margin: auto;
  border-radius:15px;
}
.link-box {
  width:100%;
}
.icon {
  width: 1em;
  height: 1em;
  vertical-align: -0.15em;
  fill: currentColor;
  overflow: hidden;
}
.logo {
  width: 110px;
  height: 100px;
  text-align: center;
  background: url(../assets/images/logo.png);
  background-size: 100% 100%;
  margin:0 auto;
  margin-bottom: 20px;
  margin-top: 40px;
}
.logreset-link {
  float: right;
  position: relative;
  right:0%;
}
.logup-link {
  float: left;
  position: relative;
  left:0%;
}
.login-button {
    color:#ffffff;
    width: 100%;
    font-size: 18px;
    background-color: #FBE484;
    border-color: #FBE484;
    height: 36px;
  }
.login-button:hover,.logup-outer .el-button:focus {
    background-color: #e8d173;
    color:#ffffff;
    border-color: #e8d173;
  }
.el-button--active {
    background-color: #e8d173;
    border-color: #e8d173;
  }
.exp-ratio {
  line-height: 22px;
}
.el-button--primary {
  background-color: #5EABBF;
  border-color: #5EABBF;
  width :100%;
}

.el-button--info {
  background-color: #FBE484;
  border-color: #FBE484;
  color:#4E5969;
}
.login-form {
  margin-left: 20%;
  margin-right: 20%;
}
.info-row-one {
  margin-top: 12%;
  padding-left: 60px;
}
::v-deep .el-progress-bar__innerText{
  color: #54501d;
}
.exp-bar {
  margin-top: 2px;
}
.info-row-font {
  float:left;
}
.info-right-row {
  margin-top: 1%;
  padding-left: 60px;
  color: #4E5969;
}
.big-avatar {
  margin-left: 50px;
  margin-top: 50%;
  margin-bottom: 50%;
}
.background-box {
  width: 100%;
  height: 100%;
  background: url(../assets/images/background.png);
  background-size: 100% 100%;
  text-align: center;
}

</style>
