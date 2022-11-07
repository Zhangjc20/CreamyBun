<template>
  <el-main class="main-style" >
    <el-row style="height: 50px;">
      <span class="header-title" style="margin: auto,auto,auto,20px;">请上传任务素材</span>
      <CustomButton @click="clickEdit" isRound="true" style="float: right; right: 20px; position: absolute" title="提交修改" v-if="false"/>
    </el-row>
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
        width="120">
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
    <el-pagination
      :page-sizes="[10, 15, 20, 25]"
      :small="small"
      :disabled="disabled"
      :background="background"
      layout="sizes, prev, pager, next, jumper"
      :total="fileList.length"
      :pager-count="pagerCount"
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
  },
  data(){
    return {
      progress:0,
      idRef:['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
      fileList:[],
      page:1,
      pageSize:10,
      pagerCount:1,
      currentTime:'',
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
                this.fileList = []
                this.fileList = res.data['list']
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

    // beforeUpload(file, fileList){
      
    // }
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