# 定义定时刷新的函数
from ..classDefination.userClass import *

# 每日的定时刷新
def daily_update(u:User, now_time:str, is_next_day:bool):
    # 刷新签到信息
    u.reset_clock_in_info(is_next_day)

    # 刷新违规信息
    u.reset_violation()

    # 刷新每日已完成任务数
    u.reset_finished_task_number()

    u.last_enter_activity_center_time = now_time
    u.save()