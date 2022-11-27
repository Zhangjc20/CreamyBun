<template>
    <el-container class="container">
      <el-header class="header-style">
        <NavBar :login="true" activeItem="2" :username="username" :imageUrl="image.src"></NavBar>
      </el-header>
      <el-container>
        <el-aside class="left-menu-area">
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
              <el-menu-item index="1-1" @click="menuAction(0)">当前任务</el-menu-item>
              <el-menu-item index="1-2" @click="menuAction(1)">任务列表</el-menu-item>
              <el-menu-item index="1-3" @click="menuAction(2)">历史任务</el-menu-item>
              <el-menu-item index="1-4" @click="menuAction(3)">任务详情</el-menu-item>
              <el-menu-item index="1-5" @click="menuAction(4)">个人中心</el-menu-item>
            </el-sub-menu>
          </el-menu>
        </el-aside>
        <el-main class="main-style">
          <PerformTask
          :login="true"
          :username="username"
          :taskId="taskId"
          :taskName="taskName"
          :imageSrc="image.src"
          />
        </el-main>
      </el-container>
    </el-container>
</template>
  
  <script>
//   import {
//   Menu as IconMenu,
// } from '@element-plus/icons-vue'
  import NavBar from '@/components/NavBar.vue';
  import PerformTask from '@/components/PerformTask.vue';
  export default{
    name: 'MineView',
    components:{
      NavBar,
      PerformTask,
    },
    data(){
      return {
        show_content:"MineInfoView",
        username:"",
        taskId:-1,
        taskName:'/*这里填写任务名字*/',
        image:{
          src:"",
          type:""
        },
      }
    },
    methods:{
      menuAction(type){
        switch (type) {
          case 0:
            this.$message({
              type: "success",
              message: "当前任务",
            });
            break;
          case 1:
            this.$message({
              type: "success",
              message: "任务列表",
            });
            break;
          case 2:
            this.$message({
              type: "success",
              message: "历史列表",
            });
            break;
          case 3:
            this.$message({
              type: "success",
              message: "任务详情",
            });
            break;
          case 4:
            this.$message({
              type: "success",
              message: "个人中心",
            });
            break;
          default:
        }
      },
      clickUser(){
          this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
          }).then(() => {
              this.$message({
                  type: 'success',
                  message: '删除成功!'
              });
          }).catch(() => {
              this.$message({
                  type: 'info',
                  message: '已取消删除'
              });          
              });
          },

    },
    mounted() {
      if (this.$route.query.username) {
        this.username = this.$route.query.username;
        console.log(this.username);
      }
      if (this.$route.query.taskId) {
        this.taskId = this.$route.query.taskId;
        console.log(this.taskId)
      }
      if (this.$route.query.imageSrc) {
        this.image.src = this.$route.query.imageSrc;
      }
      if (this.$route.query.taskName) {
        this.taskName = this.$route.query.taskName;
      }
    },
  }
  </script>
  
  <style scoped>
  .container {
    margin:0;
    height:100%;
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
    /* border-right: 1px solid; */
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 5px 0 rgba(0, 0, 0, 0.19);
  }
  /* .el-aside .el-menu .el-menu-item {
    border-radius: 20px;
  } */
.icon-menu{
  font-size:30px;
}
  .el-aside .el-menu .el-menu-item:hover {
    background-color: #F2F2F2;
  }
  /* .el-aside .el-menu .el-menu-item.is-active {
    background-color: #5EABBF;
  } */
  .el-button--primary {
    background: #FBE484 !important;
    border-color: #FBE484 !important;
    color:#6C6C6C;
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
    color: #5EABBF;
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
    width:470px;
    overflow: hidden;
    border-radius: 40px;
    margin-top: 10px;
    display: flex;
  }
  .main-style {
    background-color:transparent;
  }
  .el-nav-menu {
    width:480px;
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
  .el-menu-item.is-active{
    border-left: 5px solid #5EABBF;
  }
  .el-menu--horizontal .el-menu-item:not(.is-disabled):focus{
    background-color: transparent;
  }
  .el-menu--horizontal .el-menu-item:not(.is-disabled):hover{
    background-color: #f8f8f8;
  }
  </style>