<template>
  <el-main class="main-style">
    <el-row style="height: 50px;">
      <span class="header-title" style="margin: auto,auto,auto,20px;">请上传任务素材</span>
      <CustomButton @click="testListDialogVisible = true" isRound="true"
        style="float: right; right: 20px; position: absolute" v-if="!newOrEdit" title="编辑资质测试列表" />
      <el-popover placement="top" title="上传提示" :width="200" trigger="click"
        content="上传时，请您将每一组相同类型的素材放置于一个文件夹中，将几个文件夹在同级目录下直接压缩至一个zip包，系统会自动根据您的输入生成多个素材列表~">
        <template #reference>
          <el-button circle style="float: left; left: 130px;top: -5px; position: absolute">
            <span class="iconfont icon-question"></span>
          </el-button>
        </template>
      </el-popover>
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
      <el-upload class="upload-demo" multiple="false" action="api" drag :show-file-list="false"
        :http-request="handleChangeUpload">
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">点击上传</div>
        <div class="el-upload__tip">
          请上传压缩包
        </div>
      </el-upload>
      <el-progress :percentage="progress" :stroke-width="10" style="margin: 10px 10px 10px 10px" color="#5EABBF" />
      <el-table :data="listList" height="150" :style="table" @row-click="rowClick" class="customer-table">
        <el-table-column prop="index" label="序号" width="60">
        </el-table-column>
        <el-table-column prop="listLen" label="素材数" width="60">
        </el-table-column>
        <el-table-column prop="listName" label="表名" width="100">
        </el-table-column>
        <el-table-column prop="notes" label="注释" width="200">
          <template v-slot="scope">
            <div v-if="scope.row.index == currentEditingSubList">
              <el-input v-model="scope.row.notes" placeholder="请输入注释内容" />
            </div>
            <div v-else>{{ (scope.row.notes) }}</div>
          </template>
        </el-table-column>

        <el-table-column prop="" label="" width="">
        </el-table-column>

        <!-- <el-table-column
          prop=""
          label="删除"
          width="">
          <span class="iconfont icon-menu"></span>
        </el-table-column> -->
      </el-table>
      <el-row v-if="listList.length" style="height: 40px;">
        <span class="header-title" style="padding:10px">当前素材列表：{{ currentShowingName }}</span>
      </el-row>
      <el-table :data="showingList" height="500" :style="table" ref="materialShowingTable" @select="handleMaterial"
        @select-all="handleMaterial" class="customer-table">
        <el-table-column v-if="isSelectingMaterial" type="selection" width="50">
        </el-table-column>
        <el-table-column prop="index" label="卷号" width="60">
        </el-table-column>
        <el-table-column prop="fileName" label="文件名" width="180">
        </el-table-column>
        <el-table-column prop="fileSize" label="大小" width="100">
        </el-table-column>
        <!-- <el-table-column
          prop="fileType"
          label="类型"
          width="100">
        </el-table-column> -->



        <el-table-column prop="" label="操作" width="60">
          <template v-slot="scope">
            <el-dropdown>
              <span class="iconfont icon-menu"></span>
              <template #dropdown>
                <el-dropdown-menu>
                  <el-dropdown-item icon="el-icon-s-order"
                    @click="setTest(scope.row, scope.$index)">设置为测试题</el-dropdown-item>
                  <el-dropdown-item v-if="!isSelectingMaterial" icon="el-icon-s-order"
                    @click="isSelectingMaterial = true">多选</el-dropdown-item>
                  <el-dropdown-item v-if="!isSelectingMaterial" icon="el-icon-s-order"
                    @click="deleteMaterialSingle(scope.row, scope.$index); isSelectingMaterial = false;">删除</el-dropdown-item>
                  <el-dropdown-item v-if="!isSelectingMaterial && !isMovingMaterial" icon="el-icon-s-order"
                    @click="isMovingMaterial = true; movingMaterialIndex = getActualIndex(scope.$index)">移动</el-dropdown-item>
                  <!--                   
                  <el-input v-if="isMovingMaterial" 
                    @input="onInput()"
                    style="padding = 5px" 
                    v-model="movingMaterialTarget" 
                    placeholder="请输入目标位置"
                  /> -->
                  <!-- <el-form class="change-form">
                    <el-form-item label="任务描述" :required="true">
                      <el-input v-if="isMovingMaterial" 
                        style="padding = 5px" 
                        v-model="movingMaterialTarget" 
                        placeholder="请输入目标位置"
                      />               
                    </el-form-item>
                  </el-form> -->

                  <!-- <el-dropdown-item v-if="isMovingMaterial" icon="el-icon-s-order" @click="moveMaterial(scope.$index);isMovingMaterial = false;">
                    确认移位
                  </el-dropdown-item>
   -->

                  <el-dropdown-item v-if="isSelectingMaterial" icon="el-icon-s-order"
                    @click="initSelected(); updateShowingList(); isSelectingMaterial = false;">取消多选</el-dropdown-item>
                  <el-dropdown-item v-if="isSelectingMaterial" icon="el-icon-s-order"
                    @click="deleteMaterialMultiple(scope.row, scope.$index); isSelectingMaterial = false;">删除多个</el-dropdown-item>

                  <!-- <el-dropdown-item icon="el-icon-remove" @click="moveQuestionDown(scope.row, scope.$index)">下移</el-dropdown-item>
                  <el-dropdown-item icon="el-icon-remove" @click="editQuestion(scope.row, scope.$index)">编辑</el-dropdown-item>
                  <el-dropdown-item icon="el-icon-download" @click="deleteQuestion(scope.row, scope.$index)">删除</el-dropdown-item> -->
                </el-dropdown-menu>
              </template>

            </el-dropdown>
          </template>
        </el-table-column>
        <el-table-column prop="" label="" width="">
        </el-table-column>
      </el-table>
      <el-pagination :page-sizes="[10, 15, 20, 25]" :small="small" :disabled="disabled" :background="background"
        layout="sizes, prev, pager, next, jumper" :total="fileList.length" :pager-count="3"
        @size-change="handleSizeChange" @current-change="handleCurrentChange" />
    </template>
    <el-dialog v-model="isMovingMaterial" title="设置移动位置" width="20%">
      <el-row style="height: 50px;">
        <span class="header-title" style="margin: auto,auto,auto,20px;">当前被移动卷号：{{ movingMaterialIndex }}</span>
      </el-row>
      <el-form class="change-form">
        <el-form-item label="目标位置" :required="true">
          <el-input v-model="movingMaterialTarget" placeholder="请输入目标位置" @input="onInput()" />
        </el-form-item>
      </el-form>
      <span class="dialog-footer">
        <CustomButton @click="moveMaterial(movingMaterialIndex)" width="100px" style="margin-left:20px" isRound="true"
          title="移位" />
        <CustomButton @click="exchangeMaterial(movingMaterialIndex)" width="100px" style="margin-left:20px"
          isRound="true" title="交换" />
      </span>
    </el-dialog>
    <el-dialog v-model="testSetDialogVisible" title="设置题目答案" width="50%" height="80%">
      <span class="header-title" style="margin: auto,auto,auto,20px;">请设置题目答案</span>
      <el-table :data="currentTestAnsList" height="500" :style="table" @row-click="rowClickTestSetDialog"
        class="customer-table">
        <el-table-column prop="index" label="题号" width="60">
        </el-table-column>
        <el-table-column prop="questionTypeName" label="题型" width="60">
        </el-table-column>
        <el-table-column prop="questionDescription" label="题干" width="150">
        </el-table-column>
        <el-table-column prop="questionAns" label="答案" width="200">
          <template v-slot="scope">
            <div v-if="scope.row.index == currentTestSetDialogList">
              <el-input v-model="scope.row.questionAns" placeholder="请输入注释内容" />
            </div>
            <div v-else>{{ (scope.row.questionAns) }}</div>
          </template>
        </el-table-column>

        <el-table-column prop="" label="" width="">
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
            <CustomButton @click="testSetDialogVisible = false" style="margin-right:20px" isRound="true" title="取消提交" />
          </el-col>
          <el-col :span="12">
            <CustomButton v-if="!isEditingTestAns" @click="handleTestSetDialogAdd" style="margin-left:20px"
              isRound="true" title="提交答案" />
            <CustomButton v-if="isEditingTestAns" @click="handleTestSetDialogEdit" style="margin-left:20px"
              isRound="true" title="提交修改" />
          </el-col>
        </el-row>

      </span>

    </el-dialog>
    <el-dialog v-model="testListDialogVisible" title="设置题目答案" width="50%" height="80%">
      <span class="header-title" style="margin: auto,auto,auto,20px;">请设置题目答案</span>
      <el-table :data="testList" height="500" :style="table" class="customer-table">
        <el-table-column prop="index" label="测试卷号" width="100">
        </el-table-column>
        <el-table-column prop="materialIndex" label="测试文件号" width="100">
        </el-table-column>
        <el-table-column prop="materialNames" label="测试文件名" width="300">
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

        <el-table-column prop="" label="" width="">
        </el-table-column>
        <el-table-column prop="" label="操作" width="60">
          <template v-slot="scope">
            <el-dropdown>
              <span class="iconfont icon-menu"></span>
              <template #dropdown>
                <el-dropdown-menu>
                  <el-dropdown-item icon="el-icon-remove"
                    @click="editQAA(scope.row, scope.$index)">编辑</el-dropdown-item>
                  <el-dropdown-item icon="el-icon-download"
                    @click="deleteQAA(scope.row, scope.$index)">删除</el-dropdown-item>
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
            <CustomButton @click="testListDialogVisible = false" style="margin-left:20px" isRound="true" title="确定" />
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
    username: String,
    questionList: Array,
    materialType: Number,
  },
  watch: {
    materialType(newVal) {
      this.localMaterialType = newVal
    },
  },
  data() {
    return {
      localMaterialType: 0,
      progress: 0,
      idRef: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
      fileList: [],
      showingList: [],
      listList: [],
      fullList: [],
      testList: [],
      handleMaterialList: [],
      page: 1,
      pageSize: 10,
      pagerCount: 1,
      currentTime: '',
      listNum: 0,
      currentShowingSubList: 0,
      currentEditingSubList: 0,
      testSetDialogVisible: 0,
      testListDialogVisible: 0,
      currentSelectedMaterialIndex: 0,
      currentShowingName: '',
      // currentSelectedMaterialName:'',
      currentTestAnsList: [],
      currentTestSetDialogList: 0,
      isEditingTestAns: 0,
      isSelectingMaterial: 0,

      isMovingMaterial: 0,
      movingMaterialTarget: '',
      movingMaterialIndex: 0,
    }
  },
  methods: {

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
    onInput() {
      this.$forceUpdate();
    },
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
    handleChangeUpload(option) {
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
      this.currentTime = this.dateFtt("yyyyMMddhhmmss", time)
      this.progress = 0;
      this.uploadFile(file, 0)

    },
    httpRequest(option) {
      //获取文件对象
      var file = option.file
      console.info("files is ", file);
      console.info("files is " + JSON.stringify(file));
      console.info("filesName is " + JSON.stringify(file.name));
      this.handleChangeUpload(file)
    },
    async uploadFile(file, shardIndex, createTime, savePath) {
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
      console.log("生成块", start, end, packet)
      let formData = new FormData()

      console.log("我是个jb", packet)
      formData.append("file", packet)
      formData.append("fileName", name)
      formData.append("size", size)
      formData.append("shardIndex", shardIndex)
      formData.append("shardSize", shardSize)
      formData.append("shardTotal", shardTotal)
      formData.append("materialType", this.localMaterialType)

      console.log("shardTotal", shardTotal)

      formData.append("currentTime", this.currentTime)
      formData.append("username", this.username)

      let fileTypeList = file.name.split('.')
      let fileType = fileTypeList[fileTypeList.length - 1]
      formData.append("fileType", fileType)
      // 下面这些值是后端组装切片时需要的，跟前端关系不大
      if (createTime) formData.append("createTime", createTime)
      if (savePath) formData.append("savePath", savePath)
      if (shardIndex < shardTotal) {
        // 进度条保留两位小数展示
        this.progress = ((shardIndex / shardTotal) * 100).toFixed(2) * 1
        console.log("当前进度", this.progress)
        console.log("开始上传", formData)
        axios({
          method: "Post",
          url: 'http://101.42.118.80:8000/get_material_zip/',
          headers: {
            //请求头这个一定要写
            'Content-Type': 'multipart/form-data',
          },
          data: formData
        })
          .then(res => {
            console.log("成功上传块：" + shardIndex, res)
            console.log(res.code)
            if (res.status !== 200) {
              this.$message.error(res.msg)
              this.progress = 0
              return
            }
            if (res.data['status'] == 'done') {
              // 这里为所有切片上传成功后进行的操作
              console.log("已成功上传", res.data['list'])

              this.fullList = []
              this.listList = []
              this.fileList = []
              this.showingList = []
              this.testList = []
              this.handleMaterialList = []
              console.log("jcggcw", this.listList)
              this.fullList = res.data['fullList']
              this.listList = res.data['listList']
              if (this.fullList.length == 0 || this.listList.length == 0) {
                this.$message({
                  message: '您上传的压缩包里没有有效文件！',
                  type: 'error'
                });
                this.fileList = []
                this.showingList = []
                this.progress = 0
                return
              }
              this.initAllLists()

            }
            shardIndex++
            this.uploadFile(file, shardIndex, res.data.createTime, res.data.savePath, res.data.relativePath, res.data.timeMillis)
          }).catch(error => {
            console.log(error);
            this.$message({
              message: '链接失败',
              type: 'error'
            });
          })

      }
    },
    initAllLists() {
      this.currentShowingName = this.listList[this.currentShowingSubList]['listName']
      this.fileList = this.fullList[0]
      this.updateShowingList()
      console.log("this.fullList", this.fullList)
      console.log("this.listList.", this.listList)
      console.log("this.fileList.", this.fileList)


      let tempHandleList = []
      for (var subList of this.fullList) {
        tempHandleList = []
        let i = 1
        for (var itemMaterial of subList) {//初始化选择串
          itemMaterial['index'] = i//初始化所有fullList的index
          i++
          tempHandleList.push({ 'index': itemMaterial['index'], 'selected': 0 })
        }
        this.handleMaterialList.push(tempHandleList)
        console.log("subList", subList)
      }
      let tempLen = this.fileList.length
      for (var subList of this.fullList) {
        if (subList.length !== tempLen) {
          this.$message({
            message: '您的题表中题目不相等，请注意调整您的题表！',
            type: 'warning'
          });
          break;
        }
      }
      console.log("handleMaterialList", this.handleMaterialList)
      this.listNum = this.listList.length
      this.pagerCount = Math.trunc(this.fileList.length / this.pageSize)
    },
    updateSelect() {//翻页后更新列表
      this.$nextTick(() => {
        let table = this.showingList;
        // console.log(this.handleMaterialList)
        table.forEach(row => {
          // console.log("正在遍历：", row,row['index'] - 1, this.handleMaterialList[this.currentShowingSubList][row['index'] - 1]['selected'])
          if (this.handleMaterialList[this.currentShowingSubList][row['index'] - 1]['selected'] == 1) {
            this.$refs.materialShowingTable.toggleRowSelection(row, true);
            //这一行不管用！！！！！
            // console.log("更新了一个！", row, this.handleMaterialList[this.currentShowingSubList][row['index'] - 1]['selected'])
          }
        });
      })

    },
    handleCurrentChange(val) {
      this.page = val
      this.updateShowingList()
      this.updateSelect()
    },
    handleSizeChange(val) {
      this.pageSize = val
      this.updateShowingList()
      this.updateSelect()
    },
    updateShowingList() {
      this.showingList = this.fileList.slice((this.page - 1) * this.pageSize, this.page * this.pageSize)
    },
    rowClick(row, column) {
      console.log("showingList", this.showingList)
      this.currentShowingSubList = row.index - 1
      this.fileList = this.fullList[this.currentShowingSubList]
      this.currentShowingName = this.listList[this.currentShowingSubList]['listName']
      this.updateShowingList()
      this.updateSelect()
      if (column.label == "注释") {
        this.currentEditingSubList = row.index
        console.log(row, column)
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
      index = this.getActualIndex(index)
      this.currentSelectedMaterialIndex = index
      this.isEditingTestAns = false
      console.log(this.questionList)
      //深复制数组
      this.currentTestAnsList = JSON.parse(JSON.stringify(this.questionList))
      if (this.currentTestAnsList.length === 0) {
        this.$message({
          message: '您的题目列表为空，请先在左侧题目栏添加题目！',
          type: 'error'
        });
        return
      }
      for (var item of this.testList) {
        if (item['materialIndex'] == index + 1) {
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
    rowClickTestSetDialog(row, column) {
      if (column.label == "答案") {
        this.currentTestSetDialogList = row.index
        console.log(row, column)
      }
    },
    strSort(line) {
      let s = line.split("");
      let box = [];
      //symbols数组非字母：每一项元素是数组，由索引和索引所在的数据组成
      for (let i = 0; i < 256; i++) {
        box[i] = "";
      }
      //box数组收集26个数据：每一个数据是字母或字母大小写的组合串或空串（初始化没有值）
      for (let i = 0; i < s.length; i++) {
        let code = s[i].charCodeAt();
        box[code] += s[i];
      }

      let res = "";
      box.forEach(item => {
        res += item;
      })
      return res
    },
    handleTestSetDialogAdd() {
      for (var i = 0; i < this.questionList.length; i++) {
        var tempAns = this.currentTestAnsList[i]['questionAns']
        if (this.currentTestAnsList[i]['questionType'] == 3) {//框图题跳过
          continue;
        }
        if (tempAns.length < this.currentTestAnsList[i]['minOptionNum']) {
          if(tempAns.length == 0 && !this.currentTestAnsList[i]['mustDo']){
            continue
          }
          this.$message({
            message: '您第' + (i + 1) + '题提供的答案过短',
            type: 'error'
          });
          return
        }
        if (tempAns.length > this.currentTestAnsList[i]['maxOptionNum']) {
          this.$message({
            message: '您第' + (i + 1) + '题提供的答案过长',
            type: 'error'
          });
          return
        }
        if (this.currentTestAnsList[i]['questionType'] == 0 || this.currentTestAnsList[i]['questionType'] == 1) {//如果是填空题
          if(tempAns.length == 0){
            continue
          }
          this.currentTestAnsList[i]['questionAns'] = this.strSort(this.currentTestAnsList[i]['questionAns'])
          tempAns = this.currentTestAnsList[i]['questionAns']
          console.log("'A'.charCodeAt() + this.currentTestAnsList[i]['optionList'].length - 1",'A'.charCodeAt() + this.currentTestAnsList[i]['optionList'].length - 1,tempAns[tempAns.length - 1].charCodeAt())
          if(tempAns[0].charCodeAt() < 'A'.charCodeAt() || tempAns[tempAns.length - 1].charCodeAt() > 'A'.charCodeAt() + this.currentTestAnsList[i]['optionList'].length - 1){
            this.$message({
              message: '您第' + (i + 1) + '题选择题的答案不合法',
              type: 'error'
            });
            return
          }
          var tempChar = '-'
          for(var j = 0;j<tempAns.length;j++){
            if(tempChar == tempAns[j]){
              this.$message({
                message: '您第' + (i + 1) + '题选择题答案存在重复选项',
                type: 'error'
              });
              return
            }
            tempChar = tempAns[j]
          }
        }
      }
      let length = this.testList.length
      let tempNames = ''
      for (var item of this.fullList) {
        tempNames += item[this.currentSelectedMaterialIndex]['fileName']
        tempNames += '\n'
      }
      tempNames = tempNames.substring(0, tempNames.length - 1)
      this.testList.push({
        'index': length + 1,
        'materialIndex': this.currentSelectedMaterialIndex + 1,
        'materialNames': tempNames,
        'questionsAndAns': this.currentTestAnsList
      })
      this.testSetDialogVisible = false
      this.$message({
        message: '添加测试卷成功',
        type: 'success'
      });
    },
    handleTestSetDialogEdit() {
      this.testSetDialogVisible = false
      this.$message({
        message: '修改测试卷成功',
        type: 'success'
      });
    },
    editQAA(row, index) {
      this.currentTestAnsList = this.testList[index]['questionsAndAns']
      this.testSetDialogVisible = true
      this.isEditingTestAns = true
    },
    deleteQAA(row, index) {
      var deleteTarget = index + 1
      console.log(deleteTarget)
      this.testList.forEach(function (item, index, arr) {
        if (item.index == deleteTarget) {
          arr.splice(index, 1);
        }
      });
      for (let i = 0; i < this.testList.length; i++) {
        this.testList[i]['index'] = i + 1
      }
      this.$message({
        message: '删除测试卷成功',
        type: 'success'
      });
    },
    getActualIndex(index) {
      return this.pageSize * (this.page - 1) + index
    },
    // //处理单个选中
    // handleSelectedMaterial(selection, row){

    //   let index = this.getActualIndex(row.index - 1)
    //   console.log("单个选中！",this.currentShowingSubList,selection, row.index,this.handleMaterialList)
    //   this.handleMaterialList[this.currentShowingSubList][index]['selected'] = selection
    //   console.log("handleMaterialList",this.handleMaterialList)
    // },
    // handleAllMaterial(selection){
    //   //改变所有选中状态
    //   for(var subList of this.handleMaterialList){
    //     for(var item of subList){
    //       item['selected'] = selection
    //     }
    //   }
    //   console.log("handleMaterialList",this.handleMaterialList)
    // },
    initSelected() {
      for (var subList of this.handleMaterialList) {
        for (var item of subList) {
          item['selected'] = 0
        }
      }
    },
    handleMaterial(selection) {
      //改变所有选中状态
      //   updateShowingList(){
      //   this.showingList = this.fileList.slice((this.page - 1) * this.pageSize, this.page * this.pageSize)
      // },
      let tempTable = this.handleMaterialList[this.currentShowingSubList].slice((this.page - 1) * this.pageSize, this.page * this.pageSize)
      for (var item of tempTable) {
        item['selected'] = 0
      }
      for (var item of selection) {
        this.handleMaterialList[this.currentShowingSubList][item['index'] - 1]['selected'] = 1
        console.log("修改了！！！", this.handleMaterialList[this.currentShowingSubList][item['index'] - 1])
      }
      console.log("handleMaterialList", selection, this.handleMaterialList)
    },
    deleteMaterialSingle(row, index) {
      console.log(row, index)
      this.handleMaterialList[this.currentShowingSubList][row['index'] - 1]['selected'] = 1
      this.deleteMaterialMultiple(row, index)
      console.log("handleMaterialList", this.handleMaterialList)
    },
    getActionMsg(act) {
      let msgList = []
      console.log("getActionMsg", this.fullList, act)
      for (let i = 0; i < this.handleMaterialList.length; i++) {
        var subList = this.handleMaterialList[i]
        for (var item of subList) {
          if (item['selected']) {
            let targetIndex = item['index'] - 1
            msgList.push({
              'filePath': this.fullList[i][targetIndex]['filePath']
            })
            if (act === 'delete') {
              this.fullList[i][targetIndex]['index'] = -1
            }
          }
        }
        for (let j = this.fullList[i].length - 1; j >= 0; j--) {
          if (this.fullList[i][j]['index'] < 0) {
            this.fullList[i].splice(j, 1)
            console.log("删除坐标：", i, j)
          }
        }
        for (let j = 0; j < this.fullList[i].length; j++) {
          this.fullList[i][j]['index'] = j + 1
        }
      }
      console.log("刚修改完啦啦啦啦啦啦啦啦啦啦", this.fullList)
      return msgList
    },

    deleteMaterialMultiple(row, index) {
      let act = 'delete'
      console.log(row, index)
      let msgList = this.getActionMsg(act)
      axios.post("http://101.42.118.80:8000/handle_release_action/",
        {
          act: act,
          msgList: msgList,
        }).then(res => {
          if (res.data['status'] == 'done') {
            this.initSelected()
            this.initAllLists()
            this.updateShowingList()
            this.$message({
              message: '操作素材列表成功',
              type: 'success'
            });
          } else {
            this.$message({
              message: '操作素材列表失败',
              type: 'error'
            });
          }
        }).catch(error => {
          console.log(error);
          this.$message({
            message: '链接失败',
            type: 'error'
          });
        })

    },
    moveMaterial(index) {
      if (this.movingMaterialTarget < 1 || this.movingMaterialTarget > this.fullList[this.currentShowingSubList].length) {
        this.$message({
          message: '您输入的目标位置不合法！',
          type: 'error'
        });
        return
      }
      this.movingMaterialTarget--
      console.log("被移动：index", index, "目标：movingMaterialTarget", this.movingMaterialTarget)
      let moveData = this.fullList[this.currentShowingSubList][index]
      this.fullList[this.currentShowingSubList].splice(index, 1);
      this.fullList[this.currentShowingSubList].splice(this.movingMaterialTarget, 0, moveData);
      this.initAllLists()
      this.updateShowingList()
      this.$message({
        message: '移位成功！',
        type: 'success'
      });
      this.movingMaterialTarget = '';
      this.isMovingMaterial = false
    },
    exchangeMaterial(index) {
      if (this.movingMaterialTarget < 1 || this.movingMaterialTarget > this.fullList[this.currentShowingSubList].length) {
        this.$message({
          message: '您输入的目标位置不合法！',
          type: 'error'
        });
        return
      }
      this.movingMaterialTarget--
      console.log("被移动：index", index, "目标：movingMaterialTarget", this.movingMaterialTarget)
      let moveData = this.fullList[this.currentShowingSubList][index]
      let targetData = this.fullList[this.currentShowingSubList][this.movingMaterialTarget]
      this.fullList[this.currentShowingSubList][index] = targetData
      this.fullList[this.currentShowingSubList][this.movingMaterialTarget] = moveData
      this.initAllLists()
      this.updateShowingList()
      this.$message({
        message: '移位成功！',
        type: 'success'
      });
      this.movingMaterialTarget = '';
      this.isMovingMaterial = false
    }
  }
}

</script>

<style scoped>
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
  font-size: 17px;
  font-weight: 700;
}

.main-style {
  padding: 20px 20px 20px 40px;
  border-radius: 5px;
  box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
  margin-left: 40px;
  margin-right: 20px;
}

.el-table .cell {
  white-space: pre-wrap;
  /*这是重点。文本换行*/
}
</style>