<template>
  <el-header class="header-style">
    <el-breadcrumb separator="/" class="header-breadcrumb">
      <el-breadcrumb-item :to="{ path: '/' }">奶黄包</el-breadcrumb-item>
      <el-breadcrumb-item>任务选择</el-breadcrumb-item>
      <el-breadcrumb-item>{{this.materialTypeName}}</el-breadcrumb-item>
    </el-breadcrumb>
    <span class="header-title">
      {{this.materialTypeName}}任务
    </span>
    <el-input v-model="abc" style="width: 300px" placeholder="这是一个阴险的字符串输入接口"/>
    <CustomButton 
      @click="abcSubmit" 
      isRound="true" 
      style="float: right; right: 200px; top: 100px; position: absolute"
      height="40px"
      width="150px"
      title="阴险的临时按钮"
    />
    <CustomButton 
      @click="finalSubmit" 
      isRound="true" 
      style="float: right; right: 50px; top: 100px; position: absolute"
      height="40px"
      width="150px"
      title="提交任务"
    />

  </el-header>
  <el-main class="main-style">
    <el-row style="height: 50px;">
      <span class="header-title">
        基本信息
      </span>
      
    </el-row>
    <el-row>
      
      <el-col :span="12">
        <el-form :model="form" label-width="100px" class="change-form">
          <el-row style="height: 50px;">
            <el-form-item label="名称" :required="true">
              <el-input v-model="form.taskName" placeholder="请输入任务名字"/>
              <!-- <CustomButton
                >保存</CustomButton> -->
            </el-form-item>
          </el-row>
          <el-row style="height: 80px;">
            <el-form-item label="任务描述" :required="true">
              <el-input
                v-model="form.description"
                :rows="3"
                type="textarea"
                placeholder="请输入任务描述"
                resize="none"
                style="width: 300px;"
              />
            </el-form-item>
          </el-row>
          <el-row style="height: 50px;">
            <el-form-item label="题型" :required="true" style="margin-top: 10px;">
              <el-select v-model="form.questionType" class="m-2" placeholder="请选择题型">
                <el-option
                  @click="showQuestionPage(item)"
                  v-for="item in options"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                />
              </el-select>
            </el-form-item>
          </el-row>
          <el-row >
            <component 
              :is="componentName" 
              :multiple="multiple" 
              :editingQuestion="editingQuestion" 
              :questionList="questionList" 
              :newOrEdit="newOrEdit"
              @questionSubmit="addQuestion">
            </component>
            <!-- <ReleaseChoice multiple="1"></ReleaseChoice> -->
          </el-row>
          <el-row>
            <el-main class="main-style" style="margin-right: 40px;">
              <el-row style="height: 50px;">
                <span class="header-title" style="margin: auto,auto,auto,20px;">当前题目列表</span>
              </el-row>
              <el-table
                  :data="questionList"
                  height="200"
                  :style="table"
                  class="customer-table">
                  <el-table-column
                    prop="index"
                    label="题号"
                    width="60">
                  </el-table-column>
                  <el-table-column
                    prop="questionTypeName"
                    label="题型"
                    width="60">
                  </el-table-column>
                  <el-table-column
                    prop="questionDescription"
                    label="题干"
                    width="150">
                  </el-table-column>
                  
                  <el-table-column
                    prop=""
                    label=""
                    width="">
                  </el-table-column>
                  
                  <el-table-column
                    prop=""
                    label="操作"
                    width="60">
                    <template v-slot="scope">
                      <el-dropdown>
                        <span class="iconfont icon-menu"></span>
                        <template #dropdown>
                          <el-dropdown-menu>
                            <el-dropdown-item icon="el-icon-s-order" @click="moveQuestionUpward(scope.row, scope.$index)">上移</el-dropdown-item>
                            <el-dropdown-item icon="el-icon-remove" @click="moveQuestionDown(scope.row, scope.$index)">下移</el-dropdown-item>
                            <el-dropdown-item icon="el-icon-remove" @click="editQuestion(scope.row, scope.$index)">编辑</el-dropdown-item>
                            <el-dropdown-item icon="el-icon-download" @click="deleteQuestion(scope.row, scope.$index)">删除</el-dropdown-item>
                          </el-dropdown-menu>
                        </template>
                        
                      </el-dropdown>
                    </template>
                  </el-table-column>
                </el-table>
            </el-main>
          </el-row>
        </el-form>
      </el-col>
      
      
      <el-col :span="12" style="border-left: 1px solid #999999;">
        <el-row style="margin-left:40px;margin-right:20px;">
          <el-main class="main-style">
            <el-row style="height: 50px;">
              <span class="header-title" style="margin: auto,auto,auto,20px;font-size:17px;">请上传任务封面</span>
            </el-row>
            <UploadCropper @getImage="getImage"/>

          </el-main>
          
        </el-row>
        <el-row>
          <MaterialUpload 
          ref="MyMaterialUpload"
          :username="username"
          :questionList="questionList"
          :materialType="localMaterialType"
          />
        </el-row>
      </el-col>
    </el-row>

  </el-main>
  <el-main class="main-style">
    <el-row style="height: 50px;">
      <span class="header-title">
        发布信息
      </span>
    </el-row>
    <el-form :model="form" label-width="100px" class="change-form">

      <el-row style="height: 50px;">
        <el-form-item label="任务星级" :required="true">
          <el-select v-model="form.starRank" class="m-2" placeholder="请选择星级">
            <el-option
              v-for="item in levels"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
        </el-form-item>
      </el-row>
      <el-row style="height: 50px;">
        <el-form-item label="题目奖励" :required="true">
          <el-input v-model="form.singleBonus" placeholder="请输入单个题目的奖励" type="number" @blur="form.singleBonus=Number(form.singleBonus)" oninput="value=value.replace(/[^\d]/g,'')"/>
        </el-form-item>
      </el-row>
      <el-row style="height: 50px;">
        <el-form-item label="领取人数" :required="true">
          <el-input v-model="form.receiverNum" placeholder="请输如本任务的领取人数" type="number" @blur="form.receiverNum=Number(form.receiverNum)" oninput="value=value.replace(/[^\d]/g,'')"/>
        </el-form-item>
      </el-row>
      <el-row style="height: 50px;">
        <el-form-item label="发布方式" :required="true">
          <el-radio-group v-model="form.releaseMode">
            <el-radio label="立即发布" />
            <el-radio label="暂不发布" />
            <el-radio label="定时发布" />
          </el-radio-group>
        </el-form-item>

        
      </el-row>
      <el-row v-if="form.releaseMode == '定时发布'" style="height: 50px;">
        <el-form-item label="发布时间" :required="true" >
          <!-- <el-time-picker
            v-model="form.startLine"
            placeholder="请选择发布时间"
            style="width: 100%"
          /> -->
          <el-col :span="11">
            <el-date-picker
              v-model="form.startLine1"
              type="date"
              placeholder="请选择发布日期"
              style="width: 100%"
            />
          </el-col>
          <el-col :span="2" class="text-center">
            <span class="text-gray-500">:</span>
          </el-col>
          <el-col :span="11">
            <el-time-picker
              v-model="form.startLine2"
              placeholder="请选择发布时间"
              style="width: 100%"
            />
          </el-col>
        </el-form-item>
      </el-row>
      <el-row style="height: 50px;">
        <el-form-item label="截止时间" :required="true">

          <!-- <el-time-picker
            v-model="form.deadLine"
            placeholder="请选择截止时间"
            style="width: 100%"
          /> -->
          <el-col :span="11">
            <el-date-picker
              v-model="form.deadLine1"
              type="date"
              placeholder="请选择截止日期"
              style="width: 200px"
              value-format="YYYY-MM-DD"
            />
          </el-col>
          <el-col :span="2" class="text-center">
            <!-- <span class="text-gray-500">  :</span> -->
          </el-col>
          <el-col :span="11">
            <el-time-picker
              v-model="form.deadLine2"
              placeholder="请选择截止时间"
              style="width: 200px"
              value-format="HH:mm:ss"
            />
          </el-col>
        </el-form-item>
      </el-row>
    </el-form>
    
  </el-main>
</template>

<script>
import axios from "axios";
import CustomButton from './CustomButton.vue';
import ReleaseBasicQuestion from '@/components/ReleaseBasicQuestion.vue';
import UploadCropper from '@/components/ImageUploadCropper.vue';
import MaterialUpload from '@/components/MaterialUpload.vue';
import { ElMessageBox } from "element-plus";

export default {
  name: 'ReleasePicture',

  components:{
    ReleaseBasicQuestion,
    UploadCropper,
    MaterialUpload,
    CustomButton,
  },
  props: {
    username:String,
    login:Boolean,
    materialType:Number,
  },
  watch:{
    materialType(newVal){
      this.localMaterialType = newVal
      switch(this.localMaterialType)
      {
        case 0:
          this.materialTypeName = '图像'
          break;
        case 1:
          this.materialTypeName = '文本'
          break;
        case 2:
          this.materialTypeName = '视频'
          break;
        case 3:
          this.materialTypeName = '音频'
          break;
        case 4:
          this.materialTypeName = '自定义类型'
          break;
      }
    },
  },
  data(){
    return {
      imageFile:null,
      componentName:'ReleaseBasicQuestion',
      localMaterialType:0,
      options:[
        {
          value: 0,
          label: '单选题',
        },
        {
          value: 1,
          label: '多选题',
        },
        {
          value: 2,
          label: '填空题',
        },
        {
          value: 3,
          label: '框图题',
        },
      ],
      levels:[
        {
          value: 1,
          label: '1',
        },
        {
          value: 2,
          label: '2',
        },
        {
          value: 3,
          label: '3',
        },
        {
          value: 4,
          label: '4',
        },
        {
          value: 5,
          label: '5',
        },
      ],
      form: {//questionNum taskLevel username
        taskName:"",
        poster: "",
        description: "",
        questionType: "",
        receiverNum:0,
        problemTotalNum: "",
        releaseMode: "",
        releaseModeInt: "",
        singleBonus: "",
        starRank: "",
        startLine1: "",
        startLine2: "",
        deadLine1: "",
        deadLine2: "",
        coverUrl:"",
        materialType:"",
      },
      abc:"",
      //传回后端的题目列表，需要复制一百万次给每个problem都一个
      questionTypeMixed:0,
      questionTypeOld:"",
      questionList:[],
      multiple:0,
      editingQuestion:'',
      newOrEdit:0,
      materialTypeName:'图像',
      donutList:[],
      userDonutNum:-1,
    }
  },
  mounted(){
    this.$nextTick(() => {
      axios.get("http://localhost:8000/get_release_info/", {
        params: {
          username:this.username
        }
      }).then((res) => {
        console.log("get_release_info",res.data)
        this.donutList = res.data["donutList"];
        this.userDonutNum = res.data["userDonutNum"];
      }).catch();
    })

  },
  methods:{
    getImage(file){
      this.imageFile = file;
      console.log(file);

    },
    clickHome(){
      this.$router.push({
            name: 'home',
        });
    },
    showQuestionPage(selected){
      this.newOrEdit = 0
      let value = selected.value
      if(this.questionTypeOld != value){
        this.questionTypeMixed = 1
      }
      if(value == 0){
        this.componentName = 'ReleaseBasicQuestion'
        this.multiple = 0
      }else if(value == 1){
        this.componentName = 'ReleaseBasicQuestion'
        this.multiple = 1
      }else if(value == 2){
        this.componentName = 'ReleaseBasicQuestion'
        this.multiple = 2
      }else if(value == 3){
        this.componentName = 'ReleaseBasicQuestion'
        this.multiple = 3
      }
      //记录上一次的question选择
      this.questionTypeOld = value
    },
    addQuestion(newQuestion){
      console.log("新的题目：",newQuestion)
      var len = this.questionList.length
      newQuestion['index'] = len + 1
      this.questionList.push(newQuestion)
    },
    moveQuestionUpward(row, index) {
      if (index > 0) {
        let upData = this.questionList[index - 1];
        this.questionList[index - 1]['index'] ++
        this.questionList[index]['index'] --
        this.questionList.splice(index - 1, 1);
        this.questionList.splice(index, 0, upData);
      } else {
        this.$message({
          message: '已经是第一条，上移失败',
          type: 'warning'
        });
      }
    },
    moveQuestionDown(row, index) {
      if ((index + 1) == this.questionList.length) {
        this.$message({
          message: '已经是最后一条，下移失败',
          type: 'warning'
        });
      } else {
        this.questionList[index + 1]['index'] --
        this.questionList[index]['index'] ++
        let downData = this.questionList[index + 1];
        this.questionList.splice(index + 1, 1);
        this.questionList.splice(index, 0, downData);
      }
    },
    editQuestion(row, index){
      this.editingQuestion = index
      this.newOrEdit = 1
    },
    deleteQuestion(row, index){
      var deleteTarget = index + 1
      console.log(deleteTarget)
      this.questionList.forEach(function (item,index,arr){
          if (item.index == deleteTarget) {
              arr.splice(index,1);
          }
      });
      for(let i = 0; i<this.questionList.length;i++){
        this.questionList[i]['index'] = i + 1
      }
      this.$message({
        message: '删除题目成功',
        type: 'success'
      });
    },
    finalCheck(){
      if(this.form.taskName == ''){
        this.$message({
          message: '您尚未填写任务名！',
          type: 'error'
        });
      }else if(this.form.description == ''){
        this.$message({
          message: '您尚未填写任务描述！',
          type: 'error'
        })
      }else if(this.form.releaseMode == ''){
        this.$message({
          message: '您尚选择发布模式！',
          type: 'error'
        })
      }else if(this.form.deadLine1 == '' || this.form.deadLine2 == ''){
        this.$message({
          message: '您尚未填写完成截止日期！',
          type: 'error'
        })
      }else if(this.form.releaseMode == '定时发布' && (this.form.startLine1 == '' || this.form.startLine2 == '')){
        this.$message({
          message: '您尚未填写完成发布日期！',
          type: 'error'
        })
      }else if(this.form.starRank == ''){
        this.$message({
          message: '您尚未选择星级！',
          type: 'error'
        })
      }else if(this.form.singleBonus == ''){
        this.$message({
          message: '您尚未填写单个试卷奖励！',
          type: 'error'
        })
      }else if(this.questionList.length == 0){
        this.$message({
          message: '您尚未设定任何题目！',
          type: 'error'
        })
      }else if(this.imageFile == null){
        this.$message({
          message: '您尚未设置封面！',
          type: 'error'
        })
      }else if(this.$refs.MyMaterialUpload.fullList.length == 0){
        this.$message({
          message: '您尚未上传任何素材列表！',
          type: 'error'
        })
      }else if(this.donutList[this.form.starRank - 1] > this.form.singleBonus){
        this.$message({
          message: '您的设置的单个题目奖励过低！最低为：'+ this.donutList[this.form.starRank - 1].toString() + "个甜甜圈！",
          type: 'error'
        })
      }else{
        console.log("离开单个题目奖励测试！",this.donutList,[this.form.starRank - 1],this.form.singleBonus)
        let tempLen = this.$refs.MyMaterialUpload.fullList[0].length
        console.log("releaseData:this.$refs.MyMaterialUpload.fullList",this.$refs.MyMaterialUpload.fullListt)
        for(var subList of this.$refs.MyMaterialUpload.fullList){
          if(subList.length !== tempLen){
            this.$message({
              message: '您的题表中题目不相等！',
              type: 'error'
            });
            return false
          }
        }
        if(tempLen == 0){
          this.$message({
            message: '您的题表中没有题目！',
            type: 'error'
          });
          return false
        }
        console.log("进入分配测试：",tempLen,this.$refs.MyMaterialUpload.testList.length,this.form.receiverNum)
        if((tempLen - this.$refs.MyMaterialUpload.testList.length)/this.form.receiverNum < 1){
          this.$message({
            message: '您的题目过少，不足以分配！',
            type: 'error'
          });
          return false
        }
        console.log("进入甜甜圈余额测试",tempLen,this.$refs.MyMaterialUpload.testList.length,this.form.singleBonus,this.userDonutNum)
        console.log("进入甜甜圈余额测试",(tempLen - this.$refs.MyMaterialUpload.testList.length),(tempLen - this.$refs.MyMaterialUpload.testList.length) * this.form.singleBonus)
        if((tempLen - this.$refs.MyMaterialUpload.testList.length) * this.form.singleBonus > this.userDonutNum){
          this.$message({
            message: '您的甜甜圈余额不足！',
            type: 'error'
          });
          return false
        }
        return true
      }
      return false
    },
    blobToFile(blob, fileName, mimeType) {
      return new File([blob], fileName, { type: mimeType });
    },
    preCheck(){
      ElMessageBox.confirm("您现在的甜甜圈余额为"+ this.userDonutNum.toString() + "请问是否要继续发布？", "确认发布", {
        confirmButtonText: "确认",
        cancelButtonText: "取消",
        type: "warning",
        draggable: true,
      }).then(() => {
        this.finalSubmit()
      });
    },
    async finalSubmit(){
      this.form.poster = this.username
      this.form.materialType = this.materialType
      this.form.problemTotalNum = this.$refs.MyMaterialUpload.fullList[0].length
      if(this.questionTypeMixed){
        this.form.questionType = 4
      }
      if(!this.finalCheck()){
        return
      }
      switch (this.form.releaseMode) {
        case "立即发布":
          this.form.releaseModeInt = 0;
          break;
        case "暂不发布":
          this.form.releaseModeInt = 1;
          break;
        default:
          this.form.releaseModeInt = 2;
      }
      var formData = new FormData();
      formData.append("image",this.imageFile);
      formData.append("username", this.username);
      formData.append("fileName", 'image')
      formData.append("size", '-1')
      await axios({
              method:"Post",
              url:'http://localhost:8000/release_task/',
              headers: {
              //请求头这个一定要写
                'Content-Type': 'multipart/form-data',
              },
              data:formData
            })
      .then((res) => {
        console.log(res);
        try{
          if(res.data['status'] == 'get the image'){
            console.log(res);
            this.form.coverUrl = res.data['url']
          }
        }catch(err){
          this.$message({
            message: '上传封面失败',
            type: 'error'
          });
        }
      })
      .catch((err) => {
        console.log(err);
        this.$message({
          message: '上传封面失败',
          type: 'error'
        });
      });     
      await axios.post("http://localhost:8000/release_task/",
        {basicInfoForm:this.form,
          questionList:this.questionList,
          fullList:this.$refs.MyMaterialUpload.fullList,
          testList:this.$refs.MyMaterialUpload.testList,
          listList:this.$refs.MyMaterialUpload.listList,
      }).then(res => {
        if (res.data['status'] == 'done'){
          var confirmRes = this.$confirm('您已成功创建任务，请问是否要继续创建？', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'success'
          }).catch(err => err)
          console.log("confirmResconfirmResconfirmRes", confirmRes)
          if ('confirm' === confirmRes){
            location.reload();
          }
          if ('cancel' === confirmRes) {//用户点击了取消
            location.reload();
            //此处可以跳转到已发布任务列表
          }
          // this.$message({
          //   message: '操作素材列表成功',
          //   type: 'success'
          // });
        }else{
          this.$message({
            message: '操作素材列表失败',
            type: 'error'
          });
        }
      }).catch(error => {
        console.log(error);
        this.$message({
          message: error,
          type: 'error'
        });
      })
    },
    abcSubmit(){
      axios({
          method: 'POST',
          url: 'http://localhost:8000/release_task/',
          data: JSON.parse(this.abc),
          headers: {
              'Content-Type': 'application/json'
          }
      }).then(({ data }) => {
          console.log(data)
      })

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
    font-size:20px;
    font-weight:bold;
  }
  .main-style{
    padding: 20px 20px 20px 40px;
    margin-top: 20px;
    border-radius: 5px;
    box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
  }
  .cropper {
  height: 600px;
  width: 600px;
  background: #ddd;
  border-radius: 20px;
}

</style>