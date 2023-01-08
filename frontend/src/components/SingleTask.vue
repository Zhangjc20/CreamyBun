<template>
  <div class="task-container" v-if="isSpace" :style="{ cursor: 'default' }">
    <div class="task-container-inner"></div>
  </div>
  <div class="task-container" :style="{ cursor: 'pointer' }" v-else>
    <div class="task-container-inner" style="border: 2px solid #e9e9e9">
      <el-image
        :src="src"
        style="
          display: block;
          margin-bottom: 1px;
          width: 180px;
          height: 180px;
          box-shadow: 3px 3px 12px 0 rgba(0, 0, 0, 0.315);
        "
      >
        <template #placeholder>
          <div class="image-slot">
            <el-image
              style="width: 84px; height: 75px"
              fit="cover"
              :src="require('@/assets/images/logo_small.png')"
              class="jump-logo"
            ></el-image>
            <div class="jump-shadow">封面加载中~</div>
          </div>
        </template>
        <template #error>
          <div class="image-slot">
            <el-image
              style="width: 84px; height: 75px"
              fit="cover"
              :src="require('@/assets/images/logo_small.png')"
              class="jump-logo-err"
            ></el-image>
            <div class="jump-shadow">封面加载失败</div>
          </div>
        </template>
      </el-image>
      <div class="color-bg-box">
        <div class="title-font">{{ props.taskName }}</div>
        <el-row class="donut-font">
          <el-col :span="16" style="text-align: left; padding-left: 10px">
            <el-rate v-model="starNum" disabled class="rate-star" />
          </el-col>
          <el-col :span="8" class="donut-num">
            <svg class="icon" aria-hidden="true">
              <use xlink:href="#icon-tiantianquan"></use>
            </svg>
            {{ props.donut }}
          </el-col>
        </el-row>
        <el-row class="type-font">
          <el-col :span="15" class="type-container">
            类型：{{ props.dataType }}
          </el-col>
          <el-col :span="7">{{ props.problemType }}</el-col>
        </el-row>
        <div class="time-font">{{ props.startTime }} ~ {{ props.endTime }}</div>
        <div v-if="hasOver" class="task-container-inner mask-box">
          <div class="over-box">已结束</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SingleTask",
  props: {
    props: {
      type: Object,
      default: undefined,
    },
  },
  data() {
    return {
      starNum: this.props.starNum,
      isSpace: this.props.isSpace,
      src: this.props.src
        ? this.props.src
        : require("@/assets/images/recognize.jpeg"),
      hasOver:
        this.props.taskStatus == 3 || this.props.taskStatus == 5 ? true : false,
    };
  },
  methods: {},
  updated() {
    this.isSpace = this.props.isSpace;
    this.starNum = this.props.starNum;
    this.src = this.props.src
      ? this.props.src
      : require("@/assets/images/recognize.jpeg");
    this.hasOver =
      this.props.taskStatus == 3 || this.props.taskStatus == 5 ? true : false;
  },
};
</script>

<style scoped>
.type-container {
  text-align: center;
}
.image-slot {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  color: var(--el-text-color-secondary);
  font-size: 18px;
}
.task-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 200px;
  height: 300px;
  cursor: pointer;
}
.donut-num {
  line-height: 34px;
  font-size: 16px;
  text-align: left;
}
.title-font {
  padding-top: 4px;
  margin-left: 10px;
  text-align: left;
  color: #ffffff;
}
.task-container-inner {
  width: 180px;
  position: relative;
}
.color-bg-box {
  background-color: #4dafc7;
  box-shadow: 3px 3px 12px 0 rgba(0, 0, 0, 0.315);
}
.icon {
  width: 1em;
  height: 1em;
  vertical-align: -0.15em;
  fill: currentColor;
  overflow: hidden;
}
.donut-font {
  font-size: 14px;
  color: #fff958;
  margin-bottom: -4px;
  margin-top: -2px;
}
.time-font {
  font-size: 14px;
  color: #ffffff;
  margin-top: 6px;
  padding-bottom: 4px;
}
.type-font {
  font-size: 14px;
  color: #face3c;
}
:deep .el-rate .el-rate__icon {
  margin-right: 0;
}
.mask-box {
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 2;
  top: 0;
}
.over-box {
  margin-bottom: 80px;
  border: 3px solid #fbe484;
  width: 110px;
  height: 32px;
  line-height: 32px;
  border-radius: 4px;
  font-size: 28px;
  color: #ffeda7;
  font-family: YouSheRound;
}
.jump-logo {
  z-index: 2;
  animation: jump-logo 1s infinite;
  animation-timing-function: ease;
  position: absolute;
}
.jump-logo-err {
  z-index: 2;
  position: absolute;
  bottom: 60px;
}
.jump-shadow {
  position: absolute;
  bottom: 30px;
}
@keyframes jump-logo {
  0% {
    bottom: 60px;
  }

  50% {
    bottom: 80px;
  }

  100% {
    bottom: 60px;
  }
}
</style>
