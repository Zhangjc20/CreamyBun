<template>
    <div class="task-container">
        <el-image :src="require('@/assets/images/recognize.jpeg')" style="width:200px;height:200px;"></el-image>
        <div>图像识别</div>
        <div class="picture-font">
          <el-rate v-model="starNum" disabled/>
          类型：图片
        </div>
        <div class="donut-font">
          <svg class="icon" aria-hidden="true">
            <use xlink:href="#icon-tiantianquan"></use>
          </svg>
          20
        </div>
        <div class="time-font">2022年10月22日 ~ 2022年10月23日</div>
    </div>
</template>

  <script>
  export default{
    name: 'SimpleTask',
    data(){
      return {
        starNum:2,
      }
    },
    methods:{
    }
  }
  </script>
  
  <style scoped>
  .task-container {
    border: 1px solid #e9e9e9;
    background-color: transparent;
    width: 200px;
    height: 320px;
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
  }
  .time-font {
    font-size: 12px;
  }
  .picture-font {
    font-size: 14px;
  }
  ::v-deep .el-rate .el-rate__icon {
    margin-right: 0;
  }
  </style>