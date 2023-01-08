# 在此处定义可修改的全局变量

# 各等级升级所需经验
exp_for_upgrade = [100,500,2000,6000,15000]

# 最高等级
max_credit_rank = len(exp_for_upgrade) + 1

# 惩罚扣除当前等级经验比例
punish_sub_rank_rate = 0.05

# 用户一天最多可违规次数
violation_number_per_day = 3

# 各星级任务完成后可获得的经验值，下标从0开始，用任务星级作为下标时务必记得减一
exp_by_task_rank = [10,20,40,70,100]

# 各星级任务的单题保底甜甜圈报酬
donut_from_a_problem_by_task_rank = [5,7,10,12,15]

# 一周每天签到可获得的甜甜圈数量
donut_for_clock_in = [5,10,20,40,60,80,100]

# 每日任务可获得甜甜圈数量
finish_task_donut = [50,100]

# 一元人民币可兑换的甜甜圈数量
money_to_donut = 100

# 多少甜甜圈可兑换一元
donut_to_money = 120

# 管理员用户名
admin_username = "admin"

# 管理员密码
admin_password = "123456"

# 管理员密令
admin_token = "MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBA"