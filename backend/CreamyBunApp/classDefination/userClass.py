from .universalClass import *

# 只能在注册后调用该类在数据库创建一个用户
class User(models.Model):
    # ID会自动生成
    # 以下传入的信息全都是经过检查，在此不作限制要求

    username = models.CharField(max_length=12,default="username")
    password = models.CharField(max_length=18,default="password")
    email = models.CharField(max_length=350,default="email")
    mobile_number = models.CharField(max_length=11,default="")
    donut_number = models.IntegerField(default=0)
    credit_rank = models.IntegerField(default=1)
    current_exp = models.IntegerField(default=0)
    dark_mode = models.BooleanField(default=False)
    today_violation = models.IntegerField(default=0) # 该用户当天已违规次数
    is_today_sign_in = models.BooleanField(default=False) # 用户当天是否已经签到
    continue_sign_in_days = models.IntegerField(default=0) # 用户当前连续签到天数

    # 该用户所拥有的所有任务信息，该列表增加的成员为字典类型，表示{任务id:任务状态（已领取或已发布）}
    # 该列表在数据库中的存储格式为字典，如“{1:HAS_POSTED} {2:HAS_RECEIVED}”
    task_info_list = models.ManyToManyField(BigIntToInt)

    # 如何设置用户当天已违规次数定时刷新为0（24：00）？