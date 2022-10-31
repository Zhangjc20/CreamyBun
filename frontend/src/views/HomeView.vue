<template>
  <el-container class="container">
    <el-header class="header-style">
      <NavBar :login="false" activeItem="1"></NavBar>
    </el-header>
    <el-main class="main-style">
      <div class="custom-box">
        <div class="custom-title-outer"><span class="custom-title">个性化数据标注服务</span></div>
        <el-row>
          <el-col :span="6">
            <div class="round-background">
              <svg class="icon" aria-hidden="true">
                <use xlink:href="#icon-text"></use>
              </svg>
            </div>
            <span class="round-back-font">文本</span>
          </el-col>
          <el-col :span="6">
            <div class="round-background">
              <svg class="icon" aria-hidden="true">
                <use xlink:href="#icon-tupian"></use>
              </svg>
            </div>
            <span class="round-back-font">图片</span>
          </el-col>
          <el-col :span="6">
            <div class="round-background">
              <svg class="icon" aria-hidden="true">
                <use xlink:href="#icon-a-5Jyinboyinpin"></use>
              </svg>
            </div>
            <span class="round-back-font">音频</span>
          </el-col>
          <el-col :span="6">
            <div class="round-background">
              <svg class="icon" aria-hidden="true">
                <use xlink:href="#icon-shipin"></use>
              </svg>
            </div>
            <span class="round-back-font">视频</span>
          </el-col>
        </el-row>
      </div>
      <div class="basic-types-area">
        <span class="basic-types-title">参与众包 互利共赢</span>
        <div class="basic-types-content"> 
          <el-carousel height="280px">
            <el-carousel-item key="1">
              <el-image style="width: 360px; height: 280px" :src="require('@/assets/images/pet1.jpeg')" fit="contain" />
            </el-carousel-item>
            <el-carousel-item key="2">
              <el-image style="width: 360px; height: 280px" :src="require('@/assets/images/pet2.jpeg')" fit="contain" />
            </el-carousel-item>
            <el-carousel-item key="3">
              <el-image style="width: 360px; height: 280px" :src="require('@/assets/images/pet3.jpeg')" fit="contain" />
            </el-carousel-item>
            <el-carousel-item key="4">
              <el-image style="width: 360px; height: 280px" :src="require('@/assets/images/pet4.jpeg')" fit="contain" />
            </el-carousel-item>
        </el-carousel>
        </div>
        <span style="float:right;top:-260px;right:520px;position: relative; font-size: 28px;font-family: YouSheRound;">图片识别</span>
      </div>
    </el-main>
  </el-container>
</template>

<script>
// @ is an alias to /src
import NavBar from "@/components/NavBar.vue";
export default {
  name: 'HomeView',
  components: {
    NavBar,
  },
  data(){
    return {
      itemList:['@/assets/images/pet1.jpeg',
      '@/assets/images/pet2.jpeg',
      '@/assets/images/pet3.jpeg',
      '@/assets/images/pet4.jpeg'
      ],
    }
  }
}
</script>


<style scoped>
.container {
  margin:0;
  height:100%;
}
.basic-types-area {
  margin-top: 60px;
  width:100%;
}
.basic-types-title {
  font-family: YouSheBlack;
  color: #5EABBF;
  font-size: 32px;
}
.basic-types-content {
  width:480px;
  margin-top: 50px;
  margin-left: 240px;
}
.icon {
  width: 3em;
  height: 3em;
  margin-top: 24px;
  vertical-align: -0.15em;
  fill: currentColor;
  overflow: hidden;
}
.round-back-font {
  position: relative;
  top:70px;
  font-size: 26px;
  margin-left: 16px;
  font-family: YouSheBlack;
  color:#E8BF19;
}
.round-background {
  position: relative;
  top:50px;
  left:60px;
  background-color: #ffffff;
  box-shadow: 0 0 6px 1px rgba(0,0,0,0.4);
  border-radius: 50px;
  width: 100px;
  height: 100px;
}
.custom-title-outer {
  padding-top: 50px;
}
.custom-title {
  font-family: YouSheRound;
  font-size: 36px;
  color: #5EABBF;
}
.custom-box {
  border-radius: 20px;
  height:380px;
  width:60%;
  margin-left: 20%;
  box-shadow: 0 0 5px 1px rgba(0,0,0,0.2);
}
.main-style {
  background-color:transparent;
}
.header-style {
  background-image: url(@/assets/images/nav-background.png);
  background-size: cover;
  height: 60px;
  box-shadow: 0 0px 8px 0;
  display: flex;
}
</style>

