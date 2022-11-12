import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import "@/assets/icons/iconfont.js";
import "@/assets/icons/iconfont.css";
import * as ElementPlusIconsVue from '@element-plus/icons-vue';
import { Cropper,Preview,CircleStencil } from "vue-advanced-cropper";
import "vue-advanced-cropper/dist/style.css";
import { vfmPlugin } from 'vue-final-modal';

const app = createApp(App)
app.component('image-cropper', Cropper)
app.component('image-preview', Preview)
app.component('CircleStencil', CircleStencil)
app.use(vfmPlugin)
app.use(ElementPlus)
app.use(router).mount('#app')
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
  }