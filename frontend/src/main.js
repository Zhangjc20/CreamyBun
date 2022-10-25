import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import "@/assets/icons/iconfont.js";
import "@/assets/icons/iconfont.css";

const app = createApp(App)
app.use(ElementPlus)
app.use(router).mount('#app')
