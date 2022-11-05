# 在此处定义全局通用函数

import datetime

# 获取系统当前时间，为datetime相关类型
# 可通过成员变量获取年月日时分秒等属性，通过strftime转成字符串
def get_now_time():
    return datetime.datetime.now()