<template>
  <el-config-provider :locale="locale">
    <router-view />
  </el-config-provider>
</template>

<script>
import zhCn from "element-plus/lib/locale/lang/zh-cn";
export default {
  components: {},
  data() {
    return {
      locale: zhCn,
    };
  },
};
</script>

<style lang="scss">
@font-face {
  font-family: "YouSheRound";
  src: url(@/assets/fonts/优设标题圆.otf);
}
@font-face {
  font-family: "YouSheBlack";
  src: url(@/assets/fonts/优设标题黑.ttf);
}
@font-face {
  font-family: "QianTuBlack";
  src: url(@/assets/fonts/千图厚黑体.ttf);
}
@font-face {
  font-family: "YiPinChuangXiang";
  src: url(@/assets/fonts/一品创享体.ttf);
}
@font-face {
  font-family: "XiaWuManHei";
  src: url(@/assets/fonts/霞鹜漫黑.ttf);
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
  padding: 0;
  margin: 0;
}

html {
  height: 100%;
  margin: 0;
  padding: 0;
}

/*重置body属性*/
body {
  padding: 0;
  margin: 0;
  /*继承html*/
  height: 100%;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}

::-webkit-scrollbar {
  width: 12px; /*对垂直流动条有效*/
}

/*定义滚动条的轨道颜色、内阴影及圆角*/
::-webkit-scrollbar-track {
  border-radius: 4px;
}

/*定义滑块颜色、内阴影及圆角*/
::-webkit-scrollbar-thumb {
  border-radius: 8px;
  background-color: #efefef;
}

/*定义滑块悬停变化颜色、内阴影及圆角*/
::-webkit-scrollbar-thumb:hover {
  background-color: #dddddd;
}
</style>
