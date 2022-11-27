<template>
  <div class="feedback-page">
    <div class="feedback-title-outer">
      <span class="feedback-title">反馈问题</span>
    </div>
    <div class="feedback-box">
      <SingleFeedback
        v-for="item in items"
        :key="item.index"
        :props="item"
      ></SingleFeedback>
    </div>
    <div class="pagnation-box">
      <el-pagination
        background
        layout="total, prev, pager, next, jumper"
        v-model:currentPage="currentPage"
        :total="total"
        :page-size="10"
      />
    </div>
  </div>
</template>

<script>
import SingleFeedback from "./SingleFeedback.vue";
export default {
  name: "FeedbackPage",
  props: {
    items: {
      type: Array,
      default: undefined,
    },
    total: {
      type: Number,
      default: 1,
    },
  },
  components: {
    SingleFeedback,
  },
  data() {
    return {
      currentPage: 1,
    };
  },
  methods: {},
};
</script>

<style scoped>
.pagnation-box {
  display: flex;
  flex-direction: row;
  justify-content: center;
}
.feedback-box {
  display: flex;
  width: 100%;
  flex-direction: column;
  align-items: center;
}
.feedback-page {
  width: 70%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.feedback-title {
  font-family: YouSheRound;
  font-size: 30px;
  color: #5eabbf;
}
.feedback-title-outer {
  margin-top: 10px;
  margin-bottom: 20px;
}
</style>
