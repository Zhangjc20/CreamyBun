<template>
  <el-main class="main-style" >
    <el-row style="height: 50px;">
      <span class="header-title" style="margin: auto,auto,auto,20px;">{{title}}</span>
      <CustomButton @click="clickAddOption" isRound="true" style="float: right; right: 120px; position: absolute" title="新增选项"/>
    </el-row>

    <template v-if="!isPreview">
        <el-upload
          class="upload-demo"
          action=""
          drag
          :auto-upload="false"
          :show-file-list="false"
          :on-change="handleChangeUpload"
        >
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">点击上传</div>
          <div class="el-upload__tip">
            支持绝大多数图片格式，单张图片最大支持5MB
          </div>
        </el-upload>
      </template>
      <div class="pre-box" v-else>
        <img :src="previewImg" alt="裁剪图片" />
        <el-upload
          class="upload-demo"
          action=""
          :auto-upload="false"
          :show-file-list="false"
          :on-change="handleChangeUpload"
        >
          <el-button type="primary" plain>更换图片</el-button>
        </el-upload>
      </div>

      <el-dialog
        v-model="dialogVisible"
        title="Tips"
        width="60%"
        :before-close="handleClose"
      >
        <div class="cut">
          <VueCropper ref="cropper" 
            img="https://avatars2.githubusercontent.com/u/15681693?s=460&v=4" 
            :output-size="option.size" 
            :output-type="option.outputType" 
            :info="true" 
            :full="option.full" 
            :fixed="fixed" 
            :fixed-number="fixedNumber"
            :can-move="option.canMove" 
            :can-move-box="option.canMoveBox" 
            :fixed-box="option.fixedBox" 
            :original="option.original"
            :auto-crop="option.autoCrop" 
            :auto-crop-width="option.autoCropWidth" 
            :auto-crop-height="option.autoCropHeight" 
            :center-box="option.centerBox"
            @real-time="realTime" 
            :high="option.high"
            @img-load="imgLoad" 
            mode="cover" 
            :max-img-size="option.max" 
            @crop-moving="cropMoving">
          </VueCropper>
        </div>
        <template #footer>
          <span class="dialog-footer">
            <el-button @click="isPreview = true">Cancel</el-button>
            <el-button type="primary" @click="dialogVisible = false">
              Confirm
            </el-button>
          </span>
        </template>
      </el-dialog>


      
  </el-main>
</template>

<script>
import { VueCropper } from 'vue-cropper'
import CustomButton from './CustomButton.vue';
export default {
  name: 'ImageUpload',
  components: {
    CustomButton,
    VueCropper,
  },
  props: {
    title:String,
  },
  data(){
    return {
      dialogVisible:false,
      questionType: this.multiple,
      currentOption:'26',
      description:'',
      optionList:[],
      idRef:['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
      minOptionNum:'',
      maxOptionNum:'',
      mustDo:true,
      tempQuestion:{},
      isPreview:false,
      option: {
        img: 'https://avatars2.githubusercontent.com/u/15681693?s=460&v=4',
        size: 1,
        full: false,
        outputType: 'png',
        canMove: true,
        fixedBox: false,
        original: false,
        canMoveBox: true,
        autoCrop: true,
        // 只有自动截图开启 宽度高度才生效
        autoCropWidth: "180px",
        autoCropHeight: "180px",
        centerBox: false,
        high: true,
        max: 99999,
      },
      show: true,
      fixed: true,
      fixedNumber: [16, 9],
    }
  },
  methods:{
    clickAddOption(){
      var tempOption = {}
      var len = this.optionList.length
      if(len < 26){
        tempOption['index'] = len
        tempOption['name'] = this.idRef[len]
        tempOption['content'] = ''
        this.optionList.push(tempOption)
        console.log(this.optionList)
      }
      
    },
    handleChangeUpload(file){
      const isJPG =
        file.raw.type === "image/jpeg" || file.raw.type === "image/png";
      const isLt2M = file.size / 1024 / 1024 < 5;
      if (!isJPG) {
        this.$message.error("上传头像图片只能是 JPG/PNG 格式!");
        return false;
      }
      if (!isLt2M) {
        this.$message.error("上传头像图片大小不能超过 2MB!");
        return false;
      }
      this.$nextTick(async () => {
        // base64方式
        this.option.img = URL.createObjectURL(file.raw);
        console.log("suhadbouhfdaibvailuhfba",this.option.img)
        this.loading = false;
        this.dialogVisible = true;
      });
    },
    cropMoving(data) {
            // 截图框的左上角 x，y和右下角坐标x，y
      let cropAxis = [data.axis.x1, data.axis.y1, data.axis.x2, data.axis.y2]
      console.log(cropAxis)
    },
  }
}

</script>

<style scoped>
  .cut {
    width: 500px;
    height: 500px;
    margin: 30px auto;
  }
  .cropper-box .cropper {
    width: 700px;
    height: 30px;
  }
  .header-style{
    border-radius: 5px;
    box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
    height: 100px;
    padding: 20px 20px 20px 40px;
  }
  .header-breadcrumb{
    margin:0 0 10px 0;
  }
  .header-title{
    float:left;
    font-size:17px;
    font-weight:700;
  }
  .main-style{
    padding: 20px 20px 20px 40px;
    border-radius: 5px;
    box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
    margin-left: 40px;
    margin-right: 40px;
  }
</style>