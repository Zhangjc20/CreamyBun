<template>
  <div class="task-page-container">
    <el-dialog v-model="dialogShow" center width="70%">
      <div
        style="
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
        "
      >
        <TaskCheck :mode="type" ref="taskCheck" @postTaskImmediately="postTaskImmediately" @stopTask="stopTask" @giveUpTask="giveUpTask"/>
      </div>
    </el-dialog>
    <el-dialog title="任务反馈" v-model="dialogVisible" center width="60%">
      <div
        style="
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
        "
      >
        <div style="width: 100%; display: flex; justify-content: space-around">
          <CustomButton title="查看任务详情" @click="checkDetail" />
          <CustomButton title="删除举报信息" @click="deleteReport" />
        </div>
        <div class="report-title">举报者描述及配图</div>
        <el-input
          v-model="textarea0"
          :rows="2"
          :maxlength="200"
          type="textarea"
          placeholder="举报信息"
          disabled
          style="margin-bottom: 10px"
        />
        <el-image :src="src" style="width: 400px" :preview-src-list="srcList">
        </el-image>
        <div class="report-title">反馈信息至发布者</div>
        <el-input
          v-model="textarea1"
          :rows="4"
          :maxlength="200"
          type="textarea"
          placeholder="请输入反馈信息"
          style="margin-bottom: 10px"
        />
        <CustomButton title="邮箱发送" @click="sendReportEmail(0)" />
        <div class="report-title">反馈信息至举报者</div>
        <el-input
          v-model="textarea2"
          :rows="4"
          :maxlength="200"
          type="textarea"
          placeholder="请输入反馈信息"
          style="margin-bottom: 10px"
        />
        <CustomButton title="邮箱发送" @click="sendReportEmail(1)" />
      </div>
    </el-dialog>
    <div class="task-list-title" v-if="type != 0">
      {{
        type === 1 ? "领取任务列表" : type === 2 ? "发布任务列表" : "待审核任务"
      }}
    </div>
    <div class="radio-box" v-if="type == 1 || type == 2">
      筛选条件：
      <el-radio-group
        v-model="sortChoice"
        @change="handleSortChange"
        style="margin-left: 15px"
      >
        <el-radio :label="0">所有</el-radio>
        <el-radio :label="1">{{
          type === 1 ? "正在进行" : "暂未发布"
        }}</el-radio>
        <el-radio :label="2">{{
          type === 1 ? "已结束" : "发布但未结束"
        }}</el-radio>
        <el-radio :label="3" v-if="type === 2">已结束</el-radio>
      </el-radio-group>
      <el-popover
        placement="left"
        title="条件说明"
        :width="230"
        trigger="hover"
        :content="
          type == 1
            ? '&emsp;&emsp;已结束包括领取题目全部完成和本身已结束的任务'
            : '&emsp;&emsp;已结束包括截止时间已过、任务全部完成和已中断任务'
        "
      >
        <template #reference>
          <span class="iconfont icon-infofill tip-box"></span>
        </template>
      </el-popover>
    </div>
    <el-row class="task-box">
      <el-col :span="4.8" v-for="item in items.slice(0, 5)" :key="item.index">
        <SingleTask
          :props="item"
          @click="
            handleClickTask(item.id, item.isSpace, item.reportId, item.index)
          "
        ></SingleTask>
      </el-col>
    </el-row>
    <el-row class="task-box">
      <el-col :span="4.8" v-for="item in items.slice(5, 10)" :key="item.index">
        <SingleTask
          :props="item"
          @click="
            handleClickTask(item.id, item.isSpace, item.reportId, item.index)
          "
        ></SingleTask>
      </el-col>
    </el-row>
    <div class="pagnation-box">
      <el-pagination
        background
        layout="total, prev, pager, next, jumper"
        v-model:currentPage="currentPage"
        :total="total"
        :page-size="10"
        @current-change="clickPage"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import SingleTask from "./SingleTask.vue";
import CustomButton from "./CustomButton.vue";
import { ElMessage } from "element-plus";
import TaskCheck from "@/components/TaskCheck.vue";
export default {
  name: "TaskPage",
  props: {
    type: {
      type: Number,
      default: 1, //0:任务大厅 1:领取列表 2:发布列表 3:管理员界面
    },
    username: {
      type: String,
      default: "",
    },
  },
  components: {
    SingleTask,
    CustomButton,
    TaskCheck,
  },
  data() {
    return {
      dialogShow: false,
      curId: -1,
      curTaskId: -1,
      total: 20,
      src: "",
      srcList: [""],
      textarea0: "",
      textarea1:
        "尊敬的任务发布者，您的任务不幸被举报，经核实确实存在如下问题：/并不存在问题",
      textarea2:
        "尊敬的奶黄包用户，感谢您的举报，经核实确实存在您所述问题，现已经解决。",
      dialogVisible: false,
      items: [
        {
          index: 1,
          isSpace: true,
        },
        {
          index: 2,
          isSpace: true,
        },
        {
          index: 3,
          isSpace: true,
        },
        {
          index: 4,
          isSpace: true,
        },
        {
          index: 5,
          isSpace: true,
        },
        {
          index: 6,
          isSpace: true,
        },
        {
          index: 7,
          isSpace: true,
        },
        {
          index: 8,
          isSpace: true,
        },
        {
          index: 9,
          isSpace: true,
        },
        {
          index: 10,
          isSpace: true,
        },
      ],
      currentPage: 1,
      sortChoice: 0,
      searchInput: "",
      onlyLevel: false,
      donutType: 1,
      overType: 1,
      newType: 1,
      hardType: 1,
      chosenDataType: 1,
      chosenProblemType: 1,
    };
  },
  methods: {
    postTaskImmediately(){
      this.dialogShow = false;
      this.init(1);
    },
    giveUpTask(){
      this.dialogShow = false;
      this.init(1);
    },
    stopTask() {
      this.dialogShow = false;
      this.init(2);
    },
    sendReportEmail(type) {
      axios
        .get("http://101.42.118.80:8000/send_report_email", {
          params: {
            type: type,
            reportId: this.curId,
            taskId: this.curTaskId,
            textarea: type == 0 ? this.textarea1 : this.textarea2,
          },
        })
        .then((res) => {
          if (res.data["status"] == "ok") {
            ElMessage({
              type: "success",
              message: "邮件发送成功",
            });
          }
        });
    },
    deleteReport() {
      for (var i = 0; i < this.items.length; i++) {
        if (this.items[i].reportId == this.curId) {
          axios
            .get("http://101.42.118.80:8000/delete_reported_task", {
              params: {
                reportId: this.curId,
              },
            })
            .then((res) => {
              if (res.data["status"] === "ok") {
                ElMessage({
                  type: "success",
                  message: "成功删除举报任务信息",
                });
                this.dialogVisible = false;
                this.init();
              }
            });
          break;
        }
      }
    },
    checkDetail() {
      this.$emit("checkDetail", this.curTaskId);
    },
    handleClickTask(taskId, isSpace, id, index) {
      if (isSpace === true) {
        return;
      }
      if (this.type === 0) {
        this.$router.push({
          name: "taskdetail",
          query: {
            id: taskId,
          },
        });
      } else if (this.type == 1) {
        this.dialogShow = true;
        this.$nextTick(() => {
          this.$refs.taskCheck.showTaskDetail(
            taskId,
            this.username,
            this.sortChoice,
            index
          );
        });
      } else if (this.type == 2) {
        this.dialogShow = true;
        this.$nextTick(() => {
          this.$refs.taskCheck.showTaskDetail(
            taskId,
            this.username,
            this.sortChoice,
            index
          );
        });
      } else if (this.type == 3) {
        axios
          .get("http://101.42.118.80:8000/get_reported_task", {
            params: {
              reportId: this.curId,
            },
          })
          .then((res) => {
            if (res.data["status"] === "ok") {
              this.textarea0 = res.data["description"];
              this.src = "data:image/png;base64," + res.data["image"];
              this.srcList = [this.src];
              this.dialogVisible = true;
            }
          });
      }
      this.curTaskId = taskId;
      this.curId = id;
    },
    sort(
      searchInput,
      onlyLevel,
      donutType,
      overType,
      newType,
      hardType,
      chosenDataType,
      chosenProblemType
    ) {
      this.searchInput = searchInput;
      this.onlyLevel = onlyLevel;
      this.donutType = donutType;
      this.overType = overType;
      this.newType = newType;
      this.hardType = hardType;
      this.chosenDataType = chosenDataType;
      this.chosenProblemType = chosenProblemType;
      //onlyLevel:bool false:所有 true:只选入满足等级的
      //donutType:int 1:所有 2:从多到少 3:从少到多
      //newType:int 1:所有 2：最新发布 3：最早结束
      //hardType:int 1:所有 2：从难到易 3：从易到难
      //chosenDataType:int 1:所有 2：图片 3：文本 4：音频  5：视频
      //chosenProblemType:int 1:所有 2：单选 3：多选 4：填空 5：框图 6：混合
      axios
        .get("http://101.42.118.80:8000/get_sorted_tasks", {
          params: {
            //onlyLevel:bool false:所有 true:只选入满足做题者等级的
            //donutType:int 1:默认 2:从多到少 3:从少到多
            //newType:int 1:默认 2：最新发布 3：最早结束
            //hardType:int 1:默认 2：从难到易 3：从易到难
            //chosenDataType:int 1:所有 2：图片 3：文本 4：音频  5：视频 6：混合
            //chosenProblemType:int 1:所有 2：单选 3：多选 4：填空 5：框图 6：混合
            username: this.username,
            searchInput: searchInput,
            onlyLevel: onlyLevel,
            donutType: donutType,
            overType: overType,
            newType: newType,
            hardType: hardType,
            chosenDataType: chosenDataType,
            chosenProblemType: chosenProblemType,
            pageNumber: 1,
          },
        })
        .then((res) => {
          if (res.data["status"] === "ok") {
            this.items = res.data["taskInfoList"];
            this.total = res.data["totalNumber"];
          }
          this.$message({
            type: "success",
            message: "筛选成功",
          });
        })
        .catch((err) => {
          console.log(err);
        });
    },
    clickPage(page) {
      if (this.type === 0) {
        axios
          .get("http://101.42.118.80:8000/get_sorted_tasks", {
            params: {
              username: this.username,
              searchInput: this.searchInput,
              onlyLevel: this.onlyLevel,
              donutType: this.donutType,
              overType: this.overType,
              newType: this.newType,
              hardType: this.hardType,
              chosenDataType: this.chosenDataType,
              chosenProblemType: this.chosenProblemType,
              pageNumber: page,
            },
          })
          .then((res) => {
            if (res.data["status"] === "ok") {
              this.items = res.data["taskInfoList"];
              this.total = res.data["totalNumber"];
              console.log("ok");
            }
          })
          .catch((err) => {
            console.log(err);
          });
      } else if (this.type === 1) {
        axios
          .get("http://101.42.118.80:8000/get_user_received_task_info", {
            params: {
              username: this.username, //String 用户名
              sortChoice: this.sortChoice, //int 1是所有 2是正在进行，3是已结束
              pageNumber: page, //int页码
            },
          })
          .then((res) => {
            if (res.data["status"] === "ok") {
              this.items = res.data["taskInfoList"];
              this.total = res.data["totalNumber"];
              console.log("ok");
            }
          })
          .catch((err) => {
            console.log(err);
          });
      } else if (this.type === 2) {
        axios
          .get("http://101.42.118.80:8000/get_user_released_task_info", {
            params: {
              username: this.username, //String 用户名
              sortChoice: this.sortChoice, //int 1是所有，2是暂未发布 3是发布但未结束 4是已结束
              pageNumber: page, //int页码
            },
          })
          .then((res) => {
            if (res.data["status"] === "ok") {
              this.items = res.data["taskInfoList"];
              this.total = res.data["totalNumber"];
              console.log("ok");
            }
          })
          .catch((err) => {
            console.log(err);
          });
      } else if (this.type === 3) {
        axios
          .get("http://101.42.118.80:8000/get_examining_tasks", {
            params: {
              pageNumber: page,
              adminToken: localStorage.getItem("adminToken"),
            },
          })
          .then((res) => {
            if (res.data["status"] === "ok") {
              this.items = res.data["taskInfoList"];
              this.total = res.data["totalNumber"];
            }
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
    handleSortChange(value) {
      if (this.type === 1) {
        axios
          .get("http://101.42.118.80:8000/get_user_received_task_info", {
            params: {
              username: this.username, //String 用户名
              sortChoice: value, //int 1是所有 2是正在进行，3是已结束
              pageNumber: 1, //int页码
            },
          })
          .then((res) => {
            if (res.data["status"] === "ok") {
              this.items = res.data["taskInfoList"];
              this.total = res.data["totalNumber"];
            }
          })
          .catch((err) => {
            console.log(err);
          });
      } else if (this.type === 2) {
        axios
          .get("http://101.42.118.80:8000/get_user_released_task_info", {
            params: {
              username: this.username, //String 用户名
              sortChoice: value, //int 1是所有，2是暂未发布 3是发布但未结束 4是已结束
              pageNumber: 1, //int页码
            },
          })
          .then((res) => {
            if (res.data["status"] === "ok") {
              this.items = res.data["taskInfoList"];
              this.total = res.data["totalNumber"];
              console.log("ok");
            }
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
    init(sortChoice) {
      //初始化任务列表
      if (sortChoice) {
        this.sortChoice = sortChoice;
      } else {
        this.sortChoice = 0;
      }
      this.currentPage = 1;
      if (this.type === 0) {
        axios
          .get("http://101.42.118.80:8000/get_sorted_tasks", {
            params: {
              username: this.username,
              searchInput: this.searchInput,
              onlyLevel: this.onlyLevel,
              donutType: this.donutType,
              overType: this.overType,
              newType: this.newType,
              hardType: this.hardType,
              chosenDataType: this.chosenDataType,
              chosenProblemType: this.chosenProblemType,
              pageNumber: 1,
            },
          })
          .then((res) => {
            if (res.data["status"] === "ok") {
              this.items = res.data["taskInfoList"];
              this.total = res.data["totalNumber"];
            }
          })
          .catch((err) => {
            console.log(err);
          });
      } else if (this.type === 1) {
        axios
          .get("http://101.42.118.80:8000/get_user_received_task_info", {
            params: {
              username: this.username, //String 用户名
              sortChoice: this.sortChoice, //int 1是所有 2是正在进行，3是已结束
              pageNumber: 1, //int页码
            },
          })
          .then((res) => {
            if (res.data["status"] === "ok") {
              this.items = res.data["taskInfoList"];
              this.total = res.data["totalNumber"];
              console.log("ok");
            }
          })
          .catch((err) => {
            console.log(err);
          });
      } else if (this.type === 2) {
        axios
          .get("http://101.42.118.80:8000/get_user_released_task_info", {
            params: {
              username: this.username, //String 用户名
              sortChoice: this.sortChoice, //int 1是所有，2是暂未发布 3是发布但未结束 4是已结束
              pageNumber: 1, //int页码
            },
          })
          .then((res) => {
            if (res.data["status"] === "ok") {
              this.items = res.data["taskInfoList"];
              this.total = res.data["totalNumber"];
              console.log(this.items);
            }
          })
          .catch((err) => {
            console.log(err);
          });
      } else if (this.type === 3) {
        axios
          .get("http://101.42.118.80:8000/get_examining_tasks", {
            params: {
              pageNumber: 1,
              adminToken: localStorage.getItem("adminToken"),
            },
          })
          .then((res) => {
            if (res.data["status"] === "ok") {
              this.items = res.data["taskInfoList"];
              this.total = res.data["totalNumber"];
            }
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
  },
  computed: {
    myType() {
      return this.type;
    },
  },
  watch: {
    myType: function (newData, oldData) {
      if (newData != oldData) {
        this.init();
      }
    },
  },
  mounted() {
    this.$nextTick(() => {
      this.init();
    });
  },
};
</script>

<style scoped>
.tip-box {
  color: #e6a23c;
  font-size: 18px;
  margin-left: 4px;
}
.task-page-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
}
.report-title {
  font-size: 16px;
  text-align: left;
  width: 100%;
  margin: 10px 0 10px 0;
}

.radio-box {
  width: 100%;
  display: flex;
  justify-content: right;
  padding: 0 20px 10px 0;
  align-items: center;
}
.task-list-title {
  font-size: 26px;
  font-family: YouSheRound;
  margin-bottom: 10px;
}
.pagnation-box {
  display: flex;
  flex-direction: row;
  justify-content: center;
}
.task-box {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-evenly;
  width: 100%;
}
</style>
