<template>
  <el-container class="container">
    <div class="detail-title">
      {{ mode == 1 ? "领取任务详情" : "发布任务详情（进行中）" }}
    </div>
    <el-row>
      <el-col :span="15">
        <el-row style="margin-top: 20px" class="flex-box">
          <div class="pic-box flex-box">
            <el-image
              style="width: 100%; height: 100%; border-radius: 5px"
              :src="require('@/assets/images/pet1.jpeg')"
              fit="cover"
            >
            </el-image>
          </div>
        </el-row>
      </el-col>
      <el-col :span="9" class="right-box">
        <div
          v-if="mode == 1"
          style="
            padding-bottom: 18px;
            margin-bottom: 20px;
            border-bottom: 2px solid rgba(0, 0, 0, 0.2);
            width: 60%;
          "
        >
          <div style="height: 30px; text-align: center; font-size: 18px">
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
        </div>
        <div>
          <div style="height: 20px; text-align: center; font-size: 18px">
            任务持续时间
          </div>
          <div
            class="flex-box"
            style="font-size: 20px; margin-top: 16px; font-family: YouSheBlack"
          >
            开始时间：{{ startTime }}
          </div>
          <div
            class="flex-box"
            style="font-size: 20px; margin-top: 2px; font-family: YouSheBlack"
          >
            结束时间：{{ endTime }}
          </div>
        </div>
        <div
          v-if="mode == 1"
          style="width: 60%; border-top: 2px solid rgba(0, 0, 0, 0.2);margin-top:18px;padding-top: 26px;"
          class="finish-progress"
        >
          <span style="font-family: YouSheRound; font-size: 22px;margin-bottom: 10px;"
            >完成进度：8/10</span
          >
          <el-progress
            style="width: 100%"
            :text-inside="true"
            :stroke-width="22"
            :percentage="80"
            status="warning"
          />
        </div>
        <div
          v-if="mode == 2"
          class="flex-box"
          style="
            margin-top: 20px;
            padding-top: 20px;
            border-top: 2px solid rgba(0, 0, 0, 0.1);
          "
        >
          <span>
            <div style="font-family: YouSheRound; font-size: 22px">
              题目领取情况：
            </div>
            <div style="text-align: center; margin-top: 4%; font-size: 18px">
              {{ finishedProblemNum }}/{{ problemTotalNum }}
            </div>
          </span>
          <el-progress type="dashboard" :percentage="ratio" status="warning">
            <template #default="{ percentage }">
              <span class="percentage-value">{{ percentage }}%</span>
              <span class="percentage-label">领取进度</span>
            </template>
          </el-progress>
        </div>
        <div
          v-if="mode == 2"
          class="flex-box"
          style="
            margin-top: 20px;
            padding-top: 20px;
            border-top: 2px solid rgba(0, 0, 0, 0.1);
          "
        >
          <span>
            <div style="font-family: YouSheRound; font-size: 22px">
              题目完成情况：
            </div>
            <div style="text-align: center; margin-top: 4%; font-size: 18px">
              {{ finishedProblemNum }}/{{ problemTotalNum }}
            </div>
          </span>
          <el-progress type="dashboard" :percentage="80" status="success">
            <template #default="{ percentage }">
              <span class="percentage-value">{{ percentage }}%</span>
              <span class="percentage-label">完成进度</span>
            </template>
          </el-progress>
        </div>
      </el-col>
    </el-row>
    <el-row style="margin-top: 25px">
      <el-col :span="8">
        <el-form label-width="100px" class="c ge-form">
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
      <el-col :span="11">
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
      <el-col :span="5" class="rb-box">
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
    <el-row v-if="mode == 2">
      <el-col :span="10" style="display: flex; justify-content: center"
        ><CustomButton
          title="答案数据下载"
          :isRound="true"
          @click.stop="clickDownload"
        ></CustomButton
      ></el-col>
      <el-col :span="8" style="display: flex; justify-content: center"
        ><CustomButton
          title="中断当前任务"
          :isRound="true"
          @click.stop="clickStopTask"
        ></CustomButton
      ></el-col>
      <el-col :span="6"></el-col>
    </el-row>
    <el-row v-else-if="mode == 1">
      <el-col :span="10" style="display: flex; justify-content: center"
        ><CustomButton @click="routerPerform" title="继续当前任务" :isRound="true"></CustomButton
      ></el-col>
      <el-col :span="8" style="display: flex; justify-content: center"
        ><CustomButton title="停止当前任务" :isRound="true"></CustomButton
      ></el-col>
      <el-col :span="6"> </el-col>
    </el-row>
  </el-container>
</template>

<script>
// import axios from "axios";
import CustomButton from "@/components/CustomButton.vue";
import axios from "axios";
// import { ElMessage } from "element-plus";
export default {
  name: "TaskCheck",
  components: {
    CustomButton,
  },
  props: {
    mode: {
      type: Number,
      default: 1,
    },
  },
  data() {
    return {
      fileList: [],
      textarea: "",
      showModal: false,
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
    };
  },
  mounted() {
    console.log("niihap");
  },
  methods: {
    routerPerform(){
      console.log({
          username: this.username,
          taskId: this.id, //任务id
          taskName: this.taskName,
          materialType: this.materialType,
        },"{username: this.username,taskId: this.id, //任务idtaskName: this.taskName,materialType: this.materialType,}")
      this.$router.push({
        name: "perform",
        query: {
          username: this.username,
          taskId: this.id, //任务id
          taskName: this.taskName,
          materialType: this.materialType,
        },
      });
    },
    clickDownload() {
      //todo数据下载
    },
    clickStopTask() {
      //todo 中断当前任务
    },
    showTaskDetail(id,username) {
      axios
        .get("/get_task_basic_info", {
          params: {
            id: id,
          },
        })
        .then((res) => {
          console.log("chijiba",res)
          this.taskName = "taskName";
          if (res.data["status"] === "ok") {
            this.taskName = res.data["taskName"];
            this.answerType = res.data["answerType"];
            this.description = res.data["description"];
            this.problemTotalNum = res.data["problemTotalNum"];
            this.finishedProblemNum = res.data["finishedProblemNum"];
            this.ratio =
              Math.floor(
                (this.finishedProblemNum / this.problemTotalNum) * 1000
              ) / 10;
            this.posterAvatar = "data:image/png;base64," + res.data["posterAvatar"];
            this.singleBonus = res.data["singleBonus"];
            this.starRank = res.data["starRank"];
            this.materialType = res.data["materialType"];
            this.posterName = res.data["posterName"];
            this.startTime = res.data["startTime"];
            this.endTime = res.data["endTime"];
            this.id = id;
            this.username = username
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style scoped>
.flex-box {
  display: flex;
  justify-content: center;
  align-items: center;
}
.right-box {
  margin-top: 16px;
  height: 410px;
  border-left: 4px solid rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.rb-box {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  align-items: center;
}
.percentage-value {
  display: block;
  margin-top: 10px;
  font-size: 28px;
}
.percentage-label {
  display: block;
  margin-top: 10px;
  font-size: 12px;
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
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.detail-title {
  text-align: center;
  width: 100%;
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
  width: 360px;
  height: 360px;
  text-align: center;
  background-size: 100% 100%;
  border: 20px solid #efefef;
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
  width: 300px;
  margin: 8px 10px 8px 10px;
}
.user-center {
  margin-left: 10px;
  line-height: 58px;
  font-size: 26px;
  color: #5eabbf;
  font-family: YouSheBlack;
}
.finish-progress {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
