<template>
  <el-main class="main-style" >
    <div class="cropper-wrapper">
      <!-- element 上传图片按钮 -->
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
      
      <!-- vueCropper 剪裁图片实现-->
      <el-dialog
        title="图片剪裁"
        v-model="dialogVisible"
        class="crop-dialog"
        append-to-body
      >
        <div class="cropper-content">
          <div class="cropper" style="text-align: center">
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
        <div class="action-box">
          <el-upload
            class="upload-demo"
            action=""
            :auto-upload="false"
            :show-file-list="false"
            :on-change="handleChangeUpload"
          >
            <el-button type="primary" plain>更换图片</el-button>
          </el-upload>
          <el-button type="primary" plain @click="clearImgHandle"
            >清除图片</el-button
          >
          <el-button type="primary" plain @click="rotateLeftHandle"
            >左旋转</el-button
          >
          <el-button type="primary" plain @click="rotateRightHandle"
            >右旋转</el-button
          >
          <el-button type="primary" plain @click="changeScaleHandle(1)"
            >放大</el-button
          >
          <el-button type="primary" plain @click="changeScaleHandle(-1)"
            >缩小</el-button
          >
          <el-button type="primary" plain @click="downloadHandle('blob')"
            >下载</el-button
          >
        </div>
        <!-- <template #footer class="dialog-footer">
          <el-button @click="dialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="finish" :loading="loading"
            >确认</el-button
          >
        </template> -->
          
      </el-dialog>
    </div>
  </el-main>

</template>

<script>
import { VueCropper } from 'vue-cropper'
export default {
  name: "ImageUpload",
  components: {
    VueCropper
  },
  data() {
    return {
      isPreview: false,
      dialogVisible: false,
      previewImg: "", // 预览图片地址
      // 裁剪组件的基础配置option
      option: {
        img: "https://pic1.zhimg.com/80/v2-366c0aeae2b4050fa2fcbfc09c74aad4_720w.jpg", // 裁剪图片的地址
        info: true, // 裁剪框的大小信息
        outputSize: 1, // 裁剪生成图片的质量
        outputType: "png", // 裁剪生成图片的格式
        canScale: true, // 图片是否允许滚轮缩放
        autoCrop: true, // 是否默认生成截图框
        canMoveBox: true, // 截图框能否拖动
        autoCropWidth: 200, // 默认生成截图框宽度
        autoCropHeight: 200, // 默认生成截图框高度
        fixedBox: false, // 固定截图框大小 不允许改变
        fixed: true, // 是否开启截图框宽高固定比例
        fixedNumber: [1, 1], // 截图框的宽高比例
        full: false, // 是否输出原图比例的截图
        original: false, // 上传图片按照原始比例渲染
        centerBox: false, // 截图框是否被限制在图片里面
        infoTrue: true, // true 为展示真实输出图片宽高 false 展示看到的截图框宽高
      },
      // 防止重复提交
      loading: false,
    };
  },
  methods: {
    // 上传按钮 限制图片大小和类型
    handleChangeUpload(file, fileList) {
      console.log(fileList)
      const isJPG =
        file.raw.type === "image/jpeg" || file.raw.type === "image/png";
      const isLt2M = file.size / 1024 / 1024 < 2;
      if (!isJPG) {
        this.$message.error("上传头像图片只能是 JPG/PNG 格式!");
        return false;
      }
      if (!isLt2M) {
        this.$message.error("上传头像图片大小不能超过 2MB!");
        return false;
      }
      // 上传成功后将图片地址赋值给裁剪框显示图片
      this.$nextTick(async () => {
        // base64方式
        // this.option.img = await fileByBase64(file.raw)
        this.loading = false;
        this.dialogVisible = true;
      });
    },
    // 放大/缩小
    changeScaleHandle(num) {
      num = num || 1;
      this.$refs.cropper.changeScale(num);
    },
    // 左旋转
    rotateLeftHandle() {
      this.$refs.cropper.rotateLeft();
    },
    // 右旋转
    rotateRightHandle() {
      this.$refs.cropper.rotateRight();
    },
    // 下载
    downloadHandle(type) {
      let aLink = document.createElement("a");
      aLink.download = "author-img";
      if (type === "blob") {
        this.$refs.cropper.getCropBlob((data) => {
          aLink.href = URL.createObjectURL(data);
          aLink.click();
        });
      } else {
        this.$refs.cropper.getCropData((data) => {
          aLink.href = data;
          aLink.click();
        });
      }
    },
    // 清理图片
    clearImgHandle() {
      this.option.img = "";
    },
    // 截图框移动回调函数
    cropMoving(data) {
      // 截图框的左上角 x，y和右下角坐标x，y
      let cropAxis = [data.axis.x1, data.axis.y1, data.axis.x2, data.axis.y2]
      console.log(cropAxis)
    },
    finish() {
      // 获取截图的 blob 数据
      this.$refs.cropper.getCropBlob((blob) => {
        this.loading = true;
        this.dialogVisible = false;
        this.previewImg = URL.createObjectURL(blob);
        this.isPreview = true;
      });
      // 获取截图的 base64 数据
      // this.$refs.cropper.getCropData(data => {
      //     console.log(data)
      // })
    },
  },
};
</script>

<style lang="scss" scoped>
.cropper-wrapper {
  //height: calc(100vh - 50px);
  display: flex;
  justify-content: center;
  align-items: center;
  .pre-box {
    display: flex;
    flex-direction: column;
    align-items: center;
    button {
      width: 100px;
      margin-top: 15px;
    }
  }
}
.main-style{
    padding: 20px 20px 20px 40px;
    margin-left: 40px;
    border-radius: 5px;
    box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
  }
.crop-dialog {
  .cropper-content {
    padding: 0 40px;

    .cropper {
      width: auto;
      height: 350px;
    }
  }

  .action-box {
    padding: 25px 40px 0 40px;
    display: flex;
    justify-content: center;

    button {
      width: 80px;
      margin-right: 15px;
    }
  }

  .dialog-footer {
    button {
      width: 100px;
    }
  }
}
</style>