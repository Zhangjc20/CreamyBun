<template>
  <el-main class="main-style" >
    <el-row style="height: 50px;">
      <span class="header-title" style="margin: auto,auto,auto,20px;">请上传任务素材</span>
      <CustomButton @click="clickEdit" isRound="true" style="float: right; right: 20px; position: absolute" title="提交修改"/>
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
      <el-progress
        :percentage="progress"
        :indeterminate="true"
      />
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
  data(){
    return {
      progress:0,
      idRef:['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],

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
    handleChangeUpload(option){
      var file = option.file
      let fileTypeList = file.name.split('.')
      let fileType = fileTypeList[fileTypeList.length - 1]
      //校验文件格式
      if (fileType !== 'acow2' 
      && fileType !== 'iso' 
      && fileType !== 'ovf' 
      && fileType !== 'zip' 
      && fileType !== 'tar') {
          this.$message.error('文件格式错误，仅支持.acow2/.iso/.ovf/.zip/.tar');
          return false
      }
      let fileSize = file.size
      //限制文件大小
      if (fileSize > 4 * 1024 * 1024 * 1024) {
        this.$message.error('上传文件大小不超过4G')
        return false
      }
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
            if (res.msg == '上传成功' && res.data.fileName && res.data.filePath) {
                // 这里为所有切片上传成功后进行的操作
            }
            shardIndex++
            this.uploadFile(file, shardIndex, res.data.createTime, res.data.savePath, res.data.relativePath, res.data.timeMillis)
          })

      }
    }

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