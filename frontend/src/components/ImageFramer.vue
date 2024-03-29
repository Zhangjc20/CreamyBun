<template>
  <el-container v-show="loading">
    <div
      style="
        position: relative;
        width: 250px;
        height: 200px;
        margin-left: auto;
        margin-right: auto;
      "
    >
      <div
        style="
          position: absolute;
          bottom: 50px;
          left: 60px;
          width: 250px;
          height: 250px;
        "
      >
        <div
          style="
            flex-direction: column;
            position: absolute;
            bottom: 0px;
            margin-left: auto;
            margin-right: auto;
            text-align: center;
          "
        >
          <el-image
            style="width: 88px; height: 80px"
            fit="cover"
            :src="require('@/assets/images/logo_small.png')"
            class="jump-logo"
          ></el-image>
          <div class="jump-shadow"></div>
        </div>
      </div>
      <div
        style="
          position: absolute;
          bottom: -210px;
          left: -20px;
          width: 250px;
          height: 250px;
        "
      >
        <span style="color: #5eabbf; font-size: 20px; font-family: YouSheBlack">
          正在加载图片，请稍等~
        </span>
      </div>
    </div>
  </el-container>
  <div class="framer-container" v-show="!loading">
    <div ref="framerContainer" style="width: 90%">
      <canvas
        :style="{
          background: 'url(' + image.src + ') no-repeat',
          backgroundSize: '100% 100%',
        }"
        id="canvas"
        ref="canvas"
        @mousedown="handleMouseDown"
        @mouseup="handleMouseUp"
        @mousemove="handleMouseMove"
      ></canvas>
    </div>
    <el-row style="width: 100%">
      <el-col :span="12" class="center-box" style="padding-left: 10%">
        <span>线框类型：</span>
        <el-radio-group v-model="lineStyle" class="ml-4">
          <el-radio label="solid" size="large">实线</el-radio>
          <el-radio label="dash" size="large">虚线</el-radio>
        </el-radio-group>
      </el-col>
      <el-col :span="12" class="center-box">
        <span style="margin-left: 40px">线框颜色：&emsp;</span>
        <el-color-picker v-model="color" />
      </el-col>
    </el-row>
    <el-row style="width: 100%">
      <el-col :span="12" class="center-box" style="padding-left: 10%">
        <div class="slider-box center-box">
          <span>线框粗细&emsp;&emsp;</span>
          <el-slider
            v-model="penWidth"
            :step="1"
            :min="2"
            :max="4"
            class="width-slider"
          />
        </div>
      </el-col>
      <el-col :span="12" class="center-box">
        <CustomButton title="清空选框" marginLeft="40px" @click="clearCanvas" />
      </el-col>
    </el-row>
  </div>
</template>

<script>
import CustomButton from "./CustomButton.vue";
export default {
  name: "ImageFramer",
  components: {
    CustomButton,
  },
  props: {
    src: {
      type: String,
      default: "",
    },
    minFrameNum: {
      type: Number,
      default: 1,
    },
    maxFrameNum: {
      type: Number,
      default: 3,
    },
    initRects: {
      type: Array,
      default: undefined,
    },
  },
  data() {
    return {
      loading: false,
      srcUpdated: false,
      initRectsUpdated: false,
      ratioST: 1,
      ratioHW: 1,
      penWidth: 2,
      canvas: null,
      color: "#ffffff",
      lineStyle: "dash",
      mouse: {
        current: {
          x: 0,
          y: 0,
        },
        previous: {
          x: 0,
          y: 0,
        },
        down: false,
        up: true,
      },
      frameRects: [],
      rect: {
        startX: 0,
        startY: 0,
        width: 0,
        height: 0,
      },
      image: {
        src: this.src,
      },
    };
  },
  watch: {
    src() {
      this.srcUpdated = true;
      if (this.srcUpdated && this.initRectsUpdated) {
        this.init();
        this.srcUpdated = false;
        this.initRectsUpdated = false;
      }
    },
    initRects() {
      this.initRectsUpdated = true;
      if (this.srcUpdated && this.initRectsUpdated) {
        this.init();
        this.srcUpdated = false;
        this.initRectsUpdated = false;
      }
    },
  },
  methods: {
    clearCanvas() {
      var img = new Image();
      img.onload = () => {
        img.setAttribute("crossOrigin", "anonymous");
        this.image = img;
      };
      this.frameRects = [];
      img.src = this.src;
      this.canvas
        .getContext("2d")
        .clearRect(0, 0, this.canvas.width, this.canvas.height);
    },
    draw(clear, rect) {
      if (this.frameRects.length >= this.maxFrameNum) {
        return;
      }
      if (!clear) {
        let canvas = this.$refs.canvas;
        let ctx = canvas.getContext("2d");
        ctx.strokeStyle = this.color;
        ctx.lineWidth = this.penWidth;
        if (this.lineStyle === "dash") {
          ctx.setLineDash([6]);
        } else {
          ctx.setLineDash([]);
        }
        ctx.strokeRect(rect.startX, rect.startY, rect.width, rect.height);
      } else if (this.mouse.down) {
        let canvas = this.$refs.canvas;
        let ctx = canvas.getContext("2d");
        ctx.strokeStyle = this.color;
        ctx.lineWidth = this.penWidth;
        if (this.lineStyle === "dash") {
          ctx.setLineDash([6]);
        } else {
          ctx.setLineDash([]);
        }
        ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        ctx.strokeRect(rect.startX, rect.startY, rect.width, rect.height);
      }
    },
    handleMouseDown(event) {
      if (!this.mouse.up) {
        return;
      }
      this.mouse.down = true;
      this.mouse.up = false;
      this.mouse.current = {
        x: event.offsetX,
        y: event.offsetY,
      };
      this.rect.startX = this.mouse.current.x * this.ratioST;
      this.rect.startY = this.mouse.current.y * this.ratioST;
    },
    handleMouseUp() {
      this.mouse.down = false;
      this.mouse.up = true;
      if (this.frameRects.length < this.maxFrameNum) {
        let ctx = this.canvas.getContext("2d");
        ctx.drawImage(this.image, 0, 0, this.image.width, this.image.height);
        this.draw(false, this.rect);
        this.frameRects.push(Object.assign({}, this.rect));
        this.$refs.canvas.toBlob((blob) => {
          var img = new Image();
          img.setAttribute("crossOrigin", "anonymous");
          img.onload = () => {
            this.image = img;
          };
          img.src = URL.createObjectURL(blob);
        });
      }
    },
    handleMouseMove(event) {
      this.mouse.current = {
        x: event.offsetX,
        y: event.offsetY,
      };
      if (this.mouse.down) {
        this.rect.width =
          this.mouse.current.x * this.ratioST - this.rect.startX;
        this.rect.height =
          this.mouse.current.y * this.ratioST - this.rect.startY;
        this.draw(true, this.rect);
      }
    },
    onResize() {
      if (this.src && this.$refs.framerContainer.clientWidth) {
        this.ratioST =
          this.image.width / this.$refs.framerContainer.clientWidth;
      }
    },
    initRectConvert(rect) {
      return {
        startX: Math.floor(rect.startX / this.ratioST),
        startY: Math.floor(rect.startY / this.ratioST),
        width: Math.floor(rect.width / this.ratioST),
        height: Math.floor(rect.height / this.ratioST),
      };
    },
    init() {
      var canvas = this.$refs.canvas;
      var ctx = canvas.getContext("2d");
      ctx.translate(0, 0);
      ctx.imageSmoothingEnabled = false;
      var img = new Image();
      img.onload = () => {
        this.loading = false;
        this.ratioHW = img.height / img.width;
        let clientWidth = this.$refs.framerContainer.clientWidth;
        this.ratioST = img.width / clientWidth;
        canvas.width = img.width;
        canvas.height = img.height;
        canvas.style.width = "100%";
        this.image = img;
        this.canvas = canvas;
        if (this.initRects) {
          this.frameRects = this.initRects;
          let ctx = this.canvas.getContext("2d");
          ctx.drawImage(this.image, 0, 0, this.image.width, this.image.height);
          for (var rect of this.initRects) {
            this.draw(false, rect);
          }
          this.$refs.canvas.toBlob((blob) => {
            var img = new Image();
            img.setAttribute("crossOrigin", "anonymous");
            img.onload = () => {
              this.image = img;
            };
            img.src = URL.createObjectURL(blob);
          });
        }
      };
      img.setAttribute("crossOrigin", "anonymous");
      img.src = this.src;
    },
  },
  mounted() {
    window.addEventListener("resize", this.onResize, true);
    this.$nextTick(() => {
      this.loading = true;
      this.init(false);
    });
  },
  beforeUnmount() {
    window.removeEventListener("resize", this.onResize, true);
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.framer-container {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.slider-box {
  width: 80%;
}
.center-box {
  display: flex;
  align-items: center;
}
.width-slider {
  width: 50px;
}
canvas {
  box-shadow: 0px 2px 3px rgba(0, 0, 0, 0.2);
}
.jump-logo {
  z-index: 2;
  animation: jump-logo 1s infinite;
  animation-timing-function: ease;
}
.jump-shadow {
  z-index: 1;
  width: 100px;
  height: 5px;
  background: #eaeaea;
  border-radius: 100%;
  animation: shadow 1s infinite;
  animation-timing-function: ease;
  margin-left: auto;
  margin-right: auto;
}
@keyframes jump-logo {
  0% {
    margin-bottom: 0px;
  }

  50% {
    margin-bottom: 30px;
  }

  100% {
    margin-bottom: 0px;
  }
}
@keyframes shadow {
  0% {
    width: 85px;
  }

  50% {
    width: 65px;
  }

  100% {
    width: 85px;
  }
}
</style>
