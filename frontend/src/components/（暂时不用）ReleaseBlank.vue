<template>
  <el-main class="main-style" >
    <el-row style="height: 50px;">
      <span class="header-title" style="margin: auto,auto,auto,20px;">题目设置：填空题</span>
      <CustomButton @click="clickSubmit" isRound="true" style="float: right; right: 20px; position: absolute" title="提交题目"/>
    </el-row>
    <el-row style="height: 50px;">
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
      <el-form-item label="题目描述" :required="true">
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
    </el-row>

  </el-main>
</template>

<script>

import CustomButton from './CustomButton.vue';
export default {
  name: 'ReleaseBlank',
  components: {
    CustomButton
  },
  data(){
    return {
      description:'',
      optionList:[],
      minOptionNum:'',
      maxOptionNum:'',
      mustDo:true,
    }
  },
  methods:{
    clickSubmit(){
      let tempType = '填空'
      this.$emit("questionSubmit", 
      { questionType:tempType,
        questionDescription:this.description, 
        optionList:[],
        minOptionNum:this.minOptionNum,
        maxOptionNum:this.maxOptionNum,
        mustDo:this.mustDo
      })
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
    margin-top: 20px;
    border-radius: 5px;
    box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
    margin-right: 40px;
  }
</style>