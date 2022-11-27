<template>
  <div class="task-page-container">
    <el-dialog title="任务反馈" v-model="dialogVisible" center width="60%">
      <div
        style="
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
        "
      >
      <div style="width:100%;display:flex;justify-content: space-around;">
        <CustomButton title="查看任务详情" @click="checkDetail"/>
        <CustomButton title="删除举报信息" />
      </div>
      <div class="report-title">举报者描述及配图</div>
      <el-input
          v-model="textarea0"
          :rows="2"
          :maxlength="200"
          type="textarea"
          placeholder="举报信息"
          disabled
          style="margin-bottom:10px"
        />
        <el-image :src="src" style="width:400px;" :preview-src-list="srcList">
        </el-image>
        <div class="report-title">反馈信息至发布者</div>
        <el-input
          v-model="textarea1"
          :rows="4"
          :maxlength="200"
          type="textarea"
          placeholder="请输入反馈信息"
          style="margin-bottom:10px"
        />
        <CustomButton title="邮箱发送" />
        <div class="report-title">反馈信息至举报者</div>
        <el-input
          v-model="textarea2"
          :rows="4"
          :maxlength="200"
          type="textarea"
          placeholder="请输入反馈信息"
          style="margin-bottom:10px"
        />
        <CustomButton title="邮箱发送" />
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
    </div>
    <div class="task-box">
      <SingleTask
        v-for="item in items"
        :key="item.index"
        :props="item"
        @click="handleClickTask(item.id,item.isSpace)"
      ></SingleTask>
    </div>
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
    imageSrc: {
      type: String,
      default: "",
    },
  },
  components: {
    SingleTask,
    CustomButton
  },
  data() {
    return {
      total: 20,
      src:"https://img2.baidu.com/it/u=2591611833,3173732768&fm=253&fmt=auto&app=138&f=JPEG?w=889&h=500",
      srcList:["https://img2.baidu.com/it/u=2591611833,3173732768&fm=253&fmt=auto&app=138&f=JPEG?w=889&h=500"],
      textarea0:"",
      textarea1:"尊敬的任务发布者，您的任务不幸被举报，经核实确实存在如下问题：/并不存在问题",
      textarea2:"尊敬的奶黄包用户，感谢您的举报，经核实确实存在您所述问题，现已经解决。",
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
    checkDetail(){
      this.$emit('checkDetail',);
    },
    handleClickTask(id,isSpace) {
      if(isSpace===true){
        return;
      }
      if (this.type === 0) {
        //管理员任务不触发
        this.$router.push({
          name: "taskdetail",
          query: {
            id: id,
            username: this.username,
            imageSrc: this.imageSrc,
          },
        });
      }
      else if(this.type == 3){
        this.dialogVisible = true;
      }
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
        .get("/get_sorted_tasks", {
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
        })
        .catch((err) => {
          console.log(err);
        });
    },
    clickPage(page) {
      if (this.type === 0) {
        axios
          .get("/get_sorted_tasks", {
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
          .get("/get_user_received_task_info", {
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
          .get("/get_user_released_task_info", {
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
        //todo:获得指定页数待审核任务
        axios
          .get("/get_examining_tasks", {
            params: {
              pageNumber: page,
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
          .get("/get_user_received_task_info", {
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
          .get("/get_user_released_task_info", {
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
    init() {
      //初始化任务列表
      this.sortChoice = 0;
      console.log("username");
      console.log(this.username);
      if (this.type === 0) {
        axios
          .get("/get_sorted_tasks", {
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
          .get("/get_user_received_task_info", {
            params: {
              username: this.username, //String 用户名
              sortChoice: 0, //int 1是所有 2是正在进行，3是已结束
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
          .get("/get_user_released_task_info", {
            params: {
              username: this.username, //String 用户名
              sortChoice: 0, //int 1是所有，2是暂未发布 3是发布但未结束 4是已结束
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
      } else if (this.type === 3) {
        //todo:获得所有需要审核的任务
        axios
          .get("/get_examining_tasks", {
            params: {
              pageNumber: 1,
              adminToken:sessionStorage.getItem("adminToken")
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
.task-page-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.report-title {
  font-size:16px;
  text-align:left;
  width:100%;
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
  width: 1080px;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-evenly;
}
</style>
