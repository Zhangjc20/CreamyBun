<template>
  <div>
    <canvas
      id="canvas"
      :style="{ backgroundImage: 'url(' + imageSrc + ')' }"
      ref="canvas"
      @mousedown="handleMouseDown"
      @mouseup="handleMouseUp"
      @mousemove="handleMouseMove"
      width="800px"
      height="800px"
    ></canvas>
  </div>
</template>

<script>
export default {
  name: "ImageFramer",
  props: {
    imageSrc: {
      type: String,
      default: "",
    },
    dash: {
      type: Boolean,
      default: false,
    },
    color:{
        type:String,
        default:"#ffffff"
    }
  },
  data() {
    return {
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
      },
      canvasPos: {
        left: 0,
        top: 0,
      },
      lastestRect: {
        startX: 0,
        startY: 0,
        width: 0,
        height: 0,
      },
      rect: {
        startX: 0,
        startY: 0,
        width: 0,
        height: 0,
      },
    };
  },
  methods: {
    draw() {
      if (this.mouse.down) {
        let canvas = this.$refs.canvas;
        let ctx = canvas.getContext("2d");
        ctx.strokeStyle = this.color;
        if (this.dash) {
          ctx.setLineDash([6]);
        }
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.strokeRect(
          this.rect.startX - this.canvasPos.left,
          this.rect.startY - this.canvasPos.top,
          this.rect.width,
          this.rect.height
        );
      }
    },
    handleMouseDown(event) {
      this.mouse.down = true;
      this.mouse.current = {
        x: event.pageX,
        y: event.pageY,
      };
      this.rect.startX = this.mouse.current.x;
      this.rect.startY = this.mouse.current.y;
      this.lastestRect = JSON.parse(JSON.stringify(this.rect));
    },
    handleMouseUp() {
      this.mouse.down = false;
    },
    handleMouseMove(event) {
      this.mouse.current = {
        x: event.pageX,
        y: event.pageY,
      };
      if (this.mouse.down) {
        this.rect.width = this.mouse.current.x - this.rect.startX;
        this.rect.height = this.mouse.current.y - this.rect.startY;
        this.draw();
      }
    },
  },
  mounted() {
    this.$nextTick(() => {
      var canvas = this.$refs.canvas;
      var ctx = canvas.getContext("2d");
      ctx.translate(0.5, 0.5);
      ctx.imageSmoothingEnabled = false;
      // var img = document.getElementById("imageRef");
      // ctx.drawImage(img);
      var img = new Image();
      img.onload = function () {
        ctx.drawImage(img, 0, 0);
        canvas.width = img.width;
        canvas.height = img.height;
      };
      img.src = this.imageSrc;
      canvas.width = img.width;
      canvas.height = img.height;
      let canvasBound = canvas.getBoundingClientRect();
      this.canvasPos.top = canvasBound.top;
      this.canvasPos.left = canvasBound.left;
    });
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
canvas {
  box-shadow: 0px 2px 3px rgba(0, 0, 0, 0.2);
}
</style>
