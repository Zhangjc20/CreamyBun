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
        兑换
        <el-input class="value-input" v-model="input" placeholder="请输入金额" clearable />
      </div>
    </div>
</template>
  
  <script>
  export default {
    name: 'GiftCenter',
    props: {
    },
    data(){
        return {
        }
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped lang="scss">
  .icon {
  width: 1em;
  height: 1em;
  vertical-align: -0.15em;
  fill: currentColor;
  overflow: hidden;
}
.value-input {
  width: 300px;
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
  