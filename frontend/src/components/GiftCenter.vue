<template>
  <div class="gift-container">
    <div class="back-box">
      <div class="gift-title">奖励中心</div>
      <div class="exchange-rate-title">
        当前汇率: {{ donutToMoney }}
        <svg class="icon" aria-hidden="true">
          <use xlink:href="#icon-tiantianquan"></use>
        </svg>
        &nbsp;=> 1 元&emsp;&emsp; 1 元 => {{ moneyToDonut }}
        <svg class="icon" aria-hidden="true">
          <use xlink:href="#icon-tiantianquan"></use>
        </svg>
        &emsp;&emsp; 拥有
        <svg class="icon" aria-hidden="true">
          <use xlink:href="#icon-tiantianquan"></use>
        </svg>
        &nbsp;= {{ donutNumber }}
      </div>
      <div class="exchange-area">
        兑换甜甜圈 ：
        <el-input
          class="value-input"
          v-model="donutInput"
          placeholder="请输入金额"
          clearable
        />
        &nbsp;&nbsp;元
        <el-button class="confirm-exchange-btn" @click="handleTopUp"
          >确认兑换</el-button
        >
      </div>
      <div class="exchange-area">
        兑换现金 ：
        <el-input
          class="value-input"
          v-model="valueInput"
          placeholder="请输入金额"
          clearable
        />
        &nbsp;&nbsp;元
        <el-button class="confirm-exchange-btn" @click="handleWithdraw"
          >确认兑换</el-button
        >
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { ElMessage, ElMessageBox } from "element-plus";
export default {
  name: "GiftCenter",
  data() {
    return {
      valueInput: "",
      donutInput: "",
      donutToMoney: -1,
      moneyToDonut: -1,
      donutNumber: -1,
    };
  },
  methods: {
    handleTopUp() {
      if (!this.donutInput.match(/^[1-9]\d*$/g)) {
        ElMessage({
          type: "error",
          message: "请输入正整数",
        });
        return;
      }
      ElMessageBox.confirm(
        "您将要花费" +
          this.donutInput +
          "元兑换" +
          this.getEqualDonuts(this.donutInput, this.moneyToDonut) +
          "甜甜圈",
        "确认兑换",
        {
          confirmButtonText: "确认",
          cancelButtonText: "取消",
          type: "warning",
          draggable: true,
        }
      )
        .then(() => {
          axios
            .get("http://101.42.118.80:8000/top_up/", {
              params: {
                username: localStorage.getItem('username'),
                money: this.donutInput,
              },
            })
            .then((res) => {
              if (res.data["status"] === "ok") {
                ElMessage({
                  type: "success",
                  message: "兑换成功",
                });
                this.donutNumber = res.data["donutNum"];
              }
            });
        })
        .catch(() => {});
    },
    getEqualDonuts(money, rate) {
      return Number(money) * rate;
    },
    handleWithdraw() {
      if (!this.valueInput.match(/^[1-9]\d*$/g)) {
        ElMessage({
          type: "error",
          message: "请输入正整数",
        });
        return;
      }
      if(this.getEqualDonuts(this.valueInput, this.donutToMoney)>this.donutNumber){
        ElMessage({
          type: "error",
          message: "您的甜甜圈余额不足",
        });
        return;
      }
      ElMessageBox.confirm(
        "您将要花费" +
          this.getEqualDonuts(this.valueInput, this.donutToMoney) +
          "甜甜圈兑换" +
          this.valueInput +
          "元",
        "确认兑换",
        {
          confirmButtonText: "确认",
          cancelButtonText: "取消",
          type: "warning",
          draggable: true,
        }
      )
        .then(() => {
          axios
            .get("http://101.42.118.80:8000/withdraw_money/", {
              params: {
                username: localStorage.getItem('username'),
                money: this.valueInput,
              },
            })
            .then((res) => {
              if (res.data["status"] === "ok") {
                if(res.data['withdrawStatus']== true){
                  ElMessage({
                    type: "success",
                    message: "兑换成功",
                  });
                  this.donutNumber = res.data["donutNum"];
                }
                else{
                  ElMessage({
                    type: "error",
                    message: "您的甜甜圈余额不足",
                  });
                }
              }
            });
        })
        .catch(() => {});
    },
  },
  beforeMount() {
    axios
      .get("http://101.42.118.80:8000/get_user_bonus_info/", {
        params: {
          username: localStorage.getItem('username'),
        },
      })
      .then((res) => {
        if (res.data["status"] === "ok") {
          this.donutNumber = res.data["donutNumber"];
          this.donutToMoney = res.data["donutToMoney"];
          this.moneyToDonut = res.data["moneyToDonut"];
        }
      })
      .catch();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.gift-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.back-box {
  width: 80%;
  box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
  border-radius: 10px;
  padding-top: 10px;
  padding-bottom: 38px;
  margin-top: 20px;
}
.confirm-exchange-btn {
  background-color: #fbe484;
  border-color: #fbe484;
  color: #606266;
  margin-left: 20px;
}
.confirm-exchange-btn:focus {
  background-color: #e8d175;
  border-color: #e8d175;
  color: #606266;
}
.confirm-exchange-btn:hover {
  background-color: #e2cc73;
  border-color: #e2cc73;
  color: #606266;
}
.confirm-exchange-area {
  margin-top: 20px;
}
.exchange-area {
  margin-top: 40px;
  font-family: YiPinChuangXiang;
}
.icon {
  width: 1em;
  height: 1em;
  vertical-align: -0.15em;
  fill: currentColor;
  overflow: hidden;
}
.value-input {
  width: 200px;
}
.gift-title {
  margin-top: 20px;
  font-family: YouSheRound;
  color: #5eabbf;
  font-size: 30px;
}
.own-font {
  margin-top: 6px;
  font-family: YouSheBlack;
  color: #5eabbf;
  font-size: 22px;
}
.exchange-rate-title {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
  height: 60px;
  font-family: YouSheBlack;
  color: #5eabbf;
  font-size: 25px;
}
</style>
