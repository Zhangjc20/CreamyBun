from .universalClass import *
from ..variables.globalConstants import MAX_CHOICE_NUMBER,MAX_DESCRIPTION_LENGTH,MAX_ANSWER_LENGTH

class Question(models.Model):
    index = models.BigIntegerField(default=-1) # 该question在problem内的序号，从1开始好了
    question_type = models.IntegerField(default=0)
    description = models.CharField(max_length=MAX_DESCRIPTION_LENGTH,default="no description") # 题干
    must_do = models.BooleanField(default=False)
    answer = models.CharField(max_length=MAX_ANSWER_LENGTH,default="")# 领取者作答的答案，答案统一为字符串
    standard_answer = models.CharField(max_length=MAX_CHOICE_NUMBER,default="") # 如果是测试题，会有标答，否则为空

class ChoiceQuestion(Question):
    option_list = models.ManyToManyField(StringToString) # 选项列表，成员为字典，如{A:xxxxx}，{B:xxxxx}等
    min_option_num = models.IntegerField(default=MAX_CHOICE_NUMBER) # 最少需要选择的选项数
    max_option_num = models.IntegerField(default=0) # 最多需要选择的选项数

class FillBlankQuestion(Question):
    min_answer_length = models.IntegerField(default=MAX_ANSWER_LENGTH)
    max_answer_length = models.IntegerField(default=0)

class FrameSelectionQuestion(Question):
    # 框图题可以框多个框
    picture_index = models.IntegerField(default=-1) # 这题框图题指向哪张图片
    min_frame_number = models.IntegerField(default=MAX_FRAME_NUM)
    max_frame_number = models.IntegerField(default=0)

