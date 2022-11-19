<template>
    <div class="task-container" v-if="isSpace">
      <div class="task-container-inner">
      </div>
    </div>
    <div class="task-container" v-else>
      <div class="task-container-inner" style="border: 2px solid #e9e9e9;">
        <el-image :src="require('@/assets/images/recognize.jpeg')" style="width:180px;height:180px;"></el-image>
        <div class="color-bg-box">
          <div class="title-font">{{props.taskName}}</div>
          <el-row class="donut-font">
            <el-col :span="16" style="text-align:left;padding-left:10px;">
              <el-rate v-model="starNum" disabled class='rate-star'/>
            </el-col>
            <el-col :span="8" class="donut-num">
              <svg class="icon" aria-hidden="true">
                  <use xlink:href="#icon-tiantianquan"></use>
                </svg>
                {{props.donut}}
            </el-col>
          </el-row>
          <el-row class="type-font">
            <el-col :span="12">
              类型：{{props.dataType}}
            </el-col>
            <el-col :span="12">{{props.problemType}}</el-col>
          </el-row>
          <div class="time-font">{{props.startTime}} ~ {{props.endTime}}</div>
        </div>
      </div>
    </div>
</template>

  <script>
  export default{
    name: 'SingleTask',
    props:{
      props:{
        type:Object,
        default:undefined
      }
    },
    data(){
      return {
        starNum: this.props.starNum,
        isSpace: this.props.isSpace
      }
    },
    methods:{
      
    },
    updated(){
      this.isSpace = this.props.isSpace;
      this.starNum = this.props.starNum;
    }
  }
  </script>
  
  <style scoped>
  .task-container {
    background-color: transparent;
    width: 200px;
    height: 300px;
  }
  .donut-num {
    line-height: 34px;
    font-size: 16px;
    text-align: left;
  }
  .title-font {
    padding-top:4px;
    margin-left: 10px;
    text-align: left;
    color:#ffffff;
  }
  .task-container-inner {
    width: 180px;
    border-radius: 6px;
  }
  .color-bg-box {
    background-color: #4dafc7;
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
    color:#fff958;
    margin-bottom: -4px;
    margin-top: -2px;
  }
  .time-font {
    font-size: 14px;
    color:#ffffff;
    margin-top: 6px;
    padding-bottom: 4px;
  }
  .type-font {
    font-size: 14px;
    color:#face3c;
  }
  :deep .el-rate .el-rate__icon {
    margin-right: 0;
  }
  </style>