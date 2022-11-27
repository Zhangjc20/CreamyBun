<template>
    <el-container class="container">
      <el-header class="header-style">
        <NavBar
          :login="true"
          activeItem="4"
          :username="username"
          :imageUrl="image.src"
        ></NavBar>
      </el-header>
      <el-container>
        <el-main class="main-style">
          <keep-alive
            include="FeedbackPage"
          >
            <component
              :is="show_content"
              :key="show_content"
              :items="items"
              :total="total"
              :username="username"
              ref="coreComponent"
              @initAvatar="initAvatar"
              @changeUsername="changeUsername"
              @changeAvatar="changeAvatar"
            ></component>
          </keep-alive>
        </el-main>
      </el-container>
    </el-container>
  </template>
  
  <script>
  import NavBar from "@/components/NavBar.vue";
  import FeedbackPage from "@/components/FeedbackPage.vue";
  import axios from "axios";
  export default {
    name: "FeedbackManagerView",
    components: {
      NavBar,
      FeedbackPage, 
    },
    data() {
      return {
        image: {
          src: "",
          type: "",
        },
        show_content: "FeedbackPage",
        total: 4,
        username: "",
        items: [
        ],
      };
    },
    methods: {
      changeAvatar(src) {
        this.image.src = src;
      },
      changeUsername(newUsername) {
        this.username = newUsername;
        console.log(this.username);
      },
      initAvatar(src) {
        this.image.src = src;
      },
    },
    mounted() {
      let formData = new FormData();
      formData.append("email", "sdfsdfsdf");
      this.show_content = "FeedbackPage";
      axios({method:"Post",url:'http://localhost:8000/get_feedback/',headers: {'Content-Type': 'multipart/form-data',},data:formData})
      .then(res => {
        //alert(res.data['feedback_list'][1]['image_url']);
        this.items = res.data['feedback_list'];
      })
    },
  };
  </script>
  
  <style scoped>
  .container {
    margin: 0;
    height: 100%;
  }
  .left-menu-area {
    padding-top: 100px;
    padding-left: 10px;
    padding-right: 10px;
  }
  .el-aside .el-menu {
    border-right: 0;
  }
  .el-aside .el-menu .el-menu-item {
    border-radius: 20px;
  }
  .el-aside .el-menu .el-menu-item:hover {
    background-color: #f2f2f2;
  }
  .el-aside .el-menu .el-menu-item.is-active {
    background-color: #5eabbf;
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
  .el-menu--horizontal .el-menu-item:not(.is-disabled):focus {
    background-color: transparent;
  }
  .el-menu--horizontal .el-menu-item:not(.is-disabled):hover {
    background-color: #f8f8f8;
  }
  </style>
  