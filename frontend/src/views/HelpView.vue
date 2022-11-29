<template>
  <el-container class="container">
    <el-header class="header-style">
      <NavBar :login="true" activeItem="5" :username="username" :imageUrl="image.src"></NavBar>
    </el-header>
    <el-main class="main-style">
      <div class="feedback-box">
        <div class="feedback-title-outer">
          <span class="feedback-title">反馈问题</span>
        </div>
        <div class="feedback-type">
          <el-row class="el-row">
            <span class="in-feedback-title">反馈类型</span>
          </el-row>
          <el-row class="el-row">
            <el-form-item style="width: 100%">
              <el-select v-model="questionID" style="width: 100%">
                <el-option
                  v-for="item in questionTypes"
                  :key="item.id"
                  :label="item.value"
                  :value="item.id"
                >
                </el-option>
              </el-select>
            </el-form-item>
          </el-row>
          <el-row class="el-row">
            <span class="in-feedback-title">问题描述</span>
          </el-row>
          <el-row>
            <el-input
              type="textarea"
              :rows="6"
              placeholder="请说明问题描述与建议，我们将为您不断改进~"
              v-model="textarea"
            ></el-input>
          </el-row>
          <el-row>
            <div>
              <button id="select_img_button" @click="select_img_button_onclick">选择图片</button>
            </div>
          </el-row>
          <el-row>
            <input type='file' id="inputImgFile" style="display:none" accept="image/*"  @change="inputImgFile_onchange"/>
            <!-- 预览图片S -->
            <el-image id="show_img" :src="require('@/assets/images/logo.png')" style="width:160px;height:160px;"/>
            <!-- 预览图片E -->
          </el-row>
          <el-row class="row2">
            <span class="in-feedback-title">通知邮箱</span>
          </el-row>
          <el-row class="el-row">
            <el-input
              type="textarea"
              :rows="1"
              placeholder="请输入邮箱~"
              v-model="email"
            ></el-input>
          </el-row>
        </div>
        <div class="feedback-title-outer">
          <CustomButton title="提交反馈" fontSize="18px" @click="submitFeedback"></CustomButton>
        </div>
        <div class="feedback-title-outer">
          <span class="feedback-title">联系信息</span>
        </div>
        <div class="feedback-title-outer">
          <pre class="contact-info">
电话：13812341234      邮箱：baidu@123.com</pre
          >
        </div>
      </div>
    </el-main>
  </el-container>
</template>

<script>
// @ is an alias to /src
import NavBar from "@/components/NavBar.vue";
import CustomButton from "@/components/CustomButton.vue";
import { ElMessage } from 'element-plus';
import axios from "axios";
export default {
  name: "HelpView",
  components: {
    NavBar,
    CustomButton
  },
  data() {
    return {
      image:{
        src:"",
        type:""
      },
      imageUrl: "",
      textarea: "",
      email: "",
      questionID: "",
      questionTypes: [
        {
          value: "功能建议",
          id: "1",
        },
        {
          value: "界面优化",
          id: "2",
        },
        {
          value: "产品bug",
          id: "3",
        },
        {
          value: "其它问题",
          id: "4",
        },
      ],
    };
  },
  methods: {
    select_img_button_onclick(){
    var ie = navigator.appName == "Microsoft Internet Explorer" ? true : false;
    var inputImgFile = document.getElementById("inputImgFile");

      if (ie) {
        inputImgFile.click();
      } else {
        var a = document.createEvent("MouseEvents");
        a.initEvent("click", true, true);
        inputImgFile.dispatchEvent(a);
      }
    },
    inputImgFile_onchange()
    {
    var inputImgFile = document.getElementById("inputImgFile");
    var show_img = document.getElementById("show_img");
    var my_data = inputImgFile.files[0];
    this.imageUrl = inputImgFile.files[0];
    // 获取上传图片信息
    var reader = new FileReader();
    // 监听reader对象的的onload事件，当图片加载完成时，把base64编码賦值给预览图片
    reader.addEventListener("load", function () {
        show_img.src = reader.result;
        }, false);
      // 调用reader.readAsDataURL()方法，把图片转成base64
      reader.readAsDataURL(my_data);
    },
    submitFeedback(){
      if(!this.textarea){
        ElMessage({
          type:"warning",
          message:"描述不可为空"
        })
        return;
      }
      if(!this.email.match(/[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+/g)){
        ElMessage({
          type:"warning",
          message:"邮箱格式不正确"
        })
        return;
      }
      let formData = new FormData();
      formData.append("email", this.email);
      formData.append("questionType", this.questionID);
      formData.append("textarea", this.textarea);
      formData.append("image", this.imageUrl);
      axios({
              method:"Post",
              url:'http://localhost:8000/submit_feedback/',
              headers: {
            //请求头这个一定要写
                'Content-Type': 'multipart/form-data',
            },
              data:formData
      })
      .then((res)=>{
        if(res.data['status']==='ok'){
          ElMessage({
            type:'success',
            message:"反馈已经收到，感谢您的支持~"
          });
          console.log(res);
        }
        else{
          ElMessage({
            type:'error',
            message:"反馈失败"
          });
        }
      })
    },
  },
  mounted() {
    if (localStorage.getItem('username')) {
      this.username = localStorage.getItem('username');
    }
    if(!localStorage.getItem('avatar')){
      axios.get('/get_avatar',{
        params:{
          username:this.username
        }
      })
      .then((res)=>{
        if(res.data['status']==='ok'){
          this.image.src = "data:image/png;base64,"+res.data['avatar'];
          localStorage.setItem('avatar',this.image.src);
        }
      })
    }
    else{
      this.image.src = localStorage.getItem('avatar');
    }
  },
};
</script>

<style scoped>
.container {
  margin: 0;
  height: 100%;
}
.icon {
  width: 3em;
  height: 3em;
  margin-top: 24px;
  vertical-align: -0.15em;
  fill: currentColor;
  overflow: hidden;
}
.round-back-font {
  position: relative;
  top: 70px;
  font-size: 26px;
  margin-left: 16px;
  font-family: YouSheBlack;
  color: #e8bf19;
}
.round-background {
  position: relative;
  top: 50px;
  left: 60px;
  background-color: #ffffff;
  box-shadow: 0 0 6px 1px rgba(0, 0, 0, 0.4);
  border-radius: 50px;
  width: 100px;
  height: 100px;
}
.feedback-title-outer {
  margin-top: 50px;
  margin-bottom: 50px;
}
.feedback-title {
  font-family: YouSheRound;;
  font-size: 36px;
  color: #5eabbf;
}
.contact-info {
  font-family: XiaWuManHei;;
  font-size: 23px;
  color: #5eabbf;
}
.in-feedback-title {
  font-family: YouSheRound;
  font-size: 26px;
  color: #060707;
  float: left;
}
.feedback-box {
  border-radius: 20px;
  height: 1080px;
  width: 40%;
  margin-left: 30%;
}
.main-style {
  background-color: transparent;
}
.header-style {
  background-image: url(@/assets/images/nav-background.png);
  background-size: cover;
  height: 60px;
  box-shadow: 0 0px 8px 0;
  display: flex;
}
.el-row {
  margin-bottom: 20px;
}
.row2 {
  margin-top: 40px;
}
.help-button {
  color: #ffffff;
  width: 20%;
  font-size: 18px;
  background-color: #fbe484;
  border-color: #fbe484;
  height: 36px;
}
.help-button:hover {
  background-color: #e8d173;
  color: #ffffff;
  border-color: #e8d173;
}
.el-button--active {
  background-color: #e8d173;
  border-color: #e8d173;
}
.exp-ratio {
  line-height: 22px;
}
</style>
