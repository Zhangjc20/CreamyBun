# 在此处定义全局通用函数

import datetime
import random
from django.core.mail import send_mail
from databaseOperations import *
from ..variables.globalVariables import *

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

# 检查用户名和密码是否匹配
def match_username_with_password(username,password):
    cur_user = get_a_user_data(username)
    if cur_user.password == password:
        return True
    else:
        return False 

# 管理员修改指定等级的升级所需经验
def set_exp_for_upgrade(rank,exp):
    global exp_for_upgrade
    exp_for_upgrade[rank-1]=exp

# 管理员修改指定星级任务完成后可获得的经验值
def set_exp_by_task_rank(rank,exp):
    global exp_by_task_rank
    exp_by_task_rank[rank-1]=exp

# 管理员修改指定星级任务的单题保底甜甜圈报酬
def set_donut_from_a_problem_by_task_rank(rank,donut):
    global donut_from_a_problem_by_task_rank
    donut_from_a_problem_by_task_rank[rank-1]=donut

# 获取当前等级所需的升级经验
def get_exp_for_upgrade(rank):
    global exp_for_upgrade
    return exp_for_upgrade[rank-1]

# 获取当前星级任务完成后可获得的经验
def get_exp_by_task_rank(rank):
    global exp_by_task_rank
    return exp_by_task_rank[rank-1]

# 获取当前星级任务的单题保底甜甜圈报酬
def get_donut_from_a_problem_by_task_rank(rank):
    global donut_from_a_problem_by_task_rank
    return donut_from_a_problem_by_task_rank[rank-1]

# 管理员设置多少甜甜圈可兑换一元
def set_donut_to_money(donut_number):
    global donut_to_money
    donut_to_money=donut_number


# 获取多少甜甜圈可兑换一元
def get_donut_to_money():
    global donut_to_money
    return donut_to_money

# 管理员设置一元人民币可兑换的甜甜圈数量
def set_money_to_donut(donut_number):
    global money_to_donut
    money_to_donut = donut_number

# 获取一元人民币可兑换的甜甜圈数量
def get_money_to_donut():
    global money_to_donut
    return money_to_donut