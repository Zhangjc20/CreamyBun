<template>
  <el-main class="main-style" >
    <el-row style="height: 50px;">
      <span class="header-title" style="margin: auto,auto,auto,20px;">请上传任务素材</span>
      <CustomButton @click="testListDialogVisible = true" isRound="true" style="float: right; right: 20px; position: absolute" v-if="!newOrEdit" title="编辑资质测试列表"/>
    </el-row>
    <!-- <el-row style="height: 50px;">
      <el-input
        v-model="minOptionNum"
        :rows="1"
        type="textarea"
        placeholder="最小数量"
        resize="none"
        style="width: 100px;height: 40px;"
      />
    </el-row> -->
    <!-- 这里好像必须加个if -->
    <template v-if="true">
      <el-upload
        class="upload-demo"
        multiple="false"
        action="api"
        drag
        :show-file-list="false"
        :http-request="handleChangeUpload"
      >
      <i class="el-icon-upload"></i>
            <div class="el-upload__text">点击上传</div>
            <div class="el-upload__tip">
              请上传压缩包
            </div>
      </el-upload>
      <el-progress
        :percentage="progress"
        :stroke-width="10"
        style="margin: 10px 10px 10px 10px"
        color="#5EABBF"
      />
      <el-table
        :data="listList"
        height="150"
        :style="table"
        @row-click="rowClick"
        class="customer-table">
        <el-table-column
          prop="index"
          label="序号"
          width="60">
        </el-table-column>
        <el-table-column
          prop="listName"
          label="表名"
          width="100">
        </el-table-column>
        <el-table-column
          prop="notes"
          label="注释"
          width="200">
          <template v-slot="scope">
            <div v-if="scope.row.index == currentList">
              <el-input v-model="scope.row.notes" placeholder="请输入注释内容"/>
            </div>
            <div v-else>{{ (scope.row.notes) }}</div>
          </template>
        </el-table-column>
        
        <el-table-column
          prop=""
          label=""
          width="">
        </el-table-column>
        
        <!-- <el-table-column
          prop=""
          label="删除"
          width="">
          <span class="iconfont icon-menu"></span>
        </el-table-column> -->
      </el-table>

      <el-table
        :data="fileList.slice((page - 1) * pageSize, (page - 1) * pageSize + pageSize)"
        height="500"
        :style="table"
        class="customer-table">
        <el-table-column
          prop="index"
          label="题号"
          width="60">
        </el-table-column>
        <el-table-column
          prop="fileName"
          label="文件名"
          width="180">
        </el-table-column>
        <el-table-column
          prop="fileSize"
          label="大小"
          width="100">
        </el-table-column>
        <!-- <el-table-column
          prop="fileType"
          label="类型"
          width="100">
        </el-table-column> -->
        

        
        <el-table-column
          prop=""
          label="操作"
          width="60">
          <template v-slot="scope">
            <el-dropdown>
              <span class="iconfont icon-menu"></span>
              <template #dropdown>
                <el-dropdown-menu>
                  <el-dropdown-item icon="el-icon-s-order" @click="setTest(scope.row, scope.$index)">设置为测试题</el-dropdown-item>
                  <!-- <el-dropdown-item icon="el-icon-remove" @click="moveQuestionDown(scope.row, scope.$index)">下移</el-dropdown-item>
                  <el-dropdown-item icon="el-icon-remove" @click="editQuestion(scope.row, scope.$index)">编辑</el-dropdown-item>
                  <el-dropdown-item icon="el-icon-download" @click="deleteQuestion(scope.row, scope.$index)">删除</el-dropdown-item> -->
                </el-dropdown-menu>
              </template>
              
            </el-dropdown>
          </template>
        </el-table-column>
        <el-table-column
          prop=""
          label=""
          width="">
        </el-table-column>
      </el-table>
      <el-pagination
        :page-sizes="[10, 15, 20, 25]"
        :small="small"
        :disabled="disabled"
        :background="background"
        layout="sizes, prev, pager, next, jumper"
        :total="fileList.length"
        :pager-count="3"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
      />

      <!-- <el-upload
            class="upload-demo"
            action=""
            drag
            :auto-upload="false"
            :show-file-list="false"
            :on-change="handleChangeUpload"
          >
            <i class="el-icon-upload"></i>
            <div class="el-upload__text">点击上传</div>
            <div class="el-upload__tip">
              请上传压缩包
            </div>
          </el-upload> -->
    </template>
    <el-dialog
      v-model="testSetDialogVisible"
      title="设置题目答案"
      width="50%"
      height="80%"
    >
      <span class="header-title" style="margin: auto,auto,auto,20px;">请设置题目答案</span>
      <el-table
        :data="currentTestAnsList"
        height="500"
        :style="table"
        @row-click="rowClickTestSetDialog"
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
          label="答案"
          width="200">
          <template v-slot="scope">
            <div v-if="scope.row.index == currentTestSetDialogList">
              <el-input v-model="scope.row.questionAns" placeholder="请输入注释内容"/>
            </div>
            <div v-else>{{ (scope.row.questionAns) }}</div>
          </template>
        </el-table-column>
        
        <el-table-column
          prop=""
          label=""
          width="">
        </el-table-column>
        
        <!-- <el-table-column
          prop=""
          label="删除"
          width="">
          <span class="iconfont icon-menu"></span>
        </el-table-column> -->
      </el-table>
      <span class="dialog-footer">
        <el-row style="height: 50px;">
          <el-col :span="12">
            <CustomButton @click="testSetDialogVisible = false" style="margin-right:20px" isRound="true" title="取消提交"/>
          </el-col>
          <el-col :span="12">
            <CustomButton v-if="!isEditingTestAns" @click="handleTestSetDialogAdd" style="margin-left:20px" isRound="true" title="提交答案"/>
            <CustomButton v-if="isEditingTestAns" @click="handleTestSetDialogEdit" style="margin-left:20px" isRound="true" title="提交修改"/>
          </el-col>
        </el-row>
        
      </span>
    
    </el-dialog>
    <el-dialog
      v-model="testListDialogVisible"
      title="设置题目答案"
      width="50%"
      height="80%"
    >
      <span class="header-title" style="margin: auto,auto,auto,20px;">请设置题目答案</span>
      <el-table
        :data="testList"
        height="500"
        :style="table"
        class="customer-table">
        <el-table-column
          prop="index"
          label="测试卷号"
          width="100">
        </el-table-column>
        <el-table-column
          prop="materialIndex"
          label="测试文件号"
          width="100">
        </el-table-column>
        <el-table-column
          prop="materialNames"
          label="测试文件名"
          width="300">
        </el-table-column>
        <!-- <el-table-column
          prop="questionDescription"
          label="题干"
          width="150">
        </el-table-column>
        <el-table-column
          prop="questionAns"
          label="答案"
          width="200">
          <template v-slot="scope">
            <div v-if="scope.row.index == currentTestSetDialogList">
              <el-input v-model="scope.row.questionAns" placeholder="请输入注释内容"/>
            </div>
            <div v-else>{{ (scope.row.questionAns) }}</div>
          </template>
        </el-table-column> -->
        
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
                  <el-dropdown-item icon="el-icon-remove" @click="editQAA(scope.row, scope.$index)">编辑</el-dropdown-item>
                  <el-dropdown-item icon="el-icon-download" @click="deleteQAA(scope.row, scope.$index)">删除</el-dropdown-item>
                </el-dropdown-menu>
              </template>
              
            </el-dropdown>
          </template>
        </el-table-column>
        <!-- <el-table-column
          prop=""
          label="删除"
          width="">
          <span class="iconfont icon-menu"></span>
        </el-table-column> -->
      </el-table>
      <span class="dialog-footer">
        <el-row style="height: 50px;">
          <el-col :span="20">
          </el-col>
          <el-col :span="4">
            <CustomButton @click="testListDialogVisible = false" style="margin-left:20px" isRound="true" title="确定"/>
          </el-col>
        </el-row>
        
      </span>
    
    </el-dialog>
  </el-main>
</template>

<script>
import axios from "axios";
import CustomButton from './CustomButton.vue';
export default {
  name: 'MaterialUpload',
  components: {
    CustomButton
  },
  props: {
    username:String,
    questionList:Array,
  },
  data(){
    return {
      progress:0,
      idRef:['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
      fileList:[],
      listList:[],
      fullList:[],
      testList:[],
      page:1,
      pageSize:10,
      pagerCount:1,
      currentTime:'',
      listNum:0,
      currentList:0,
      testSetDialogVisible:0,
      testListDialogVisible:0,
      currentSelectedMaterialIndex:0,
      // currentSelectedMaterialName:'',
      currentTestAnsList:[],
      currentTestSetDialogList:0,
      isEditingTestAns:0,
    }
  },
  methods:{

    // clickAddOption(){
    //   var tempOption = {}
    //   var len = this.optionList.length
    //   if(len < 26){
    //     tempOption['index'] = len
    //     tempOption['name'] = this.idRef[len]
    //     tempOption['content'] = ''
    //     this.optionList.push(tempOption)
    //     console.log(this.optionList)
    //   }
      
    // },
    dateFtt(fmt, date) { //author: meizz
    var o = {
        "M+": date.getMonth() + 1,     //月份
        "d+": date.getDate(),     //日
        "h+": date.getHours(),     //小时
        "m+": date.getMinutes(),     //分
        "s+": date.getSeconds(),     //秒
        "q+": Math.floor((date.getMonth() + 3) / 3), //季度
        "S": date.getMilliseconds()    //毫秒
    };
    if (/(y+)/.test(fmt))
        fmt = fmt.replace(RegExp.$1, (date.getFullYear() + "").substr(4 - RegExp.$1.length));
    for (var k in o)
        if (new RegExp("(" + k + ")").test(fmt))
            fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
    return fmt;
    },
    handleChangeUpload(option){
      var file = option.file
      let fileTypeList = file.name.split('.')
      let fileType = fileTypeList[fileTypeList.length - 1]
      //校验文件格式
      if (fileType !== 'zip') {
          this.$message.error('文件格式错误，仅支持.zip');
          return false
      }
      let fileSize = file.size
      //限制文件大小
      if (fileSize > 4 * 1024 * 1024 * 1024) {
        this.$message.error('上传文件大小不超过4G')
        return false
      }
      var time = new Date();
      this.currentTime = this.dateFtt("yyyyMMddhhmmss",time)
      this.progress = 0;
      this.uploadFile(file, 0)

    },
    httpRequest(option) {
    //获取文件对象
      var file = option.file
      console.info("files is ",file);
      console.info("files is " + JSON.stringify(file));
      console.info("filesName is " + JSON.stringify(file.name));
      this.handleChangeUpload(file)
    },
    async uploadFile(file, shardIndex, createTime, savePath){
      // 文件名
      let name = file.name
      // 文件大小
      let size = file.size
      // 分片大小
      let shardSize = 1024 * 1024 * 1
      // 分片总数
      let shardTotal = Math.ceil(size / shardSize)
      if (shardIndex >= shardTotal) {
          this.progress = 100
          return
      }
      // 文件开始结束的位置
      let start = shardIndex * shardSize
      let end = Math.min(start + shardSize, size)
      // 开始切割
      
      let packet = file.slice(start, end)
      console.log("生成块", file)
      console.log("生成块",start,end, packet)
      let formData = new FormData()
      
      formData.append("file", packet)
      formData.append("fileName", name)
      formData.append("size", size)
      formData.append("shardIndex", shardIndex)
      formData.append("shardSize", shardSize)
      formData.append("shardTotal", shardTotal)
      formData.append("currentTime", this.currentTime)
      // formData.append("username",this.username)
      formData.append("username","tempName")

      let fileTypeList = file.name.split('.')
      let fileType = fileTypeList[fileTypeList.length - 1]
      formData.append("fileType",fileType)
      // 下面这些值是后端组装切片时需要的，跟前端关系不大
      if (createTime) formData.append("createTime", createTime)
      if (savePath) formData.append("savePath", savePath)
      if (shardIndex < shardTotal) {
          // 进度条保留两位小数展示
          this.progress = ((shardIndex / shardTotal) * 100).toFixed(2) * 1
          console.log("当前进度", this.progress)
          console.log("开始上传", formData)
          axios({
                  method:"Post",
                  url:'http://localhost:8000/get_material_zip/',
                  headers: {
                  //请求头这个一定要写
                    'Content-Type': 'multipart/form-data',
                  },
                  data:formData
                })
          .then(res => {
            console.log("成功上传块："+shardIndex,res)
            console.log(res.code)
            if (res.status !== 200) {
              this.$message.error(res.msg)
              this.progress = 0
              return
            }
            if (res.data['status'] == 'done') {
                // 这里为所有切片上传成功后进行的操作
                console.log("已成功上传",res.data['list'])

                this.fullList = []
                this.listList = []
                this.fileList = []

                this.fullList = res.data['fullList']
                this.listList = res.data['listList']
                this.fileList = this.fullList[0]
                
                console.log("this.fullList",this.fullList)
                console.log("this.listList.",this.listList)
                console.log("this.fileList.",this.fileList)
                if(this.fullList.length == 0 || this.listList.length == 0){
                  this.$message({
                    message: '您上传的压缩包里没有有效文件！',
                    type: 'error'
                  });
                  this.fileList = []
                  this.progress = 0
                  return
                }
                let tempLen = this.fileList.length
                for(var subList of this.fullList){
                  console.log("subList",subList)
                  if(subList.length !== tempLen){
                    this.$message({
                      message: '您的题表中题目不相等！',
                      type: 'error'
                    });
                    this.fileList = []
                    this.progress = 0
                    return
                  }
                }
                this.listNum = this.listList.length
                this.pagerCount = Math.trunc(this.fileList.length / this.pageSize)
            }
            shardIndex++
            this.uploadFile(file, shardIndex, res.data.createTime, res.data.savePath, res.data.relativePath, res.data.timeMillis)
          })

      }
    },
    
    handleCurrentChange(val) {
      this.page = val
    },
    handleSizeChange(val) {
      this.pageSize = val
    },
    rowClick(row,column){
      this.fileList = this.fullList[row.index - 1]
      if(column.label == "注释"){
        
        this.currentList = row.index
        console.log(row,column)
      }
      // else if(column.label == "删除"){//删除特定行的内容
      //   var deleteTarget = row.index
      //   console.log(deleteTarget)
      //   this.optionList.forEach(function (item,index,arr){
      //       if (item.index == deleteTarget) {
      //           arr.splice(index,1);
      //       }
      //   });
      //   for(let i = 0; i<this.optionList.length;i++){
      //     this.optionList[i]['index'] = i
      //     this.optionList[i]['name'] = this.idRef[i]
      //   }
      //   console.log(row,column)
      // }
    },
    // beforeUpload(file, fileList){
      
    // }
    setTest(row, index) {
      //转换为实际index
      index = this.pageSize * (this.page - 1) + index
      this.currentSelectedMaterialIndex = index
      this.isEditingTestAns = false
      console.log(this.questionList)
      //深复制数组
      this.currentTestAnsList = JSON.parse(JSON.stringify(this.questionList))
      for(var item of this.testList){
        if(item['materialIndex'] == index + 1){
          this.currentTestAnsList = item['questionsAndAns']
          this.isEditingTestAns = true
          this.$message({
            message: '该题目已经存在，下面将进行修改',
            type: 'warning'
          });
        }
      }
      this.testSetDialogVisible = true
      
    },
    rowClickTestSetDialog(row,column){
      if(column.label == "答案"){
        this.currentTestSetDialogList = row.index
        console.log(row,column)
      }
    },
    handleTestSetDialogAdd(){
      let length = this.testList.length
      let tempNames = ''
      for(var item of this.fullList){
        tempNames += item[this.currentSelectedMaterialIndex]['fileName']
        tempNames += '\n'
      }
      tempNames = tempNames.substring(0,tempNames.length - 1)
      this.testList.push({'index': length + 1, 
      'materialIndex': this.currentSelectedMaterialIndex + 1, 
      'materialNames': tempNames, 
      'questionsAndAns': this.currentTestAnsList})
      this.testSetDialogVisible = false
      this.$message({
        message: '添加测试卷成功',
        type: 'success'
      });
    },
    handleTestSetDialogEdit(){
      this.testSetDialogVisible = false
      this.$message({
        message: '修改测试卷成功',
        type: 'success'
      });
    },
    editQAA(row, index){
      this.currentTestAnsList = this.testList[index]['questionsAndAns']
      this.testSetDialogVisible = true
      this.isEditingTestAns = true
    },
    deleteQAA(row, index){
      var deleteTarget = index + 1
      console.log(deleteTarget)
      this.testList.forEach(function (item,index,arr){
          if (item.index == deleteTarget) {
              arr.splice(index,1);
          }
      });
      for(let i = 0; i<this.testList.length;i++){
        this.testList[i]['index'] = i + 1
      }
      this.$message({
        message: '删除测试卷成功',
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
  .el-table .cell {
    white-space: pre-wrap;   /*这是重点。文本换行*/
  }
</style>