<template>
    <el-container class="container">
      <el-header class="header-style">
        <NavBar :login="true" activeItem="2"></NavBar>
      </el-header>
      <el-container style="height:100%">
        <el-aside class="left-menu-area">
            <div class="sort-title">
              <span class="iconfont icon-menu icon-choose"></span>
              <span class="sort-font">筛选排序</span>
            </div>
            <div class="sort-area">
              <span class="sort-font">满足等级要求</span>
              <span class="level-switch"><el-switch v-model="onlyLevel" size="small"/></span>
            </div>
            <div class="over-area">
              <div class="sort-title-line">
                <span class="sort-title-area">是否结束</span>
              </div>
              <div class="button-area">
                <CustomButton height="32px" width="88px" marginRight="16px" title="未结束" fontWeight="bold" fontColor="#5EABBF" normalColor="#FBE484" hoverColor="#EED87C" focusColor="#EED87C"></CustomButton>
                <CustomButton height="32px" width="88px" marginLeft="17px" title="所有" normalColor="#FFFFFF" hoverColor="#EAE9E9" focusColor="#EAE9E9"></CustomButton>
              </div>
            </div>
            <div class="later-area">
              <div class="sort-title-line">
                <span class="sort-title-area">按时间排序</span>
              </div>
              <div class="button-area">
                <CustomButton height="32px" width="88px" marginRight="16px" title="最新发布" fontWeight="bold" fontColor="#5EABBF" normalColor="#FBE484" hoverColor="#EED87C" focusColor="#EED87C"></CustomButton>
                <CustomButton height="32px" width="88px" marginLeft="17px" title="最早结束" normalColor="#FFFFFF" hoverColor="#EAE9E9" focusColor="#EAE9E9"></CustomButton>
              </div>
            </div>
            <div class="later-area">
              <div class="sort-title-line">
                <span class="sort-title-area">按难度排序</span>
              </div>
              <div class="button-area">
                <CustomButton height="32px" width="88px" marginRight="16px" title="从难到易" fontWeight="bold" fontColor="#5EABBF" normalColor="#FBE484" hoverColor="#EED87C" focusColor="#EED87C"></CustomButton>
                <CustomButton height="32px" width="88px" marginLeft="17px" title="从易到难" normalColor="#FFFFFF" hoverColor="#EAE9E9" focusColor="#EAE9E9"></CustomButton>
              </div>
            </div>
            <div class="later-area">
              <div class="sort-title-line">
                <span class="sort-title-area">按甜甜圈排序</span>
              </div>
              <div class="button-area">
                <CustomButton height="32px" width="88px" marginRight="16px" title="从多到少" fontWeight="bold" fontColor="#5EABBF" normalColor="#FBE484" hoverColor="#EED87C" focusColor="#EED87C"></CustomButton>
                <CustomButton height="32px" width="88px" marginLeft="17px" title="从少到多" normalColor="#FFFFFF" hoverColor="#EAE9E9" focusColor="#EAE9E9"></CustomButton>
              </div>
            </div>
            <div class="later-area">
              <div class="sort-title-line">
                <span class="sort-title-area">数据类型</span>
              </div>
              <div class="button-area">
                <CustomButton height="32px" width="88px" marginRight="16px" title="图片" fontWeight="bold" fontColor="#5EABBF" normalColor="#FBE484" hoverColor="#EED87C" focusColor="#EED87C"></CustomButton>
                <CustomButton height="32px" width="88px" marginLeft="17px" title="文本" normalColor="#FFFFFF" hoverColor="#EAE9E9" focusColor="#EAE9E9"></CustomButton>
              </div>
              <div class="button-area second-line">
                <CustomButton height="32px" width="88px" marginRight="16px" title="音频" fontWeight="bold" fontColor="#5EABBF" normalColor="#FBE484" hoverColor="#EED87C" focusColor="#EED87C"></CustomButton>
                <CustomButton height="32px" width="88px" marginLeft="17px" title="视频" normalColor="#FFFFFF" hoverColor="#EAE9E9" focusColor="#EAE9E9"></CustomButton>
              </div>
            </div>
            <div class="later-area">
              <div class="sort-title-line">
                <span class="sort-title-area">题型</span>
              </div>
              <div class="button-area">
                <CustomButton height="32px" width="88px" marginRight="16px" title="选择题" fontWeight="bold" fontColor="#5EABBF" normalColor="#FBE484" hoverColor="#EED87C" focusColor="#EED87C"></CustomButton>
                <CustomButton height="32px" width="88px" marginLeft="17px" title="判断题" normalColor="#FFFFFF" hoverColor="#EAE9E9" focusColor="#EAE9E9"></CustomButton>
              </div>
              <div class="button-area second-line">
                <CustomButton height="32px" width="88px" marginRight="16px" title="填空题" fontWeight="bold" fontColor="#5EABBF" normalColor="#FBE484" hoverColor="#EED87C" focusColor="#EED87C"></CustomButton>
                <CustomButton height="32px" width="88px" marginLeft="17px" title="所有" normalColor="#FFFFFF" hoverColor="#EAE9E9" focusColor="#EAE9E9"></CustomButton>
              </div>
            </div>
            <div class="confirm-button-area">
              <CustomButton width="120px" fontSize="17px" fontColor="#FFFFFF" normalColor="#5EABBF" title="确认筛选"></CustomButton>
            </div>
        </el-aside>
        <el-main class="main-style">
          <SimpleTask></SimpleTask>
        </el-main>
      </el-container>
  </el-container>
</template>

  <script>
  import NavBar from '@/components/NavBar.vue';
  import CustomButton from '@/components/CustomButton.vue';
  import SimpleTask from "@/components/SimpleTask.vue";
  export default{
    name: 'TaskCenterView',
    components:{
        NavBar,
        CustomButton,
        SimpleTask,
    },
    data(){
      return {
        onlyLevel: false,
      }
    },
    methods:{
    }
  }
  </script>
  
  <style scoped>
  .container {
    margin:0;
    height:100%;
  }
  .confirm-button-area {
    margin-top: 30px;
  }
  .sort-title-line {
    height:32px;
    padding-left: 36px;
  }
  .second-line {
    margin-top:10px;
  }
  .sort-title-area {
    float: left;
  }
  .level-switch {
    float: left;
    margin-left: 20px;
  }
  .sort-font {
    float:left;
  }
  .sort-title {
    padding-left: 30px;
    width:100%;
    height:50px;
    font-size: 17px;
  }
  .sort-area {
    margin-left: 48px;
    font-size: 15px;
  }
  .over-area {
    margin-left: 10px;
    margin-top: 40px;
    font-size: 15px;
  }
  .later-area {
    margin-top: 20px;
    margin-left: 10px;
    font-size: 15px;
  }
  .icon-choose {
    float: left;
    font-size:20px;
    vertical-align: -6%;
  }
  .left-menu-area {
    margin-top: 4px;
    padding-top: 40px;
    padding-left: 0px;
    padding-right: 10px;
    border-right: 1px solid #e9e9e9;
    overflow: hidden;
  }
  .header-style {
    background-image: url(@/assets/images/nav-background.png);
    background-size: cover;
    height: 60px;
    box-shadow: 0 0px 8px 0;
    display: flex;
  }
  </style>