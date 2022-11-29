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
        }
        init_list.append(t_info)
    length = len(all_report_id_list)
    if length < 10:
        for i in range( 10 - length):
            init_list.append({'isSpace':True,'index': length + i})
    return total_number, init_list


# 从用户列表中删除指定用户
def delete_a_user(username):
    User.objects.filter(username=username).delete()


# 获取指定用户的数据
# 返回的对象可以通过.获取成员变量
def get_a_user_data(username):
    return User.objects.filter(username=username).first()


# 通过id获得用户
def get_a_user_data_by_id(id):
    return User.objects.filter(id=id).first()


# 获取指定任务的数据
def get_a_task_data(id):
    return Task.objects.filter(id=id).first()


# 通过用户名修改密码
def update_password_by_username(username, password):
    User.objects.filter(username=username).update(password=password)


# 通过用户名修改用户名
def update_username_by_username(username, new_username):
    User.objects.filter(username=username).update(username=new_username)


# 通过用户名修改邮箱
def update_email_by_username(username, new_email):
    User.objects.filter(username=username).update(email=new_email)


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
    else:
        begin_time = datetime.datetime.now().strftime('%F %T')

    # 获得结束时间
    temp_end_time = []
    temp_end_time.append(basic_info_form["deadLine1"])
    temp_end_time.append(basic_info_form["deadLine2"])
    end_time = " ".join(temp_end_time)

    # 这个返回值是一个task对象
    t = Task.objects.create(poster=poster_id, task_name=task_name, description=description, \
                            task_type=task_type, answer_type=answer_type, problem_total_number=problem_total_number, \
                            star_rank=star_rank, single_bonus=single_bonus, release_mode=release_mode, \
                            begin_time=begin_time, end_time=end_time)

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
    t.problem_number_for_single_receiver = math.ceil(1.00 * t.problem_total_number / receiver_number)
    t.save()

    # task的problem列表随机排个序
    # random_list = list(range(len(problem_list)))
    # random.shuffle(random_list)
    # for i,p in enumerate(problem_list):
    #     p.index = random_list[i] + 1
    #     p.save()
    
    # 返回刚刚创建的任务的id和发布状态给用户
    return basic_info_form['poster'], t.id, t.release_mode


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
    problem_state_list = []

    # 用户正在做的任务的信息
    td_temp = u.task_info_list.filter(task_id=task_id)  
    td = td_temp.filter(task_status_for_user=HAS_RECEIVED).first()

    # 确定是否在进行测试
    if td.current_problem_index < td.test_problem_number:
        is_test = True
        current_problem_index = td.current_problem_index + 1
        current_total_problem_number = td.test_problem_number
        for i in range(current_total_problem_number):
            pass
    else:
        is_test = False
        current_problem_index = td.current_problem_index + 1 - td.test_problem_number
        current_total_problem_number = len(td.received_problem_id_list.all()) - td.test_problem_number
        for i in range(current_total_problem_number):
            pass

    # 下一题
    if type == 'next':
        if is_test:
            if td.current_problem_index < (td.test_problem_number - 1):
                td.current_problem_index += 1
        else:
            if td.current_problem_index < (len(td.received_problem_id_list.all()) - 1):
                td.current_problem_index += 1
        td.save()
    
    # 上一题
    elif type == 'last':
        if is_test:
            if td.current_problem_index > 0:
                td.current_problem_index -= 1
        else:
            if td.current_problem_index > td.test_problem_number:
                td.current_problem_index -= 1
        td.save()

    # 跳转到指定题
    elif type == 'jump':
        if is_test:
            td.current_problem_index = jmp_target - 1
        else:
            td.current_problem_index = jmp_target - 1 + td.test_problem_number
        td.save()

    # 确定当前的大题
    p = None
    for i, x in enumerate(td.received_problem_id_list.all()):
        if i == td.current_problem_index:
            p = t.problem_list.filter(id=x.key).first()

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

        q_info = {
            'questionType': question_type,
            'questionTypeName': ANSWER_TYPE_DICT[question_type],
            'questionDescription': q.description,
            'optionList': option_list,
            'minOptionNum': min_option_num,
            'maxOptionNum': max_option_num,
            'mustDo': q.must_do,
            'index': q.index,
        }
        question_list.append(q_info)

    return material_list, question_list, is_test, current_problem_index, current_total_problem_number

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