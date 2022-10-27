<template>
  <el-container class="container">
    <el-header class="header-style">
      <NavBar :login="false" activeItem="1"></NavBar>
    </el-header>
    <el-main class="main-style">

    </el-main>
  </el-container>
</template>

<script>
// @ is an alias to /src
import NavBar from "@/components/NavBar.vue";
export default {
  name: 'HomeView',
  components: {
    NavBar,
  },
  data(){
    return {

    }
  }
}
</script>


<style scoped>
.container {
  margin:0;
  height:100%;
}
.main-style {
  background-color:transparent;
}
.header-style {
  background-image: url(@/assets/images/nav-background.png);
  background-size: cover;
  height: 60px;
  box-shadow: 0 0px 8px 0;
  display: flex;
}
</style>

