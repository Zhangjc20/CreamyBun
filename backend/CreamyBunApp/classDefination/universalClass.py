from django.db import models
from ..variables.globalConstants import *

class TaskDict(models.Model):
    task_id = models.BigIntegerField(default=-1)
    task_status_for_user = models.IntegerField(default=0) # 已领取或已发布
    task_status_for_itself = models.IntegerField(default=-1) # 二级检索，发布模式或者完成状态

class StringToString(models.Model):
    key = models.CharField(max_length=MAX_DESCRIPTION_LENGTH,default="")
    value = models.CharField(max_length=MAX_DESCRIPTION_LENGTH,default="")

class Str(models.Model):
    str_content = models.CharField(max_length=MAX_ANSWER_LENGTH,default="")

class Int(models.Model):
    int_content = models.IntegerField(default=-1)