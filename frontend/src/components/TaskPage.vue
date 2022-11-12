<template>
  <div>
    <div class="task-box">
      <SingleTask
        v-for="item in items"
        :key="item.index"
        :props="item"
      ></SingleTask>
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
import SingleTask from "./SingleTask.vue";
export default {
  name: "TaskPage",
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
    SingleTask,
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
.task-box {
  display: flex;
  width: 100%;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-between;
}
</style>
