<template>
  <div class="wrapper">
    <vue-final-modal
      v-model="showModal"
      classes="modal-container"
      content-class="modal-content"
    >
        <div class="modal-title">图片裁剪</div>
      <image-cropper
        ref="cropper"
        class="cropper"
        :src="image.src"
        @change="onChange"
        :debounce="false"
        :auto-zoom="true"
        :stencil-size="{
          width: 400,
          height: 400,
        }"
        image-restriction="stencil"
      />
      <div class="button-area">
      <CustomButton title="确认" @click="handleConfirm" marginRight="30px"/>
      <CustomButton title="取消" @click="showModal = false"/>
      </div>
    </vue-final-modal>
    <image-preview
      :width="150"
      :height="150"
      :image="result.image"
      :coordinates="result.coordinates"
      v-if="uploaded"
    />
    <el-upload action="#" :disabled="true" list-type="picture-card" :auto-upload="false" @click="inputClick" v-else>
        <input
        type="file"
        ref="file"
        @change="loadImage($event)"
        accept="image/*"
        class="file-input"
      />
        <el-icon><Plus /></el-icon>
    </el-upload>
  </div>
</template>

<script>
import CustomButton from './CustomButton.vue';
function getMimeType(file, fallback = null) {
  const byteArray = new Uint8Array(file).subarray(0, 4);
  let header = "";
  for (let i = 0; i < byteArray.length; i++) {
    header += byteArray[i].toString(16);
  }
  switch (header) {
    case "89504e47":
      return "image/png";
    case "47494638":
      return "image/gif";
    case "ffd8ffe0":
    case "ffd8ffe1":
    case "ffd8ffe2":
    case "ffd8ffe3":
    case "ffd8ffe8":
      return "image/jpeg";
    default:
      return fallback;
  }
}

export default {
  name: "UploadCropper",
  components:{
    CustomButton
  },
  data() {
    return {
      showModal: false,
      image: {
        src: null,
        type: null,
      },
      result: {
        coordinates: null,
        image: null,
      },
      uploaded: false,
    };
  },
  methods: {
    handleConfirm(){
        this.showModal = false;
        this.crop();
    },
    inputClick(){
        this.$refs.file.click();
    },
    onChange({ coordinates, image }) {
      this.result = {
        coordinates,
        image,
      };
    },
    crop() {
      const { canvas } = this.$refs.cropper.getResult();
      canvas.toBlob((blob) => {
        // 可以上传blob
        console.log(blob);
      }, this.image.type);
    },
    reset() {
      this.image = {
        src: null,
        type: null,
      };
    },
    loadImage(event) {
      // DOM input组件得引用
      const { files } = event.target;
      // 确保有文件
      if (files && files[0]) {
        // 如果存在要销毁
        if (this.image.src) {
          URL.revokeObjectURL(this.image.src);
        }
        // 创建blob链接
        const blob = URL.createObjectURL(files[0]);

        // 创建FileReader读取图片的二进制数据
        const reader = new FileReader();
        // 定义回调函数->当FileReader运行完毕
        reader.onload = (e) => {
          this.image = {
            //设定src
            src: blob,
            //确定图片类型保证从画布中提取图片无误
            type: getMimeType(e.target.result, files[0].type),
          };
        };
        //以url读取图片(base64 format)
        reader.readAsArrayBuffer(files[0]);
        this.showModal = true;
        this.uploaded = true;
      }
    },
  },
  unmounted() {
    // 废除图片的url,让garbage collector销毁图片
    if (this.image.src) {
      URL.revokeObjectURL(this.image.src);
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
}
.button-area {
    display: flex;
    justify-content: center;
    margin-top: 40px;
}
.modal-title {
    color:#ffffff;
    font-size:18px;
}
:deep .modal-container {
  display: flex;
  justify-content: center;
  align-items: center;
}
:deep .modal-content {
  display: flex;
  flex-direction: column;
  margin: 0 1rem;
  padding: 1rem;
  border-radius: 0.25rem;
}
.modal__title {
  font-size: 1.5rem;
  font-weight: 700;
}
.input-button {
  border: none;
  color: #fff;
  font-size: 16px;
  width: 80px;
  height: 30px;
  background: #5eabbf;
  cursor: pointer;
  border-radius: 6px;
}
.input-button:hover {
  background: #5297a8;
}
.file-input {
  display: none;
}
.cropper {
  height: 600px;
  width: 600px;
  background: #ddd;
  border-radius: 20px;
}
</style>
