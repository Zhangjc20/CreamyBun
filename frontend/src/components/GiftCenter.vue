<template>
  <div class="gift-container">
    <div class="gift-title">奖励中心</div>
    <div class="exchange-rate-title">
      当前汇率: {{ donutToMoney }}
      <svg class="icon" aria-hidden="true">
        <use xlink:href="#icon-tiantianquan"></use>
      </svg>
      => 1 元&emsp;&emsp;&emsp; 1 元 => {{ moneyToDonut }}
      <svg class="icon" aria-hidden="true">
        <use xlink:href="#icon-tiantianquan"></use>
      </svg>
      &emsp;&emsp;&emsp;
      拥有
      <svg class="icon" aria-hidden="true">
        <use xlink:href="#icon-tiantianquan"></use>
      </svg>
      = {{ donutNumber }}
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
      <el-button class="confirm-exchange-btn" @click="handleClickExchange"
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
      <el-button class="confirm-exchange-btn" @click="handleClickExchange"
        >确认兑换</el-button
      >
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { ElMessage, ElMessageBox } from "element-plus";
export default {
  name: "GiftCenter",
  props: {
    username: {
      type: String,
      default: "",
    },
  },
  data() {
    return {
      valueInput: "",
      donutToMoney: -1,
      moneyToDonut: -1,
      donutNumber: -1,
    };
  },
  methods: {
    getEqualDonuts(rate) {
      return Number(this.valueInput) * rate;
    },
    handleClickExchange() {
      ElMessageBox.confirm(
        "您将要花费" +
          this.getEqualDonuts(120) +
          "甜甜圈兑换" +
          this.valueInput +
          "元",
        "确认兑换",
        {
          confirmButtonText: "OK",
          cancelButtonText: "Cancel",
          type: "warning",
          draggable: true,
        }
      )
        .then(() => {
          ElMessage({
            type: "success",
            message: "兑换成功",
          });
        })
        .catch(() => {
          ElMessage({
            type: "info",
            message: "取消兑换",
          });
        });
    },
  },
  beforeMount() {
    axios
      .get("/get_user_bonus_info", {
        params: {
          username: this.username,
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
.gift-box {
  box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
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
  width: 80%;
  height: 60px;
  font-family: YouSheBlack;
  color: #5eabbf;
  font-size: 22px;
  box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
}
</style>
