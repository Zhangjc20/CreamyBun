<template>
  <el-main class="main-style" >
    <el-row style="height: 50px;">
      <span class="header-title" style="margin: auto,auto,auto,20px;">题目设置：单选题</span>
    </el-row>

  </el-main>
</template>

<script>
export default {
  name: 'PerformTaskMaterial',
  props: {
    materialInfo:Object,
  },
  // watch: {
  //   multiple(newVal, oldVal){
  //     console.log(newVal,oldVal)
  //     this.questionType = newVal
  //     this.init()
  //   },
  //   editingQuestion(newVal, oldVal){
  //     // newVal是新值，oldVal是旧值
  //     console.log(newVal,oldVal)
  //     console.log(this.questionList)
  //     this.tempQuestion = this.questionList[newVal]
  //     this.description = this.tempQuestion.questionDescription
  //     this.minOptionNum = this.tempQuestion.minOptionNum
  //     this.maxOptionNum = this.tempQuestion.maxOptionNum
  //     this.questionType = this.tempQuestion.questionType
  //     this.mustDo = this.tempQuestion.mustDo
  //     this.optionList = this.tempQuestion.optionList
  //   }
  // },
  data(){
    return {
      idRef:['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
    }
  },
  methods:{
    init(){
      this.currentOption = '26',
      this.description = '',
      this.optionList = [],
      this.minOptionNum = '',
      this.maxOptionNum = '',
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
      }
      this.$emit("questionSubmit", 
      { questionTypeName:tempType,
        questionType:this.questionType,
        questionDescription:this.description, 
        optionList:this.optionList.concat(),
        minOptionNum:this.minOptionNum,
        maxOptionNum:this.maxOptionNum,
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