# 定义定时刷新的函数
from .function.databaseOperations import *

# 每日的定时刷新
def daily_update():
    user_list = User.objects.all()
    for u in user_list:

        # 刷新签到信息
        u.reset_clock_in_info()

        # 刷新违规信息
        u.reset_violation()