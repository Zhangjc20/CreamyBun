<template>
  <div class="settings-container">
    <div class="setting-title">设置</div>
    <div class="logout-button-outer">
      <CustomButton
        @click="handleLogout"
        title="退出登录"
        fontColor="#ffffff"
        normalColor="#5EABBF"
        focusColor="#4E98AB"
        hoverColor="#4E98AB"
      />
    </div>
  </div>
</template>

<script>
import CustomButton from "@/components/CustomButton.vue";
import { ElMessage, ElMessageBox } from "element-plus";

export default {
  name: "AdminSettings",
  components:{
    CustomButton
  },
  props: {},
  data() {
    return {
    };
  },
  methods: {
      handleLogout(){
          ElMessageBox.confirm("确认退出管理员吗", "退出登录", {
          confirmButtonText: "确认",
          cancelButtonText: "取消",
          type: "warning",
          draggable: true,
        })
          .then(() => {
            ElMessage({
              type: "success",
              message: "退出登录",
            });
            sessionStorage.setItem("adminAuth",false);
            this.$router.push({
                name:"home"
            })
          });
      }
  },
};
</script>

<style scoped>
.setting-title {
    font-family: YouSheRound;
    font-size: 28px;
    margin-bottom: 20px;
}
.settings-container{
    background-color: transparent;
}
</style>
