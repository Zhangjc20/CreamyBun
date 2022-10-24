<template>
    <el-container>
        <div class="basic-info-box">
            <el-row :span="12">
                <el-col :span="4">
                    <el-avatar class="big-avatar" :size="100" :src="require('@/assets/images/avatar.jpeg')"></el-avatar>
                </el-col>
                <el-col :span="20">
                    <el-row :span="14" class="info-row-one">
                        <el-col :span="8"><span class="info-row-font">用户名 : test-admin</span></el-col>
                        <el-col :span="8"><span class="info-row-font">手机号 : 13823849322</span></el-col>
                    </el-row>
                    <el-row :span="20" class="info-right-row">
                        <el-col :span="8"><span class="info-row-font">昵称 : 你猜我是谁</span></el-col>
                        <el-col :span="8"><span class="info-row-font">邮箱 : baidu@123.com</span></el-col>
                    </el-row>
                    <el-row :span="20" class="info-right-row">
                        <el-col :span="3"><span class="info-row-font">等级 LV : 1</span></el-col>
                        <el-col :span="5">
                            <el-progress
                                :text-inside="true"
                                :stroke-width="18"
                                :percentage="80"
                                color="#FFF82C"
                                class="exp-bar"
                            />
                        </el-col>
                        <el-col :span="3"><span class="exp-ratio">400/500</span></el-col>
                    </el-row>
                </el-col>
            </el-row>
            <el-row :span="12">
                <div class="change-title">修改信息</div>
                <el-form :model="form" label-width="120px" class="change-form">
                    <el-form-item label="用户名" :required="true">
                    <el-input v-model="form.name" />
                    </el-form-item>
                    <el-form-item label="昵称" :required="true">
                    <el-input v-model="form.name" />
                    </el-form-item>
                    <el-form-item>
                    <el-button type="primary" @click="onSubmit">保存</el-button>
                    <el-button type="info">重置</el-button>
                    </el-form-item>
                </el-form>
            </el-row>
        </div>
    </el-container>
  </template>
  
  <script>
  export default {
    name: 'MineInfoView',
    props: {
    },
    data(){
        return {
            form:{
                name: '',
                region: '',
            }
        }
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped lang="scss">
  .change-title {
    width: 80%;
    text-align: center;
    font-family: YouSheRound;
    font-size: 22px;
    margin-bottom: 20px;
  }
  .exp-ratio {
    line-height: 22px;
  }
  .el-button--primary {
    background-color: #5EABBF;
    border-color: #5EABBF;
    margin-left: 20px;
    margin-right: 10px;
  }

  .el-button--info {
    background-color: #FBE484;
    border-color: #FBE484;
    color:#4E5969;
  }
  .change-form {
    margin-left: 20%;
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
  .basic-info-box {
    width: 100%;
  }
  </style>
  