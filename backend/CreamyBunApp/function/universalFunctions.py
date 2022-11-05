# 在此处定义全局通用函数

import datetime
import random
from django.core.mail import send_mail

# 获取系统当前时间，为datetime相关类型
# 可通过成员变量获取年月日时分秒等属性，通过strftime转成字符串返回
# 参考https://www.cnblogs.com/jszfy/p/11143048.html
def get_now_time():
    return datetime.datetime.now().strftime('%F %T')

#发送邮件并返回验证码
def send_email(email):
    code_base = '0123456789'
    varify_code = ''
    for i in range(0, 6):
        varify_code += code_base[random.randrange(0, len(code_base))]
    
    # 发送邮件：
    # send_mail的参数分别是  邮件标题，邮件内容，发件箱(settings.py中设置过的那个)，收件箱列表(可以发送给多个人),失败静默(若发送失败，报错提示我们)
    message = "您的验证码是" + varify_code + "，10分钟内有效，请尽快填写"
    emailBox = []
    emailBox.append(email)
    send_mail('奶黄包数据标注平台邮箱验证码', message, '1596741408@qq.com', emailBox, fail_silently=False)
    return varify_code
    