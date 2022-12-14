<template>
  <el-container class="container">
    <FeedbackPage :items="items" />
  </el-container>
</template>

<script>
import FeedbackPage from "@/components/FeedbackPage.vue";
import axios from "axios";
export default {
  name: "FeedbackManagerView",
  components: {
    FeedbackPage,
  },
  data() {
    return {
      total: 4,
      username: "",
      items: [],
    };
  },
  mounted() {
    let formData = new FormData();
    formData.append("email", "sdfsdfsdf");
    axios({
      method: "Post",
      url: "http://101.42.118.80:8000/get_feedback/",
      headers: { "Content-Type": "multipart/form-data" },
      data: formData,
    }).then((res) => {
      this.items = res.data["feedback_list"];
    });
  },
};
</script>

<style scoped>
.container {
  margin: 0;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
