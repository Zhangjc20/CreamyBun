<template>
  <div class="task-page-container">
    <div class="task-list-title" v-if="type != 0">
      {{ type === 1 ? "领取任务列表" : "发布任务列表" }}
    </div>
    <div class="radio-box" v-if="type != 0">
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
        @click="handleClickTask(item.id)"
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
export default {
  name: "TaskPage",
  props: {
    type: {
      type: Number,
      default: 1, //0:任务大厅 1:领取列表 2:发布列表
    },
    username: {
      type: String,
      default: "",
    },
  },
  components: {
    SingleTask,
  },
  data() {
    return {
      total: 20,
      items: [
        {
          index: 1,
          taskName: "图像识别",
          starNum: 2,
          donut: 20,
          dataType: "图片",
          id: "123",
          problemType: "选择题",
          startTime: "2020.1.1",
          endTime: "2020.1.28",
        },
        {
          index: 2,
          taskName: "垃圾邮件",
          starNum: 1,
          donut: 70,
          dataType: "文本",
          id: "123",
          problemType: "选择题",
          startTime: "2020.1.1",
          endTime: "2020.1.28",
        },
        {
          index: 3,
          taskName: "音频识别",
          starNum: 3,
          donut: 80,
          dataType: "音频",
          id: "123",
          problemType: "选择题",
          startTime: "2020.1.1",
          endTime: "2020.1.28",
        },
        {
          index: 4,
          taskName: "垃圾邮件",
          starNum: 2,
          donut: 90,
          dataType: "文本",
          id: "123",
          problemType: "选择题",
          startTime: "2020.1.1",
          endTime: "2020.1.28",
        },
        {
          index: 5,
          taskName: "垃圾邮件",
          starNum: 2,
          donut: 90,
          dataType: "文本",
          id: "123",
          problemType: "选择题",
          startTime: "2020.1.1",
          endTime: "2020.1.28",
        },
        {
          index: 6,
          taskName: "垃圾邮件",
          starNum: 2,
          donut: 90,
          dataType: "文本",
          id: "123",
          problemType: "选择题",
          startTime: "2020.1.1",
          endTime: "2020.1.28",
        },
        {
          index: 7,
          isSpace: true,
          id: "123",
        },
        {
          index: 8,
          isSpace: true,
          id: "123",
        },
        {
          index: 9,
          isSpace: true,
          id: "123",
        },
        {
          index: 10,
          isSpace: true,
          id: "123",
        },
      ],
      currentPage: 1,
      sortChoice: 0,
    };
  },
  methods: {
    handleClickTask(value){
      console.log(value);
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
      //onlyLevel:bool false:所有 true:只选入满足等级的
      //donutType:int 1:所有 2:从多到少 3:从少到多
      //newType:int 1:所有 2：最新发布 3：最早结束
      //hardType:int 1:所有 2：从难到易 3：从易到难
      //chosenDataType:int 1:所有 2：图片 3：文本 4：音频  5：视频
      //chosenProblemType:int 1:所有 2：单选 3：多选 4：填空 5：框图 6：混合
      console.log(
        searchInput,
        onlyLevel,
        donutType,
        overType,
        newType,
        hardType,
        chosenDataType,
        chosenProblemType
      );
      axios
        .get("/url", {
          //todo 改成对应的url，参数含义见上注释
          params: {
            username: this.username,
            searchInput: searchInput,
            onlyLevel: onlyLevel,
            donutType: donutType,
            overType: overType,
            newType: newType,
            hardType: hardType,
            chosenDataType: chosenDataType,
            chosenProblemType: chosenProblemType,
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
      if (this.type === 1) {
        //个人领取列表 todo
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
        //个人发布列表 todo
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
      }
    },
    handleSortChange(value) {
      if (this.type === 1) {
        //个人领取列表 todo
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
              console.log("ok");
            }
          })
          .catch((err) => {
            console.log(err);
          });
      } else if (this.type === 2) {
        //个人发布列表 todo
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
      if (this.type === 1) {
        //个人领取列表 todo
        axios
          .get("/get_user_received_task_info", {
            params: {
              username: this.username, //String 用户名
              sortChoice: 1, //int 1是所有 2是正在进行，3是已结束
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
        //个人发布列表 todo
        axios
          .get("/get_user_released_task_info", {
            params: {
              username: this.username, //String 用户名
              sortChoice: 1, //int 1是所有，2是暂未发布 3是发布但未结束 4是已结束
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
    this.init();
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
