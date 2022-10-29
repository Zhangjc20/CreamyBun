<template>
    <div>
      <div class="gift-title">奖励中心</div>
      <div class="exchange-rate-title">当前汇率: 120
        <svg class="icon" aria-hidden="true">
          <use xlink:href="#icon-tiantianquan"></use>
        </svg>
        = 1 元
      </div>
      <div class="own-font">
        拥有
        <svg class="icon" aria-hidden="true">
          <use xlink:href="#icon-tiantianquan"></use>
        </svg> = 240
      </div>
      <div class="exchange-area">
        兑换 ： 
        <el-input class="value-input" v-model="valueInput" placeholder="请输入金额" clearable />
        &nbsp;&nbsp;元
      </div>
      <div class="confirm-exchange-area">
        <el-button class="confirm-exchange-btn" @click="handleClickExchange">确认兑换</el-button>
      </div>
    </div>
</template>
  
  <script>
  import { ElMessage, ElMessageBox } from 'element-plus';
  export default {
    name: 'GiftCenter',
    props: {
    },
    data(){
        return {
          valueInput:""
        }
    },
    methods:{
      getEqualDonuts(rate){
          return Number(this.valueInput)*rate;
      },
      handleClickExchange(){
        ElMessageBox.confirm(
          '您将要花费'+this.getEqualDonuts(120)+'甜甜圈兑换'+this.valueInput+'元',
          '确认兑换',
          {
            confirmButtonText: 'OK',
            cancelButtonText: 'Cancel',
            type: 'warning',
            draggable: true,
          }
        )
          .then(() => {
            ElMessage({
              type: 'success',
              message: '兑换成功',
            })
          })
          .catch(() => {
            ElMessage({
              type: 'info',
              message: '取消兑换',
            })
          })
      }
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped lang="scss">
  .confirm-exchange-btn {
    background-color: #FBE484;
    border-color: #FBE484;
    color: #606266;
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
    color: #5EABBF;
    font-size: 30px;
  }
  .own-font {
    margin-top: 6px;
    font-family: YouSheBlack;
    color: #5EABBF;
    font-size: 22px;
  }
  .exchange-rate-title {
    margin-top: 20px;
    font-family: YouSheBlack;
    color: #5EABBF;
    font-size: 22px;
  }
  </style>
  