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
    <el-container class="main-area">
      <el-aside class="left-menu-area">
        <div class="sort-title">
          <span class="iconfont icon-menu icon-choose"></span>
          <span class="sort-font">筛选排序</span>
        </div>
        <div class="sort-area">
          <span class="sort-font">满足等级要求</span>
          <span class="level-switch"
            ><el-switch v-model="onlyLevel" size="small"
          /></span>
        </div>
        <div class="over-area">
          <div class="sort-title-line">
            <span class="sort-title-area">按甜甜圈排序</span>
          </div>
          <div class="button-area">
            <CustomButton
              title="默认"
              :props="donutType === 1 ? activeProps : normalProps"
              @click="handleClickBtn(4, 1)"
            ></CustomButton>
            <CustomButton
              title="从多到少"
              :props="donutType === 2 ? activeProps : normalProps"
              @click="handleClickBtn(4, 2)"
            ></CustomButton>
          </div>
          <div class="button-area second-line">
            <CustomButton
              title="从少到多"
              :props="donutType === 3 ? activeProps : normalProps"
              @click="handleClickBtn(4, 3)"
            ></CustomButton>
            <CustomButton :props="disabledProps"></CustomButton>
          </div>
        </div>
        <div class="later-area">
          <div class="sort-title-line">
            <span class="sort-title-area">是否结束</span>
          </div>
          <div class="button-area">
            <CustomButton
              title="所有"
              :props="overType === 1 ? activeProps : normalProps"
              @click="handleClickBtn(1, 1)"
            ></CustomButton>
            <CustomButton
              title="未结束"
              :props="overType === 2 ? activeProps : normalProps"
              @click="handleClickBtn(1, 2)"
            ></CustomButton>
          </div>
          <div class="button-area second-line">
            <CustomButton
              title="已结束"
              :props="overType === 3 ? activeProps : normalProps"
              @click="handleClickBtn(1, 3)"
            ></CustomButton>
            <CustomButton :props="disabledProps"></CustomButton>
          </div>
        </div>
        <div class="later-area">
          <div class="sort-title-line">
            <span class="sort-title-area">按时间排序</span>
          </div>
          <div class="button-area">
            <CustomButton
              title="默认"
              :props="newType === 1 ? activeProps : normalProps"
              @click="handleClickBtn(2, 1)"
            ></CustomButton>
            <CustomButton
              title="最新发布"
              :props="newType === 2 ? activeProps : normalProps"
              @click="handleClickBtn(2, 2)"
            ></CustomButton>
          </div>
          <div class="button-area second-line">
            <CustomButton
              title="最早结束"
              :props="newType === 3 ? activeProps : normalProps"
              @click="handleClickBtn(2, 3)"
            ></CustomButton>
            <CustomButton :props="disabledProps"></CustomButton>
          </div>
        </div>
        <div class="later-area">
          <div class="sort-title-line">
            <span class="sort-title-area">按难度排序</span>
          </div>
          <div class="button-area">
            <CustomButton
              title="默认"
              :props="hardType === 1 ? activeProps : normalProps"
              @click="handleClickBtn(3, 1)"
            ></CustomButton>
            <CustomButton
              title="从难到易"
              :props="hardType === 2 ? activeProps : normalProps"
              @click="handleClickBtn(3, 2)"
            ></CustomButton>
          </div>
          <div class="button-area second-line">
            <CustomButton
              title="从易到难"
              :props="hardType === 3 ? activeProps : normalProps"
              @click="handleClickBtn(3, 3)"
            ></CustomButton>
            <CustomButton :props="disabledProps"></CustomButton>
          </div>
        </div>
        <div class="later-area">
          <div class="sort-title-line">
            <span class="sort-title-area">数据类型</span>
          </div>
          <div class="button-area">
            <CustomButton
              title="所有"
              :props="chosenDataType === 1 ? activeProps : normalProps"
              @click="handleClickBtn(5, 1)"
            ></CustomButton>
            <CustomButton
              title="图片"
              :props="chosenDataType === 2 ? activeProps : normalProps"
              @click="handleClickBtn(5, 2)"
            ></CustomButton>
          </div>
          <div class="button-area second-line">
            <CustomButton
              title="文本"
              :props="chosenDataType === 3 ? activeProps : normalProps"
              @click="handleClickBtn(5, 3)"
            ></CustomButton>
            <CustomButton
              title="视频"
              :props="chosenDataType === 4 ? activeProps : normalProps"
              @click="handleClickBtn(5, 4)"
            ></CustomButton>
          </div>
          
          <div class="button-area second-line">
            <CustomButton
              title="音频"
              :props="chosenDataType === 5 ? activeProps : normalProps"
              @click="handleClickBtn(5, 5)"
            ></CustomButton>
            <CustomButton title="混合" 
              :props="chosenDataType === 6 ? activeProps : normalProps" 
              @click="handleClickBtn(5, 6)">
            </CustomButton>
          </div>
        </div>
        <div class="later-area">
          <div class="sort-title-line">
            <span class="sort-title-area">题型</span>
          </div>
          <div class="button-area">
            <CustomButton
              title="所有"
              :props="chosenProblemType === 1 ? activeProps : normalProps"
              @click="handleClickBtn(6, 1)"
            ></CustomButton>
            <CustomButton
              title="单选"
              :props="chosenProblemType === 2 ? activeProps : normalProps"
              @click="handleClickBtn(6, 2)"
            ></CustomButton>
          </div>
          <div class="button-area second-line">
            <CustomButton
              title="多选"
              :props="chosenProblemType === 3 ? activeProps : normalProps"
              @click="handleClickBtn(6, 3)"
            ></CustomButton>
            <CustomButton
              title="填空"
              :props="chosenProblemType === 4 ? activeProps : normalProps"
              @click="handleClickBtn(6, 4)"
            ></CustomButton>
          </div>
          <div class="button-area second-line">
            <CustomButton
              title="框图"
              :props="chosenProblemType === 5 ? activeProps : normalProps"
              @click="handleClickBtn(6, 5)"
            ></CustomButton>
            <CustomButton
              title="混合"
              :props="chosenProblemType === 6 ? activeProps : normalProps"
              @click="handleClickBtn(6, 6)"
            ></CustomButton>
          </div>
        </div>
        <div class="confirm-button-area">
          <CustomButton :props="confirmProps" title="确认筛选" @click.stop="handleSort"></CustomButton>
        </div>
      </el-aside>
      <el-main>
        <el-header style="display: flex;justify-content: center;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);border-radius: 5px;">
            <div class="search-area">
            搜索任务
            <el-input
              v-model="searchInput"
              placeholder="请输入搜索的任务"
              class="search-input"
            >
              <template #append>
                <el-button @click="handleSort"
                  ><el-icon><Search /></el-icon
                ></el-button>
              </template>
            </el-input>
          </div>
        </el-header>
        <div style="margin-top:24px;">
          <TaskPage :type="0" ref="taskPage" :username="username" :imageSrc="image.src"></TaskPage>
        </div>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import CustomButton from "@/components/CustomButton.vue";
import TaskPage from "@/components/TaskPage.vue";
import axios from 'axios';
export default {
  name: "TaskCenterView",
  components: {
    NavBar,
    CustomButton,
    TaskPage,
  },
  data() {
    return {
      image: {
        src: "",
        type: "",
      },
      confirmProps: {
        width: "120px",
        fontSize: "16px",
        fontColor: "#FFFFFF",
        normalColor: "#5EABBF",
        hoverColor: "#549fb2",
        focusColor: "#549fb2",
      },
      disabledProps: {
        hasBorder: false,
        height: "32px",
        width: "88px",
        fontWeight: "normal",
        fontColor: "transparent",
        normalColor: "transparent",
        hoverColor: "transparent",
        focusColor: "transparent",
      },
      activeProps: {
        hasBorder: false,
        height: "32px",
        width: "88px",
        fontWeight: "bold",
        fontColor: "#5EABBF",
        normalColor: "#FBE484",
        hoverColor: "#EED87C",
        focusColor: "#EED87C",
      },
      normalProps: {
        hasBorder: true,
        borderColor: "#bbbbbb",
        height: "32px",
        width: "88px",
        normalColor: "#FFFFFF",
        hoverColor: "#EAE9E9",
        focusColor: "#EAE9E9",
      },
      onlyLevel: false,
      overType: 1,
      newType: 1,
      hardType: 1,
      donutType: 1,
      chosenDataType: 1,
      chosenProblemType: 1,
      searchInput: "",
      username: "",
      items: [
        {
          index: 1,
          taskName: "图像识别",
          starNum: 2,
          donut: 20,
          dataType: "图片",
        },
        {
          index: 2,
          taskName: "垃圾邮件",
          starNum: 1,
          donut: 70,
          dataType: "文本",
        },
        {
          index: 3,
          taskName: "音频识别",
          starNum: 3,
          donut: 80,
          dataType: "音频",
        },
        {
          index: 4,
          taskName: "垃圾邮件",
          starNum: 2,
          donut: 90,
          dataType: "文本",
        },
        {
          index: 5,
          taskName: "图像框图",
          starNum: 5,
          donut: 100,
          dataType: "图片",
        },
        {
          index: 6,
          taskName: "垃圾邮件",
          starNum: 4,
          donut: 10,
          dataType: "文本",
        },
      ],
    };
  },
  methods: {
    handleSort(){
      this.$refs.taskPage.sort(this.searchInput,this.onlyLevel,this.donutType,this.overType,this.newType,this.hardType,this.chosenDataType,this.chosenProblemType);
    },
    handleClickBtn(btn, val) {
      switch (btn) {
        case 1: //调整overType即是否结束
          this.overType = val;
          break;
        case 2: //调整newType即按时间排序
          this.newType = val;
          break;
        case 3: //调整hardType即按难度排序
          this.hardType = val;
          break;
        case 4: //调整donutType即按甜甜圈排序
          this.donutType = val;
          break;
        case 5: //调整chosenDataType即数据类型
          this.chosenDataType = val;
          break;
        case 6:
          this.chosenProblemType = val;
          break;
        default:
      }
    },
  },
  mounted() {
    if (localStorage.getItem('username')) {
      this.username = localStorage.getItem('username');
    }
    if(!localStorage.getItem('avatar')){
      axios.get('http://101.42.118.80:8000/get_avatar/',{
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
.icon {
  width: 1em;
  height: 1em;
  vertical-align: -0.15em;
  fill: currentColor;
  overflow: hidden;
}
.container {
  margin: 0;
  height: 100%;
}
.button-area {
  display: flex;
  justify-content: space-evenly;
}
.search-area {
  margin-top: 15px;
  margin-left: 40px;
  color: #555555;
  float:left;
}
.main-area {
  height: 100%;
  overflow: hidden;
}
.search-input {
  width: 400px;
  margin-left: 10px;
  vertical-align: 0%;
}
.confirm-button-area {
  margin-top: 30px;
}
.sort-title-line {
  height: 32px;
  padding-left: 36px;
}
.second-line {
  margin-top: 10px;
}
.sort-title-area {
  float: left;
}
.level-switch {
  float: left;
  margin-left: 20px;
}
.sort-font {
  float: left;
}
.sort-title {
  padding-left: 30px;
  width: 100%;
  height: 50px;
  font-size: 17px;
}
.sort-area {
  margin-left: 46px;
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
  font-size: 20px;
  vertical-align: -6%;
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
.el-aside {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 5px 0 rgba(0, 0, 0, 0.19);
}
.header-style {
  background-image: url(@/assets/images/nav-background.png);
  background-size: cover;
  height: 60px;
  box-shadow: 0 0px 8px 0;
  display: flex;
}
.main-style{
    padding: 20px 20px 20px 40px;
    margin-left: 20px;
    border-radius: 5px;
    box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
  }
</style>
