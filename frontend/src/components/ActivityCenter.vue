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
                      <div class="num-area black-font">
                        ×{{ donutListForClockIn[0] }}
                      </div>
                      <div class="white-font green-bg">第一天</div>
                    </div>
                    <div
                      class="little-inner mask-box"
                      v-show="clockinDays >= 1"
                    >
                      <div class="got-box">已领取</div>
                    </div>
                  </div>
                </el-col>
                <el-col :span="8">
                  <div class="little-item-box">
                    <div class="little-inner green-bg">
                      <svg class="icon" aria-hidden="true">
                        <use xlink:href="#icon-tiantianquan"></use>
                      </svg>
                      <div class="num-area white-font">
                        ×{{ donutListForClockIn[1] }}
                      </div>
                      <div class="black-font yellow-bg">第二天</div>
                    </div>
                    <div
                      class="little-inner mask-box"
                      v-show="clockinDays >= 2"
                    >
                      <div class="got-box">已领取</div>
                    </div>
                  </div>
                </el-col>
                <el-col :span="8">
                  <div class="little-item-box">
                    <div class="little-inner yellow-bg">
                      <svg class="icon" aria-hidden="true">
                        <use xlink:href="#icon-tiantianquan"></use>
                      </svg>
                      <div class="num-area black-font">
                        ×{{ donutListForClockIn[2] }}
                      </div>
                      <div class="white-font green-bg">第三天</div>
                    </div>
                    <div
                      class="little-inner mask-box"
                      v-show="clockinDays >= 3"
                    >
                      <div class="got-box">已领取</div>
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
                      <div class="num-area white-font">
                        ×{{ donutListForClockIn[3] }}
                      </div>
                      <div class="black-font yellow-bg">第四天</div>
                    </div>
                    <div
                      class="little-inner mask-box"
                      v-show="clockinDays >= 4"
                    >
                      <div class="got-box">已领取</div>
                    </div>
                  </div>
                </el-col>
                <el-col :span="8">
                  <div class="little-item-box">
                    <div class="little-inner yellow-bg">
                      <svg class="icon" aria-hidden="true">
                        <use xlink:href="#icon-tiantianquan"></use>
                      </svg>
                      <div class="num-area black-font">
                        ×{{ donutListForClockIn[4] }}
                      </div>
                      <div class="white-font green-bg">第五天</div>
                    </div>
                    <div
                      class="little-inner mask-box"
                      v-show="clockinDays >= 5"
                    >
                      <div class="got-box">已领取</div>
                    </div>
                  </div>
                </el-col>
                <el-col :span="8">
                  <div class="little-item-box">
                    <div class="little-inner green-bg">
                      <svg class="icon" aria-hidden="true">
                        <use xlink:href="#icon-tiantianquan"></use>
                      </svg>
                      <div class="num-area white-font">
                        ×{{ donutListForClockIn[5] }}
                      </div>
                      <div class="black-font yellow-bg">第六天</div>
                    </div>
                    <div
                      class="little-inner mask-box"
                      v-show="clockinDays >= 6"
                    >
                      <div class="got-box">已领取</div>
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
                  <div class="num-area large-num">
                    ×{{ donutListForClockIn[6] }}
                  </div>
                  <div class="day-large-font green-bg">第七天</div>
                </div>
                <div
                  class="large-inner mask-box large-mask-params"
                  v-show="clockinDays >= 7"
                >
                  <div class="got-box large-got-params">已领取</div>
                </div>
              </div>
            </el-col>
          </el-row>
        </div>
      </div>
    </div>
    <div>
      <CustomButton
        :title="clocked ? '已签到' : '签到'"
        fontSize="18px"
        width="100px"
        @click="handleClockIn"
        :disabled="clocked"
        disabledColor="#fbedb3"
      ></CustomButton>
    </div>
    <div class="daily-box">
      <div style="font-size: 30px; font-family: YouSheRound;margin: 20px 0 20px 0;">每日任务</div>
      <div class="daily-task">
        <div style="text-align:left;font-size:20px;margin:10px 0 10px 20px;font-family: YouSheBlack;">任务描述：今日完成一个任务</div>
        <div style="font-family:YiPinChuangXiang;">
          任务奖励：
          <svg class="icon" style="width:1.5em;height:1.5em;vertical-align: -20%;" aria-hidden="true">
            <use xlink:href="#icon-tiantianquan"></use>
          </svg>{{finishTaskDonut[0]}}
          &emsp;&emsp;
          完成进度：{{finishTaskNum}}/1
        </div>
        <div class="daily-btn-area">
          <CustomButton :title="accepted1?'已领取':(finished1?'领取奖励':'尚未完成')" :props="!finished1||accepted1?disabledProps:undefined" @click="acceptDonut1"/>
        </div>
      </div>
      <div class="daily-task" style="margin-top:20px">
        <div style="text-align:left;font-size:20px;margin:10px 0 10px 20px;font-family: YouSheBlack;">任务描述：今日完成三个任务</div>
        <div style="font-family:YiPinChuangXiang;">
          任务奖励：
          <svg class="icon" style="width:1.5em;height:1.5em;vertical-align: -20%;" aria-hidden="true">
            <use xlink:href="#icon-tiantianquan"></use>
          </svg>{{finishTaskDonut[1]}}
          &emsp;&emsp;
          完成进度：{{finishTaskNum}}/3
        </div>
        <div class="daily-btn-area">
          <CustomButton @click="acceptDonut2" :title="accepted2?'已领取':(finished2?'领取奖励':'尚未完成')" :props="!finished2||accepted2?disabledProps:undefined"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CustomButton from "./CustomButton.vue";
import { ElMessage } from "element-plus";
import axios from "axios";
export default {
  name: "ActivityCenter",
  components: {
    CustomButton,
  },
  props: {
    username: {
      type: String,
      default: "",
    },
  },
  data() {
    return {
      clocked: false,
      clockinDays: 0,
      donutListForClockIn: [],
      finished1:false,
      finished2:false,
      accepted1:false,
      accepted2:false,
      disabledProps:{
        disabled:"true",
        disabledColor:"#FCE5B1" ,
      },
      finishTaskDonut:[0,0],
      finishTaskNum:0,
    };
  },
  methods: {
    acceptDonut1(){
      if(!this.finished1 || this.accepted1){
        return ;
      }
      axios
        .get("http://101.42.118.80:8000/finish_daily_task/", {
          params: {
            username: localStorage.getItem('username'),
            index:0
          },
        })
        .then((res) => {
          if(res.data['status']=='ok'){
            ElMessage({
              type:'success',
              message:'恭喜你完成任务，获得奖励甜甜圈'+String(this.finishTaskDonut[0]),
            })
            this.accepted1 = true;
          }
      })
    },
    acceptDonut2(){
      if(!this.finished2 || this.accepted2){
        return ;
      }
      axios
        .get("http://101.42.118.80:8000/finish_daily_task/", {
          params: {
            username: localStorage.getItem('username'),
            index:1
          },
        })
        .then((res) => {
          if(res.data['status']=='ok'){
            ElMessage({
              type:'success',
              message:'恭喜你完成任务，获得奖励甜甜圈'+String(this.finishTaskDonut[1]),
            })
            this.accepted2 = true;
          }
      })
    },
    handleClockIn() {
      if (this.clocked) {
        return;
      }
      axios
        .get("http://101.42.118.80:8000/clock_in/", {
          params: {
            username: localStorage.getItem('username')
          },
        })
        .then((res) => {
          if(res.data['status']=='ok'){
            this.clocked = true;
            this.clockinDays += 1;
            ElMessage({
              type: "success",
              message: "签到成功,获得甜甜圈"+String(this.donutListForClockIn[this.clockinDays-1]),
            });
          }
      })
    },
  },
  created() {
    //从后端获得该用户的连续签到天数
    //从后端获得该用户是否已经签到
    axios
      .get("http://101.42.118.80:8000/get_user_activity_info/", {
        params: {
          username: this.username,
        },
      })
      .then((res) => {
        if (res.data["status"] === "ok") {
          this.clockinDays = res.data["continueSignInDays"];
          this.clocked = res.data["isTodaySignIn"];
          this.donutListForClockIn = res.data["donutListForClockIn"];
          this.finishTaskDonut = res.data['finishTaskDonut'];
          this.finishTaskNum = res.data['finishTaskNum']
          if (this.finishTaskNum >= 1) {
            this.finished1 = true;
          }
          if (this.finishTaskNum >= 3) {
            this.finished2 = true;
          }
          this.accepted1 = res.data['taskOneState']?true:false;
          this.accepted2 = res.data['taskTwoState']?true:false;
        }
      })
      .catch();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.daily-btn-area {
  display: flex;
  justify-content: flex-end;
  padding: 0 20px 10px 0;
}
.daily-task {
  box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
  border-radius: 20px;
  width: 72%;
}
.daily-task:hover {
  position: relative;
  top:-3px;
  left:-3px;
}
.yellow-bg {
  background-color: #fbe484;
}
.green-bg {
  background-color: #5eabbf;
}
.got-box {
  border: 2px solid #fbe484;
  width: 80px;
  height: 20px;
  border-radius: 4px;
  font-size: 20px;
  color: #ffeda7;
  font-family: YouSheRound;
}
.little-inner {
  padding-top: 10px;
  width: 110px;
  height: 120px;
  border: 1px solid rgba(0, 0, 0, 0.5);
  border-radius: 4px;
}
.mask-box {
  width: 110px;
  height: 120px;
  background-color: rgba(0, 0, 0, 0.7);
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
  background-color: #fbe484;
  border: 1px solid rgba(0, 0, 0, 0.5);
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
  height: 430px;
}
.large-mask-params {
  height: 240px;
  width: 200px;
  padding-top: 0;
}
.large-got-params {
  font-size: 30px;
  height: 30px;
  width: 100px;
}
.daily-box {
  margin-top: 30px;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
