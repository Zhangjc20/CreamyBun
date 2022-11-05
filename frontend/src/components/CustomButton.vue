<template>
    <span>
        <el-button :round="risRound" class="button-class" @click="clickBack" :disabled="rdisabled">{{title}}</el-button>
    </span>
</template>
  
  <script>
  export default {
    name: 'CustomButton',
    props: {
        disabled:{
          type:Boolean,
          default:false
        },
        title:{
          type:String,
          default:"确认",//按钮中心的文字
        },
        clickBack:{
          type:Function,
          default:undefined
        },
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
        disabledColor:{
            type:String,
            default:"#6cb7ca",
        },
        isRound:{//是否圆角
            type:Boolean,
            default:false
        },
        props:{
            type:Object,
            default:undefined
        }
    },
    data(){
      if(this.props){
        return {
          rwidth:this.props.width,
          rheight:this.props.height,
          rmarginRight:this.props.marginRight,
          rmarginLeft:this.props.marginRight,
          rfontColor:this.props.fontColor,
          rfontSize:this.props.fontSize,
          rfontWeight:this.props.fontWeight,
          rnormalColor:this.props.normalColor,
          rfocusColor:this.props.focusColor,
          rhoverColor:this.props.hoverColor,
          risRound:this.props.isRound,
          rborderWidth:this.props.hasBorder?"1px":"0",
          rborderColor:this.props.borderColor,
          rdisabled:this.props.disabled,
          rdisabledColor:this.props.disabledColor
        }
      }
      else{
        return {
          rwidth:this.width,
          rheight:this.height,
          rmarginRight:this.marginRight,
          rmarginLeft:this.marginRight,
          rfontColor:this.fontColor,
          rfontSize:this.fontSize,
          rfontWeight:this.fontWeight,
          rnormalColor:this.normalColor,
          rfocusColor:this.focusColor,
          rhoverColor:this.hoverColor,
          risRound:this.isRound,
          rborderWidth:this.hasBorder?"1px":"0",
          rborderColor:this.borderColor,
          rdisabled:this.disabled,
          rdisabledColor:this.disabledColor
        }
      }
    },
    methods:{
    },
    updated(){
      if(this.props){
        this.rwidth =this.props.width;
        this.rheight =this.props.height;
        this.rmarginRight = this.props.marginRight;
        this.rmarginLeft= this.props.marginRight;
        this.rfontColor=this.props.fontColor;
        this.rfontSize=this.props.fontSize;
        this.rfontWeight=this.props.fontWeight;
        this.rnormalColor=this.props.normalColor;
        this.rfocusColor=this.props.focusColor;
        this.rhoverColor=this.props.hoverColor;
        this.risRound=this.props.isRound;
        this.rborderWidth=this.props.hasBorder?"1px":"0";
        this.rborderColor=this.props.borderColor;
        this.rdisabled=this.props.disabled;
        this.rdisabledColor=this.props.disabledColor;
      }
      else{
        this.rwidth =this.width;
        this.rheight =this.height;
        this.rmarginRight = this.marginRight;
        this.rmarginLeft= this.marginRight;
        this.rfontColor=this.fontColor;
        this.rfontSize=this.fontSize;
        this.rfontWeight=this.fontWeight;
        this.rnormalColor=this.normalColor;
        this.rfocusColor=this.focusColor;
        this.rhoverColor=this.hoverColor;
        this.risRound=this.isRound;
        this.rborderWidth=this.hasBorder?"1px":"0";
        this.rborderColor=this.borderColor;
        this.rdisabled=this.disabled;
        this.rdisabledColor=this.disabledColor;
      }
    }
  }
  </script>
  
  <style scoped lang="scss">
  .el-button.is-disabled, .el-button.is-disabled:focus, .el-button.is-disabled:hover {
    background-color: v-bind(rdisabledColor);
  }
  .button-class {
    background-color: v-bind(rnormalColor);
    border-color: v-bind(rnormalColor);
    font-size: v-bind(rfontSize);
    color:v-bind(rfontColor);
    font-weight:v-bind(rfontWeight);
    margin-right:v-bind(rmarginRight);
    margin-left:v-bind(rmarginLeft);
    width: v-bind(rwidth);
    height: v-bind(rheight);
    border-width: v-bind(rborderWidth);
    border-color: v-bind(rborderColor);
  }
  .button-class:focus {
    background-color: v-bind(rfocusColor);
    border-color: v-bind(rfocusColor);
    color:v-bind(rfontColor);
    border-width: v-bind(rborderWidth);
    border-color: v-bind(rborderColor);
  }
  .button-class:hover {
    background-color: v-bind(rhoverColor);
    border-color: v-bind(rhoverColor);
    color:v-bind(rfontColor);
    border-width: v-bind(rborderWidth);
    border-color: v-bind(rborderColor);
  }
  </style>
  