<template>
  <el-header class="header-style">
    <el-breadcrumb separator="/" class="header-breadcrumb">
      <el-breadcrumb-item :to="{ path: '/' }">奶黄包</el-breadcrumb-item>
      <el-breadcrumb-item>任务选择</el-breadcrumb-item>
      <el-breadcrumb-item>{{ this.materialTypeName }}</el-breadcrumb-item>
    </el-breadcrumb>
    <span class="header-title">
      {{taskName}}
    </span>
    <CustomButton isRound="true" style="float: right; right: 50px; top: 100px; position: absolute" height="40px"
      width="150px" title="提交任务" />
  </el-header>
  <!-- <el-row :gutter="20">
      <el-col :span="16"><div class="grid-content ep-bg-purple" /></el-col>
      <el-col :span="8"><div class="grid-content ep-bg-purple" /></el-col>
    </el-row> -->
  <el-row :gutter="20" style="margin-top:20px">
    <el-col :span="15">
      <el-main class="main-style-two" style="height:calc(100vh - 220px)">
        <el-row class="main-style" v-for="material in materialList" :key="material">
          <!-- {{material['fileNotes']}} -->
          <PerformTaskMaterial ref="materialBlock" :materialInfo="material">

          </PerformTaskMaterial>
        </el-row>
      </el-main>


    </el-col>
    <!-- <el-col :span="16" v-for="material in materialList" :key="material">
      <PerformTaskMaterial
      :materialInfo="material"
      >
      </PerformTaskMaterial>
    </el-col> -->
    <el-col :span="9">
      <el-main class="main-style-two" style="height:calc(100vh - 220px)">
        <el-row class="question-row" v-for="question in questionList" :key="question">
          <span class="header-title" style="margin: auto,auto,auto,20px;">
            {{ question["index"] + '.[' + question["questionTypeName"] + ']: ' + question["questionDescription"] }}
          </span>
          <CustomButton @click="currentQuestionIndex = question['index'] - 1;clickFillBlank(question['targetIndex'] - 1,question['minOptionNum'],question['maxOptionNum'] )" v-if="question['questionType'] == 3" isRound="true" style="float: right; right: 0px; top: 5px; position: absolute" height="30px"
            width="100px" title="点击框图" />
          <el-table v-if="question['questionType'] == 0 || question['questionType'] == 1" :data="question['optionList']"
            :style="table" ref="regTable"
            @selection-change="handleSelectionChange($event, question['minOptionNum'], question['maxOptionNum'], question['index'] - 1)"
            class="selection-table">
            <el-table-column type="selection" width="50">
            </el-table-column>
            <el-table-column prop="name" label="选项" width="100">
            </el-table-column>
            <el-table-column prop="content" label="选项内容" width="200">
              <template v-slot="scope">
                <div>{{ (scope.row.content) }}</div>
              </template>
            </el-table-column>

            <el-table-column prop="" label="" width="">
            </el-table-column>

            <el-table-column prop="" label="删除" width="">
              <span class="iconfont icon-menu"></span>
            </el-table-column>
          </el-table>
          <el-input v-if="question['questionType'] == 2" v-model="this.ansList[question['index'] - 1]" :rows="3"
            type="textarea" placeholder="请输入填空题答案" resize="none" :maxlength="question['maxOptionNum']" show-word-limit
            style="margin: 20px;" />
            
        </el-row>
      </el-main>

    </el-col>
  </el-row>
  <!-- <el-col :span="8" style="border-left: 1px solid #999999;"></el-col> -->
  <!-- <el-main class="main-style">
    
  </el-main> -->
  <el-dialog
      v-model="fillBlankDialogVisible"
      title="设置题目答案"

    >
      <span class="header-title" style="margin: auto,auto,auto,20px;">请进行框图</span>
        <ImageFramer ref="MyImageFramer" style="width:100%" :minFrameNum="currentMin" :maxFrameNum="currentMax" :src="currentImage.src"/>
      <span class="dialog-footer">
        <el-row style="height: 50px;">
          <el-col :span="20">
          </el-col>
          <el-col :span="4">
            <CustomButton @click="getFillBlankAns" style="margin-left:20px" isRound="true" title="确定"/>
          </el-col>
        </el-row>
        
      </span>
    
    </el-dialog>
</template>

<script>
import axios from "axios";
import CustomButton from './CustomButton.vue';
import PerformTaskMaterial from "@/components/PerformTaskMaterial.vue";
import ImageFramer from "@/components/ImageFramer.vue";
// import { ElMessageBox } from "element-plus";

export default {
  name: 'PerformTask',

  components: {
    CustomButton,
    PerformTaskMaterial,
    ImageFramer
  },
  props: {
    username: String,
    login: Boolean,
    taskId: Number,
    taskName:String,
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
  data() {
    return {
      imageFile: null,
      questionList: [],
      materialList: [],
      ansList: [],
      lastSelectedList: [],
      currentImage:undefined,
      fillBlankDialogVisible:false,
      currentMin:-1,
      currentMax:-1,
      currentQuestionIndex:-1,
    }
  },
  mounted() {
    //nextTick:加载完参数后再运行下面的
    this.$nextTick(() => {
      // dom元素更新后执行，因此这里能正确打印更改之后的值
      // console.log("http://localhost:8000/uck_me/")
      // axios.get("http://localhost:8000/uck_me/", {
          console.log("http://localhost:8000/perform_basic_info/")
        axios.get("http://localhost:8000/perform_basic_info/",{
        params: {
          username: this.username,
          taskId: this.taskId
        }
      }).then((res) => {
        console.log("成功加载一个material", res)
        this.questionList = res.data['questionList'];
        this.materialList = res.data['materialList'];
        for (var i = 0; i < this.questionList.length; i++) {
          this.lastSelectedList.push(undefined)
          var tempQuestion = this.questionList[i]
          // 如果题目是选择题
          if (tempQuestion['questionType'] == 0 || tempQuestion['questionType'] == 1) {
            this.ansList.push([])
            // 初始化对应串
            for (var j = 0; j < tempQuestion['optionList'].length; j++) {
              // console.log(j,tempQuestion['optionList'][j])
              this.ansList[i].push({
                index: tempQuestion['optionList'][j]['index'],
                name: tempQuestion['optionList'][j]['name'],
                selected: 0
              })
            }
            // 否则
          } else {
            this.ansList.push('')
          }

        }

      }).catch();
    })

  },
  methods: {
    clickFillBlank(targetIndex,min,max){
      this.currentImage = this.$refs.materialBlock[targetIndex].image
      console.log("this.currentImage",this.currentImage)
      this.fillBlankDialogVisible = true
      this.currentMax = max
      this.currentMin = min
    },
    getFillBlankAns(){
      this.fillBlankDialogVisible = false; 
      var tempAnsList = this.$refs.MyImageFramer.frameRects
      console.log("tempAnsList",tempAnsList,this.currentQuestionIndex)
      var ans = ''
      for(var rect of tempAnsList){
        var temp = '(' + rect.startX.toString() + ',' + rect.startY.toString()
         + ',' + (rect.startX + rect.width).toString() + ',' + (rect.startY + rect.height).toString() + ')'
        ans += temp
      }
      this.ansList[this.currentQuestionIndex] = ans
      console.log("this.ansList[this.currentQuestionIndex]",this.ansList[this.currentQuestionIndex])
    },
    // rowClick(row,minOptionNum,maxOptionNum,dom) {
    //   // 单击行，设置选中
    //   console.log(":::::::::",row,minOptionNum,maxOptionNum,dom)
    //   const check = this.checkTableList.find((v) => {return v.id == row.id})
    //   if (!check && this.checkTableList.length >= maxOptionNum) {
    //     this.$message.warning(`最多只能选minOptionNum条！`)
    //     return
    //   }
    //   if (check && this.checkTableList.length <= minOptionNum) {
    //     this.$message.warning(`最少需要选minOptionNum条！`)
    //     return
    //   }
    //   dom.toggleRowSelection(row)
    // },
    // checkboxInit(row) {
    //   // 设置checkbox，选中状态，是否可选
    //   const check = this.checkTableList.find((v) => {return v.id == row.id})
    //   if (!check && this.checkTableList.length == this.checkNumber) {
    //     return 0
    //   } else {
    //     return 1
    //   }
    // }
    getDeletedRow(selection, questionIndex) {
      var judgeList = JSON.parse(JSON.stringify(this.ansList[questionIndex]))
      // console.log("judgeListjudgeListjudgeList",judgeList)
      for (var tempRow of selection) {
        var tempTarget = tempRow['index']
        judgeList[tempTarget]['selected'] = 0
      }
      // console.log("judgeListjudgeListjudgeList",judgeList)
      var targetIndex = -1;
      for (var tempRow of judgeList) {
        if (tempRow['selected']) {
          targetIndex = tempRow['index']
        }
      }
      // console.log("targetIndextargetIndextargetIndex",targetIndex)
      // console.log("lastSelectedListlastSelectedListlastSelectedList",this.lastSelectedList[questionIndex])
      for (var tempRow of this.lastSelectedList[questionIndex]) {
        if (tempRow['index'] == targetIndex) {
          return tempRow
        }
      }
      return
    },
    handleSelectionChange(selection, minOptionNum, maxOptionNum, index) { // section 被选中状态修改后触发事件，根据被选择的数量控制是否还可被选中

      // console.log("selection", selection)
      // console.log("this.ansList[index]", this.ansList[index])
      // 如果是单选
      // if(minOptionNum == 1 && maxOptionNum == 1){

      // }else{
      if (selection.length > maxOptionNum) {
        // 如果这个题是单选
        if (minOptionNum == 1 && maxOptionNum == 1) {
          for (var tempRow of this.ansList[index]) {
            tempRow['selected'] = 0
          }
          this.ansList[index][selection[1]['index']]['selected'] = 1
          this.$refs.regTable[index].toggleRowSelection(selection[0], false)
          return
        }
        this.$message.warning(`最多只能选${maxOptionNum}条！`);
        this.$refs.regTable[index].toggleRowSelection(selection[selection.length - 1], false)
        return
      }
      var lastLen = 0
      for (var tempRow of this.ansList[index]) {
        if (tempRow['selected']) {
          lastLen++
        }
      }
      if (selection.length < minOptionNum && selection.length < lastLen && minOptionNum < maxOptionNum) {
        this.$message.warning(`最少需要选${maxOptionNum}条！`);
        var targetRow = this.getDeletedRow(selection, index)
        // console.log("targetRowtargetRowtargetRow",targetRow)
        this.$refs.regTable[index].toggleRowSelection(targetRow)
        return
      }
      for (var tempRow of this.ansList[index]) {
        tempRow['selected'] = 0
      }
      for (var tempRow of selection) {
        // this.ansList[i].push({
        //   index: tempQuestion['optionList'][j]['index'],
        //   name: tempQuestion['optionList'][j]['name'],
        //   selected:0
        // })
        // console.log("tempRow",tempRow)
        // console.log("tempRow['index']",tempRow['index'])
        // console.log("this.ansList[index][tempRow['index']]",this.ansList[index][tempRow['index']])
        this.ansList[index][tempRow['index']]['selected'] = 1
      }
      this.lastSelectedList[index] = selection
      //  else if (selection.length <= minOptionNum) {
      //   this.$message.warning(`最少只能选${minOptionNum}条！`);
      //   for (let j of this.popTableData) {
      //     j.status = 0;
      //     for (let i of selection) {
      //      if (i.id == j.id) {
      //       j.status = 1;
      //      }
      //     }
      //   }
      //   return
      //  } 
      // else {
      // for (let i in this.popTableData) {
      //   this.popTableData[i].status = 1;
      // }
      // }
      // }

    }
  }
}
</script>

<style scoped>
/* 隐藏多选框 */
.selection-table /deep/ .el-table__header-wrapper .el-checkbox {
  display: none
}

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
  font-size: 15px;
  font-weight: bold;
}

.main-style-two {
  padding: 20px 20px 20px 20px;
  border-radius: 5px;
  box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
}

.main-style {
  padding: 20px 20px 20px 20px;
  margin-top: 20px;
  border-radius: 5px;
  box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
}

.question-row {
  margin-top: 10px;
  border-top: 1px dashed #999999;
  padding-top: 10px;
}

.material-row {
  margin-top: 20px;
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