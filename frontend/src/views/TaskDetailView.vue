<template>
  <el-container class="container">
    <el-header class="header-style">
      <NavBar :login="true" activeItem="2" :imageUrl="imageSrc"></NavBar>
    </el-header>
    <el-container>
      <el-main class="main-style">
        <div class="phone-box">
          <vue-final-modal
            v-model="showModal"
            classes="modal-container"
            content-class="modal-content"
            :debounce="false"
            :prevent-click="true"
          >
            <div style="font-family: YouSheRound; font-size: 26px">
              举报任务
            </div>
            <div
              style="
                text-align: left;
                font-size: 18px;
                padding-left: 20px;
                width: 100%;
              "
            >
              理由描述：
            </div>
            <div style="margin: 15px 0 10px 0; width: 100%; height: 80%">
              <el-input
                type="textarea"
                :rows="12"
                placeholder="请输入举报该任务的理由"
                v-model="textarea"
                :maxlength="200"
                resize="none"
              >
              </el-input>
              <el-upload
                style="margin-top: 20px"
                v-model:file-list="fileList"
                action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
                list-type="picture-card"
                :auto-upload="false"
                :limit="1"
                :on-exceed="uploadExceed"
              >
                <el-icon><Plus /></el-icon>
                <div style="font-size: 14px">上传图片</div>
              </el-upload>
            </div>
            <div
              style="
                margin-top: 20px;
                display: flex;
                justify-content: space-around;
                width: 60%;
              "
            >
              <CustomButton title="确认" @click="reportTask"></CustomButton>
              <CustomButton
                title="取消"
                @click="this.showModal = false"
              ></CustomButton>
            </div>
          </vue-final-modal>
          <div class="main-box">
            <div class="detail-title">任务详情</div>
            <el-row>
              <el-col :span="17">
                <el-row
                  style="height: 450px; margin-top: 20px"
                  class="flex-box"
                >
                  <div class="pic-box flex-box">
                    <el-image
                      style="width: 420px; height: 420px; border-radius: 5px"
                      :src="
                        coverImage
                          ? coverImage
                          : require('@/assets/images/default.jpg')
                      "
                      fit="cover"
                    >
                    </el-image>
                  </div>
                </el-row>
                <el-row style="height: 80px" class="flex-box">
                  <el-col :span="4"> </el-col>
                  <el-col :span="16"> </el-col>
                </el-row>
              </el-col>
              <el-col
                :span="7"
                style="
                  margin-top: 20px;
                  height: 490px;
                  box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
                  border-radius: 10px;
                "
              >
                <div style="padding: 20px">
                  <div
                    style="
                      height: 50px;
                      text-align: center;
                      font-size: 20px;
                      margin-top: 10%;
                    "
                  >
                    发布者信息
                  </div>
                  <el-row class="flex-box">
                    <el-avatar
                      :src="
                        posterAvatar
                          ? posterAvatar
                          : require('@/assets/images/default.jpg')
                      "
                    ></el-avatar>
                    <span class="flex-box">
                      <span class="user-center">{{ posterName }}</span>
                    </span>
                  </el-row>
                  <div
                    style="
                      height: 30px;
                      text-align: center;
                      font-size: 20px;
                      margin-top: 30px;
                    "
                  >
                    任务持续时间
                  </div>
                  <div
                    class="flex-box"
                    style="
                      font-size: 22px;
                      margin-top: 16px;
                      font-family: YouSheBlack;
                    "
                  >
                    开始时间：{{ startTime }}
                  </div>
                  <div
                    class="flex-box"
                    style="
                      font-size: 22px;
                      margin-top: 10px;
                      font-family: YouSheBlack;
                    "
                  >
                    结束时间：{{ endTime }}
                  </div>
                  <div class="progress-title" style="padding-top: 10px">
                    <span style="text-align: center; font-size: 20px"
                      >领取进度：</span
                    >
                  </div>
                  <div class="progress-bar">
                    <div style="padding-top: 10px">
                      <span style="text-align: center; font-size: 20px"></span>
                    </div>
                    <el-progress
                      class="level-progress"
                      :text-inside="true"
                      :stroke-width="25"
                      :percentage="ratio"
                      color="#fbe484"
                      status="warning"
                    />
                  </div>
                </div>
              </el-col>
            </el-row>
            <el-row style="margin-top: 0px">
              <el-col :span="8">
                <el-form label-width="100px" class="change-form">
                  <el-row style="height: 50px">
                    <el-form-item label="名称" :required="true">
                      <el-input
                        v-model="taskName"
                        placeholder="名称"
                        :disabled="true"
                      />
                    </el-form-item>
                  </el-row>
                  <el-row style="height: 50px">
                    <el-form-item label="题型" :required="true">
                      <el-input
                        v-model="answerType"
                        placeholder="题型"
                        :disabled="true"
                      />
                    </el-form-item>
                  </el-row>
                  <el-row style="height: 50px">
                    <el-form-item label="分类" :required="true">
                      <el-input
                        v-model="materialType"
                        placeholder="分类"
                        :disabled="true"
                      />
                    </el-form-item>
                  </el-row>
                  <el-row style="height: 50px">
                    <el-form-item label="等级" :required="true">
                      <el-input
                        v-model="starRank"
                        placeholder="等级"
                        :disabled="true"
                      />
                    </el-form-item>
                  </el-row>
                </el-form>
              </el-col>
              <el-col :span="8">
                <el-form label-width="100px" class="change-form">
                  <el-row style="height: 50px">
                    <el-form-item label="题目数量" :required="true">
                      <el-input
                        v-model="problemTotalNum"
                        placeholder="题目数量"
                        :disabled="true"
                      />
                    </el-form-item>
                  </el-row>
                  <el-row style="height: 50px">
                    <el-form-item label="奖励额度" :required="true">
                      <el-input
                        v-model="singleBonus"
                        placeholder="奖励额度"
                        :disabled="true"
                      />
                    </el-form-item>
                  </el-row>
                  <el-row style="height: 50px">
                    <el-form-item label="任务描述" :required="true">
                      <el-input
                        v-model="description"
                        :rows="3"
                        type="textarea"
                        placeholder="任务描述"
                        :disabled="true"
                        resize="none"
                        style="width: 300px"
                      />
                    </el-form-item>
                  </el-row>
                </el-form>
              </el-col>
              <el-col :span="8" class="rb-box">
                <div class="flex-box" style="flex-direction: column">
                  <el-image
                    style="width: 112px; height: 100px"
                    fit="cover"
                    :src="require('@/assets/images/logo.png')"
                    class="jump-logo"
                  ></el-image>
                  <div class="jump-shadow"></div>
                </div>
              </el-col>
            </el-row>
            <el-row v-if="mode == 0 && (hasOver || noTask)">
              <el-col :span="1"></el-col>
              <el-col :span="5"
                ><CustomButton
                  :title="noTask ? '暂无可领项' : '任务已结束'"
                  :isRound="true"
                  :disabled="true"
                ></CustomButton
              ></el-col>
              <el-col :span="5"
                ><CustomButton
                  title="举报该任务"
                  :isRound="true"
                  @click.stop="clickReport"
                ></CustomButton
              ></el-col>
              <el-col :span="5"
                ><CustomButton
                  title="取消并返回"
                  :isRound="true"
                  @click.stop="clickCancel"
                ></CustomButton
              ></el-col>
              <el-col :span="8"></el-col>
            </el-row>
            <el-row v-if="mode == 0 && !hasOver && !noTask">
              <el-col :span="4"
                ><CustomButton
                  title="领取并开始"
                  :isRound="true"
                  @click="clickReceiveStart"
                  :disabled="cantReceive"
                ></CustomButton
              ></el-col>
              <el-col :span="4"
                ><CustomButton
                  title="领取至列表"
                  :isRound="true"
                  :disabled="cantReceive"
                  @click.stop="clickToList"
                ></CustomButton
              ></el-col>
              <el-col :span="4"
                ><CustomButton
                  title="举报该任务"
                  :isRound="true"
                  @click.stop="clickReport"
                ></CustomButton
              ></el-col>
              <el-col :span="4"
                ><CustomButton
                  title="取消并返回"
                  :isRound="true"
                  @click.stop="clickCancel"
                ></CustomButton
              ></el-col>
              <el-col :span="8"></el-col>
            </el-row>
            <el-row v-else-if="mode == 1">
              <el-col :span="8"
                ><CustomButton
                  title="下架该任务"
                  :isRound="true"
                  @click="clickDeleteTask"
                ></CustomButton
              ></el-col>
              <el-col :span="8"
                ><CustomButton
                  title="返回管理员"
                  :isRound="true"
                  @click.stop="clickToAdmin"
                ></CustomButton
              ></el-col>
              <el-col :span="8"> </el-col>
            </el-row>
          </div>
        </div>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
// @ is an alias to /src
import axios from "axios";
import NavBar from "@/components/NavBar.vue";
import CustomButton from "@/components/CustomButton.vue";
import { ElMessage, ElMessageBox } from "element-plus";
export default {
  name: "TaskDetailView",
  components: {
    NavBar,
    CustomButton,
  },
  data() {
    return {
      coverImage: "",
      mode: 0,
      fileList: [],
      textarea: "",
      showModal: false,
      imageSrc: "",
      username: "",
      id: 1,
      taskName: "",
      description: "",
      answerType: "",
      problemTotalNum: "",
      finishedProblemNum: "",
      starRank: "",
      singleBonus: "",
      materialType: "",
      posterName: "",
      posterAvatar: "",
      startTime: "",
      endTime: "",
      ratio: 0,
      cantReceive: false,
      hasOver: false,
      noTask: false,
    };
  },
  methods: {
    clickDeleteTask() {
      ElMessageBox.confirm(
        "下架该任务以后对该任务的举报信息也会被全部删除，是否确认删除？",
        "确认下架",
        {
          confirmButtonText: "确认",
          cancelButtonText: "取消",
          type: "warning",
        }
      )
        .then(() => {
          axios
            .get("http://101.42.118.80:8000/delete_task/", {
              params: {
                taskId: this.id, //任务id
              },
            })
            .then((res) => {
              if (res.data["status"] == "ok") {
                ElMessage({
                  type: "success",
                  message: "删除任务成功",
                });
              }
              this.$router.push({
                name: "admin",
              });
            })
            .catch((err) => {
              console.log(err);
            });
        })
        .catch(() => {});
    },
    clickToAdmin() {
      this.$router.push({
        name: "admin",
      });
    },
    reportTask() {
      if (this.textarea == "") {
        ElMessage({
          type: "warning",
          message: "请填写举报描述",
        });
        return;
      }
      this.showModal = false;
      var formData = new FormData();
      if (this.fileList[0]) {
        formData.append("image", this.fileList[0].raw); //上传图片
      }
      formData.append("username", this.username);
      formData.append("id", this.id);
      formData.append("description", this.textarea);
      axios
        .post("http://101.42.118.80:8000/add_reported_task/", formData)
        .then(() => {
          ElMessage({
            type: "success",
            message: "举报成功，处理后的结果会发到您的邮箱中",
          });
        });
    },
    clickReport() {
      this.showModal = true;
    },
    clickReceiveStart() {
      if (this.cantReceive) {
        return;
      }
      axios
        .get("http://101.42.118.80:8000/receive_task/", {
          params: {
            username: this.username,
            taskId: this.id, //任务id
          },
        })
        .then((res) => {
          if (res.data["status"] == "ok") {
            if (res.data["type"] == "success") {
              this.$router.push({
                name: "perform",
                query: {
                  username: this.username,
                  taskId: this.id, //任务id
                  imageSrc: this.imageSrc,
                  taskName: this.taskName,
                  materialType: this.materialType,
                },
              });
            } else if (res.data["failType"] == "lowRank") {
              this.cantReceive = true;
              ElMessage({
                type: "warning",
                message: "您的信誉等级未达到要求",
              });
            } else if (res.data["failType"] == "hasReceived") {
              this.cantReceive = true;
              ElMessageBox.confirm(
                "您已经领取过该任务，是否跳转到继续任务",
                "确认跳转",
                {
                  confirmButtonText: "确认",
                  cancelButtonText: "取消",
                  type: "info",
                  draggable: true,
                }
              )
                .then(() => {
                  this.$router.push({
                    name: "perform",
                    query: {
                      username: this.username,
                      taskId: this.id, //任务id
                      imageSrc: this.imageSrc,
                      taskName: this.taskName,
                      materialType: this.materialType,
                    },
                  });
                })
                .catch(() => {});
            }
          }
        });
    },
    clickToList() {
      if (this.cantReceive) {
        return;
      }
      axios
        .get("http://101.42.118.80:8000/receive_task/", {
          params: {
            username: this.username,
            taskId: this.id, //任务id
          },
        })
        .then((res) => {
          if (res.data["status"] == "ok") {
            if (res.data["type"] == "success") {
              this.$router.push({
                //跳转到个人中心领取列表
                name: "mine",
                query: {
                  username: this.username,
                  imageSrc: this.imageSrc,
                  defaultActive: "2",
                },
              });
            } else if (res.data["failType"] == "lowRank") {
              this.cantReceive = true;
              ElMessage({
                type: "warning",
                message: "您的信誉等级未达到要求",
              });
            } else if (res.data["failType"] == "hasReceived") {
              this.cantReceive = true;
              ElMessageBox.confirm(
                "您已经领取过该任务，是否跳转到已领取列表",
                "确认跳转",
                {
                  confirmButtonText: "确认",
                  cancelButtonText: "取消",
                  type: "info",
                  draggable: true,
                }
              )
                .then(() => {
                  this.$router.push({
                    //跳转到个人中心领取列表
                    name: "mine",
                    query: {
                      username: this.username,
                      imageSrc: this.imageSrc,
                      defaultActive: "2",
                    },
                  });
                })
                .catch(() => {});
            }
          }
        });
    },
    clickCancel() {
      this.$router.go(-1);
    },
    uploadExceed() {
      ElMessage({
        type: "warning",
        message: "最多只能上传一张图片",
      });
    },
  },
  beforeMount() {
    if (localStorage.getItem("username")) {
      this.username = localStorage.getItem("username");
    }
    if (!localStorage.getItem("avatar")) {
      axios
        .get("http://101.42.118.80:8000/get_avatar/", {
          params: {
            username: this.username,
          },
        })
        .then((res) => {
          if (res.data["status"] === "ok") {
            if (res.data["avatar"]) {
              this.image.src = "data:image/png;base64," + res.data["avatar"];
              localStorage.setItem("avatar", this.image.src);
            }
          }
        });
    } else {
      this.imageSrc = localStorage.getItem("avatar");
    }
  },
  mounted() {
    if (this.$route.query.id) {
      this.id = this.$route.query.id;
    }
    if (this.$route.query.mode && localStorage.getItem("adminAuth")) {
      this.mode = this.$route.query.mode;
    }
    axios
      .get("http://101.42.118.80:8000/get_task_basic_info/", {
        params: {
          id: this.id,
        },
      })
      .then((res) => {
        this.taskName = "taskName";
        if (res.data["status"] === "ok") {
          if (res.data["taskStatus"] == 3) {
            this.hasOver = true;
          }
          this.coverImage = res.data["coverImage"];
          this.taskName = res.data["taskName"];
          this.answerType = res.data["answerType"];
          this.description = res.data["description"];
          this.problemTotalNum = res.data["problemTotalNum"];
          this.finishedProblemNum = res.data["finishedProblemNum"];
          this.ratio = res.data["receiveProcess"];
          if (parseInt(this.ratio) == 100) {
            this.noTask = true;
          }
          this.singleBonus = res.data["singleBonus"];
          this.starRank = res.data["starRank"];
          this.materialType = res.data["materialType"];
          this.posterName = res.data["posterName"];
          this.startTime = res.data["startTime"];
          this.endTime = res.data["endTime"];
          this.posterAvatar = res.data["posterAvatar"];
        }
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style scoped>
.flex-box {
  display: flex;
  justify-content: center;
  align-items: center;
}

:deep .modal-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
}
:deep .modal-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 0 1rem;
  padding: 1rem;
  border-radius: 0.25rem;
  height: 70%;
  width: 40%;
  background-color: #efefef;
}
.jump-logo {
  z-index: 2;
  animation: jump-logo 1s infinite;
  animation-timing-function: ease;
}
.jump-shadow {
  z-index: 1;
  width: 120px;
  height: 5px;
  background: #eaeaea;
  border-radius: 100%;
  animation: shadow 1s infinite;
  animation-timing-function: ease;
}
@keyframes jump-logo {
  0% {
    margin-bottom: 0px;
  }

  50% {
    margin-bottom: 30px;
  }

  100% {
    margin-bottom: 0px;
  }
}
@keyframes shadow {
  0% {
    width: 100px;
  }

  50% {
    width: 70px;
  }

  100% {
    width: 100px;
  }
}
.container {
  margin: 0;
  height: 100%;
}

.detail-title {
  font-size: 28px;
  font-family: YouSheRound;
}
.header-style {
  background-image: url(@/assets/images/nav-background.png);
  background-size: cover;
  height: 60px;
  box-shadow: 0 0px 8px 0;
  display: flex;
}
.pic-box {
  width: 420px;
  height: 420px;
  text-align: center;
  background-size: 100% 100%;
  border: 30px solid #efefef;
  border-radius: 25px;
}
.progress-bar {
  width: 100%;
  height: 40px;
  display: flex;
  background-color: #efefef;
  border-radius: 25px;
  text-align: center;
}
.progress-title {
  height: 40px;
}
.level-progress {
  position: relative;
  width: 80%;
  margin: 8px 10px 8px 30px;
}
:deep .el-progress-bar__outer {
  background-color: #5eabbf;
}
:deep .el-progress-bar__inner {
  top: 10%;
  left: 2%;
  height: 80%;
}
.user-center {
  margin-left: 10px;
  line-height: 58px;
  font-size: 26px;
  color: #5eabbf;
  font-family: YouSheBlack;
}
.left-menu-area {
  margin-top: 4px;
  padding-top: 40px;
  padding-left: 0px;
  padding-right: 10px;
  padding-bottom: 60px;
  border-right: 1px solid #e9e9e9;
  overflow-x: hidden;
}
.main-style {
  background-color: transparent;
}
.el-menu {
  border-radius: 0;
}
.el-menu-item {
  height: 50px;
  font-size: 16px;
  padding-top: 4px;
}
.el-menu-item.is-active {
  border-left: 5px solid #5eabbf;
}
.el-menu--horizontal .el-menu-item:not(.is-disabled):focus {
  background-color: transparent;
}
.el-menu--horizontal .el-menu-item:not(.is-disabled):hover {
  background-color: #f8f8f8;
}
/* 小屏幕手机端 */
@media (min-width: 0px) and (max-width: 768px) {
  .phone-box {
    width: 1100px;
  }
  .main-box {
    width: 98%;
    margin-left: 1%;
  }
  .rb-box {
    display: flex;
    justify-content: center;
    align-items: flex-end;
  }
}
/* 大屏幕（大桌面显示器，大于等于 1200px） */
@media (min-width: 768px) {
  .main-box {
    width: 80%;
    margin-left: 10%;
  }
  .rb-box {
    display: flex;
    justify-content: flex-end;
    align-items: flex-end;
  }
}
</style>
