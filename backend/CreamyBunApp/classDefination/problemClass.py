from ..variables.globalConstants import NOT_RECEIVED
from .questionClass import *

class Problem(models.Model):
    index = models.BigIntegerField(default=-1) # 该problem在task内的序号，从1开始好了
    is_test = models.BooleanField(default=False) # 本题是否为测试题
    material_info = models.ManyToManyField(MaterialDict) # 资源路径列表
    receiver = models.BigIntegerField(default=-1) # 领取者id，领取者唯一
    current_state = models.IntegerField(default=NOT_RECEIVED) # 该problem当前状态，默认未领取
    question_list = models.ManyToManyField(Question) # 小题列表，成员为Question类的子类
