<template>
  <el-container class="container">
    <el-header class="header-style">
      <NavBar :login="false" activeItem="1" :username="username" :imageUrl="image.src"></NavBar>
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
              <el-select v-model="companyType" style="width: 100%">
                <el-option label="请选择反馈类型" value=""></el-option>
                <el-option
                  v-for="item in companyTypes"
                  :key="item.id"
                  :label="item.value"
                  :value="item.value"
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
            <el-upload
              class="avatar-uploader"
              action="/api/file/upload"
              :show-file-list="false"
              :on-success="handleAvatarSuccess"
              :on-preview="handlePreview"
              :before-upload="beforeAvatarUpload"
            >
              <img v-if="imageUrl" :src="imageUrl" class="avatar" />
              <i v-else class="el-icon-plus avatar-uploader-icon"
                >点击上传图片</i
              >
              <template #tip> 支持格式:.jpg.png </template>
            </el-upload>
          </el-row>
          <el-row class="row2">
            <span class="in-feedback-title">通知邮箱</span>
          </el-row>
          <el-row class="el-row">
            <el-input
              type="textarea"
              :rows="1"
              placeholder="请输出邮箱~"
              v-model="email"
            ></el-input>
          </el-row>
        </div>
        <div class="feedback-title-outer">
          <el-button class="help-button">提交反馈</el-button>
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
export default {
  name: "HelpView",
  components: {
    NavBar,
  },
  data() {
    return {
      image:{
        src:"",
        type:""
      },
      username: "",
      companyType: "",
      imageUrl: "",
      textarea: "",
      email: "",
      tempUrl: "",
      companyTypes: [
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
    handleAvatarSuccess(res, file) {
      this.imageUrl = URL.createObjectURL(file.raw);
    },
    beforeAvatarUpload(file) {
      const isJPG = file.type === "image/jpeg";
      const isLt2M = file.size / 1024 / 1024 < 2;

      if (!isJPG) {
        this.$message.error("上传头像图片只能是 JPG 格式!");
      }
      if (!isLt2M) {
        this.$message.error("上传头像图片大小不能超过 2MB!");
      }
      return isJPG && isLt2M;
    },
  },
  mounted() {
    if (this.$route.query.username) {
      this.username = this.$route.query.username;
      console.log(this.username);
    }
    if (this.$route.query.imageSrc) {
      this.image.src = this.$route.query.imageSrc;
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
  font-family: YouSheRound;
  font-size: 36px;
  color: #5eabbf;
}
.contact-info {
  font-family: YouSheRound;
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
.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}
.avatar-uploader .el-upload:hover {
  border-color: #409eff;
}
.avatar-uploader-icon {
  font-size: 25px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  line-height: 178px;
  text-align: center;
}
.avatar-uploader {
  margin-top: 2px;
  width: 178px;
  height: 178px;
  display: block;
  border: 2px dashed #d9d9d9;
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
.el-button--primary {
  background-color: #5eabbf;
  border-color: #5eabbf;
  width: 100%;
}

.el-button--info {
  background-color: #fbe484;
  border-color: #fbe484;
  color: #4e5969;
}
</style>
