const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    open: true,           // 是否自动打开项目
    host: '127.0.0.1',      // 制定域名
    port: 8081,           // 端口号
  }
})
