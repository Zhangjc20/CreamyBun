<template>
  <el-dialog title="发送邮件" v-model="dialogVisible" center width="580px">
    <div
      style="
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
      "
    >
      <el-form :inline="true">
        <el-form-item>
          <el-input
            style="width: 380px"
            v-model="emailContent"
            placeholder="请输入邮件内容"
            type="textarea"
            :autosize="{ minRows: 5, maxRows: 5 }"
          ></el-input>
        </el-form-item>
      </el-form>
      <p style="color: #f00">
        提示: 点击发送邮件将发送到{{ props.inform_email }}
      </p>
      <p style="color: #f00"></p>
      <div class="button-box">
        <el-row>
          <CustomButton
            title="发送"
            normalColor="#fbe484"
            focusColor="#fbe487"
            hoverColor="#4E98AB"
            @click="sendTheEmail"
          />
          <CustomButton
            title="取消"
            marginLeft="60px"
            normalColor="#fbe484"
            focusColor="#fbe487"
            hoverColor="#4E98AB"
            @click="CancelSendEmail"
          />
        </el-row>
      </div>
    </div>
  </el-dialog>
  <div class="task-container" v-if="isSpace">
    <div class="task-container-inner"></div>
  </div>
  <div class="task-container" v-else>
    <div class="task-container-inner" style="border: 2px solid #e9e9e9">
      <div style="float: left">
        <el-image
          :src="image.src ? image.src : require('@/assets/images/avatar.jpeg')"
          style="width: 220px; height: 180px"
        ></el-image>
      </div>
      <div class="color-bg-box" style="float: right">
        <div class="information-box">
          <el-row>
            <div class="title-font">问题类型 : {{ props.feedback_type }}</div>
          </el-row>
          <el-row>
            <div class="email-font">通知邮箱：{{ props.inform_email }}</div>
          </el-row>
          <el-row>
            <div class="email-font">问题描述：{{ props.description }}</div>
          </el-row>
          <el-row>
            <div class="email-font">反馈内容：{{ emailContent }}</div>
          </el-row>
        </div>
        <div class="button-box">
          <el-row>
            <CustomButton
              title="删除反馈"
              normalColor="#fbe484"
              focusColor="#fbe487"
              hoverColor="#e3cc73"
              @click="deleteFeedback"
            />
            <CustomButton
              title="发送邮件"
              marginLeft="40px"
              normalColor="#fbe484"
              focusColor="#fbe487"
              hoverColor="#e3cc73"
              @click="sendEmail"
            />
          </el-row>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CustomButton from "./CustomButton.vue";
import axios from "axios";
import { ElMessage } from "element-plus";
export default {
  name: "SingleFeedback",
  components: {
    CustomButton,
  },
  props: {
    props: {
      type: Object,
      default: undefined,
    },
  },
  data() {
    return {
      dialogVisible: false,
      emailContent: "",
      starNum: this.props.starNum,
      isSpace: this.props.isSpace,
      image: {
        src: null,
        type: null,
      },
    };
  },
  methods: {
    base64ImgtoFile(dataurl, filename = "file") {
      const arr = dataurl.split(",");
      const mime = arr[0].match(/:(.*?);/)[1];
      const suffix = mime.split("/")[1];
      const bstr = atob(arr[1]);
      let n = bstr.length;
      const u8arr = new Uint8Array(n);
      while (n--) {
        u8arr[n] = bstr.charCodeAt(n);
      }
      return new File([u8arr], `${filename}.${suffix}`, {
        type: mime,
      });
    },
    sendEmail() {
      this.dialogVisible = true; //显示弹窗
    },
    sendTheEmail() {
      this.dialogVisible = false; //关闭弹窗
      let formData = new FormData();
      formData.append("email", this.props.inform_email);
      formData.append("content", this.emailContent);
      axios({
        method: "Post",
        url: "http://localhost:8000/handle_feedback_email/",
        headers: {
          //请求头这个一定要写
          "Content-Type": "multipart/form-data",
        },
        data: formData,
      })
        .then((res) => {
          if (res.data["status"] === "ok") {
            ElMessage({
              type: "success",
              message: "邮件发送成功",
            });
            return;
          }
        })
        .catch(function (err) {
          this.emailContent = "";
          console.log(err);
        });
    },
    CancelSendEmail() {
      this.emailContent = "";
      this.dialogVisible = false; //关闭弹窗
    },
    deleteFeedback() {
      let formData = new FormData();
      formData.append("email", this.props.inform_email);
      formData.append("description", this.props.description);
      formData.append("type", this.props.feedback_type);
      axios({
        method: "Post",
        url: "http://localhost:8000/delete_feedback/",
        headers: {
          //请求头这个一定要写
          "Content-Type": "multipart/form-data",
        },
        data: formData,
      })
        .then((res) => {
          if (res.data["status"] === "ok") {
            return;
          }
        })
        .catch(function (err) {
          this.emailContent = "";
          console.log(err);
        });
    },
  },
  mounted() {
    this.isSpace = this.props.isSpace;
    this.starNum = this.props.starNum;
    const imageFile = this.base64ImgtoFile(
      "data:image/png;base64," + this.props.image_url
    );
    this.image.src =
      window.webkitURL.createObjectURL(imageFile) ||
      window.URL.createObjectURL(imageFile);
    localStorage.setItem("imageSrc", this.image.src);
  },
};
</script>

<style scoped>
.task-container {
  background-color: transparent;
  width: 100%;
  height: 200px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.donut-num {
  line-height: 34px;
  font-size: 16px;
  text-align: left;
}
.title-font {
  padding-top: 4px;
  margin-left: 10px;
  text-align: left;
  color: #ffffff;
}
.email-font {
  padding-top: 4px;
  margin-left: 10px;
  text-align: left;
  color: #fff958;
}
.description-font {
  padding-top: 4px;
  margin-left: 10px;
  text-align: left;
  color: #fff958;
}
.task-container-inner {
  width: 700px;
  border-radius: 6px;
}
.color-bg-box {
  position: relative;
  background-color: #4dafc7;
  width: 480px;
  height: 180px;
}
.icon {
  width: 1em;
  height: 1em;
  vertical-align: -0.15em;
  fill: currentColor;
  overflow: hidden;
}
.donut-font {
  font-size: 14px;
  color: #fff958;
  margin-bottom: -4px;
  margin-top: -2px;
}
.time-font {
  font-size: 14px;
  color: #ffffff;
  margin-top: 6px;
  padding-bottom: 4px;
}
.type-font {
  font-size: 16px;
  color: #face3c;
}
.button-box {
  position: absolute;
  bottom: 1px;
  left: 50%;
  transform: translate(-50%, -50%);
}
:deep .el-rate .el-rate__icon {
  margin-right: 0;
}
</style>
