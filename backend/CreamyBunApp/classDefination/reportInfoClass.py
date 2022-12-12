from .questionClass import *
from ..variables.globalConstants import *

# 存储举报任务信息的类
class ReportInfo(models.Model):
    description = models.CharField(max_length=MAX_DESCRIPTION_LENGTH,default="no description")
    image_url = models.CharField(max_length=MAX_URL_LENGTH,default="image")
    reporter_name = models.CharField(max_length=12,default="image")
    task_id = models.BigIntegerField(default=-1)