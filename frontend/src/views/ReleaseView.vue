<template>
  <el-container class="container">
    <el-header class="header-style">
      <NavBar :login="true" activeItem="3" :username="username" :imageUrl="image.src"></NavBar>
    </el-header>
    <el-container>
      <el-aside class="left-menu-area">
        <el-menu
          default-active="1-1"
          active-text-color="#5EABBF"
          class="el-menu-vertical-demo"
          :default-openeds="['1']"
        >
          <el-sub-menu index="1">
            <template #title>
              <span class="iconfont icon-menu"></span>
              <span>任务选择</span>
            </template>
            <el-menu-item index="1-1" @click="materialType = 0"
              >图像</el-menu-item
            >
            <el-menu-item index="1-2" @click="materialType = 1"
              >文本</el-menu-item
            >
            <el-menu-item index="1-3" @click="materialType = 2"
              >视频</el-menu-item
            >
            <el-menu-item index="1-4" @click="materialType = 3"
              >音频</el-menu-item
            >
            <el-menu-item index="1-5" @click="materialType = 4"
              >自定义</el-menu-item
            >
          </el-sub-menu>
        </el-menu>
      </el-aside>
      <el-main class="main-style">
        <!-- <component :is="show_content"></component> -->
        <ReleaseData
          :login="true"
          :username="username"
          :materialType="materialType"
        ></ReleaseData>
        <!-- <ImageUploadCopy /> -->
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import ReleaseData from "@/components/ReleaseData.vue";
import axios from "axios";
export default {
  name: "MineView",
  components: {
    NavBar,
    ReleaseData,
  },
  data() {
    return {
      image:{
        src:"",
        type:""
      },
      show_content: "MineInfoView",
      materialType: 0,
      username: "",
    };
  },
  methods: {
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
    if (localStorage.getItem('username')) {
      this.username = localStorage.getItem('username');
    }
    if(!localStorage.getItem('avatar')){
      axios.get('http://101.42.118.80:8000/get_avatar',{
        params:{
          username:this.username
        }
      })
      .then((res)=>{
        if(res.data['status']==='ok'){
          if(res.data['avatar']){
              this.image.src = "data:image/png;base64," + res.data["avatar"];
              localStorage.setItem("avatar", this.image.src);
            }
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
.left-menu-area {
  padding-top: 50px;
  padding-left: 10px;
  padding-right: 10px;
}
.el-aside .el-menu {
  border-right: 0;
}
.el-aside {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 5px 0 rgba(0, 0, 0, 0.19);
}
.icon-menu {
  font-size: 30px;
}
.el-aside .el-menu .el-menu-item:hover {
  background-color: #f2f2f2;
}
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
</style>
