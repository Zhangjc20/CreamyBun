const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    open: true,           // 是否自动打开项目
    host: '127.0.0.1',      // 制定域名
    port: 8081,           // 端口号
    proxy: { //配置跨域
      '/log_up': {
        target: 'http://localhost:8000/log_up', //填写请求的目标地址
        changOrigin: true, //允许跨域
        pathRewrite: {
          '^/log_up': '' //请求的时候使用这个api就可以
        }
      },
      '/get_material_zip/': {
        target: 'http://localhost:8000/get_material_zip/', //填写请求的目标地址
        changOrigin: true, //允许跨域
        pathRewrite: {
          '^/get_material_zip': '' //请求的时候使用这个api就可以
        }
      },
    }
  }
})
