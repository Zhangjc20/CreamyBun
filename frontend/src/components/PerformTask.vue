<template>
  <el-header class="header-style">
    <el-breadcrumb separator="/" class="header-breadcrumb">
      <el-breadcrumb-item :to="{ path: '/' }">奶黄包</el-breadcrumb-item>
      <el-breadcrumb-item>任务选择</el-breadcrumb-item>
      <el-breadcrumb-item>{{this.materialTypeName}}</el-breadcrumb-item>
    </el-breadcrumb>
    <span class="header-title">
      /*这里填写任务名字*/
    </span>
    <CustomButton 
      isRound="true" 
      style="float: right; right: 50px; top: 100px; position: absolute"
      height="40px"
      width="150px"
      title="提交任务"
    />
  </el-header>
  <el-main class="main-style">
    <!-- <el-row :gutter="20">
      <el-col :span="16"><div class="grid-content ep-bg-purple" /></el-col>
      <el-col :span="8"><div class="grid-content ep-bg-purple" /></el-col>
    </el-row> -->
    <el-row :gutter="20">
      <el-col :span="16">
        <PerformTaskMaterial
        >
        </PerformTaskMaterial>
      </el-col>
      <!-- <el-col :span="16" v-for="material in materialList" :key="material">
        <PerformTaskMaterial
        :materialInfo="material"
        >
        </PerformTaskMaterial>
      </el-col> -->
      <el-col :span="8">
        <el-main class="main-style">
        <el-row
          v-for="question in questionList" 
          :key="question"
        >
        {{question["questionTypeName"]}}
        </el-row>
        </el-main>
        
      </el-col>
    </el-row>
    <!-- <el-col :span="8" style="border-left: 1px solid #999999;"></el-col> -->
  </el-main>
  <!-- <el-main class="main-style">
    
  </el-main> -->

</template>

<script>
import axios from "axios";
import CustomButton from './CustomButton.vue';
import PerformTaskMaterial from "@/components/PerformTaskMaterial.vue";
// import { ElMessageBox } from "element-plus";

export default {
  name: 'PerformTask',

  components:{
    CustomButton,
    PerformTaskMaterial,
  },
  props: {
    username:String,
    login:Boolean,
  },
  // watch:{
  //   materialType(newVal){
  //     this.localMaterialType = newVal
  //     switch(this.localMaterialType)
  //     {
  //       case 0:
  //         this.materialTypeName = '图像'
  //         break;
  //       case 1:
  //         this.materialTypeName = '文本'
  //         break;
  //       case 2:
  //         this.materialTypeName = '视频'
  //         break;
  //       case 3:
  //         this.materialTypeName = '音频'
  //         break;
  //       case 4:
  //         this.materialTypeName = '自定义类型'
  //         break;
  //     }
  //   },
  // },
  data(){
    return {
      imageFile:null,
      questionList:[],
      materialList:[{
                "index": 1, 
                "fileName": "2 (1).docx", 
                "fileSize": "28.7 KB", 
                "totalSize": 29414, 
                "fileType": "寄了", 
                "filePath": "./resource/task_materials\\ZDandsomSP_20221118130618\\list4\\2 (1).docx", 
                "list": "list4"
            }, ],
    }
  },
  mounted(){
    axios.get("http://localhost:8000/uck_me/",{
      params:{
        username:this.username
      }
    }).then((res)=>{
        this.questionList = res.data['questionList'];
        this.materialList = res.data['materialList'];
    }).catch();
  },
  methods:{

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
    font-size:20px;
    font-weight:bold;
  }
  .main-style{
    padding: 20px 20px 20px 20px;
    margin-top: 20px;
    border-radius: 5px;
    box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
  }
/*.header-style{
    border-radius: 5px;
    box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
    height: 100px;
    padding: 20px 20px 20px 40px;
  }
  .perform-task-header-style{
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
    font-size:20px;
    font-weight:bold;
  }
  .main-style{
    padding: 20px 20px 20px 40px;
    margin-top: 20px;
    border-radius: 5px;
    box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
    height:95%
  }*/
</style>