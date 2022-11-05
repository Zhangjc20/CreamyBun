<template>
  <el-main class="main-style" >
    <el-row style="height: 50px;">
      <span class="header-title" style="margin: auto,auto,auto,20px;" v-if="questionType == 0">题目设置：单选题</span>
      <span class="header-title" style="margin: auto,auto,auto,20px;" v-if="questionType == 1">题目设置：多选题</span>
      <span class="header-title" style="margin: auto,auto,auto,20px;" v-if="questionType == 2">题目设置：填空题</span>
      <CustomButton @click="clickAddOption" isRound="true" style="float: right; right: 120px; position: absolute" v-if="questionType == 0 || questionType == 1" title="新增选项"/>
      <CustomButton @click="clickEdit" isRound="true" style="float: right; right: 20px; position: absolute" v-if="newOrEdit" title="提交修改"/>
      <CustomButton @click="clickSubmit" isRound="true" style="float: right; right: 20px; position: absolute" v-if="!newOrEdit" title="提交题目"/>
    </el-row>
    <el-row style="height: 50px;" v-if="questionType == 1">
      <el-form-item label="选项数量" :required="true">
        <el-col :span="11">
          <el-input
            v-model="minOptionNum"
            :rows="1"
            type="textarea"
            placeholder="最小数量"
            resize="none"
            style="width: 100px;height: 40px;"
          />
        </el-col>
        <el-col :span="2" class="text-center">
        </el-col>
        <el-col :span="11">
          <el-input
            v-model="maxOptionNum"
            :rows="1"
            type="textarea"
            placeholder="最大数量"
            resize="none"
            style="width: 100px;height: 40px;"
          />
        </el-col>
      </el-form-item>
    </el-row>

    <el-row style="height: 50px;" v-if="questionType == 2">
      <el-form-item label="答案字数" :required="true">
        <el-col :span="11">
          <el-input
            v-model="minOptionNum"
            :rows="1"
            type="textarea"
            placeholder="最小字数"
            resize="none"
            style="width: 100px;height: 40px;"
          />
        </el-col>
        <el-col :span="2" class="text-center">
        </el-col>
        <el-col :span="11">
          <el-input
            v-model="maxOptionNum"
            :rows="1"
            type="textarea"
            placeholder="最大字数"
            resize="none"
            style="width: 100px;height: 40px;"
          />
        </el-col>
      </el-form-item>
    </el-row>

    <el-row style="height: 60px;">
      <el-form-item label="题干" :required="true">
        <el-input
          v-model="description"
          :rows="2"
          type="textarea"
          placeholder="请输入任务描述"
          resize="none"
          style="width: 300px;"
        />
      </el-form-item>
    </el-row>
    <el-row>
      <el-form-item label="必做">
        <el-switch v-model="mustDo" active-color="#5EABBF"/>
      </el-form-item>
    </el-row >
  </el-main>
</template>

<script>

import CustomButton from './CustomButton.vue';
export default {
  name: 'ImageUpload',
  components: {
    CustomButton
  },
  // props: {
  //   multiple:Number,
  //   editingQuestion:Number,
  //   questionList:Array,
  //   newOrEdit:Boolean,
  // },
  data(){
    return {
      questionType: this.multiple,
      currentOption:'26',
      description:'',
      optionList:[],
      idRef:['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
      minOptionNum:'',
      maxOptionNum:'',
      mustDo:true,
      tempQuestion:{},
    }
  },
  methods:{
    clickAddOption(){
      var tempOption = {}
      var len = this.optionList.length
      if(len < 26){
        tempOption['index'] = len
        tempOption['name'] = this.idRef[len]
        tempOption['content'] = ''
        this.optionList.push(tempOption)
        console.log(this.optionList)
      }
      
    },
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
    border-radius: 5px;
    box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
    margin-left: 40px;
    margin-right: 40px;
  }
</style>