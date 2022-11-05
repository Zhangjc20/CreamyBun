from .problemClass import *
from ..variables.globalConstants import MAX_TASK_NAME_LENGTH,MAX_DESCRIPTION_LENGTH,\
                                        MAX_TIME_STRING_LENGTH

class Task(models.Model):
    poster = models.BigIntegerField(default=-1) # 发布者的id
    task_name = models.CharField(max_length = MAX_TASK_NAME_LENGTH,default="task_name") # 任务名
    description = models.CharField(max_length = MAX_DESCRIPTION_LENGTH,default="task_description") # 任务描述

    # 通过以下两个变量计算该任务的完成程度
    problem_total_number = models.IntegerField(default=-1) # 任务中大题总数
    finished_problem_number = models.IntegerField(default=0) # 任务中已经完成的大题数

    # 每个用户每次可领取的题目数量
    problem_number_for_single_receiver = models.IntegerField(default=-1)

    star_rank = models.IntegerField(default=-1) # 任务星级
    single_bonus = models.IntegerField(default=-1) # 任务单题奖励
    release_mode = models.IntegerField(default=0) # 任务发布模式

    begin_time = models.CharField(max_length=MAX_TIME_STRING_LENGTH,default="begin_time") # 任务开始时间
    end_time = models.CharField(max_length=MAX_TIME_STRING_LENGTH,default="end_time") # 任务结束时间

    receiver_list = models.ManyToManyField(Int) # 该任务的所有领取者，成员为用户ID
    problem_list = models.ManyToManyField(Problem) # 该任务的所有大题，成员为Problem类实例
