from django.db import models
from ..variables.globalConstants import MAX_ANSWER_LENGTH

class KeyToValue(models.Model):
    key = models.BigIntegerField(default=-1)
    value = models.IntegerField(default=0)

class Str(models.Model):
    str_content = models.CharField(max_length=MAX_ANSWER_LENGTH,default="")

class Int(models.Model):
    int_content = models.IntegerField(default=-1)