<template>
  <div>
    <div>
      <canvas
        :style="{ background: 'url(' + image.src + ')' }"
        id="canvas"
        ref="canvas"
        @mousedown="handleMouseDown"
        @mouseup="handleMouseUp"
        @mousemove="handleMouseMove"
        width="800px"
        height="800px"
      ></canvas>
    </div>
    <div>
      <span>线框类型：</span>
      <el-radio-group v-model="lineStyle" class="ml-4">
        <el-radio label="solid" size="large">实线</el-radio>
        <el-radio label="dash" size="large">虚线</el-radio>
      </el-radio-group>
      <span style="margin-left: 40px">线框颜色：</span>
      <el-color-picker v-model="color" />
      <div>
      <span>线框粗细</span>
        <el-slider style="margin-left: 600px;" v-model="penWidth" :step="1" :min="1" :max="3" class="width-slider"/>
      </div>
      <CustomButton title="清空选框" marginLeft="40px" @click="clearCanvas" />
    </div>
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
    imageSrc: {
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
  },
  data() {
    return {
      penWidth:1,
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
        up:true,
      },
      canvasPos: {
        left: 0,
        top: 0,
      },
      frameRects: [],
      rect: {
        startX: 0,
        startY: 0,
        width: 0,
        height: 0,
      },
      image: {
        src: this.imageSrc,
      },
    };
  },
  methods: {
    clearCanvas() {
      var img = new Image();
      img.onload = () => {
        img.setAttribute("crossOrigin", "anonymous");
        this.image = img;
      };
      this.frameRects = [];
      img.src = this.imageSrc;
      this.canvas
        .getContext("2d")
        .clearRect(0, 0, this.canvas.width, this.canvas.height);
    },
    draw(clear) {
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
        }
        else{
          ctx.setLineDash([]);
        }
        ctx.strokeRect(
          this.rect.startX,
          this.rect.startY,
          this.rect.width,
          this.rect.height
        );
      } else if (this.mouse.down) {
        let canvas = this.$refs.canvas;
        let ctx = canvas.getContext("2d");
        ctx.strokeStyle = this.color;
        ctx.lineWidth = this.penWidth;
        if (this.lineStyle === "dash") {
          ctx.setLineDash([6]);
        }
        else{
          ctx.setLineDash([]);
        }
        ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        ctx.strokeRect(
          this.rect.startX,
          this.rect.startY,
          this.rect.width,
          this.rect.height
        );
      }
    },
    handleMouseDown(event) {
      if(!this.mouse.up){
        return;
      }
      this.mouse.down = true;
      this.mouse.up = false;
      this.mouse.current = {
        x: event.offsetX,
        y: event.offsetY,
      };
      this.rect.startX = this.mouse.current.x;
      this.rect.startY = this.mouse.current.y;
    },
    handleMouseUp() {
      this.mouse.down = false;
      this.mouse.up = true;
      if (this.frameRects.length < this.maxFrameNum) {
        this.canvas.getContext("2d").drawImage(this.image, 0, 0);
        this.draw(false);
        this.frameRects.push(this.rect);
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
        this.rect.width = this.mouse.current.x - this.rect.startX;
        this.rect.height = this.mouse.current.y - this.rect.startY;
        this.draw(true);
      }
    },
  },
  mounted() {
    this.$nextTick(() => {
      var canvas = this.$refs.canvas;
      var ctx = canvas.getContext("2d");
      ctx.translate(0.5, 0.5);
      ctx.imageSmoothingEnabled = false;
      var img = new Image();
      img.onload = () => {
        canvas.width = img.width;
        canvas.height = img.height;
        this.image = img;
        let canvasBound = canvas.getBoundingClientRect();
        this.canvasPos.top = canvasBound.top;
        this.canvasPos.left = canvasBound.left;
        this.canvas = canvas;
      };
      img.setAttribute("crossOrigin", "anonymous");
      img.src = this.imageSrc;
    });
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.width-slider{
  width:50px;
}
canvas {
  box-shadow: 0px 2px 3px rgba(0, 0, 0, 0.2);
}
</style>
