class Question:
    def __init__(self,index,question_type,description,must_do):
        self.index=index # 该question在problem内的序号
        self.question_type=question_type
        self.description=description # 题干
        self.must_do=must_do

class ChoiceQuestion(Question):
    def __init__(self,index,question_type,description,must_do,option_list,min_option_num,max_option_num): 
        super(ChoiceQuestion, self).__init__(index,question_type,description,must_do) # 调用父类init
        self.option_list=option_list # 选项列表，成员为字典，如{A:xxxxx}，{B:xxxxx}等
        self.min_option_num=min_option_num
        self.max_option_num=max_option_num
        self.answer=None # 领取者作答的答案，选择题为ABCD选项

class FillBlankQuestion(Question):
    def __init__(self,index,question_type,description,must_do,):
        super(FillBlankQuestion, self).__init__(index,question_type,description,must_do)
        self.answer=None # 填空题答案为一个字符串

class FrameSelectionQuestion(Question):
    def __init__(self,index,question_type,description,must_do,):
        super(FrameSelectionQuestion, self).__init__(index,question_type,description,must_do)
        self.answer=None # （暂定）该回答的存储形式为一个坐标对，表示所框部分左上和右下的坐标
