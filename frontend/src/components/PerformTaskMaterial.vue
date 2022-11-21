<template>
  <el-header style="height: 40px;">
    <span class="header-title" style="margin: auto,auto,auto,20px;">{{materialInfo['fileNotes']}}</span>
  </el-header>
  <el-row v-if="type == 0">
    <el-image :src="image.src" />
  </el-row>
  <el-main v-if="type == 1" style="min-height:50px;max-height:300px; border-left: 2px solid #999999;">
    <span class="material-content" >
      {{docContent}}
    </span>
  </el-main>
  <el-main v-if="type == 2" style="min-height:50px;max-height:300px">
    <span class="material-content" >
      <video-player
    style="width: 100%;"
    class="video-player vjs-big-play-centered"
    src="https://vjs.zencdn.net/v/oceans.mp4"
    poster="https://vjs.zencdn.net/v/oceans.png"
    crossorigin="anonymous"
    playsinline
    controls
    fluid="true"
    :volume="0.6"   
    :playback-rates="[0.7, 1.0, 1.5, 2.0]"        
    @mounted="handleMounted"
    @ready="handleEvent($event)"
    @play="handleEvent($event)"
    @pause="handleEvent($event)"
    @ended="handleEvent($event)"
    @loadeddata="handleEvent($event)"
    @waiting="handleEvent($event)"
    @playing="handleEvent($event)"
    @canplay="handleEvent($event)"
    @canplaythrough="handleEvent($event)"
    @timeupdate="handleEvent(player?.currentTime())"
  />
    </span>
    
  </el-main>
  
</template>

<script>
import axios from "axios";
import { VideoPlayer } from '@videojs-player/vue'
import 'video.js/dist/video-js.css'
export default {
  name: 'PerformTaskMaterial',
  props: {
    materialInfo:Object,
  },
  components: {
    VideoPlayer
  },
  watch: {
    materialInfo(newVal, oldVal){
      console.log(newVal,oldVal)
      this.materialInfoLocal = newVal
      axios.get("http://localhost:8000/perform_problem_material/",{
        params:this.materialInfoLocal
      }).then((res)=>{
        const imageFile = this.base64ImgtoFile(res.data["materialImage"]);
        this.image.src =
          window.webkitURL.createObjectURL(imageFile) ||
          window.URL.createObjectURL(imageFile);
      }).catch();
    },
  },
  mounted(){
    this.type = this.materialInfo['fileType']
    console.log("materialInfo",this.materialInfo)
    axios.get("http://localhost:8000/perform_problem_material/",{
      params:this.materialInfo
    }).then((res)=>{
      console.log("res",res)
      if(this.type == 0){
        const imageFile = this.base64ImgtoFile("" + res.data["materialImage"]);
        this.image.src =
          window.webkitURL.createObjectURL(imageFile) ||
          window.URL.createObjectURL(imageFile);
      }else if(this.type == 1){
        this.docContent = res.data["materialContent"]
        console.log("docContent",this.docContent)
      }
      
    }).catch();
  },
  data(){
    return {
      materialInfoLocal:{},
      image: {
        src: null,
        type: null,
      },
      type:-1,
      docContent:'',
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
    clickContentSet(){
      this.dialogVisible = false
    }
  }
}

</script>

<style scoped>

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
  .material-content{
    font-size:17px;
    font-weight:700;
    white-space:pre-wrap;
    text-align:left;
  }
  .main-style{
    padding: 20px 20px 20px 40px;
    margin-top: 20px;
    border-radius: 5px;
    box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
  }
</style>