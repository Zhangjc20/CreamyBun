<template>
  <el-main class="main-style" >
    <el-row style="height: 30px;">
      <span class="header-title" style="margin: auto,auto,auto,20px;">题目设置：单选题</span>
      <CustomButton @click="clickAddOption" isRound="true" style="float: right; right: 20px; position: absolute" title="新增选项"/>
    </el-row>
    <!-- <el-row v-for="option in optionList">
      <el-header>
        <span class="header-title" style="margin: auto,auto,auto,20px;">{{option.content}}</span>
      </el-header>
    </el-row> -->
    <el-table
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

      <!-- <el-dialog
        v-model="dialogVisible"
        title="请设置选项内容"
        width="30%"
      >
        <el-input v-model="currentContent" placeholder="请输入选项内容"/>
        <template #footer>
          <span class="dialog-footer">
            <CustomButton @click="dialogVisible = false" isRound="true" normalColor="#eeeeee" fontColor="#000000" title="取消"/>
            <CustomButton @click="clickContentSet" isRound="true" title="确定修改"/>

          </span>
        </template>
      </el-dialog> -->

  </el-main>
</template>

<script>

import CustomButton from './CustomButton.vue';
// class Option {
//   constructor(id, content) {
//     this.id = id;
//     this.content = content;
//   }
// }
export default {
  name: 'ReleaseSingleChoice',
  components: {
    CustomButton
  },
  data(){
    return {
      currentContent:'',
      currentOption:'26',
      // dialogVisible: false,
      optionList:[],
      idRef:['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
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
    rowClick(row,column){
      if(column.label == "选项内容"){
        this.currentOption = row.index
        console.log(row,column)
        // this.dialogVisible = true //这句话一旦执行必然马上触发对话框
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
        // let newOptionList = []
        
        // var i = 0
        // console.log("kaishi ")
        // console.log(this.optionList)
        // console.log("开始的newOptionList",newOptionList)
        // for(let j = 0; j < this.optionList.length; j++){
        //   console.log("i",i)
        //   console.log("this.optionList[j]",this.optionList[j])
        //   console.log("this.optionList[j].index",this.optionList[j].index)
        //   if(deleteTarget == this.optionList[j].index){
        //     continue
        //   }
        //   var tempOption = {}
          
        //   tempOption['index'] = i
        //   tempOption['name'] = this.idRef[i]
        //   tempOption['content'] = this.optionList[j].content
        //   newOptionList.push(tempOption)
        //   console.log("可以保留，tempOption：",tempOption)
        //   console.log("现在的newOptionList",newOptionList)
        //   i++
        // }
        // console.log("结束 ",newOptionList)

        // this.optionList = newOptionList
        console.log(row,column)
      }
      
    },
    clickContentSet(){

      this.dialogVisible = false
    }
    // clickAddOption(){
    //   this.optionList.push({id:"1",content:"16511653"})
    //   console.log("this.optionList")
    // },
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