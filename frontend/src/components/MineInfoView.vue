<template>
  <div class="basic-info-box">
    <el-row class="basic-info-box-inner">
      <el-col :span="6" class="left-info-box">
        <div class="avatar-box">
          <el-avatar
            :size="100"
            :src="require('@/assets/images/avatar.jpeg')"
          ></el-avatar>
        </div>
      </el-col>
      <el-col class="right-info-box" :span="18">
        <div class="describe-inner">
          <el-descriptions class="margin-top" :column="2" border>
            <el-descriptions-item :span="1">
              <template #label>
                <div class="cell-item">
                  <el-icon>
                    <user />
                  </el-icon>
                  用户名
                </div>
              </template>
              helloworld
            </el-descriptions-item>
            <el-descriptions-item :span="1">
              <template #label>
                <div class="cell-item">
                  <el-icon>
                    <iphone />
                  </el-icon>
                  手机号
                </div>
              </template>
              18100000000
            </el-descriptions-item>
            <el-descriptions-item :span="1">
              <template #label>
                <div class="cell-item">
                  <svg class="icon" aria-hidden="true">
                    <use xlink:href="#icon-tiantianquan"></use>
                  </svg>
                  甜甜圈
                </div>
              </template>
              6660
            </el-descriptions-item>
            <el-descriptions-item :span="1">
              <template #label>
                <div class="cell-item">
                  <el-icon>
                    <office-building />
                  </el-icon>
                  邮箱
                </div>
              </template>
              baidu.com
            </el-descriptions-item>
          </el-descriptions>
          <div class="level-box">
            <span>信誉等级 LV 5</span>
            <el-progress
              class="level-progress"
              :text-inside="true"
              :stroke-width="22"
              :percentage="80"
              status="warning"
            />
            <span>400/500</span>
          </div>
        </div>
      </el-col>
    </el-row>
  </div>
  <div class="change-form-area">
    <div class="change-title">修改信息</div>
    <el-row>
      <el-col :span="12">
        <el-form :model="changeForm" label-width="120px" class="change-form">
          <el-form-item label="用户名">
            <el-input v-model="changeForm.username" class="info-input" />
          </el-form-item>
          <el-form-item label="">
            <CustomButton title="修改用户名" :props="normalProps" @click="handleChangeName"></CustomButton>
          </el-form-item>
          <el-form-item label="邮箱">
            <el-input v-model="changeForm.email" class="info-input" />
          </el-form-item>
          <el-form-item label="">
            <CustomButton title="修改邮箱" :props="normalProps" @click="handleChangeEmail"></CustomButton>
          </el-form-item>
          <el-form-item label="手机号">
            <el-input v-model="changeForm.phone" class="info-input" />
          </el-form-item>
          <el-form-item label="">
            <CustomButton title="修改手机号" :props="normalProps" @click="handleChangePhone"></CustomButton>
          </el-form-item>
        </el-form>
      </el-col>
      <el-col :span="12">
        <CustomButton :props="changePassProps" title="忘记密码" @click="handleChangePass"></CustomButton>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import CustomButton from './CustomButton.vue';
import { ElMessage, ElMessageBox } from 'element-plus';
export default {
  name: "MineInfoView",
  components:{
    CustomButton
  },
  data() {
    return {
      normalProps:{
        width:'110px',
        height:'32px',
        normalColor:'#5EABBF',
        fontSize:'14px',
        fontColor:'#ffffff',
        hoverColor:'#5299AB',
        focusColor:"#5299AB"
      },
      changePassProps:{
        width:'100px',
        height:'36px',
        normalColor:'#5EABBF',
        fontSize:'15px',
        fontColor:'#ffffff',
        hoverColor:'#5299AB',
        focusColor:"#5299AB"
      },
      changeForm: {
        username: "",
        email: "",
        phone:"",
      },
    };
  },
  methods:{
    handleChangePass(){
      this.$router.push({
            name: 'logreset',
        });
    },
    handleChangeName(){
      // axios.get()
      // .then(function (response) {
      //   console.log(response);//考虑重名
      // })
      // .catch(function (error) {
      //   console.log(error);
      // });
    },
    handleChangeEmail(){
      // axios.get()
      // .then(function (response) {
      //   console.log(response);//考虑是否和当前邮箱一样
      // })
      // .catch(function (error) {
      //   console.log(error);
      // });
      ElMessageBox.prompt('请输入发送到某邮箱的验证码（请勿关闭当前窗口）', '修改邮箱', {
        confirmButtonText: '确认',
        cancelButtonText: '取消',
        inputPattern:
          /[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/,
        inputErrorMessage: '邮箱格式无效',
      })
        .then(({ value }) => {
          ElMessage({
            type: 'success',
            message: `您的邮箱成功修改成:${value}`,
          })
        })
        .catch(() => {
          ElMessage({
            type: 'info',
            message: '取消修改邮箱',
          })
        })
    },
    handleChangePhone(){
      //留待接口
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.icon {
  width: 1em;
  height: 1em;
  vertical-align: -0.15em;
  fill: currentColor;
  overflow: hidden;
}
.info-input {
  width: 300px;
}
.change-form {
  padding: 0 100px 0 40px;
}
.change-title {
  font-family: YouSheRound;
  font-size: 24px;
  padding: 20px 0 20px 0;
}
.change-form-area {
  width: 100%;
  border-radius: 10px;
  margin-top: 40px;
  box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
  padding: 0 0 20px 0;
}
.avatar-box {
  border-radius: 10px;
  width: 140px;
  height: 140px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.avatar-box:hover {
  background-color: #f8f8f8;
}
.level-progress {
  width: 200px;
  margin: 0 10px 0 10px;
}
.level-box {
  margin-top: 20px;
  display: flex;
}
.describe-inner {
  margin: 0 30px 0 10px;
}
.basic-info-box-inner {
  height: 200px;
}
.left-info-box {
  justify-content: center;
  display: flex;
  align-items: center;
}
.right-info-box {
  flex-direction: column;
  justify-content: center;
  display: flex;
}
.basic-info-box {
  width: 100%;
  border-radius: 10px;
  box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
  margin-top: 30px;
}
</style>
