from django.db import models
from ..variables.globalConstants import *

class StringToString(models.Model):
    key = models.CharField(max_length=MAX_DESCRIPTION_LENGTH,default="")
    value = models.CharField(max_length=MAX_DESCRIPTION_LENGTH,default="")

class Str(models.Model):
    str_content = models.CharField(max_length=MAX_ANSWER_LENGTH,default="")

class Int(models.Model):
    int_content = models.BigIntegerField(default=-1)

class IntToInt(models.Model):
    key = models.BigIntegerField(default=-1)
    value = models.BigIntegerField(default=-1)

class TaskDict(models.Model):
    task_id = models.BigIntegerField(default=-1)
    task_status_for_user = models.IntegerField(default=0) # 已领取或已发布
    task_status_for_itself = models.IntegerField(default=-1) # 二级检索，发布模式或者完成状态

    # 领取任务中所有problem的id及其是否做对（如果为测试题）的列表
    received_problem_id_list = models.ManyToManyField(IntToInt) 

    # 当前做到第几题了，received_problem_id_list元素的index，注意0开始
    current_problem_index = models.BigIntegerField(default=0)
 
    test_problem_number = models.IntegerField(default=-1) # 资质测试的题目总数

class MaterialDict(models.Model):
    material_type = models.IntegerField(default=-1)
    material_path = models.CharField(max_length=MAX_URL_LENGTH,default="")
    material_note = models.CharField(max_length=MAX_DESCRIPTION_LENGTH,default="no description")