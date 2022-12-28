<template>
  <el-container class="container">
    <el-header class="header-style">
      <NavBar
        :login="username != ''"
        activeItem="1"
        :username="username"
        :imageUrl="image.src"
      ></NavBar>
    </el-header>
    <el-main class="main-style">
      <div class="custom-box">
        <div class="custom-title-outer">
          <span class="custom-title">个性化数据标注服务</span>
        </div>
        <el-row class="custom-row">
          <el-col :span="6" class="type-box">
            <div class="round-background">
              <svg class="icon" aria-hidden="true">
                <use xlink:href="#icon-text"></use>
              </svg>
            </div>
            <span class="round-back-font">文本</span>
          </el-col>
          <el-col :span="6" class="type-box">
            <div class="round-background">
              <svg class="icon" aria-hidden="true">
                <use xlink:href="#icon-tupian"></use>
              </svg>
            </div>
            <span class="round-back-font">图片</span>
          </el-col>
          <el-col :span="6" class="type-box">
            <div class="round-background">
              <svg class="icon" aria-hidden="true">
                <use xlink:href="#icon-a-5Jyinboyinpin"></use>
              </svg>
            </div>
            <span class="round-back-font">音频</span>
          </el-col>
          <el-col :span="6" class="type-box">
            <div class="round-background">
              <svg class="icon" aria-hidden="true">
                <use xlink:href="#icon-shipin"></use>
              </svg>
            </div>
            <span class="round-back-font">视频</span>
          </el-col>
        </el-row>
      </div>
      <div class="basic-types-area">
        <span class="basic-types-title">参与众包 互利共赢</span>
        <div class="radio-area">
          <el-radio-group v-model="selectedItem" @change="handleClickItem">
            <el-radio-button label="0">图片分类</el-radio-button>
            <el-radio-button label="1">图片框图</el-radio-button>
            <el-radio-button label="2">邮件识别</el-radio-button>
            <el-radio-button label="3">音频分析</el-radio-button>
          </el-radio-group>
        </div>
        <div class="basic-types-content">
          <el-carousel
            height="300px"
            ref="carousel"
            @change="carouselChange"
            :initial-index="0"
          >
            <el-carousel-item key="0">
              <el-row>
                <el-col :span="12">
                  <el-image
                    class="image"
                    :src="require('@/assets/images/pet1.jpeg')"
                    fit="contain"
                  />
                </el-col>
                <el-col :span="12">
                  <div class="carousel-item-title">图片分类</div>
                  <div class="tag-area">
                    <el-tag style="margin-right: 10px">图片</el-tag>
                    <el-tag type="success">单选题</el-tag>
                  </div>
                  <div class="carousel-item-content">
                    &emsp;&emsp;对发布者提供的图片进行分类，选择正确的选项。图片类别可能涉及动物、植物、人物等领域。
                  </div>
                </el-col>
              </el-row>
            </el-carousel-item>
            <el-carousel-item key="1">
              <el-row>
                <el-col :span="12">
                  <el-image
                    class="image"
                    :src="require('@/assets/images/pet2.jpeg')"
                    fit="contain"
                  />
                </el-col>
                <el-col :span="12">
                  <div class="carousel-item-title">图片框图</div>
                  <div class="tag-area">
                    <el-tag style="margin-right: 10px">图片</el-tag>
                    <el-tag type="success">框图题</el-tag>
                  </div>
                  <div class="carousel-item-content">
                    &emsp;&emsp;根据发布者的要求框选出图片中合适的范围。图片类别可能涉及动物、植物、人物等领域。
                  </div>
                </el-col>
              </el-row>
            </el-carousel-item>
            <el-carousel-item key="2">
              <el-row>
                <el-col :span="14">
                  <el-image
                    class="image"
                    :src="require('@/assets/images/pet3.jpeg')"
                    fit="contain"
                  />
                </el-col>
                <el-col :span="10">
                  <div class="carousel-item-title">邮件识别</div>
                  <div class="tag-area">
                    <el-tag style="margin-right: 10px">文本</el-tag>
                    <el-tag type="success">单选题</el-tag>
                  </div>
                  <div class="carousel-item-content">
                    &emsp;&emsp;对发布者给出的邮件进行主观判断，确定其是否属于垃圾邮件的范畴。
                  </div>
                </el-col>
              </el-row>
            </el-carousel-item>
            <el-carousel-item key="3">
              <el-row>
                <el-col :span="12">
                  <el-image
                    class="image"
                    :src="require('@/assets/images/pet4.jpeg')"
                    fit="contain"
                  />
                </el-col>
                <el-col :span="12">
                  <div class="carousel-item-title">音频情感</div>
                  <div class="tag-area">
                    <el-tag style="margin-right: 10px">音频</el-tag>
                    <el-tag type="success">单选题</el-tag>
                  </div>
                  <div class="carousel-item-content">
                    &emsp;&emsp;分析一段音频的情感，属于所给选项中的哪个。可能是判断情感的强烈、倾向。
                  </div>
                </el-col>
              </el-row>
            </el-carousel-item>
          </el-carousel>
        </div>
      </div>
    </el-main>
  </el-container>
</template>

<script>
// @ is an alias to /src
import NavBar from "@/components/NavBar.vue";
import axios from "axios";
export default {
  name: "HomeView",
  components: {
    NavBar,
  },
  data() {
    return {
      image: {
        src: "",
        type: "",
      },
      itemList: [
        "@/assets/images/pet1.jpeg",
        "@/assets/images/pet2.jpeg",
        "@/assets/images/pet3.jpeg",
        "@/assets/images/pet4.jpeg",
      ],
      username: "",
      selectedItem: "0",
    };
  },
  methods: {
    changeDash() {
      this.dash = !this.dash;
    },
    handleClickItem(label) {
      this.$refs.carousel.setActiveItem(label);
    },
    carouselChange(cur) {
      this.selectedItem = cur;
    },
  },
  mounted() {
    if (localStorage.getItem("username")) {
      this.username = localStorage.getItem("username");
    }
    if (!localStorage.getItem("avatar")) {
      axios
        .get("http://101.42.118.80:8000/get_avatar/", {
          params: {
            username: this.username,
          },
        })
        .then((res) => {
          if (res.data["status"] === "ok") {
            if (res.data["avatar"]) {
              this.image.src = "data:image/png;base64," + res.data["avatar"];
              localStorage.setItem("avatar", this.image.src);
            }
          }
        });
    } else {
      this.image.src = localStorage.getItem("avatar");
    }
  },
};
</script>

<style scoped>
.container {
  margin: 0;
  height: 100%;
}
.type-box {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.radio-area {
  margin: 20px 0 20px 0;
}
.basic-types-area {
  margin-top: 60px;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.custom-title-outer {
  padding-top: 50px;
}

/* 小屏幕手机端 */
@media (min-width: 0px) and (max-width: 768px) {
  .custom-box {
    border-radius: 20px;
    height: 260px;
    width: 80%;
    margin-left: 10%;
    box-shadow: 0 0 5px 1px rgba(0, 0, 0, 0.2);
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .custom-title {
    font-family: YouSheRound;
    font-size: 1.5rem;
    color: #5eabbf;
  }
  .round-background {
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #ffffff;
    box-shadow: 0 0 6px 1px rgba(0, 0, 0, 0.4);
    border-radius: 50px;
    width: 3rem;
    height: 3rem;
  }
  .icon {
    width: 2em;
    height: 2em;
    vertical-align: -0.15em;
    fill: currentColor;
    overflow: hidden;
  }
  .custom-row {
    width: 90%;
    padding-top: 40px;
  }
  .round-back-font {
    padding-top: 10px;
    width: 100%;
    font-size: 1.2rem;
    text-align: center;
    font-family: YouSheBlack;
    color: #e8bf19;
  }
  .basic-types-title {
    font-family: YouSheBlack;
    color: #5eabbf;
    font-size: 1.5rem;
  }
  :deep .el-radio-button__inner {
    font-size: 0.6rem;
  }
  .image{
    width: 100%;
  }
  .carousel-item-title {
    text-align: left;
    font-size: 0.9rem;
    font-family: XiaWuManHei;
    font-weight: bold;
    margin: 0 0 0 10px;
  }
  .tag-area {
    display: flex;
    margin: 8px 0 0 8px;
    justify-content: flex-start;
  }
  .basic-types-content {
    width: 90%;
  }
  :deep .el-tag__content {
    font-size:5px;
  }
  .carousel-item-content {
    text-align: left;
    font-size: 0.5em;
    margin: 4px 0 0 10px;
  }
}
/* 大屏幕（大桌面显示器，大于等于 1200px） */
@media (min-width: 768px) {
  .custom-box {
    border-radius: 20px;
    height: 380px;
    width: 60%;
    margin-left: 20%;
    box-shadow: 0 0 5px 1px rgba(0, 0, 0, 0.2);
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .custom-title {
    font-family: YouSheRound;
    font-size: 36px;
    color: #5eabbf;
  }
  .round-background {
    top: 50px;
    background-color: #ffffff;
    box-shadow: 0 0 6px 1px rgba(0, 0, 0, 0.4);
    border-radius: 50px;
    width: 100px;
    height: 100px;
  }
  .icon {
    width: 3em;
    height: 3em;
    margin-top: 24px;
    vertical-align: -0.15em;
    fill: currentColor;
    overflow: hidden;
  }
  .custom-row {
    width: 90%;
    padding-top: 58px;
  }
  .round-back-font {
    padding-top: 10px;
    width: 100%;
    font-size: 26px;
    text-align: center;
    font-family: YouSheBlack;
    color: #e8bf19;
  }
  .basic-types-title {
    font-family: YouSheBlack;
    color: #5eabbf;
    font-size: 32px;
  }
  .image{
    width: 360px;
    height: 280px;
  }
  .carousel-item-title {
    text-align: left;
    font-size: 24px;
    font-family: XiaWuManHei;
    font-weight: bold;
    margin: 40px 0 0 20px;
  }
  .tag-area {
    display: flex;
    margin: 20px 0 0 15px;
    justify-content: flex-start;
  }
  .basic-types-content {
    width: 70%;
  }
  .carousel-item-content {
    text-align: left;
    margin: 30px 70px 0 10px;
  }
}

.main-style {
  background-color: transparent;
}
.header-style {
  background-image: url(@/assets/images/nav-background.png);
  background-size: cover;
  height: 60px;
  box-shadow: 0 0px 8px 0;
  display: flex;
}
</style>
