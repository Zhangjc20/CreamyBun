from .universalClass import *
from ..variables.globalConstants import MAX_CHOICE_NUMBER,MAX_DESCRIPTION_LENGTH,MAX_ANSWER_LENGTH

class Question(models.Model):
    index = models.BigIntegerField(default=-1) # 该question在problem内的序号
    question_type = models.IntegerField(default=0)
    description = models.CharField(max_length=MAX_DESCRIPTION_LENGTH,default="no description") # 题干
    must_do = models.BooleanField(default=False)

class ChoiceQuestion(Question):
    option_list = models.ManyToManyField(KeyToValue) # 选项列表，成员为字典，如{A:xxxxx}，{B:xxxxx}等
    min_option_num = models.IntegerField(default=MAX_CHOICE_NUMBER) # 最少需要选择的选项数
    max_option_num = models.IntegerField(default=0) # 最多需要选择的选项数
    answer = models.ManyToManyField(Str)# 领取者作答的答案，选择题为ABCD选项列表

class FillBlankQuestion(Question):
    answer = models.CharField(max_length=MAX_ANSWER_LENGTH,default="")# 领取者作答的答案，填空题答案为一个字符串

class FrameSelectionQuestion(Question):
    # （暂定）框图题回答的存储形式为一个坐标对，表示所框部分左上和右下的坐标
    left_up_coordinate_x = models.IntegerField(default=-1)
    left_up_coordinate_y = models.IntegerField(default=-1)
    right_down_coordinate_x = models.IntegerField(default=-1)
    right_down_coordinate_y = models.IntegerField(default=-1)

