<template>
  <div class="change-params-container">
    <div class="params-title">参数调整</div>
    <div class="donut-rate-box">
      <div class="rate-title">汇率调整</div>
      <div class="donut-rate-box-inner">
        <div style="font-family:YouSheBlack;font-size:25px;margin-bottom: 20px;">
          当前汇率: {{ donutToMoney }}
          <svg class="icon" aria-hidden="true">
            <use xlink:href="#icon-tiantianquan"></use>
          </svg>
          => 1 元&emsp;&emsp;&emsp; 1 元 => {{ moneyToDonut }}
          <svg class="icon" aria-hidden="true">
            <use xlink:href="#icon-tiantianquan"></use>
          </svg>
        </div>
        <el-form
          label-position="right"
          label-width="140px"
          :model="form"
          class="flex-box form"
          style="max-width: 1000px"
        >
          <el-form-item label="甜甜圈转现金汇率">
            <el-row style="width: 100%">
              <el-col :span="16"
                ><el-input v-model="form.donutToMoney"
              /></el-col>
              <el-col :span="8"
                ><CustomButton
                  title="确认修改"
                  fontSize="16px"
                  @click="changeDonutToMoney"
              /></el-col>
            </el-row>
          </el-form-item>
          <el-form-item label="现金转甜甜圈汇率">
            <el-row style="width: 100%">
              <el-col :span="16"
                ><el-input v-model="form.moneyToDonut"
              /></el-col>
              <el-col :span="8"
                ><CustomButton
                  title="确认修改"
                  fontSize="16px"
                  @click="changeMoneyToDonut"
              /></el-col>
            </el-row>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
import CustomButton from "./CustomButton.vue";
import axios from "axios";
import { ElMessage} from 'element-plus';
export default {
  name: "ChangeParams",
  components: {
    CustomButton,
  },
  props: {},
  data() {
    return {
      form: {
        donutToMoney: "",
        moneyToDonut: "",
      },
      donutToMoney:0,
      moneyToDonut:0,
    };
  },
  methods: {
    changeDonutToMoney() {
      axios
        .get("http://101.42.118.80:8000/change_current_rate_info/", {
          params: {
            adminToken:localStorage.getItem('adminToken'),
            type: "donutToMoney",
            donutToMoney: this.form.donutToMoney,
          },
        })
        .then((res) => {
          ElMessage({
            type: 'success',
            message: '汇率修改成功',
          });
          this.donutToMoney = res.data['donutToMoney'];
        })
        .catch((err) => {
          console.log(err);
        });
    },
    changeMoneyToDonut() {
      axios
        .get("http://101.42.118.80:8000/change_current_rate_info/", {
          params: {
            adminToken:localStorage.getItem('adminToken'),
            type: "moneyToDonut",
            moneyToDonut: this.form.moneyToDonut,
          },
        })
        .then((res) => {
          ElMessage({
            type: 'success',
            message: '汇率修改成功',
          });
          this.moneyToDonut = res.data["moneyToDonut"];
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  mounted() {
    axios
      .get("http://101.42.118.80:8000/get_current_rate_info/", {
        params: {
          adminToken:localStorage.getItem('adminToken')
        },
      })
      .then((res) => {
        if(res.data['status']=='wrong'){
          ElMessage({
            type:'error',
            message:"权限不足"
          })
          return;
        }
        else if(res.data['status']=='ok'){
          this.donutToMoney = res.data["donutToMoney"];
          this.moneyToDonut = res.data["moneyToDonut"];
        }
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style scoped>
:deep .el-form-item__label {
  font-size: 15px;
}
.flex-box {
  display: flex;
  justify-content: center;
  align-items: center;
}
.form {
  width: 90%;
  flex-direction: column;
}
.icon {
  width: 1em;
  height: 1em;
  vertical-align: -0.15em;
  fill: currentColor;
  overflow: hidden;
}
.el-form-item {
  width: 100%;
}
.rate-title {
  margin-top: 20px;
  font-size: 26px;
  font-family: YouSheBlack;
  color: #5eabbf;
}
.donut-rate-box-inner {
  padding: 10px 0 0 20px;
  width: 90%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
.change-params-container {
  background-color: transparent;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.donut-rate-box {
  box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
  border-radius: 10px;
  width: 80%;
  height: 240px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.params-title {
  font-family: YouSheRound;
  font-size: 28px;
  margin-bottom: 20px;
}
</style>
