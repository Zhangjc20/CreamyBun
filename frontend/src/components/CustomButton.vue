<template>
    <span>
        <el-button :round="isRound" class="button-class" @click="clickBack" :style="style">{{title}}</el-button>
    </span>
</template>
  
  <script>
  export default {
    name: 'CustomButton',
    props: {
        width:{
            type:String,
            default:""
        },
        height:{
            type:String,
            default:""
        },
        marginRight:{
            type:String,
            default:"0"
        },
        marginLeft:{
            type:String,
            default:"0"
        },
        fontColor:{//字体颜色
            type:String,
            default:"#ffffff"
        },
        fontSize:{//字体大小
            type:Number,
            default:12
        },
        fontWeight:{
            type:String,
            default:"normal"
        },
        title:{//按钮中心的文字
            type:String,
            default:"确认"
        },
        normalColor:{//正常按钮颜色
            type:String,
            default:"#5EABBF"
        },
        focusColor:{//选中状态颜色
            type:String,
            default:"#5EABBF"
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
    font-weight:v-bind(fontWeight);
    margin-right:v-bind(marginRight);
    margin-left:v-bind(marginLeft);
    width: v-bind(width);
    height: v-bind(height);
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
  