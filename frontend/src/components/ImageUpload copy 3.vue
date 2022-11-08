<template>
  <div>
      <!-- element 上传图片按钮 -->
      <el-upload class="upload-demo" action="" drag 
        :auto-upload="false" :show-file-list="false" :on-change='changeUpload'>
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">点击上传</div>
        <div class="el-upload__tip">支持绝大多数图片格式，单张图片最大支持5MB</div>
      </el-upload>
       <!-- vueCropper 剪裁图片实现-->
    <el-dialog title="图片剪裁" v-model="dialogVisible" append-to-body>
      <div class="cropper-content">
        <div class="cropper">
          <VueCropper
              ref="cropper"
              :img="option.img"
              :outputSize="option.size"
              :outputType="option.outputType"
              :info="true"
              :full="option.full"
              :canMove="option.canMove"
              :canMoveBox="option.canMoveBox"
              :original="option.original"
              :autoCrop="option.autoCrop"
              :fixed="option.fixed"
              :fixedNumber="option.fixedNumber"
              :centerBox="option.centerBox"
              :infoTrue="option.infoTrue"
              :fixedBox="option.fixedBox"
              :autoCropWidth="option.autoCropWidth"
              :autoCropHeight="option.autoCropHeight"
              @cropMoving="cropMoving"
            />
        </div>
      </div>
      <!-- <template #footer>
          <span class="dialog-footer">
            <el-button @click="dialogVisible = false">Cancel</el-button>
            <el-button type="primary" @click="dialogVisible = false">
              Confirm
            </el-button>
          </span>
        </template> -->
      <template #footer>
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="finish" :loading="loading">确认</el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script>
// import { client } from '@/utils/alioss'
// import { VueCropper } from 'vue-cropper'
export default {
  name: "ImageUpload",
  components: {
    // VueCropper
  },
  data() {
    return {
      dialogVisible: false,
      // 裁剪组件的基础配置option
      option: {
        img: '', // 裁剪图片的地址
        info: true, // 裁剪框的大小信息
        outputSize: 0.8, // 裁剪生成图片的质量
        outputType: 'jpeg', // 裁剪生成图片的格式
        canScale: false, // 图片是否允许滚轮缩放
        autoCrop: true, // 是否默认生成截图框
        // autoCropWidth: 300, // 默认生成截图框宽度
        // autoCropHeight: 200, // 默认生成截图框高度
        fixedBox: true, // 固定截图框大小 不允许改变
        fixed: true, // 是否开启截图框宽高固定比例
        fixedNumber: [7, 5], // 截图框的宽高比例
        full: true, // 是否输出原图比例的截图
        canMoveBox: false, // 截图框能否拖动
        original: false, // 上传图片按照原始比例渲染
        centerBox: false, // 截图框是否被限制在图片里面
        infoTrue: true // true 为展示真实输出图片宽高 false 展示看到的截图框宽高
      },
      picsList: [],  //页面显示的数组
      // 防止重复提交
      loading: false,
      fileinfo:'',
    }
  },
  methods: {
    // 上传按钮   限制图片大小
    changeUpload(file) {
      const isLt5M = file.size / 1024 / 1024 < 5
      if (!isLt5M) {
        this.$message.error('上传文件大小不能超过 5MB!')
        return false
      }
      this.fileinfo = file
      console.log(file,'---------file')
      // 上传成功后将图片地址赋值给裁剪框显示图片
      this.dialogVisible = true
      this.option.img='https://avatars.githubusercontent.com/u/15681693?s=88&u=2097736bf929136febb8c52df09f10290930fdef&v=1'
      // this.$nextTick(() => {
      //   this.option.img = file.url
      //   this.dialogVisible = true
      // })
      console.log(this.option.img,'---------futo')
    },
    // 点击裁剪，这一步是可以拿到处理后的地址
    finish() {
      this.$refs.cropper.getCropBlob((data) => {
        this.loading = true
        console.log(data,'---------------裁剪信息')
       //上传阿里云服务器
        // client().put(fileName, data).then(result => {
        //   this.dialogVisible = false
        //   this.picsList.push(result.url)
        // }).catch(err => {
        //   console.log(err)
        //   this.loading = false
        // })
      })
    }
  }
}
</script>

<style>
.cropper-content .cropper {
  width: 700px;
  height: 300px;
}
/* .cropper {
  width: 500px;
  height: 500px;
} */
</style>