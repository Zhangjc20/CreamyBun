<template>
  <el-header class="main-header-style">
    
  </el-header>
</template>

<script>
export default {
  name: 'ReleasePicture',
  props: {
    login:Boolean,
    activeItem:String,
  },
  data(){
      return {
      }
  },
  methods:{
    clickHome(){
      this.$router.push({
            name: 'home',
        });
    },
    clickLogin(){
        this.$router.push({
            name: 'login',
        });
    },
    clickLogup(){
        this.$router.push({
            name: 'logup',
        });
    },
    clickMine(){
        this.$router.push({
            name: 'mine',
        });
    },
    clickRelease(){
        this.$router.push({
            name: 'release',
        });
    }
  }
}
</script>

<style scoped>

.main-header-style{
    border-radius: 5px;
    box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
    height: 100px;
  }
/* 
  .user-area {
    float: right;
    position: absolute;
    top:0;
    right: 0;
    height: 60px;
    margin-right: 90px;
  }
   .avatar {
    float: right;
    position: absolute;
    top:0;
    right: 0;
    margin-right: 180px;
    margin-top: 10px;
  }
  .user-center {
    line-height: 60px;
    margin-bottom: 20px;
    font-size: 22px;
    color:#f8f8f8;
    font-family: YouSheBlack;
    cursor: pointer;
  }
  .user-center:hover {
    opacity: 0.6;
  }
.nav-title {
    float: left;
    height: 60px;
    font-family: YouSheRound;
    line-height: 50px;
    font-size: 28px;
    color: #5EABBF;
    margin-left: 80px;
    display: flex;
  }
  .nav-title-font {
    margin-left: 10px;
    line-height: 60px;
  }
  .menu-out {
    margin-left: 80px;
    background-color: #ffffff;
    width:470px;
    overflow: hidden;
    border-radius: 40px;
    margin-top: 10px;
    display: flex;
   }
   .el-button--primary {
  background: #FBE484 !important;
  border-color: #FBE484 !important;
  color:#6C6C6C;
}
.el-button--medium {
  width: 80px;
}

.logo {
  width: 45px; 
  height: 40px; 
  margin-top: 10px;
}
.login-button {
  margin-right: 30px;
}

.log-buttons {
  float: right;
  position: absolute;
  top:0;
  right: 0;
  line-height: 60px;
  margin-right: 100px;
}
.el-nav-menu {
  width:480px;
  padding-left: 46px;
}
.el-menu {
  border-radius: 0;
}
.el-menu-item {
  height: 50px;
  font-size: 16px;
  padding-top: 4px;
}
.el-menu--horizontal .el-menu-item:not(.is-disabled):focus{
  background-color: transparent;
}
.el-menu--horizontal .el-menu-item:not(.is-disabled):hover{
  background-color: #f8f8f8;
} */
</style>