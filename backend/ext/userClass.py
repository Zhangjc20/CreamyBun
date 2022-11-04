class User:
    def __init__(self,ID,username,password,email): #只能在注册后调用该类创建一个用户
        self.ID=ID
        self.username=username
        self.password=password
        self.email=email
        self.moblie_number=None
        self.donut_number=0
        self.credit_rank=1
        self.current_exp=0
        self.dark_mode=False
        self.today_violation=0 #该用户当天已违规次数
        self.task_info=[] #该用户所拥有的所有任务信息，该列表增加的成员为字典类型，表示{任务id:任务状态（已领取或已发布）}

        # 如何设置用户当天已违规次数定时刷新为0？