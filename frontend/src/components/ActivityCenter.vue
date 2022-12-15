<template>
  <div class="activity-container">
    <div class="clockin-box">
      <span class="clockin-title">天道酬勤 恒者能胜</span>
      <div class="clockin-inner">
        <div class="clockin-content">
          <el-row>
            <el-col :span="15">
              <el-row>
                <el-col :span="8">
                  <div class="little-item-box">
                    <div class="little-inner yellow-bg">
                      <svg class="icon" aria-hidden="true">
                        <use xlink:href="#icon-tiantianquan"></use>
                      </svg>
                      <div class="num-area black-font">×200</div>
                      <div class="white-font green-bg">第一天</div>
                    </div>
                    <div class="little-inner mask-box" v-show="clockinDays>=1">
                      <div class="got-box">
                        已领取
                      </div>
                    </div>
                  </div>
                </el-col>
                <el-col :span="8">
                  <div class="little-item-box">
                    <div class="little-inner green-bg">
                      <svg class="icon" aria-hidden="true">
                        <use xlink:href="#icon-tiantianquan"></use>
                      </svg>
                      <div class="num-area white-font">×200</div>
                      <div class="black-font yellow-bg">第二天</div>
                    </div>
                    <div class="little-inner mask-box" v-show="clockinDays>=2">
                      <div class="got-box">
                        已领取
                      </div>
                    </div>
                  </div>
                </el-col>
                <el-col :span="8">
                  <div class="little-item-box">
                    <div class="little-inner yellow-bg">
                      <svg class="icon" aria-hidden="true">
                        <use xlink:href="#icon-tiantianquan"></use>
                      </svg>
                      <div class="num-area black-font">×200</div>
                      <div class="white-font green-bg">第三天</div>
                    </div>
                    <div class="little-inner mask-box" v-show="clockinDays>=3">
                      <div class="got-box">
                        已领取
                      </div>
                    </div>
                  </div>
                </el-col>
              </el-row>
              <el-row>
                <el-col :span="8">
                  <div class="little-item-box">
                    <div class="little-inner green-bg">
                      <svg class="icon" aria-hidden="true">
                        <use xlink:href="#icon-tiantianquan"></use>
                      </svg>
                      <div class="num-area white-font">×200</div>
                      <div class="black-font yellow-bg">第四天</div>
                    </div>
                    <div class="little-inner mask-box" v-show="clockinDays>=4">
                      <div class="got-box">
                        已领取
                      </div>
                    </div>
                  </div>
                </el-col>
                <el-col :span="8">
                  <div class="little-item-box">
                    <div class="little-inner yellow-bg">
                      <svg class="icon" aria-hidden="true">
                        <use xlink:href="#icon-tiantianquan"></use>
                      </svg>
                      <div class="num-area black-font">×200</div>
                      <div class="white-font green-bg">第五天</div>
                    </div>
                    <div class="little-inner mask-box" v-show="clockinDays>=5">
                      <div class="got-box">
                        已领取
                      </div>
                    </div>
                  </div>
                </el-col>
                <el-col :span="8">
                  <div class="little-item-box">
                    <div class="little-inner green-bg">
                      <svg class="icon" aria-hidden="true">
                        <use xlink:href="#icon-tiantianquan"></use>
                      </svg>
                      <div class="num-area white-font">×200</div>
                      <div class="black-font yellow-bg">第六天</div>
                    </div>
                    <div class="little-inner mask-box" v-show="clockinDays>=6">
                      <div class="got-box">
                        已领取
                      </div>
                    </div>
                  </div>
                </el-col>
              </el-row>
            </el-col>
            <el-col :span="9">
              <div class="large-item-box">
                <div class="large-inner">
                  <svg class="icon large-icon" aria-hidden="true">
                    <use xlink:href="#icon-tiantianquan"></use>
                  </svg>
                  <div class="num-area large-num">×200</div>
                  <div class="day-large-font green-bg">第七天</div>
                </div>
                <div class="large-inner mask-box large-mask-params" v-show="clockinDays>=7">
                  <div class="got-box large-got-params">
                    已领取
                  </div>
                </div>
              </div>
            </el-col>
          </el-row>
        </div>
      </div>
    </div>
    <div>
        <CustomButton :title="clocked?'已签到':'签到'" fontSize="18px" width="100px" @click="handleClockIn" :disabled="clocked" disabledColor="#fbe484"></CustomButton>
    </div>
  </div>
</template>

<script>
import CustomButton from './CustomButton.vue';
import { ElMessage } from 'element-plus';
import axios from 'axios';
export default {
  name: "ActivityCenter",
  components:{
    CustomButton
  },
  props: {
    username:{
      type:String,
      default:""
    }
  },
  data() {
    return {
      clocked: false,
      clockinDays: 0,
    };
  },
  methods:{
    handleClockIn(){
      if(this.clocked){
        return;
      }
      this.clocked = true;
      this.clockinDays += 1;
      ElMessage({
        type: 'success',
        message: '签到成功',
      });
    }
  },
  created(){
    //从后端获得该用户的连续签到天数
    //从后端获得该用户是否已经签到
    axios.get("http://101.42.118.80:8000/get_user_activity_info/",{
      params:{
        username:this.username
      }
    }).then((res)=>{
        if(res.data['status']==='ok'){
          this.clockinDays = res.data['continueSignInDays'];
          this.clocked = res.data['isTodaySignIn'];
        }
    }).catch();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.yellow-bg {
  background-color: #fbe484;
}
.green-bg {
  background-color: #5eabbf;
}
.got-box {
  border: 2px solid #fbe484;
  width:80px;
  height: 20px;
  border-radius: 4px;
  font-size: 20px;
  color:#ffeda7;
  font-family: YouSheRound;
}
.little-inner {
  padding-top: 10px;
  width: 110px;
  height: 120px;
  border: 1px solid rgba(0,0,0,0.5);
  border-radius: 4px;
}
.mask-box {
  width: 110px;
  height: 120px;
  background-color: rgba(0,0,0,0.7);
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
}
.activity-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.icon {
  width: 4em;
  height: 4em;
  vertical-align: -0.15em;
  fill: currentColor;
  overflow: hidden;
}
.large-icon {
  width: 8em;
  height: 8em;
}
.large-inner {
  padding-top: 20px;
  width: 200px;
  height: 240px;
  background-color:#fbe484;
  border: 1px solid rgba(0,0,0,0.5);
  border-radius: 4px;
}
.black-font {
  color: #555555;
}
.white-font {
  color: #ffffff;
}
.day-large-font {
  color: #ffffff;
  font-size: 27px;
}
.large-item-box {
  width: 262px;
  height: 300px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.num-area {
  text-align: right;
  width: 100%;
  font-size: 20px;
  font-family: YouSheRound;
  padding-right: 30px;
}
.large-num {
  font-size: 36px;
}
.little-item-box {
  width: 146px;
  height: 150px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.clockin-content {
  width: 700px;
  height: 300px;
}
.clockin-inner {
  margin-top: 20px;
  border-radius: 10px;
  box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
  width: 760px;
  height: 360px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.clockin-title {
  font-family: YouSheRound;
  font-size: 30px;
}
.clockin-box {
  width: 760px;
  height: 450px;
}
.large-mask-params {
  height:240px;
  width:200px;
  padding-top: 0;
}
.large-got-params {
  font-size: 30px;
  height: 30px;
  width: 100px;
}
</style>
