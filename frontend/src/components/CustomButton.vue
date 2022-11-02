<template>
    <span>
        <el-button :round="isRound" class="button-class" @click="clickBack">{{title}}{{sa}}</el-button>
    </span>
</template>
  
  <script>
  export default {
    name: 'CustomButton',
    props: {
        title:{
          type:String,
          default:"确认",//按钮中心的文字
        },
        clickBack:{
          type:Function,
          default:undefined
        },
        props:{
            type:Object,
            default:function(){
                return {
                    width:"",
                    height:"",
                    marginRight:"0",
                    marginLeft:"0",
                    fontColor:"#606266",//字体颜色
                    fontSize:12,//字体大小
                    fontWeight:"normal",
                    normalColor:"#409eff",//正常按钮颜色
                    focusColor:"#337ecc",//选中状态颜色
                    hoverColor:"#79bbff",//悬停颜色
                    borderColor:"#555555",
                    hasBorder:false,
                    isRound:false,//是否圆角
                }
            }
        }
    },
    data(){
        return {
          width:this.props.width,
          height:this.props.height,
          marginRight:this.props.marginRight,
          marginLeft:this.props.marginRight,
          fontColor:this.props.fontColor,
          fontSize:this.props.fontSize,
          fontWeight:this.props.fontWeight,
          normalColor:this.props.normalColor,
          focusColor:this.props.focusColor,
          hoverColor:this.props.hoverColor,
          isRound:this.props.isRound,
          borderWidth:this.props.hasBorder?"1px":"0",
          borderColor:this.props.borderColor,
        }
    },
    methods:{
    },
    updated(){
      this.width =this.props.width;
      this.height =this.props.height;
      this.marginRight = this.props.marginRight;
      this.marginLeft= this.props.marginRight;
      this.fontColor=this.props.fontColor;
      this.fontSize=this.props.fontSize;
      this.fontWeight=this.props.fontWeight;
      this.normalColor=this.props.normalColor;
      this.focusColor=this.props.focusColor;
      this.hoverColor=this.props.hoverColor;
      this.isRound=this.props.isRound;
      this.borderWidth=this.props.hasBorder?"1px":"0";
      this.borderColor=this.props.borderColor;
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
    border-width: v-bind(borderWidth);
    border-color: v-bind(borderColor);
  }
  .button-class:focus {
    background-color: v-bind(focusColor);
    border-color: v-bind(focusColor);
    color:v-bind(fontColor);
    border-width: v-bind(borderWidth);
    border-color: v-bind(borderColor);
  }
  .button-class:hover {
    background-color: v-bind(hoverColor);
    border-color: v-bind(hoverColor);
    color:v-bind(fontColor);
    border-width: v-bind(borderWidth);
    border-color: v-bind(borderColor);
  }
  </style>
  