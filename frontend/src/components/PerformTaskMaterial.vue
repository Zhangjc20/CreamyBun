<template>
  <el-container v-if="loading">
    <div style="position: relative;width: 250px;height: 200px;margin-left: auto;margin-right: auto;">
      <div style="position: absolute; bottom: 50px;left: 60px;width: 250px;height: 250px;">
        <div style="flex-direction: column;position:absolute;bottom: 0px;margin-left: auto;margin-right: auto;text-align:center ">
          <el-image
            style="width: 88px; height: 80px"
            fit="cover"
            :src="require('@/assets/images/logo_small.png')"
            class="jump-logo"
          ></el-image>
          <div class="jump-shadow"></div>
        </div>
      </div>
      <div style="position: absolute; bottom: -210px;left: -20px;width: 250px;height: 250px;">
        <span style="color:#5EABBF;font-size:20px; font-family: YouSheBlack;">
          正在加载图片，请稍等~
        </span>
      </div>
    </div>
  </el-container>
  <el-container v-else>
    <el-header style="height: 40px;">
      <span class="header-title" style="margin: auto,auto,auto,20px;">{{ materialInfo['fileNotes'] }}</span>
    </el-header>
    <el-row v-if="type == 0">
      <ImageFramer v-if="type == 1" :src="image.src" />
      <el-image :src="image.src"></el-image>
    </el-row>
    <el-main v-if="type == 1" style="min-height:50px;max-height:300px; border-left: 2px solid #999999;">
      <div class="material-content">
        {{ docContent }}
      </div>
    </el-main>
    <el-main v-if="type == 2" style="min-height:50px">
        <video style="width: 100%;"  controls>
          <source :src="streamSrc" type="video/mp4">
        </video>
        <!-- <video-player style="width: 100%;" class="video-player vjs-big-play-centered"
          :sources="sources" crossorigin="anonymous"
          playsinline controls fluid="true" :volume="0.6" :playback-rates="[0.7, 1.0, 1.5, 2.0]"
          @mounted="handleMounted" @ready="handleEvent($event)" @play="handleEvent($event)" @pause="handleEvent($event)"
          @ended="handleEvent($event)" @loadeddata="handleEvent($event)" @waiting="handleEvent($event)"
          @playing="handleEvent($event)" @canplay="handleEvent($event)" @canplaythrough="handleEvent($event)"
          @timeupdate="handleEvent(player?.currentTime())" >
        </video-player> -->

    </el-main>
    <el-main v-if="type == 3" style="height:110px">
        <audio style="width: 100%;"  controls>
          <source :src="streamSrc" :type="audioSuffix">
        </audio>
        <!-- <video-player style="width: 100%;" class="video-player vjs-big-play-centered"
          :sources="sources" crossorigin="anonymous"
          playsinline controls fluid="true" :volume="0.6" :playback-rates="[0.7, 1.0, 1.5, 2.0]"
          @mounted="handleMounted" @ready="handleEvent($event)" @play="handleEvent($event)" @pause="handleEvent($event)"
          @ended="handleEvent($event)" @loadeddata="handleEvent($event)" @waiting="handleEvent($event)"
          @playing="handleEvent($event)" @canplay="handleEvent($event)" @canplaythrough="handleEvent($event)"
          @timeupdate="handleEvent(player?.currentTime())" >
        </video-player> -->

    </el-main>
  </el-container>


</template>

<script>
import axios from "axios";
import ImageFramer from "./ImageFramer.vue";
// import { VideoPlayer } from '@videojs-player/vue'
// import 'video.js/dist/video-js.css'
export default {
  name: 'PerformTaskMaterial',
  props: {
    materialInfo: Object,
  },
  components: {
    ImageFramer
  },
  watch: {
    materialInfo(newVal, oldVal) {
      
      console.log(newVal, oldVal)
      // this.loading = true;
      // this.materialInfoLocal = newVal
      // axios.get("http://101.42.118.80:8000/perform_problem_material/", {
      //   params: this.materialInfoLocal
      // }).then((res) => {
      //   const imageFile = this.base64ImgtoFile(res.data["materialImage"]);
      //   this.image.src =
      //     window.webkitURL.createObjectURL(imageFile) ||
      //     window.URL.createObjectURL(imageFile);
      //   this.loading = false;
      // }).catch();
    },
  },
  mounted() {
    this.type = this.materialInfo['fileType']
    if(this.type == 2 || this.type == 3){
      this.streamSrc = "http://101.42.118.80:8000/stream_video/" + this.materialInfo['filePath'].replace(/\//g,"<").replace(/\\/g,"<")
      // console.log("this.streamSrc",this.streamSrc)
    }
    if(this.type == 3){
      var tempList = this.materialInfo['filePath'].split('.')
      var tempType = tempList[tempList.length - 1]
      if(tempType == 'mp3'){
        tempType = 'mpeg'
      }
      this.audioSuffix += tempType
    }
    if(this.type == 0){
      this.loading = true
      this.image = new Image();
      this.image.src ='http://101.42.118.80:8000' + this.materialInfo['filePath'].substr(1)
      
      this.image.onerror = () => {
        console.log("img onerror");
      };
      this.image.onload = () => {
        // 等背景图片加载成功后 去除loading
        console.log("加载完成");
        this.loading = false
        return false
      };
      
      return 
    }
    console.log("发射发射发射", this.materialInfo)
    axios.get("http://101.42.118.80:8000/perform_problem_material/", {
      params: this.materialInfo
    }).then((res) => {
      // console.log("res", res)
      // if (this.type == 0) {
      //   const imageFile = this.base64ImgtoFile("" + res.data["materialImage"]);
      //   this.image.src =
      //     window.webkitURL.createObjectURL(imageFile) ||
      //     window.URL.createObjectURL(imageFile);
      //   // console.log("this.image.src", this.image.src)
      //   this.loading = false
      // } else 
      if (this.type == 1) {
        this.docContent = res.data["materialContent"]
      }

    }).catch();
  },
  data() {
    return {
      loading:false,
      materialInfoLocal: {},
      image: {
        src: null,
        type: null,
      },
      type: -1,
      docContent: '',
      streamSrc:'http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4',
      audioSuffix:'audio/',
      sources:[{
        type: 'video/mp4',
        src: "http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4"
      }],
    }
  },
  methods: {
    getVideoStream() {
      axios.get("http://101.42.118.80:8000/stream_video/", {
        params: this.materialInfo,
        responseType: 'blob'
      }).then((res) => {
        // console.log("res getVideoStream", res)
        const blob = new Blob([res.data], { type: 'video/mp4' })
        // console.log("res getVideoStream", blob)
        this.sources[0]['src'] = window.webkitURL.createObjectURL(blob) ||
            window.URL.createObjectURL(blob);
        // console.log("res getVideoStream", this.sources)

      }).catch();
    },
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
    clickContentSet() {
      this.dialogVisible = false
    }
  }
}

</script>

<style scoped>
.header-style {
  border-radius: 5px;
  box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
  height: 100px;
  padding: 20px 20px 20px 40px;
}

.header-breadcrumb {
  margin: 0 0 10px 0;
}

.header-title {
  float: left;
  font-size: 17px;
  font-weight: 700;
}

.material-content {
  font-size: 17px;
  font-weight: 700;
  white-space: pre-wrap;
  text-align: left;
  width: 100%;
}

.main-style {
  padding: 20px 20px 20px 40px;
  margin-top: 20px;
  border-radius: 5px;
  box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
}
::-webkit-scrollbar {
  width: 10px; /*对垂直流动条有效*/
}

/*定义滚动条的轨道颜色、内阴影及圆角*/
::-webkit-scrollbar-track {
  border-radius: 4px;
}

/*定义滑块颜色、内阴影及圆角*/
::-webkit-scrollbar-thumb {
  border-radius: 8px;
  background-color: #efefef;
}

/*定义滑块悬停变化颜色、内阴影及圆角*/
::-webkit-scrollbar-thumb:hover {
  background-color: #dddddd;
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