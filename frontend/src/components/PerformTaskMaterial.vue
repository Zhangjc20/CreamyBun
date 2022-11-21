<template>
  <el-container>
    <el-header style="height: 40px;">
      <span class="header-title" style="margin: auto,auto,auto,20px;">{{ materialInfo['fileNotes'] }}</span>
    </el-header>
    <el-row v-if="type == 0">
      <el-image :src="image.src" />
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
// import { VideoPlayer } from '@videojs-player/vue'
// import 'video.js/dist/video-js.css'
export default {
  name: 'PerformTaskMaterial',
  props: {
    materialInfo: Object,
  },
  // components: {
  //   VideoPlayer
  // },
  watch: {
    materialInfo(newVal, oldVal) {
      console.log(newVal, oldVal)
      this.materialInfoLocal = newVal
      axios.get("http://localhost:8000/perform_problem_material/", {
        params: this.materialInfoLocal
      }).then((res) => {
        const imageFile = this.base64ImgtoFile(res.data["materialImage"]);
        this.image.src =
          window.webkitURL.createObjectURL(imageFile) ||
          window.URL.createObjectURL(imageFile);
      }).catch();
    },
  },
  mounted() {
    this.type = this.materialInfo['fileType']
    if(this.type == 2 || this.type == 3){
      this.streamSrc = "http://localhost:8000/stream_video/" + this.materialInfo['filePath'].replace(/\//g,"<").replace(/\\/g,"<")
      console.log("this.streamSrc",this.streamSrc)
    }
    if(this.type == 3){
      var tempList = this.materialInfo['filePath'].split('.')
      var tempType = tempList[tempList.length - 1]
      if(tempType == 'mp3'){
        tempType = 'mpeg'
      }
      this.audioSuffix += tempType
    }
    console.log("materialInfo", this.materialInfo)
    axios.get("http://localhost:8000/perform_problem_material/", {
      params: this.materialInfo
    }).then((res) => {
      console.log("res", res)
      if (this.type == 0) {
        const imageFile = this.base64ImgtoFile("" + res.data["materialImage"]);
        this.image.src =
          window.webkitURL.createObjectURL(imageFile) ||
          window.URL.createObjectURL(imageFile);
        console.log("this.image.src", this.image.src)
      } else if (this.type == 1) {
        this.docContent = res.data["materialContent"]
        console.log("docContent", this.docContent)
      } else if (this.type == 2) {
        this.getVideoStream()
      }

    }).catch();
  },
  data() {
    return {
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
      axios.get("http://localhost:8000/stream_video/", {
        params: this.materialInfo,
        responseType: 'blob'
      }).then((res) => {
        console.log("res getVideoStream", res)
        const blob = new Blob([res.data], { type: 'video/mp4' })
        console.log("res getVideoStream", blob)
        this.sources[0]['src'] = window.webkitURL.createObjectURL(blob) ||
            window.URL.createObjectURL(blob);
        console.log("res getVideoStream", this.sources)

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
</style>