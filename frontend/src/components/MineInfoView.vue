<template>
  <div class="mine-info-container">
    <vue-final-modal
      v-model="showModal"
      classes="modal-container"
      content-class="modal-content"
      :debounce="false"
      :prevent-click="true"
      stencil-component="circle-stencil"
    >
      <div class="modal-title">图片裁剪</div>
      <image-cropper
        ref="cropper"
        class="cropper"
        :src="image.src"
        :auto-zoom="true"
        :stencil-size="{
          width: 400,
          height: 400,
        }"
        stencil-component="circle-stencil"
      />
      <div class="button-area">
        <CustomButton title="确认" @click="handleConfirm" marginRight="30px" />
        <CustomButton title="剪切" @click="handleCrop" />
      </div>
    </vue-final-modal>
    <input
      type="file"
      ref="file"
      @change="loadImage($event)"
      accept="image/*"
      class="file-input"
    />
    <div class="basic-info-box">
      <el-row class="basic-info-box-inner">
        <el-col :span="6" class="left-info-box">
          <div class="avatar-box" @click="uploadAvatar">
            <el-avatar
              :size="100"
              :src="
                image.src ? image.src : require('@/assets/images/avatar.jpeg')
              "
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
                {{ username }}
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
                {{ phoneNumber }}
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
                {{ donutNumber }}
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
                {{ email }}
              </el-descriptions-item>
            </el-descriptions>
            <div class="level-box">
              <span>信誉等级 LV {{ creditRank }}</span>
              <el-progress
                class="level-progress"
                :text-inside="true"
                :stroke-width="22"
                :percentage="percentage"
              />
              <span>{{ currentExp }}/{{ expForUpgrade }}</span>
            </div>
          </div>
        </el-col>
      </el-row>
    </div>
    <div class="change-form-area">
      <div class="change-title">修改信息</div>
      <el-row>
        <el-col :span="12">
          <el-form
            :model="changeForm"
            label-width="120px"
            class="change-form"
            :rules="rules"
          >
            <el-form-item label="用户名" prop="username">
              <el-input
                v-model="changeForm.username"
                maxlength="12"
                class="info-input"
                clearable
              />
            </el-form-item>
            <el-form-item label="">
              <CustomButton
                title="修改用户名"
                :props="normalProps"
                @click="handleChangeName"
              ></CustomButton>
            </el-form-item>
            <el-form-item label="邮箱" prop="email">
              <el-input
                v-model="changeForm.email"
                class="info-input"
                clearable
              />
            </el-form-item>
            <el-form-item label="">
              <CustomButton
                title="修改邮箱"
                :props="normalProps"
                @click="handleChangeEmail"
              ></CustomButton>
            </el-form-item>
            <el-form-item label="手机号">
              <el-input v-model="changeForm.phone" class="info-input" />
            </el-form-item>
            <el-form-item label="">
              <CustomButton
                title="修改手机号"
                :props="normalProps"
                @click="handleChangePhone"
              ></CustomButton>
            </el-form-item>
          </el-form>
        </el-col>
        <el-col :span="12">
          <CustomButton
            :props="changePassProps"
            title="忘记密码"
            @click="handleChangePass"
          ></CustomButton>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import CustomButton from "./CustomButton.vue";
import axios from "axios";
import { ElMessage, ElMessageBox } from "element-plus";
function getMimeType(file, fallback = null) {
  const byteArray = new Uint8Array(file).subarray(0, 4);
  let header = "";
  for (let i = 0; i < byteArray.length; i++) {
    header += byteArray[i].toString(16);
  }
  switch (header) {
    case "89504e47":
      return "image/png";
    case "47494638":
      return "image/gif";
    case "ffd8ffe0":
    case "ffd8ffe1":
    case "ffd8ffe2":
    case "ffd8ffe3":
    case "ffd8ffe8":
      return "image/jpeg";
    default:
      return fallback;
  }
}
export default {
  name: "MineInfoView",
  components: {
    CustomButton,
  },
  props: {
    username: {
      type: String,
      default: "",
    },
  },
  data() {
    const validateUsername = (rule, value, callback) => {
      if (value === "") {
        this.usernameRight = false;
        callback(new Error("用户名不能为空"));
      } else if (value.match(/[a-z\d]{5,12}/g)) {
        this.usernameRight = true;
        callback();
      } else {
        this.usernameRight = false;
        callback(new Error("请输入5-12位字母和数字的组合"));
      }
    };
    const validateEmail = (rule, value, callback) => {
      if (
        value.match(
          /[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+/g
        )
      ) {
        this.emailRight = true;
        console.log("asd");
        callback();
      } else {
        this.emailRight = false;
        console.log("asasdfasd");
        callback(new Error("邮箱格式不合法"));
      }
    };
    return {
      verifyCode: "",
      usernameRight: false,
      emailRight: false,
      rules: {
        username: [
          {
            validator: validateUsername,
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
      },
      showModal: false,
      image: {
        src: null,
        type: null,
      },
      normalProps: {
        width: "110px",
        height: "32px",
        normalColor: "#5EABBF",
        fontSize: "14px",
        fontColor: "#ffffff",
        hoverColor: "#5299AB",
        focusColor: "#5299AB",
        isRound:true,
      },
      changePassProps: {
        width: "100px",
        height: "36px",
        normalColor: "#5EABBF",
        fontSize: "15px",
        fontColor: "#ffffff",
        hoverColor: "#5299AB",
        focusColor: "#5299AB",
        isRound:true,
      },
      changeForm: {
        username: "",
        email: "",
        phone: "",
      },
      phoneNumber: "12345678901",
      inited: false,
      donutNumber: -1,
      creditRank: 0,
      currentExp: -1,
      expForUpgrade: -1,
      email: "",
      percentage: 0,
      codeEmail: "",
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
    blobToFile(blob, fileName, mimeType) {
      return new File([blob], fileName, { type: mimeType });
    },
    handleConfirm() {
      this.showModal = false;
      this.crop(true);
      this.$refs.file.value = "";
    },
    handleCrop() {
      this.crop();
    },
    crop(emit) {
      const { canvas } = this.$refs.cropper.getResult();
      canvas.toBlob((blob) => {
        if (this.image.src) {
          URL.revokeObjectURL(this.image.src);
        }
        this.image.src = URL.createObjectURL(blob);
        var formData = new FormData();
        if (emit) {
        this.$emit('changeAvatar',this.image.src)
        formData.append(
          "image",
          this.blobToFile(blob, this.image.type.split("/")[1], this.image.type)
        );
        console.log("this.blobToFile(blo", this.blobToFile(blob, this.image.type.split("/")[1], this.image.type))
        formData.append("username", this.username);
        axios
          .post("/change_avatar", formData, {
            query: {
              username: this.username,
            },
          })
          .then((res) => {
            console.log(res);
          })
          .catch((err) => {
            console.log(err);
          });
      }}, this.image.type);
    },
    loadImage(event) {
      // DOM input组件得引用
      const { files } = event.target;
      // 确保有文件
      if (files && files[0]) {
        // 如果存在要销毁
        if (this.image.src) {
          URL.revokeObjectURL(this.image.src);
        }
        // 创建blob链接
        const blob = URL.createObjectURL(files[0]);

        // 创建FileReader读取图片的二进制数据
        const reader = new FileReader();
        // 定义回调函数->当FileReader运行完毕
        reader.onload = (e) => {
          this.image = {
            //设定src
            src: blob,
            //确定图片类型保证从画布中提取图片无误
            type: getMimeType(e.target.result, files[0].type),
          };
        };
        //以url读取图片(base64 format)
        reader.readAsArrayBuffer(files[0]);
        this.showModal = true;
        this.uploaded = true;
      }
    },
    uploadAvatar() {
      ElMessageBox.confirm("是否要上传头像?", "修改头像", {
        confirmButtonText: "确认",
        cancelButtonText: "取消",
      })
        .then(() => {
          this.$refs.file.click();
        })
        .catch(() => {});
    },
    getRatio() {
      return Math.floor((this.currentExp / this.expForUpgrade) * 1000) / 10;
    },
    handleChangePass() {
      this.$router.push({
        name: "logreset",
      });
    },
    handleChangeName() {
      if (!this.usernameRight) {
        ElMessage({
          type: "error",
          message: "用户名格式错误",
        });
        return;
      }
      ElMessageBox.confirm(
        "确定要修改用户名为" + this.changeForm.username,
        "修改用户名",
        {
          confirmButtonText: "确认",
          cancelButtonText: "取消",
          type: "info",
        }
      )
        .then(() => {
          var formData = new FormData();
          formData.append("username", this.username);
          formData.append("newUsername", this.changeForm.username);
          axios
            .post("/update_username", formData)
            .then((res) => {
              if (res.data["status"] === "ok") {
                ElMessage({
                  type: "success",
                  message: "修改成功",
                });
                this.$emit("changeUsername", res.data["newUsername"]);
                this.$router.push({
                  name: "mine",
                  query: {
                    username: res.data["newUsername"],
                  },
                });
              } else {
                if (res.data["type"] === "sameName") {
                  //用户名被注册过
                  ElMessage({
                    type: "error",
                    message: "该用户名已被注册",
                  });
                }
              }
            })
            .catch(function (error) {
              console.log(error);
            });
        })
        .catch(() => {});
    },
    handleChangeEmail() {
      if (!this.emailRight) {
        ElMessage({
          type: "error",
          message: "邮箱格式错误",
        });
        return;
      }
      ElMessageBox.confirm(
        "确定要修改邮箱为" + this.changeForm.email,
        "修改用户名",
        {
          confirmButtonText: "确认",
          cancelButtonText: "取消",
          type: "info",
        }
      )
        .then(() => {
          axios
            .get("/update_email", {
              params: {
                username: this.username,
                newEmail: this.changeForm.email,
                type: "getVerifyCode",
              },
            })
            .then((res) => {
              console.log(res);
              //考虑是否和当前邮箱一样
              if (res.data["status"] === "ok") {
                ElMessage({
                  type: "success",
                  message: "邮箱验证码发送成功",
                });
                this.codeEmail = this.changeForm.email;
                this.verifyCode = res.data["verifyCode"];
                ElMessageBox.prompt(
                  "请输入发送到对应邮箱的验证码（请勿关闭当前窗口）",
                  "修改邮箱",
                  {
                    confirmButtonText: "确认",
                    cancelButtonText: "取消",
                    inputPattern: /\d{6}/,
                    inputErrorMessage: "验证码格式无效",
                  }
                )
                  .then(({ value }) => {
                    if (this.changeForm.email != this.codeEmail) {
                      ElMessage({
                        type: "error",
                        message: "输入邮箱需要和发送验证码时邮箱填写一致",
                      });
                    } else {
                      if (value == this.verifyCode) {
                        axios
                          .get("/update_email", {
                            params: {
                              username: this.username,
                              newEmail: this.codeEmail,
                              type: "changeEmail",
                            },
                          })
                          .then((res) => {
                            if (res.data["status"] === "ok") {
                              ElMessage({
                                type: "success",
                                message: "邮箱修改成功",
                              });
                              this.email = this.codeEmail;
                              console.log(this.codeEmail);
                              console.log(this.email);
                            } else {
                              ElMessage({
                                type: "error",
                                message: "邮箱修改失败",
                              });
                            }
                          })
                          .catch(() => {});
                      } else {
                        ElMessage({
                          type: "error",
                          message: "验证码错误",
                        });
                      }
                    }
                  })
                  .catch(() => {
                    ElMessage({
                      type: "info",
                      message: "取消修改邮箱",
                    });
                  });
              } else {
                if (res.data["type"] === "sameEmail") {
                  ElMessage({
                    type: "error",
                    message: "邮箱已被注册",
                  });
                }
              }
            })
            .catch(function (error) {
              console.log(error);
            });
        })
        .catch(() => {});
    },
    handleChangePhone() {
      //留待接口
    },
  },
  updated() {
    //初次挂载获取后端信息
    if (!this.inited) {
      this.inited = true;
      axios
        .get("/get_user_basic_info", {
          params: {
            username: this.username,
          },
        })
        .then((res) => {
          if (res.data["status"] === "ok") {
            this.donutNumber = res.data["donutNumber"];
            this.email = res.data["email"];
            this.phoneNumber = res.data["mobileNumber"];
            this.creditRank = res.data["creditRank"];
            this.currentExp = res.data["currentExp"];
            this.expForUpgrade = res.data["expForUpgrade"];
            this.percentage = this.getRatio();
            const imageFile = this.base64ImgtoFile(
              "data:image/png;base64," + res.data["avatarImage"]
            );
            this.image.src =
              window.webkitURL.createObjectURL(imageFile) ||
              window.URL.createObjectURL(imageFile);
            localStorage.setItem('imageSrc',this.image.src);
            this.$emit("initAvatar", this.image.src);
          }
        })
        .catch((err) => {
          console.log(err);
        });
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.mine-info-container{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.modal-title {
  font-size: 1.5em;
  margin-bottom: 30px;
  color: #ffffff;
}
.cropper {
  height: 600px;
  width: 600px;
  background: #ddd;
  border-radius: 20px;
}
.file-input {
  display: none;
}
:deep .modal-container {
  display: flex;
  justify-content: center;
  align-items: center;
}
:deep .modal-content {
  display: flex;
  flex-direction: column;
  margin: 0 1rem;
  padding: 1rem;
  border-radius: 0.25rem;
}
.modal__title {
  font-size: 1.5rem;
  font-weight: 700;
}
.icon {
  width: 1em;
  height: 1em;
  vertical-align: -0.15em;
  fill: currentColor;
  overflow: hidden;
}
:deep .el-progress-bar__inner {
  background-color: #f8d45e;
}
.info-input {
  width: 300px;
}
.change-form {
  padding: 0 0 0 40px;
}
.change-title {
  font-family: YouSheRound;
  font-size: 24px;
  padding: 20px 0 20px 0;
}
.change-form-area {
  width: 94%;
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
  width: 94%;
  border-radius: 10px;
  box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
  margin-top: 30px;
}
.button-area {
  display: flex;
  justify-content: center;
  margin-top: 40px;
}
</style>
