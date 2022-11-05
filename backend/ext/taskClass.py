class Task:
    def __init__(self,ID,poster,task_name,description,problem_total_number,star_rank,single_bonus,release_mode,begin_time,end_time):
        self.ID=ID
        self.poster=poster #发布者的id
        self.task_name=task_name
        self.description=description

        # 通过以下两个变量计算该任务的完成程度
        self.problem_total_number=problem_total_number
        self.finished_problem_number=0

        self.star_rank=star_rank
        self.single_bonus=single_bonus
        self.release_mode=release_mode #见相关常量

        # 该时间须使用datetime.datetime.now()得到，可通过成员变量获取年月日时分秒等属性，通过strftime转成字符串
        # 或者通过前端获取的年月日时分秒等属性转成datetime相关类型
        # 参考https://www.cnblogs.com/jszfy/p/11143048.html
        self.begin_time=begin_time
        self.end_time=end_time
         
        self.receiver_list=[] # 该任务的所有领取者，成员为用户ID
        self.problem_list=[] # 该任务的所有大题，成员为Problem类实例