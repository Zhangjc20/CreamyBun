<template>
  <el-container class="container">
    <el-header class="header-style">
      <NavBar
        :login="true"
        activeItem="2"
        :username="username"
        :imageUrl="image.src"
      ></NavBar>
    </el-header>
    <el-container>
      <el-aside class="left-menu-area" id="left-menu">
        <div
          v-if="showLeft"
          @click="changeShow"
          class="opacity-box"
          style="margin-bottom: 1rem; cursor: pointer"
        >
          <el-icon><Hide /></el-icon
          ><span style="font-size: 0.8rem; margin-left: 0.2rem"
            >隐藏侧边栏</span
          >
        </div>
        <el-menu
          default-active="1-1"
          active-text-color="#5EABBF"
          class="el-menu-vertical-demo"
          :default-openeds="['1']"
        >
          <el-sub-menu index="1" default-active="1">
            <template #title>
              <span class="iconfont icon-menu"></span>
              <span>选项菜单</span>
            </template>
            <el-menu-item index="1-1" @click="menuAction(0)"
              >当前任务</el-menu-item
            >
            <el-menu-item index="1-2" @click="menuAction(1)"
              >任务列表</el-menu-item
            >
            <el-menu-item index="1-4" @click="menuAction(3)"
              >任务详情</el-menu-item
            >
            <el-menu-item index="1-5" @click="menuAction(4)"
              >个人中心</el-menu-item
            >
          </el-sub-menu>
        </el-menu>
        <div
          class="logo-box"
          style="
            position: fixed;
            bottom: 0px;
            left: 20px;
            width: 250px;
            height: 250px;
          "
        >
          <div
            style="
              position: absolute;
              bottom: 20px;
              left: 0px;
              width: 20px;
              height: 150px;
            "
          >
            <div
              style="
                position: absolute;
                bottom: 0px;
                border-top: 20px solid #5eabbf;
                border-left: 20px solid transparent;
              "
            ></div>
            <div
              style="
                background-color: #5eabbf;
                position: absolute;
                bottom: 20px;
                width: 20px;
                height: 110px;
              "
            ></div>
            <div
              style="
                position: absolute;
                bottom: 130px;
                border-bottom: 20px solid #5eabbf;
                border-left: 20px solid transparent;
              "
            ></div>
          </div>
          <div
            style="
              position: absolute;
              bottom: 10px;
              left: 40px;
              width: 25px;
              height: 200px;
            "
          >
            <div
              style="
                position: absolute;
                bottom: 0px;
                border-top: 25px solid #fbe484;
                border-right: 25px solid transparent;
              "
            ></div>
            <div
              style="
                background-color: #fbe484;
                position: absolute;
                bottom: 25px;
                width: 25px;
                height: 150px;
              "
            ></div>
            <div
              style="
                position: absolute;
                bottom: 175px;
                border-bottom: 25px solid #fbe484;
                border-right: 25px solid transparent;
              "
            ></div>
          </div>
          <div
            style="
              position: absolute;
              bottom: 65px;
              left: 200px;
              width: 10px;
              height: 80px;
            "
          >
            <div
              style="
                position: absolute;
                bottom: 0px;
                border-top: 10px solid #5eabbf;
                border-right: 10px solid transparent;
              "
            ></div>
            <div
              style="
                background-color: #5eabbf;
                position: absolute;
                bottom: 10px;
                width: 10px;
                height: 60px;
              "
            ></div>
            <div
              style="
                position: absolute;
                bottom: 70px;
                border-bottom: 10px solid #5eabbf;
                border-right: 10px solid transparent;
              "
            ></div>
          </div>
          <div
            style="
              position: absolute;
              bottom: 20px;
              left: 230px;
              width: 20px;
              height: 150px;
            "
          >
            <div
              style="
                position: absolute;
                bottom: 0px;
                border-top: 20px solid #fbe484;
                border-left: 20px solid transparent;
              "
            ></div>
            <div
              style="
                background-color: #fbe484;
                position: absolute;
                bottom: 20px;
                width: 20px;
                height: 110px;
              "
            ></div>
            <div
              style="
                position: absolute;
                bottom: 130px;
                border-bottom: 20px solid #fbe484;
                border-left: 20px solid transparent;
              "
            ></div>
          </div>
          <div
            style="
              position: absolute;
              bottom: 140px;
              left: 170px;
              width: 15px;
              height: 30px;
            "
          >
            <div
              style="
                position: absolute;
                bottom: 0px;
                border-top: 15px solid #fbe484;
                border-left: 15px solid transparent;
              "
            ></div>
            <div
              style="
                position: absolute;
                bottom: 15px;
                border-bottom: 15px solid #fbe484;
                border-left: 15px solid transparent;
              "
            ></div>
          </div>
          <div
            style="
              position: absolute;
              bottom: 150px;
              left: 90px;
              width: 15px;
              height: 30px;
            "
          >
            <div
              style="
                position: absolute;
                bottom: 0px;
                border-top: 15px solid #5eabbf;
                border-right: 15px solid transparent;
              "
            ></div>
            <div
              style="
                position: absolute;
                bottom: 15px;
                border-bottom: 15px solid #5eabbf;
                border-right: 15px solid transparent;
              "
            ></div>
          </div>
          <div
            style="
              position: absolute;
              bottom: 20px;
              left: 90px;
              width: 250px;
              height: 250px;
            "
          >
            <div
              style="
                flex-direction: column;
                position: absolute;
                bottom: 0px;
                margin-left: auto;
                margin-right: auto;
                text-align: center;
              "
            >
              <el-image
                style="width: 88px; height: 80px"
                fit="cover"
                :src="require('@/assets/images/logo_small.png')"
                class="jump-logo"
              ></el-image>
              <div class="jump-shadow"></div>
            </div>
          </div>
        </div>
      </el-aside>
      <el-main class="main-style">
        <div class="phone-box">
          <div
            v-if="!showLeft"
            @click="changeShow"
            class="opacity-box"
            style="position: absolute; z-index: 99; cursor: pointer"
          >
            <el-icon><View /></el-icon
            ><span style="font-size: 0.8rem; margin-left: 0.2rem"
              >显示侧边栏</span
            >
          </div>
          <PerformTask
            :login="true"
            :username="username"
            :taskId="taskId"
            :taskName="taskName"
            :imageSrc="image.src"
            :materialType="materialType"
          />
        </div>
      </el-main>
    </el-container>
  </el-container>
  <el-dialog v-model="dialogShow" center width="70%">
    <div
      style="
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
      "
    >
      <TaskCheck :mode="1" :perform="true" ref="taskCheck" />
    </div>
  </el-dialog>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import PerformTask from "@/components/PerformTask.vue";
import axios from "axios";
import TaskCheck from "@/components/TaskCheck.vue";
export default {
  name: "MineView",
  components: {
    NavBar,
    PerformTask,
    TaskCheck,
  },
  data() {
    return {
      showLeft: true,
      show_content: "MineInfoView",
      username: "",
      taskId: -1,
      taskName: "/*这里填写任务名字*/",
      image: {
        src: "",
        type: "",
      },
      materialType: "",
      dialogShow: false,
    };
  },
  methods: {
    changeShow() {
      if (this.showLeft) {
        let item = document.getElementById("left-menu");
        item.style.left = "-" + String(item.offsetWidth) + "px";
        item.style.opacity = "0";
        item.style.position = "absolute";
      } else {
        let item = document.getElementById("left-menu");
        item.style.opacity = "1";
        item.style.position = "static";
      }
      this.showLeft = !this.showLeft;
    },
    menuAction(type) {
      switch (type) {
        case 0:
          this.$message({
            type: "success",
            message: "当前任务",
          });
          break;
        case 1:
          this.$router.push({
            //跳转到个人中心领取列表
            name: "mine",
            query: {
              username: this.username,
              imageSrc: this.image.src,
              defaultActive: "2",
            },
          });
          break;
        case 2:
          this.$message({
            type: "success",
            message: "历史列表",
          });
          break;
        case 3:
          this.dialogShow = true;
          this.$nextTick(() => {
            this.$refs.taskCheck.showTaskDetail(
              this.taskId,
              this.username,
              0,
              0
            );
          });
          break;
        case 4:
          this.$router.push({
            //跳转到个人中心领取列表
            name: "mine",
            query: {
              username: this.username,
              imageSrc: this.image.src,
              defaultActive: "1",
            },
          });
          break;
        default:
      }
    },
    clickUser() {
      this.$confirm("此操作将永久删除该文件, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          this.$message({
            type: "success",
            message: "删除成功!",
          });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消删除",
          });
        });
    },
  },
  mounted() {
    if (localStorage.getItem("username")) {
      this.username = localStorage.getItem("username");
    }
    if (this.$route.query.taskId) {
      this.taskId = this.$route.query.taskId;
    }
    if (!localStorage.getItem("avatar")) {
      axios
        .get("/get_avatar", {
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
      this.image.src = localStorage.getItem("avatar");
    }
    if (this.$route.query.taskName) {
      this.taskName = this.$route.query.taskName;
    }
    if (this.$route.query.materialType) {
      this.materialType = this.$route.query.materialType;
    }
  },
};
</script>

<style scoped>
@media (min-width: 0px) and (max-width: 768px) {
  .left-menu-area {
    padding-top: 50px;
    padding-left: 10px;
    padding-right: 10px;
    width: 50%;
    transition: all 0.8s ease 0ms;
  }
  .phone-box {
    width: 1100px;
  }
  .logo-box {
    display: none;
  }
}
@media (min-width: 768px) {
  .left-menu-area {
    padding-top: 50px;
    padding-left: 10px;
    padding-right: 10px;
    transition: all 0.8s ease 0ms;
  }
}
.container {
  margin: 0;
  height: 100%;
}
.el-aside .el-menu {
  border-right: 0;
}
.el-aside {
  /* border-right: 1px solid; */
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 5px 0 rgba(0, 0, 0, 0.19);
}
/* .el-aside .el-menu .el-menu-item {
    border-radius: 20px;
  } */
.icon-menu {
  font-size: 30px;
}
.el-aside .el-menu .el-menu-item:hover {
  background-color: #f2f2f2;
}
/* .el-aside .el-menu .el-menu-item.is-active {
    background-color: #5EABBF;
  } */
.el-button--primary {
  background: #fbe484 !important;
  border-color: #fbe484 !important;
  color: #6c6c6c;
}
.el-button--medium {
  width: 80px;
}
.nav-title {
  float: left;
  height: 60px;
  font-family: YouSheRound;
  line-height: 50px;
  font-size: 28px;
  color: #5eabbf;
  margin-left: 80px;
  display: flex;
}
.nav-title-font {
  margin-left: 10px;
  line-height: 60px;
}
.logo {
  width: 45px;
  height: 40px;
  margin-top: 10px;
}
.header-style {
  background-image: url(@/assets/images/nav-background.png);
  background-size: cover;
  height: 60px;
  box-shadow: 0 0px 8px 0;
  display: flex;
}

.menu-out {
  margin-left: 80px;
  background-color: #ffffff;
  width: 470px;
  overflow: hidden;
  border-radius: 40px;
  margin-top: 10px;
  display: flex;
}
.main-style {
  background-color: transparent;
}
.el-nav-menu {
  width: 480px;
  padding-left: 46px;
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

.jump-logo {
  z-index: 2;
  animation: jump-logo 1s infinite;
  animation-timing-function: ease;
}
.jump-shadow {
  z-index: 1;
  width: 100px;
  height: 5px;
  background: #eaeaea;
  border-radius: 100%;
  animation: shadow 1s infinite;
  animation-timing-function: ease;
  margin-left: auto;
  margin-right: auto;
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
    width: 85px;
  }

  50% {
    width: 65px;
  }

  100% {
    width: 85px;
  }
}
</style>
