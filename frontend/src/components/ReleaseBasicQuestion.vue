<template>
  <el-main class="main-style" >
    <el-row style="height: 50px;">
      <span class="header-title" style="margin: auto,auto,auto,20px;" v-if="questionType == 0">题目设置：单选题</span>
      <span class="header-title" style="margin: auto,auto,auto,20px;" v-if="questionType == 1">题目设置：多选题</span>
      <span class="header-title" style="margin: auto,auto,auto,20px;" v-if="questionType == 2">题目设置：填空题</span>
      <span class="header-title" style="margin: auto,auto,auto,20px;" v-if="questionType == 3">题目设置：框图题</span>
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
            type="number"
            @blur="minOptionNum=Number(minOptionNum)"
            placeholder="最小数量"
            resize="none"
            style="width: 100px;height: 40px;"
            oninput="value=value.replace(/[^\d]/g,'')"
          />

        </el-col>
        <el-col :span="2" class="text-center">
        </el-col>
        <el-col :span="11">
          <el-input
            v-model="maxOptionNum"
            :rows="1"
            type="number"
            @blur="maxOptionNum=Number(maxOptionNum)"
            placeholder="最大数量"
            resize="none"
            style="width: 100px;height: 40px;"
            oninput="value=value.replace(/[^\d]/g,'')"
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
            type="number"
            @blur="minOptionNum=Number(minOptionNum)"
            placeholder="最小字数"
            resize="none"
            style="width: 100px;height: 40px;"
            oninput="value=value.replace(/[^\d]/g,'')"
          />
        </el-col>
        <el-col :span="2" class="text-center">
        </el-col>
        <el-col :span="11">
          <el-input
            v-model="maxOptionNum"
            :rows="1"
            type="number"
            @blur="maxOptionNum=Number(maxOptionNum)"
            placeholder="最大字数"
            resize="none"
            style="width: 100px;height: 40px;"
            oninput="value=value.replace(/[^\d]/g,'')"
          />
        </el-col>
      </el-form-item>
    </el-row>

    <el-row style="height: 50px;" v-if="questionType == 3">
      <el-form-item label="答案框数" :required="true">
        <el-col :span="11">
          <el-input
            v-model="minOptionNum"
            :rows="1"
            type="number"
            @blur="minOptionNum=Number(minOptionNum)"
            placeholder="最小框数"
            resize="none"
            style="width: 100px;height: 40px;"
            oninput="value=value.replace(/[^\d]/g,'')"
          />
        </el-col>
        <el-col :span="2" class="text-center">
        </el-col>
        <el-col :span="11">
          <el-input
            v-model="maxOptionNum"
            :rows="1"
            type="number"
            @blur="maxOptionNum=Number(maxOptionNum)"
            placeholder="最大框数"
            resize="none"
            style="width: 100px;height: 40px;"
            oninput="value=value.replace(/[^\d]/g,'')"
          />
        </el-col>
      </el-form-item>
    </el-row>
    <el-row style="height: 60px;" v-if="questionType == 3">
      <el-form-item label="题干" :required="true">
        <el-input
          v-model="targetIndex"
          :rows="1"
          placeholder="请输入指向素材"
          resize="none"
          style="width: 150px;"
          type="number"
          @blur="targetIndex=Number(targetIndex)"
          oninput="value=value.replace(/[^\d]/g,'')"
        />
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

    <el-table v-if="questionType == 0 || questionType == 1"
        :data="optionList"
        height="200"
        :style="table"
        @row-click="rowClick"
        class="customer-table">
        <el-table-column
          prop="name"
          label="选项"
          width="100">
        </el-table-column>
        <el-table-column
          prop="content"
          label="选项内容"
          width="200">
          <template v-slot="scope">
            <div v-if="scope.row.index == currentOption">
              <el-input v-model="scope.row.content" placeholder="请输入选项内容"/>
            </div>
            <div v-else>{{ (scope.row.content) }}</div>
          </template>
        </el-table-column>
        
        <el-table-column
          prop=""
          label=""
          width="">
        </el-table-column>
        
        <el-table-column
          prop=""
          label="删除"
          width="">
          <span class="iconfont icon-menu"></span>
        </el-table-column>
      </el-table>
  </el-main>
</template>

<script>

import CustomButton from './CustomButton.vue';
export default {
  name: 'ReleaseBasicQuestion',
  components: {
    CustomButton
  },
  props: {
    multiple:Number,
    editingQuestion:Number,
    questionList:Array,
    newOrEdit:Boolean,
  },
  watch: {
    multiple(newVal, oldVal){
      console.log(newVal,oldVal)
      this.questionType = newVal
      this.init()
    },
    editingQuestion(newVal, oldVal){
      // newVal是新值，oldVal是旧值
      console.log(newVal,oldVal)
      console.log(this.questionList)
      this.tempQuestion = this.questionList[newVal]
      this.description = this.tempQuestion.questionDescription
      this.minOptionNum = this.tempQuestion.minOptionNum
      this.maxOptionNum = this.tempQuestion.maxOptionNum
      this.targetIndex = this.tempQuestion.targetIndex
      this.questionType = this.tempQuestion.questionType
      this.mustDo = this.tempQuestion.mustDo
      this.optionList = this.tempQuestion.optionList
    }
  },
  data(){
    return {
      questionType: this.multiple,
      currentOption:'26',
      description:'',
      optionList:[],
      idRef:['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
      minOptionNum:'',
      maxOptionNum:'',
      targetIndex:'',
      mustDo:true,
      tempQuestion:{},
    }
  },
  methods:{
    init(){
      this.currentOption = '26',
      this.description = '',
      this.optionList = [],
      this.minOptionNum = '',
      this.maxOptionNum = '',
      this.targetIndex = '',
      this.mustDo = true
    },
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
    clickSubmit(){
      if(!this.checkContent())return
      let tempType = '单选'
      if(this.questionType == 1){
        tempType = '多选'
      }else if(this.questionType == 2){
        tempType = '填空'
      }else if(this.questionType == 3){
        tempType = '框图'
      }
      if(this.questionType == 0){
        this.minOptionNum = 1
        this.maxOptionNum = 1
      }
      this.$emit("questionSubmit", 
      { questionTypeName:tempType,
        questionType:this.questionType,
        questionDescription:this.description, 
        optionList:this.optionList.concat(),
        minOptionNum:this.minOptionNum,
        maxOptionNum:this.maxOptionNum,
        targetIndex:this.targetIndex,
        mustDo:this.mustDo,
        questionAns:'' //很久以后才会用到的接口
      })
      //提交后初始化列表
      this.init()
      this.$message({
        message: '提交题目成功',
        type: 'success'
      });
    },
    clickEdit(){
      if(!this.checkContent())return
      this.tempQuestion.questionDescription = this.description
      this.tempQuestion.minOptionNum = this.minOptionNum
      this.tempQuestion.maxOptionNum = this.maxOptionNum
      this.tempQuestion.targetIndex = this.targetIndex
      this.tempQuestion.questionType = this.questionType
      this.tempQuestion.mustDo = this.mustDo
      this.tempQuestion.optionList = this.optionList
      this.$message({
        message: '修改题目成功',
        type: 'success'
      });
    },
    rowClick(row,column){
      if(column.label == "选项内容"){
        this.currentOption = row.index
        console.log(row,column)
      }else if(column.label == "删除"){//删除特定行的内容
        var deleteTarget = row.index
        console.log(deleteTarget)
        this.optionList.forEach(function (item,index,arr){
            if (item.index == deleteTarget) {
                arr.splice(index,1);
            }
        });
        for(let i = 0; i<this.optionList.length;i++){
          this.optionList[i]['index'] = i
          this.optionList[i]['name'] = this.idRef[i]
        }
        console.log(row,column)
      }
    },
    // this.currentOption = '26',
    //   this.description = '',
    //   this.optionList = [],
    //   this.minOptionNum = '',
    //   this.maxOptionNum = '',
    //   this.mustDo = true
    checkContent(){
      if(this.optionList.length == 0 && (this.questionType == 0 || this.questionType == 1)){
        this.$message({
          message: '您尚未添加选项！',
          type: 'warning'
        });
      }else if(this.minOptionNum == '' && this.questionType == 1){
        this.$message({
          message: '您尚未设置选项最小数量！',
          type: 'warning'
        })
      }else if(this.maxOptionNum == '' && this.questionType == 1){
        this.$message({
          message: '您尚未设置选项最大数量！',
          type: 'warning'
        })
      }else if(this.minOptionNum == '' && this.questionType == 2){
        this.$message({
          message: '您尚未设置填空最小字数！',
          type: 'warning'
        })
      }else if(this.maxOptionNum == '' && this.questionType == 2){
        this.$message({
          message: '您尚未设置填空最大字数！',
          type: 'warning'
        })
      }else if(this.maxOptionNum < this.minOptionNum){
        this.$message({
          message: '您的最大量小于最小量！',
          type: 'warning'
        })
      }else if(this.targetIndex =='' && this.questionType == 3){
        this.$message({
          message: '您尚未设置框图指向！',
          type: 'warning'
        })
      }else if(this.description == ''){
        this.$message({
          message: '您尚未添加题干！',
          type: 'warning'
        })
      }else{
        return true
      }
      return false
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
  .main-style{
    padding: 20px 20px 20px 40px;
    margin-top: 20px;
    border-radius: 5px;
    box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
    margin-right: 40px;
  }
</style>