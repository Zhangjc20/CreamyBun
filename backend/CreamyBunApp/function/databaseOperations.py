# 在此处定义对数据库的操作

from ..classDefination.userClass import *
from ..classDefination.taskClass import *
from ..classDefination.questionClass import *
from ..classDefination.feedbackInfoClass import *
from ..classDefination.reportInfoClass import *
from ..variables.globalVariables import *
from ..variables.globalConstants import *
import math
import datetime
import random


# 添加一个用户到用户列表中
def add_a_user(username, password, email):
    try:
        User.objects.create(username=username, password=password, email=email)
        return True
    except:
        return False

# 通过用户名检查用户是否存在
def exist_user_by_name(username):
    try:
        User.objects.get(username=username)
        return True
    except:
        return False

# 通过手机号检查用户是否存在
def exist_user_by_mobile_number(mobile_number):
    try:
        User.objects.get(mobile_number=mobile_number)
        print(User.objects.get(mobile_number=mobile_number).username)
        print(mobile_number)
        return True
    except:
        return False

# 通过邮箱检查用户是否存在
def exist_user_by_email(email):
    try:
        User.objects.get(email=email)
        return True
    except:
        return False
    
def get_a_reported_task(report_id):
    return ReportInfo.objects.filter(id=report_id).first()

def delete_a_reported_task(report_id):
    ReportInfo.objects.filter(id=report_id).first().delete()

def get_reported_task_list(page_number):
    all_report_id_list = [[x.id,x.task_id] for x in ReportInfo.objects.all()]
    total_number = len(all_report_id_list)
    if page_number * 10 > len(all_report_id_list):
        all_report_id_list = all_report_id_list[10*(page_number-1):]
    else:
        all_report_id_list = all_report_id_list[10*(page_number-1):10*page_number]
    init_list = []
    for i, x in enumerate(all_report_id_list):
        t = get_a_task_data(x[1])
        t_info = {
            'index': i,
            'isSpace': False,
            'id': t.id,
            'taskName': t.task_name,
            'starNum': t.star_rank,
            'donut': t.single_bonus,
            'dataType': TASK_TYPE_DICT[t.task_type],
            'problemType': ANSWER_TYPE_DICT[t.answer_type],
            'startTime': t.begin_time.split(" ")[0],
            'endTime': t.end_time.split(" ")[0],
            'reportId':x[0],
            'taskStatus':get_task_status(t),
        }
        init_list.append(t_info)
    length = len(all_report_id_list)
    if length < 10:
        for i in range( 10 - length):
            init_list.append({'isSpace':True,'index': length + i})
    return total_number, init_list

# 获得某任务的已领取题目数量
def get_task_received_number(t:Task):
    has_received_problem_number = len(t.receiver_list.all())*t.problem_number_for_single_receiver
    if has_received_problem_number > t.problem_total_number:
        has_received_problem_number = t.problem_total_number
    return has_received_problem_number

# 通过id获取某任务的领取进度，百分比数字
def get_task_receive_process_by_id(id):
    t = get_a_task_data(id)
    has_received_problem_number = get_task_received_number(t)
    receive_process = round(has_received_problem_number/t.problem_total_number,4)*100
    return receive_process

# 获取用户领了多少题目，当前做到第几题
def get_user_received_problem_info(username,sort_choice,task_index):
    user_current_problem_finish_number = 0
    user_received_total_problem_number = -1
    u = get_a_user_data(username)

    # 对指定任务的所有领取情况
    td_received_list = u.task_info_list.filter(task_status_for_user=HAS_RECEIVED)

    # sort_choice: int,0是所有 1是正在进行，2是已结束
    if sort_choice != 0:
        td_received_list = td_received_list.filter(task_status_for_itself=sort_choice)
    
    td_received_list = list(reversed(list(td_received_list.all())))
    td = td_received_list[task_index]

    user_received_total_problem_number = len(td.received_problem_id_list.all())-td.test_problem_number

    for i,upinfo in enumerate(td.received_problem_id_list.all()):
        if i >= td.test_problem_number and upinfo.is_right != -1:
            user_current_problem_finish_number += 1
    
    return user_current_problem_finish_number, user_received_total_problem_number, td.task_status_for_itself

# 从用户列表中删除指定用户
def delete_a_user(username):
    User.objects.filter(username=username).delete()

# 用户增加甜甜圈
def add_donut_for_user(u:User,donut_add_number):
    u.donut_number += donut_add_number
    u.save()

# 用户充值
def user_top_up(username,money_number):
    u = get_a_user_data(username)
    add_donut_for_user(u,money_number * money_to_donut)
    return u.donut_number

# 用户减少甜甜圈
def sub_donut_for_user(u:User,donut_sub_number):
    if u.donut_number >= donut_sub_number:
        u.donut_number -= donut_sub_number
        u.save()
        return True
    else:
        return False

# 用户提现
def user_withdraw_money(username,money_number):
    u = get_a_user_data(username)
    is_success = sub_donut_for_user(u,money_number * donut_to_money)
    return is_success, u.donut_number


# 获得用户当前正在做的任务信息
def get_user_now_taskdict(u:User,task_id):
    td_temp = u.task_info_list.filter(task_id=task_id)  
    td_temp2 = td_temp.filter(task_status_for_user=HAS_RECEIVED)
    td = td_temp2.filter(task_status_for_itself=NOT_FINISHED).first()
    return td

# 将用户领取的某任务的题目打回
def remove_task_from_user(username,task_id):
    u = get_a_user_data(username)
    t = get_a_task_data(task_id)

    # 获得用户正在做的任务的信息
    td = get_user_now_taskdict(u,task_id)

    for x in td.received_problem_id_list.all():
        p = t.problem_list.filter(id=x.problem_id).first()
        p.current_state = NOT_RECEIVED
        p.save()
        td.received_problem_id_list.remove(x)
    td.save()

    # 用户删除领取的任务
    u.task_info_list.remove(td)

    # 任务删除其领取者
    u_id = t.receiver_list.filter(int_content=u.id).last()
    t.receiver_list.remove(u_id)

# 在用户穿插测试没通过的时候惩罚用户
def punish_user_by_rank(u:User):
    # flag表示是否进行了惩罚，因为一天内违规violation_number_per_day次才会惩罚
    flag, today_violation_number = u.punish_for_insertion_test()
    return flag, today_violation_number

# 做完任务时奖励用户
def reward_user(u:User,t:Task,common_problem_number):
    # 加经验
    is_upgrade, now_credit_rank =  u.add_exp_and_upgrade(exp_by_task_rank[t.star_rank - 1])
    # 加甜甜圈代币
    get_donut_num = t.single_bonus*common_problem_number
    add_donut_for_user(u,get_donut_num)
    return is_upgrade, now_credit_rank, exp_by_task_rank[t.star_rank - 1], get_donut_num
    
# 向某个小题写入答案
def write_answer(q:Question,user_ans):
    q.answer = user_ans
    q.save()

# 获取指定用户的数据
# 返回的对象可以通过.获取成员变量
def get_a_user_data(username):
    return User.objects.filter(username=username).first()

# 通过id获得用户
def get_a_user_data_by_id(id):
    return User.objects.filter(id=id).first()

# 获取指定大题
def get_a_problem_data(id):
    return Problem.objects.filter(id=id).first()

# 获取指定任务的数据
def get_a_task_data(id):
    return Task.objects.filter(id=id).first()

# 更新任务状态
def update_task_status(t:Task,task_status):
    # 如果结束了，所有领取者和发布者的所有相关任务dict状态均要更新为结束
    if task_status == OVER:
        for u in User.objects.all():
            td_list = u.task_info_list.filter(task_id=t.id).all()
            for td in td_list:
                if td.task_status_for_user == HAS_POSTED:
                    td.task_status_for_itself = OVER
                else:
                    td.task_status_for_itself = HAS_FINISHED
                td.save()
    # 如果是未发布的任务发布了，发布者那边的状态也需要更新
    elif task_status == RELEASE_BUT_NOT_OVER and t.task_status == NOT_RELEASE_YET:
        u = get_a_user_data_by_id(t.poster)
        td = u.task_info_list.filter(task_id=t.id).filter(task_status_for_user=HAS_POSTED).first()
        td.task_status_for_itself = RELEASE_BUT_NOT_OVER
        td.save()

    t.task_status = task_status
    t.save()

# 获取指定任务的状态
def get_task_status(t:Task):
    current_time = datetime.datetime.now().strftime('%F %T')
    task_status = RELEASE_BUT_NOT_OVER
    if t.begin_time > current_time or t.begin_time == "begin_time":
        task_status =  NOT_RELEASE_YET
    elif t.end_time <= current_time or t.finished_problem_number == t.problem_total_number:
        task_status =  OVER
    
    if t.task_status != task_status:
        update_task_status(t,task_status)

    return task_status

# 通过用户名修改密码
def update_password_by_username(username, password):
    User.objects.filter(username=username).update(password=password)


# 通过用户名修改用户名
def update_username_by_username(username, new_username):
    User.objects.filter(username=username).update(username=new_username)


# 通过用户名修改邮箱
def update_email_by_username(username, new_email):
    User.objects.filter(username=username).update(email=new_email)

# 通过用户名修改用户手机号
def update_user_by_mobile_number(username, new_mobile):
    User.objects.filter(username=username).update(mobile_number=new_mobile)

# 通过邮箱修改密码
def update_password_by_email(email, password):
    User.objects.filter(email=email).update(password=password)

# 通过用户名修改用户头像url
def update_avatar_url_by_username(username, avatar_url):
    User.objects.filter(username=username).update(avatar_url=avatar_url)

# 检查用户名和密码是否匹配
def match_username_with_password(username, password):
    cur_user = get_a_user_data(username)
    return cur_user.validate_password(password)

# 让用户签到
def update_clock_in_info(username):
    u = get_a_user_data(username)
    if not u.is_today_sign_in:
        u.is_today_sign_in = True
        u.continue_sign_in_days += 1
    return u.is_today_sign_in, u.continue_sign_in_days

# 修改指定用户的手机号
def update_mobile_number_of_a_user(username, mobile_number):
    User.objects.filter(username=username).update(mobile_number=mobile_number)

# 创建一个任务举报
def create_a_reported_task(description,task_id,image_url,username):
    ReportInfo.objects.create(description=description,task_id=task_id,image_url=image_url,reporter_name=username)

# 创建一个任务
def create_task(request_body):
    basic_info_form = request_body["basicInfoForm"]

    # 获得发布者id
    poster_name = basic_info_form["poster"]
    poster_id = get_a_user_data(poster_name).id

    task_name = basic_info_form["taskName"]
    description = basic_info_form["description"]
    cover_url = basic_info_form['coverUrl']
    task_type = basic_info_form["materialType"]
    answer_type = basic_info_form["questionType"]
    problem_total_number = basic_info_form["problemTotalNum"]

    star_rank = basic_info_form["starRank"]
    single_bonus = basic_info_form["singleBonus"]
    release_mode = basic_info_form["releaseModeInt"]

    # 获得开始时间
    if release_mode == TIMED_RELEASE:
        temp_begin_time = []
        temp_begin_time.append(basic_info_form["startLine1"])
        temp_begin_time.append(basic_info_form["startLine2"])
        begin_time = " ".join(temp_begin_time)
        task_status = NOT_RELEASE_YET
    elif release_mode == NOW_RELEASE:
        begin_time = datetime.datetime.now().strftime('%F %T')
        task_status = RELEASE_BUT_NOT_OVER
    else: # 暂不发布
        begin_time = "begin_time"
        task_status = NOT_RELEASE_YET

    # 获得结束时间
    temp_end_time = []
    temp_end_time.append(basic_info_form["deadLine1"])
    temp_end_time.append(basic_info_form["deadLine2"])
    end_time = " ".join(temp_end_time)

    # 这个返回值是一个task对象
    t = Task.objects.create(poster=poster_id, task_name=task_name, description=description, \
                            task_type=task_type, answer_type=answer_type, problem_total_number=problem_total_number, \
                            star_rank=star_rank, single_bonus=single_bonus, release_mode=release_mode, \
                            begin_time=begin_time, end_time=end_time, cover_url=cover_url,\
                            task_status=task_status)

    question_info = request_body["questionList"]
    material_info = request_body["fullList"]
    note_info = request_body["listList"]

    # 向task中加入problem
    for i in range(problem_total_number):
        p = Problem.objects.create(index=(i + 1))

        # 向problem中加入question
        for q_info in question_info:
            q_type = q_info["questionType"]
            q_option_list_info = q_info["optionList"]

            # 创建每个小题
            if q_type == SINGLE_CHOICE:  # 单选
                q = ChoiceQuestion.objects.create( \
                    index=q_info["index"], question_type=CHOICE_QUESTION, \
                    description=q_info["questionDescription"], must_do=q_info["mustDo"], \
                    min_option_num=1, max_option_num=1)
                for q_op in q_option_list_info:
                    sts = StringToString.objects.create(key=q_op["name"], value=q_op["content"])
                    q.option_list.add(sts)

            elif q_type == SEVERAL_CHOICES:  # 多选
                q = ChoiceQuestion.objects.create( \
                    index=q_info["index"], question_type=CHOICE_QUESTION, \
                    description=q_info["questionDescription"], must_do=q_info["mustDo"], \
                    min_option_num=q_info["minOptionNum"], max_option_num=q_info["maxOptionNum"])
                for q_op in q_option_list_info:
                    sts = StringToString.objects.create(key=q_op["name"], value=q_op["content"])
                    q.option_list.add(sts)

            elif q_type == FILL_BLANK:
                q = FillBlankQuestion.objects.create(
                    index=q_info["index"], question_type=FILL_BLANK_QUESTION,
                    description=q_info["questionDescription"], must_do=q_info["mustDo"],
                    min_answer_length=q_info["minOptionNum"], max_answer_length=q_info["maxOptionNum"])

            elif q_type == SELECT_FRAME:
                q = FrameSelectionQuestion.objects.create( \
                    index=q_info["index"], question_type=SELECT_FRAME_QUESTION, \
                    description=q_info["questionDescription"], must_do=q_info["mustDo"], \
                    min_frame_number=q_info["minOptionNum"], max_frame_number=q_info["maxOptionNum"], \
                    picture_index=q_info["targetIndex"])

            p.question_list.add(q)

        # 向problem中加入material
        for j,m_info in enumerate(material_info):
            m = m_info[i]
            n = note_info[j]
            m_dict = MaterialDict.objects.create(material_path=m["filePath"], material_type=m["fileType"],
                                                 material_note=n['notes'])
            p.material_info.add(m_dict)

        t.problem_list.add(p)

    # 确定哪些题目为测试题并设置标答
    test_info = request_body["testList"]
    problem_list = t.problem_list.all()
    for p_info in test_info:

        t.test_problem_number += 1
        t.problem_total_number -= 1
        t.save()

        p = problem_list.filter(index=p_info["materialIndex"]).first()
        p.is_test = True
        p.save()

        q_list = p.question_list.all()
        for q_info in p_info["questionsAndAns"]:
            q_list.filter(index=q_info["index"]).update(standard_answer=q_info["questionAns"])

    # 计算每个用户每次可领取的题目数量
    receiver_number = basic_info_form["receiverNum"]
    t.problem_number_for_single_receiver = math.ceil(1.00 * t.problem_total_number / receiver_number) # TODO:需要更新
    t.save()

    # 返回刚刚创建的任务的id和发布状态等信息给用户
    return basic_info_form['poster'], t.id, t.release_mode,\
           t.problem_total_number*t.single_bonus

# 为用户增加一个任务，包括状态（已领取/已发布和发布模式/完成状态）
def add_task_to_user(username, task_id, state_for_user, state_for_task):
    u = get_a_user_data(username)
    td = TaskDict.objects.create(task_id=task_id, task_status_for_user=state_for_user,
                                 task_status_for_itself=state_for_task)
    u.task_info_list.add(td)

# 添加一个问题反馈到问题反馈列表中
def add_a_feedback(feedback_type, description, image_url, inform_email):
    try:
        FeedbackInfo.objects.create(feedback_type=feedback_type, description=description, image_url=image_url,
                                    inform_email=inform_email)
        return True
    except:
        return False

# 获得指定用户当前正在做的指定任务的大题信息
def get_current_problem(username, task_id, type, jmp_target):
    u = get_a_user_data(username)
    t = get_a_task_data(task_id)  # 当前正在进行的任务

    current_total_problem_number = -1

    # 用户正在做的任务的信息 
    td = get_user_now_taskdict(u,task_id)

    # 下一题
    if type == 'next':
        # td.current_problem_index != (td.test_problem_number - 1) and 
        if td.current_problem_index < (len(td.received_problem_id_list.all()) - 1):
                td.current_problem_index += 1
        td.save()
    
    # 上一题
    elif type == 'last':
        if td.current_problem_index > 0\
           and td.current_problem_index != td.test_problem_number\
           and td.current_problem_index < len(td.received_problem_id_list.all()):
                td.current_problem_index -= 1
        td.save()

    # 跳转到指定题
    elif type == 'jump':
        if td.current_problem_index < td.test_problem_number:
            td.current_problem_index = jmp_target - 1
        else:
            td.current_problem_index = jmp_target - 1 + td.test_problem_number
        td.save()

    # 每题的状态，包括下标，是否做完和答案（如果有）
    problem_state_list = []

    # 确定是否在进行测试
    if td.current_problem_index < td.test_problem_number:
        is_test = True
        current_problem_index = td.current_problem_index + 1
        current_total_problem_number = td.test_problem_number
        for i, x in enumerate(td.received_problem_id_list.all()):
            if i >= current_total_problem_number:
                break
            else:
                p_info = {
                    'index': i+1,
                    'state': False if (x.is_right == -1) else True,
                }
                problem_state_list.append(p_info)
    else:
        is_test = False
        current_problem_index = td.current_problem_index + 1 - td.test_problem_number
        current_total_problem_number = len(td.received_problem_id_list.all()) - td.test_problem_number
        for i, x in enumerate(td.received_problem_id_list.all()):
            if i >= td.test_problem_number:
                p_info = {
                    'index': i+1-td.test_problem_number,
                    'state': False if (x.is_right == -1) else True,
                }
                problem_state_list.append(p_info)

    # 确定当前的大题
    p = None
    for i, x in enumerate(td.received_problem_id_list.all()):
        if i == td.current_problem_index:
            p = t.problem_list.filter(id=x.problem_id).first()

    material_list = []
    # 封装当前大题的素材信息
    for m in p.material_info.all():
        m_info = {
            'fileType': m.material_type,
            'filePath': m.material_path,
            'fileNotes': m.material_note,
        }
        material_list.append(m_info)

    # 封装当前大题的小题信息
    question_list = []
    for q in p.question_list.all():
        picture_index = -1

        if q.question_type == CHOICE_QUESTION:
            cq = ChoiceQuestion.objects.filter(question_ptr_id=q.id).first()
            option_list = []
            for i, op in enumerate(cq.option_list.all()):
                op_info = {
                    "index": i,
                    "name": op.key,
                    "content": op.value,
                }
                option_list.append(op_info)
            min_option_num = cq.min_option_num
            max_option_num = cq.max_option_num
            if min_option_num == max_option_num and max_option_num == 1:  # 单选
                question_type = SINGLE_CHOICE
            else:  # 多选
                question_type = SEVERAL_CHOICES

        elif q.question_type == FILL_BLANK_QUESTION:
            fbq = FillBlankQuestion.objects.filter(question_ptr_id=q.id).first()
            option_list = []
            question_type = FILL_BLANK
            min_option_num = fbq.min_answer_length
            max_option_num = fbq.max_answer_length

        else:
            fcq = FrameSelectionQuestion.objects.filter(question_ptr_id=q.id).first()
            option_list = []
            question_type = SELECT_FRAME
            min_option_num = fcq.min_frame_number
            max_option_num = fcq.max_frame_number
            picture_index = fcq.picture_index

        q_info = {
            'questionType': question_type,
            'questionTypeName': ANSWER_TYPE_DICT[question_type],
            'questionDescription': q.description,
            'optionList': option_list,
            'minOptionNum': min_option_num,
            'maxOptionNum': max_option_num,
            'mustDo': q.must_do,
            'index': q.index,
            'targetIndex':picture_index,
        }
        question_list.append(q_info)
    
    # 封装用户已经作答的答案
    up = td.received_problem_id_list.filter(problem_id=p.id).first()
    ans_li = []
    for ans in up.user_answer.all():
        ans_li.append(ans.str_content)

    return material_list, question_list, is_test, current_problem_index,\
            current_total_problem_number, problem_state_list, ans_li

# 添加一个问题反馈到问题反馈列表中
def add_a_feedback(feedback_type,description,image_url,inform_email):
    try:
        FeedbackInfo.objects.create(feedback_type=feedback_type,description=description,image_url=image_url,inform_email=inform_email)
        return True
    except:
        return False

def get_all_feedback():
    return FeedbackInfo.objects.all()

def delete_a_feedback(inform_email,description):
    return FeedbackInfo.objects.filter(inform_email=inform_email,description=description).delete()[0]

def set_task_end_time(t:Task,end_time):
    t.end_time = end_time
    t.save()

def set_task_begin_time(t:Task,begin_time):
    t.begin_time = begin_time
    t.save()

# 删除违规任务
def delete_violated_task(task_id):
    t = get_a_task_data(task_id)

    # 用户的任务信息先删
    for u in User.objects.all():
        td_list = u.task_info_list.filter(task_id=task_id).all()
        td_id_list = [td.id for td in td_list]
        for td in td_list:
            rp_id_list = [rp.id for rp in td.received_problem_id_list.all()]
            for rp in td.received_problem_id_list.all():
                ua_id_list = [ua.id for ua in rp.user_answer.all()]
                for ua in rp.user_answer.all():
                    rp.user_answer.remove(ua)
                rp.save()
                Str.objects.filter(id_in=ua_id_list).delete()
                td.received_problem_id_list.remove(rp)
            td.save()
            UserProblemInfo.objects.filter(id_in=rp_id_list).delete()
            u.task_info_list.remove(td)
        TaskDict.objects.filter(id_in=td_id_list).delete()
        u.save()
    
    # 任务本身的信息删了
    tr_id_list = [tr.id for tr in t.receiver_list.all()]
    for tr in t.receiver_list.all():
        t.receiver_list.remove(tr)
    t.save()
    Int.objects.filter(id_in=tr_id_list).delete()

    pid_list = [p.id for p in t.problem_list.all()]
    for p in t.problem_list.all():
        md_id_list = [md.id for md in p.material_info.all()]
        for md in p.material_info.all():
            p.material_info.remove(md)
        p.save()
        MaterialDict.objects.filter(id_in=md_id_list).delete()
        qid_list = [q.id for q in p.question_list.all()]
        for q in p.question_list.all():
            p.question_list.remove(q)
            if q.question_type == CHOICE_QUESTION:
                ChoiceQuestion.objects.filter(question_ptr_id=q.id).delete()
            elif q.question_type == FILL_BLANK_QUESTION:
                FillBlankQuestion.objects.filter(question_ptr_id=q.id).delete()
            elif q.question_type == SELECT_FRAME_QUESTION:
                FrameSelectionQuestion.objects.filter(question_ptr_id=q.id).delete()
        p.save()
        Question.objects.filter(id_in=qid_list).delete()
        t.problem_list.remove(p)
    t.save()
    Problem.objects.filter(id_in=pid_list).delete()
    Task.objects.filter(id=task_id).delete()