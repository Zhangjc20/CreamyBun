<template>
  <div class="change-params-container">
    <div class="params-title">参数调整</div>
    <div class="donut-rate-box">
        <div class="rate-title">汇率调整</div>
      <div class="donut-rate-box-inner">
        <el-form
          label-position="right"
          label-width="140px"
          :model="form"
          class="flex-box form"
          style="max-width: 1000px"
        >
          <el-form-item label="甜甜圈转现金汇率">
            <el-row style="width:100%;">
                <el-col :span="16"><el-input v-model="form.donutToMoney"/></el-col>
                <el-col :span="8"><CustomButton title="确认修改" fontSize="16px" /></el-col>
            </el-row>
          </el-form-item>
          <el-form-item label="现金转甜甜圈汇率">
            <el-row style="width:100%;">
                <el-col :span="16"><el-input v-model="form.moneyToDonut" /></el-col>
                <el-col :span="8"><CustomButton title="确认修改" fontSize="16px" /></el-col>
            </el-row>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
import CustomButton from './CustomButton.vue';
export default {
  name: "ChangeParams",
  components: {
    CustomButton
  },
  props: {},
  data() {
    return {
      form: {
        donutToMoney: "",
        moneyToDonut: "",
      },
    };
  },
  methods: {},
};
</script>

<style scoped>
:deep .el-form-item__label {
    font-size:15px;    
}
.flex-box {
    display: flex;
    justify-content: center;
    align-items: center;
}
.form {
    width:90%;
    flex-direction: column;
}
.el-form-item{
    width:100%;
}
.rate-title {
    margin-top:20px;
    font-size: 26px;
    font-family: YouSheBlack;
    color:#5EABBF;
}
.donut-rate-box-inner {
    padding:20px 0 0 20px;
    width:90%;
    display: flex;
    justify-content: center;
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
  width: 80%;
  height: 200px;
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
