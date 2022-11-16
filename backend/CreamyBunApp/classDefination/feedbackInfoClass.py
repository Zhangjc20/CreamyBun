from django.db import models
from ..variables.globalConstants import *

# 存储反馈信息的类
class FeedbackInfo(models.Model):
    feedback_type = models.IntegerField(default=0)
    description = models.CharField(max_length=MAX_DESCRIPTION_LENGTH,default="no description")
    image_url = models.CharField(max_length=MAX_URL_LENGTH,default="image")
    inform_email = models.CharField(max_length=MAX_EMAIL_LENGTH,default="email")
    advice = models.CharField(max_length=MAX_DESCRIPTION_LENGTH,default="")