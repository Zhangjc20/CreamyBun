<template>
    <span>
        <el-button :round="isRound" class="button-class" @click="clickBack">{{title}}</el-button>
    </span>
</template>
  
  <script>
  export default {
    name: 'CustomButton',
    props: {
        fontColor:{//字体颜色
            type:String,
            default:"#606266"
        },
        fontSize:{//字体大小
            type:Number,
            default:12
        },
        title:{//按钮中心的文字
            type:String,
            default:"确认"
        },
        normalColor:{//正常按钮颜色
            type:String,
            default:"#409eff"
        },
        focusColor:{//选中状态颜色
            type:String,
            default:"#337ecc"
        },
        hoverColor:{//悬停颜色
            type:String,
            default:"#79bbff"
        },
        isRound:{//是否圆角
            type:Boolean,
            default:false
        },
        clickBack:{//按下的回调函数
            type: Function,
            default:null
        }
    },
    data(){
        return {
          
        }
    },
    methods:{
    }
  }
  </script>
  
  <style scoped lang="scss">
  .button-class {
    background-color: v-bind(normalColor);
    border-color: v-bind(normalColor);
    font-size: v-bind(fontSize);
    color:v-bind(fontColor);
  }
  .button-class:focus {
    background-color: v-bind(focusColor);
    border-color: v-bind(focusColor);
    color:v-bind(fontColor);
  }
  .button-class:hover {
    background-color: v-bind(hoverColor);
    border-color: v-bind(hoverColor);
    color:v-bind(fontColor);
  }
  </style>
  