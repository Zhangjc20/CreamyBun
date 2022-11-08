<template>
  <el-header class="header-style">
    <el-breadcrumb separator="/" class="header-breadcrumb">
      <el-breadcrumb-item :to="{ path: '/' }">奶黄包</el-breadcrumb-item>
      <!-- <el-breadcrumb-item
        ><a href="/">promotion management</a></el-breadcrumb-item
      > -->
      <el-breadcrumb-item>任务选择</el-breadcrumb-item>
      <el-breadcrumb-item>图像</el-breadcrumb-item>
    </el-breadcrumb>
    <span class="header-title">
      图像任务
    </span>
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
              <el-input v-model="form.poster" placeholder="请输入任务名字"/>
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
          <el-row style="height: 50px;">
            <el-form-item label="题目数量" :required="true" style="margin-top: 10px;">
              <el-input v-model="form.promblemTotalNum" placeholder="请输入题目数量"/>
              <!-- <CustomButton
                >保存</CustomButton> -->
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
                    prop="questionAns"
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
        <el-row>
        </el-row>
        <el-row>
          <MaterialUpload 
          :username="username"
          :questionList="questionList"
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
          <el-input v-model="form.singleBonus" placeholder="请输入单个题目的奖励"/>
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
              style="width: 100%"
            />
          </el-col>
          <el-col :span="2" class="text-center">
            <span class="text-gray-500">:</span>
          </el-col>
          <el-col :span="11">
            <el-time-picker
              v-model="form.deadLine2"
              placeholder="请选择截止时间"
              style="width: 100%"
            />
          </el-col>
        </el-form-item>
      </el-row>
    </el-form>
    
  </el-main>
</template>

<script>

// import CustomButton from './CustomButton.vue';
import ReleaseBasicQuestion from '@/components/ReleaseBasicQuestion.vue';
import ImageUpload from '@/components/ImageUpload.vue';
import MaterialUpload from '@/components/MaterialUpload.vue';

export default {
  name: 'ReleasePicture',
  // components: {
  //   CustomButton
  // },
  components:{
    ReleaseBasicQuestion,
    ImageUpload,
    MaterialUpload,
  },
  props: {
    username:String,
    login:Boolean,
  },
  data(){
    return {
      componentName:'ReleaseBasicQuestion',

      options:[
        {
          value: 'singleChoice',
          label: '单选题',
        },
        {
          value: 'multipleChoice',
          label: '多选题',
        },
        {
          value: 'fillBlank',
          label: '填空题',
        },
        {
          value: 'frameSelection',
          label: '框图题',
        },
      ],
      levels:[
        {
          value: 'level1',
          label: '1',
        },
        {
          value: 'level2',
          label: '2',
        },
        {
          value: 'level3',
          label: '3',
        },
        {
          value: 'level4',
          label: '4',
        },
        {
          value: 'level5',
          label: '5',
        },
      ],
      form: {//questionNum taskLevel username
        poster: "",
        description: "",
        questionType: "",
        promblemTotalNum: "",
        releaseMode: "",
        singleBonus: "",
        starRank: "",
        startLine1: "",
        startLine2: "",
        deadLine1: "",
        deadLine2: "",
      },
      //传回后端的题目列表，需要复制一百万次给每个problem都一个
      questionList:[],
      multiple:0,
      editingQuestion:'',
      newOrEdit:0,

    }
  },
  methods:{
    clickHome(){
      this.$router.push({
            name: 'home',
        });
    },
    showQuestionPage(selected){
      this.newOrEdit = 0
      let value = selected.value
      if(value == 'singleChoice'){
        this.componentName = 'ReleaseBasicQuestion'
        this.multiple = 0
      }else if(value == 'multipleChoice'){
        this.componentName = 'ReleaseBasicQuestion'
        this.multiple = 1
      }else if(value == 'fillBlank'){
        this.componentName = 'ReleaseBasicQuestion'
        this.multiple = 2
      }else if(value == 'frameSelection'){
        this.componentName = 'ReleaseBasicQuestion'
        this.multiple = 3
      }
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
      // var deleteTarget = index + 1
      // console.log(deleteTarget)
      // this.questionList.forEach(function (item,index,arr){
      //     if (item.index == deleteTarget) {
      //         arr.splice(index,1);
      //     }
      // });
      // for(let i = 0; i<this.questionList.length;i++){
      //   this.questionList[i]['index'] = i + 1
      // }
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
/* 
  .user-area {
    float: right;
    position: absolute;
    top:0;
    right: 0;
    height: 60px;
    margin-right: 90px;
  }
   .avatar {
    float: right;
    position: absolute;
    top:0;
    right: 0;
    margin-right: 180px;
    margin-top: 10px;
  }
  .user-center {
    line-height: 60px;
    margin-bottom: 20px;
    font-size: 22px;
    color:#f8f8f8;
    font-family: YouSheBlack;
    cursor: pointer;
  }
  .user-center:hover {
    opacity: 0.6;
  }
.nav-title {
    float: left;
    height: 60px;
    font-family: YouSheRound;
    line-height: 50px;
    font-size: 28px;
    color: #5EABBF;
    margin-left: 80px;
    display: flex;
  }
  .nav-title-font {
    margin-left: 10px;
    line-height: 60px;
  }
  .menu-out {
    margin-left: 80px;
    background-color: #ffffff;
    width:470px;
    overflow: hidden;
    border-radius: 40px;
    margin-top: 10px;
    display: flex;
   }
   .el-button--primary {
  background: #FBE484 !important;
  border-color: #FBE484 !important;
  color:#6C6C6C;
}
.el-button--medium {
  width: 80px;
}

.logo {
  width: 45px; 
  height: 40px; 
  margin-top: 10px;
}
.login-button {
  margin-right: 30px;
}

.log-buttons {
  float: right;
  position: absolute;
  top:0;
  right: 0;
  line-height: 60px;
  margin-right: 100px;
}
.el-nav-menu {
  width:480px;
  padding-left: 46px;
}
.el-menu {
  border-radius: 0;
}
.el-menu-item {
  height: 50px;
  font-size: 16px;
  padding-top: 4px;
}
.el-menu--horizontal .el-menu-item:not(.is-disabled):focus{
  background-color: transparent;
}
.el-menu--horizontal .el-menu-item:not(.is-disabled):hover{
  background-color: #f8f8f8;
} */
</style>