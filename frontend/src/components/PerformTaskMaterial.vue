<template>
  <el-main class="main-style" >
    <el-row style="height: 50px;">
      <span class="header-title" style="margin: auto,auto,auto,20px;">{{materialInfoLocal.notes}}</span>
    </el-row>

  </el-main>
</template>

<script>
import axios from "axios";
export default {
  name: 'PerformTaskMaterial',
  props: {
    materialInfo:Object,
  },
  watch: {
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
  data(){
    return {
      materialInfoLocal:{},
      image: {
        src: null,
        type: null,
      },
    }
  },
  methods:{

    // this.currentOption = '26',
    //   this.description = '',
    //   this.optionList = [],
    //   this.minOptionNum = '',
    //   this.maxOptionNum = '',
    //   this.mustDo = true

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
  .main-style{
    padding: 20px 20px 20px 40px;
    margin-top: 20px;
    border-radius: 5px;
    box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
  }
</style>