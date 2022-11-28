const { defineConfig } = require('@vue/cli-service')
require('events').EventEmitter.defaultMaxListeners = 0; // 解除限制
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    open: true,           // 是否自动打开项目
    host: '127.0.0.1',      // 制定域名
    port: 8081,           // 端口号
    proxy: { //配置跨域
      '/log_up': {
        target: 'http://localhost:8000/log_up/', //填写请求的目标地址
        changOrigin: true, //允许跨域
        pathRewrite: {
          '^/log_up': '' //请求的时候使用这个api就可以
        }
      },
      '/log_in': {
        target: 'http://localhost:8000/log_in/', //填写请求的目标地址
        changOrigin: true, //允许跨域
        pathRewrite: {
          '^/log_in': '' //请求的时候使用这个api就可以
        }
      },
      '/get_current_rate_info': {
        target: 'http://localhost:8000/get_current_rate_info/', //填写请求的目标地址
        changOrigin: true, //允许跨域
        pathRewrite: {
          '^/get_current_rate_info': '' //请求的时候使用这个api就可以
        }
      },
      '/change_current_rate_info': {
        target: 'http://localhost:8000/change_current_rate_info/', //填写请求的目标地址
        changOrigin: true, //允许跨域
        pathRewrite: {
          '^/change_current_rate_info': '' //请求的时候使用这个api就可以
        }
      },
      '/add_reported_task': {
        target: 'http://localhost:8000/add_reported_task/', //填写请求的目标地址
        changOrigin: true, //允许跨域
        pathRewrite: {
          '^/add_reported_task': '' //请求的时候使用这个api就可以
        }
      },
      '/get_reported_task': {
        target: 'http://localhost:8000/get_reported_task/', //填写请求的目标地址
        changOrigin: true, //允许跨域
        pathRewrite: {
          '^/get_reported_task': '' //请求的时候使用这个api就可以
        }
      },
      '/delete_reported_task': {
        target: 'http://localhost:8000/delete_reported_task/', //填写请求的目标地址
        changOrigin: true, //允许跨域
        pathRewrite: {
          '^/delete_reported_task': '' //请求的时候使用这个api就可以
        }
      },
      '/send_report_email': {
        target: 'http://localhost:8000/send_report_email/', //填写请求的目标地址
        changOrigin: true, //允许跨域
        pathRewrite: {
          '^/send_report_email': '' //请求的时候使用这个api就可以
        }
      },
      '/receive_task': {
        target: 'http://localhost:8000/receive_task/', //填写请求的目标地址
        changOrigin: true, //允许跨域
        pathRewrite: {
          '^/receive_task': '' //请求的时候使用这个api就可以
        }
      },
      '/get_examining_tasks': {
        target: 'http://localhost:8000/get_examining_tasks/', //填写请求的目标地址
        changOrigin: true, //允许跨域
        pathRewrite: {
          '^/get_examining_tasks': '' //请求的时候使用这个api就可以
        }
      },
      '/get_task_basic_info': {
        target: 'http://localhost:8000/get_task_basic_info/', //填写请求的目标地址
        changOrigin: true, //允许跨域
        pathRewrite: {
          '^/get_task_basic_info': '' //请求的时候使用这个api就可以
        }
      },
      '/get_sorted_tasks': {
        target: 'http://localhost:8000/get_sorted_tasks/', //填写请求的目标地址
        changOrigin: true, //允许跨域
        pathRewrite: {
          '^/get_sorted_tasks': '' //请求的时候使用这个api就可以
        }
      },
      '/get_user_basic_info': {
        target: 'http://localhost:8000/get_user_basic_info/', //填写请求的目标地址
        changOrigin: true, //允许跨域
        pathRewrite: {
          '^/get_user_basic_info': '' //请求的时候使用这个api就可以
        }
      },
      '/get_user_activity_info': {
        target: 'http://localhost:8000/get_user_activity_info/', //填写请求的目标地址
        changOrigin: true, //允许跨域
        pathRewrite: {
          '^/get_user_activity_info': '' //请求的时候使用这个api就可以
        }
      },
      '/get_user_received_task_info': {
        target: 'http://localhost:8000/get_user_received_task_info/', //填写请求的目标地址
        changOrigin: true, //允许跨域
        pathRewrite: {
          '^/get_user_received_task_info': '' //请求的时候使用这个api就可以
        }
      },
      '/get_user_released_task_info': {
        target: 'http://localhost:8000/get_user_released_task_info/', //填写请求的目标地址
        changOrigin: true, //允许跨域
        pathRewrite: {
          '^/get_user_released_task_info': '' //请求的时候使用这个api就可以
        }
      },
      '/get_user_bonus_info': {
        target: 'http://localhost:8000/get_user_bonus_info/', //填写请求的目标地址
        changOrigin: true, //允许跨域
        pathRewrite: {
          '^/get_user_bonus_info': '' //请求的时候使用这个api就可以
        }
      },
      '/reset_password': {
        target: 'http://localhost:8000/reset_password/', //填写请求的目标地址
        changOrigin: true, //允许跨域
        pathRewrite: {
          '^/reset_password': '' //请求的时候使用这个api就可以
        }
      },
      '/update_username': {
        target: 'http://localhost:8000/update_username/', //填写请求的目标地址
        changOrigin: true, //允许跨域
        pathRewrite: {
          '^/update_username': '' //请求的时候使用这个api就可以
        }
      },
      '/update_email': {
        target: 'http://localhost:8000/update_email/', //填写请求的目标地址
        changOrigin: true, //允许跨域
        pathRewrite: {
          '^/update_email': '' //请求的时候使用这个api就可以
        }
      },
      '/change_avatar': {
        target: 'http://localhost:8000/change_avatar/', //填写请求的目标地址
        changOrigin: true, //允许跨域
        pathRewrite: {
          '^/change_avatar': '' //请求的时候使用这个api就可以
        }
      },
      '/set_admin_username_and_password': {
        target: 'http://localhost:8000/set_admin_username_and_password/', //填写请求的目标地址
        changOrigin: true, //允许跨域
        pathRewrite: {
          '^/set_admin_username_and_password': '' //请求的时候使用这个api就可以
        }
      },
      '/get_admin_username_and_password': {
        target: 'http://localhost:8000/get_admin_username_and_password/', //填写请求的目标地址
        changOrigin: true, //允许跨域
        pathRewrite: {
          '^/get_admin_username_and_password': '' //请求的时候使用这个api就可以
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
