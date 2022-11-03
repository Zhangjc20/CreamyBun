from globalConstants import NOT_RECEIVED

class Problem:
    def __init__(self,index,material_path):
        self.index=index # 该problem在task内的序号
        self.material_path=material_path
        self.receiver=None # 该problem被谁领走了，领取者唯一
        self.current_state=NOT_RECEIVED
        self.question_list=[] # 小题列表，成员必须为Question类的子类