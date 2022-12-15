<template>
  <div class="settings-container flex-box">
    <div class="setting-title">设置</div>
    <div class="flex-box change-box">
      <el-row class="info-show">
        <el-col :span="12" style="padding-left: 20px"
          >用户名：{{ adminU }}</el-col
        >
        <el-col :span="12" style="padding-left: 30px"
          >密码：{{ adminP }}</el-col
        >
      </el-row>
      <el-row class="center-box">
        <el-col :span="3"> 修改用户名 </el-col>
        <el-col :span="9">
          <el-input v-model="form.username"></el-input>
        </el-col>
        <el-col :span="3"> 修改密码</el-col>
        <el-col :span="9">
          <el-input v-model="form.password"></el-input
        ></el-col>
      </el-row>
      <el-row style="width: 100%; margin-top: 20px">
        <el-col :span="12" class="middle-box">
          <CustomButton title="确认修改" fontSize="16px" @click="setAdminU" />
        </el-col>
        <el-col :span="12" class="middle-box">
          <CustomButton title="确认修改" fontSize="16px" @click="setAdminP" />
        </el-col>
      </el-row>
    </div>
    <div class="logout-button-outer">
      <CustomButton
        @click="handleLogout"
        title="退出登录"
        fontSize="17px"
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
import axios from "axios";

export default {
  name: "AdminSettings",
  components: {
    CustomButton,
  },
  props: {},
  data() {
    return {
      adminU: "",
      adminP: "",
      form: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    setAdminU() {
      if (this.form.adminU == "") {
        ElMessage({
          type: "error",
          message: "用户名不可为空",
        });
        return;
      }
      axios
        .get("http://101.42.118.80:8000/set_admin_username_and_password/", {
          params: {
            type: "username",
            newUsername: this.form.username,
            adminToken: localStorage.getItem("adminToken"),
          },
        })
        .then((res) => {
          if (res.data["status"] === "ok") {
            this.adminU = res.data["adminUsername"];
            ElMessage({
              type: "success",
              message: "管理员用户名修改成功",
            });
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    setAdminP() {
      if (this.form.adminP == "") {
        ElMessage({
          type: "error",
          message: "密码不可为空",
        });
        return;
      }
      axios
        .get("http://101.42.118.80:8000/set_admin_username_and_password/", {
          params: {
            type: "password",
            newPassword: this.form.password,
            adminToken: localStorage.getItem("adminToken"),
          },
        })
        .then((res) => {
          if (res.data["status"] === "ok") {
            this.adminP = res.data["adminPassword"];
            ElMessage({
              type: "success",
              message: "管理员密码修改成功",
            });
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    handleLogout() {
      ElMessageBox.confirm("确认退出管理员吗", "退出登录", {
        confirmButtonText: "确认",
        cancelButtonText: "取消",
        type: "warning",
        draggable: true,
      }).then(() => {
        ElMessage({
          type: "success",
          message: "退出登录",
        });
        localStorage.setItem("adminAuth", false);
        localStorage.setItem("adminToken", "");
        this.$router.push({
          name: "home",
        });
      });
    },
  },
  mounted() {
    axios
      .get("http://101.42.118.80:8000/get_admin_username_and_password/", {
        params: {
          adminToken: localStorage.getItem("adminToken"),
        },
      })
      .then((res) => {
        if (res.data["status"] === "ok") {
          this.adminU = res.data["adminUsername"];
          this.adminP = res.data["adminPassword"];
        }
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style scoped>
.info-show {
  width: 100%;
  font-family: YouSheRound;
  font-size: 20px;
  text-align: left;
  margin: 5px 0 20px 0;
}
.center-box {
  display: flex;
  align-items: center;
  width: 100%;
}
.middle-box {
  display: flex;
  justify-content: center;
}
.logout-button-outer {
  margin-top: 30px;
}
.flex-box {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.change-box {
  width: 80%;
  box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
  padding: 20px 10px 25px 10px;
  border-radius: 8px;
}
.setting-title {
  font-family: YouSheRound;
  font-size: 28px;
  margin-bottom: 20px;
}
.settings-container {
  background-color: transparent;
}
</style>
