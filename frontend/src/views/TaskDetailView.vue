<template>
<el-container class="container">
    <el-header class="header-style">
        <NavBar :login="false" activeItem="1"></NavBar>
    </el-header>
    <el-main>
    <div class="main-box">
        <el-row style="height: 50px;">
            <span class="header-title">基本信息</span>
        </el-row>
        <el-row>
            <el-col :span="16">
                <el-row style="height: 550px;">
                  <div class="pic-box"></div>
                </el-row>
                <el-row style="height: 80px;">
                  <el-col :span="4">
                  <div class="progress-title" style="padding-top:10px;">
                    <span style="text-align: center;font-size:20px;">任务进度：</span>
                  </div>
                  </el-col>
                  <el-col :span="16">
                  <div class="progress-bar">
                    <el-col :span="8">
                      <div style="padding-top:10px;">
                        <span style="color:yellow; text-align: center;font-size:20px;">400</span>
                        <span style="text-align: center;font-size:20px;">/500</span>
                      </div>
                    </el-col>
                    <el-col :span="25">
                      <div class="progrss">
                      <el-progress class="level-progress" :text-inside="true" :stroke-width="25" :percentage="80" color="#fbe484" status="warning"/>
                      </div>
                    </el-col>
                  </div>
                  </el-col>
                </el-row>
            </el-col>
            <el-col :span="8" style="border-left: 4px solid #999999;">
                <el-row style="height: 50px;">发布者信息</el-row>
                <el-row>
                  <el-avatar :src="require('@/assets/images/avatar.jpeg')" class="avatar"></el-avatar>
                  <span class="user-area">
                  <span class="user-center" @click="clickUser">个人中心</span>
                  </span>
                </el-row>
            </el-col>
        </el-row>
        <el-row>
          <el-col :span="8">
            <el-form :model="form" label-width="100px" class="change-form">
              <el-row style="height: 50px;">
                <el-form-item label="名称" :required="true">
                <el-input v-model="taskName" placeholder="名称" :disabled="true"/>
                </el-form-item>
              </el-row>
              <el-row style="height: 50px;">
                <el-form-item label="题型" :required="true">
                <el-input v-model="questionType" placeholder="题型" :disabled="true"/>
                </el-form-item>
              </el-row>
              <el-row style="height: 50px;">
                <el-form-item label="分类" :required="true">
                <el-input v-model="materialType" placeholder="分类" :disabled="true"/>
                </el-form-item>
              </el-row>
              <el-row style="height: 50px;">
                <el-form-item label="等级" :required="true">
                <el-input v-model="starRank" placeholder="等级" :disabled="true"/>
                </el-form-item>
              </el-row>
            </el-form>
          </el-col>
          <el-col :span="8">
            <el-form :model="form" label-width="100px" class="change-form">
              <el-row style="height: 50px;">
                <el-form-item label="题目数量" :required="true">
                <el-input v-model="problemTotalNum" placeholder="题目数量" :disabled="true"/>
                </el-form-item>
              </el-row>
              <el-row style="height: 50px;">
                <el-form-item label="奖励额度" :required="true">
                <el-input v-model="singleBonus" placeholder="奖励额度" :disabled="true"/>
                </el-form-item>
              </el-row>
              <el-row style="height: 50px;">
                <el-form-item label="任务描述" :required="true">
                <el-input
                  v-model="description"
                :rows="3"
                type="textarea"
                placeholder="任务描述"
                :disabled="true"
                resize="none"
                style="width: 300px;"
                />
              </el-form-item>
              </el-row>
            </el-form>
          </el-col>
          <el-col :span="8"></el-col>
        </el-row>
        <el-row>
          <el-col :span="5"><CustomButton title="领取并开始" :props="normalProps" @click="handleChangePhone" isRound="true"></CustomButton></el-col>
          <el-col :span="5"><CustomButton title="领取至列表" :props="confirmProps" @click="handleChangePhone" isRound="true"></CustomButton></el-col>
          <el-col :span="5"><CustomButton title="取消" :props="normalProps" @click="handleChangePhone" isRound="true"></CustomButton></el-col>
          <el-col :span="8"></el-col>
        </el-row>
    </div>
    </el-main>
</el-container>
</template>


<script>
  // @ is an alias to /src
  import axios from "axios";
  import NavBar from "@/components/NavBar.vue";
  import CustomButton from "@/components/CustomButton.vue";
  export default {
    name: 'HelpView',
    components: {
      NavBar,
      CustomButton,
    },
    data(){
      return{
        taskName: "",
        description: "",
        questionType: "",
        problemTotalNum: "",
        starRank: "",
        singleBonus: "",
        materialType: "",
    }
  },
  mounted() {
    //
      axios
        .get("/get_task_basic_info", {
          params: {
          },
        })
        .then((res) => {
          this.taskName = "taskName";
          if (res.data["status"] === "ok") {
            this.taskName = res.data["taskName"];
            this.questionType = res.data["questionType"];
            this.description = res.data["description"];
            this.problemTotalNum = res.data["problemTotalNum"];
            this.singleBonus = res.data["singleBonus"];
            this.starRank = res.data["starRank"];
            this.materialType = res.data["materialType"];
            //const imageFile = this.base64ImgtoFile(
            //  "data:image/png;base64," + res.data["avatarImage"]
            //);
            //this.image.src =
            //  window.webkitURL.createObjectURL(imageFile) ||
            //  window.URL.createObjectURL(imageFile);
            //this.$emit("initAvatar", this.image.src);
          }
        })
        .catch((err) => {
          console.log(err);
        });

  },
  }
</script>

<style scoped>
  .container {
    margin:0;
    height:100%;
  }
  .header-style {
    background-image: url(@/assets/images/nav-background.png);
    background-size: cover;
    height: 60px;
    box-shadow: 0 0px 8px 0;
    display: flex;
  }
  .main-box{
    width:80%;
    margin-left: 10%;
  }
  .pic-box {
  width: 610px;
  height: 400px;
  text-align: center;
  background: url(../assets/images/pet1.jpeg);
  background-size: 100% 100%;
  margin:0 auto;
  margin-bottom: 20px;
  margin-top: 40px;
  border: 30px solid #efefef; 
  border-radius:25px;
}
  .progress-bar{
  width:100%;
  height:40px;
  display:flex;
  background-color: #efefef; 
  border-radius:25px;
  text-align:center;
  }
  .progress-title{
    height:40px;
  }
.level-progress {
  width: 300px;
  margin: 8px 10px 8px 10px;
}
:deep .el-progress-bar__outer{
  background-color:#5EABBF;
}
:deep .el-progress-bar__inner{
  top: 10%;
  left:2%;
  height:80%;
}  
.user-center {
    line-height: 60px;
    margin-bottom: 20px;
    font-size: 26px;
    color:#5EABBF;
    font-family: YouSheBlack;
    cursor: pointer;
  }
  .user-center:hover {
    opacity: 0.6;
  }
</style>