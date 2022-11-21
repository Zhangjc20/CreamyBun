<template>
    <div class="task-container" v-if="isSpace">
      <div class="task-container-inner">
      </div>
    </div>
    <div class="task-container" v-else>
      <div class="task-container-inner" style="border: 2px solid #e9e9e9;">
        <div style="float: left;">
          <el-image :src="image.src ? image.src : require('@/assets/images/avatar.jpeg')" style="width:180px;height:180px;"></el-image>
        </div>
        <div class="color-bg-box" style="float: right;">
          <div class="title-font">问题类型 : {{props.feedback_type}}</div>
          <el-row class="type-font">
            <el-col>
              通知邮箱：{{props.inform_email}}
            </el-col>
          </el-row>
          <el-row>
            <el-col>
              问题描述：{{props.description}}
            </el-col>
          </el-row>
        </div>
      </div>
    </div>
</template>

  <script>
  export default{
    name: 'SingleFeedback',
    props:{
      props:{
        type:Object,
        default:undefined
      }
    },
    data(){
      return {
        starNum: this.props.starNum,
        isSpace: this.props.isSpace,
        image: {
        src: null,
        type: null,
      },
      }
    },
    methods:{
      base64ImgtoFile(dataurl, filename = "file") {
      const arr = dataurl.split(",");
      const mime = arr[0].match(/:(.*?);/)[1];
      const suffix = mime.split("/")[1];
      const bstr = atob(arr[1]);
      let n = bstr.length;
      const u8arr = new Uint8Array(n);
      while (n--) {
        u8arr[n] = bstr.charCodeAt(n);
      }
      return new File([u8arr], `${filename}.${suffix}`, {
        type: mime,
      });
    },
    },
    mounted()
    {
      this.isSpace = this.props.isSpace;
      this.starNum = this.props.starNum;
      const imageFile = this.base64ImgtoFile(
              "data:image/png;base64," + this.props.image_url
            );
            this.image.src =
              window.webkitURL.createObjectURL(imageFile) ||
              window.URL.createObjectURL(imageFile);
            localStorage.setItem('imageSrc',this.image.src);
            //alert(this.image.src);
            //this.$emit("initAvatar", this.image.src);
    }
  }
  </script>
  
  <style scoped>
  .task-container {
    background-color: transparent;
    width: 700px;
    height: 200px;
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
    width: 700px;
    border-radius: 6px;
  }
  .color-bg-box {
    background-color: #4dafc7;
    width: 520px;
    height: 180px;
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
    font-size: 16px;
    color:#face3c;
  }
  :deep .el-rate .el-rate__icon {
    margin-right: 0;
  }
  </style>