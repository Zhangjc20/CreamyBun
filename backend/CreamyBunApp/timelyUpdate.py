# 定义定时刷新的函数
from .function.databaseOperations import *

# 每日的定时刷新
def daily_update():
    # 刷新签到信息
    user_list = User.objects.all()
    for u in user_list:
        u.reset_clock_in_info()