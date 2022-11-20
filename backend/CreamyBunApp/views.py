import os
import time

from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .function.databaseOperations import *
from .variables.globalConstants import *
from .function.universalFunctions import *
import json


# Create your views here.

# 注册
def log_up(request):
    query_dict = request.GET
    type = query_dict.get("type", "")
    email = query_dict.get("email", "")
    username = query_dict.get("username", "")

    # 如果是发邮箱,verifyCode返回应该的验证码
    if type == 'getVerifyCode':
        check_user_exist_by_email = exist_user_by_email(email)
        if check_user_exist_by_email:
            return HttpResponse(json.dumps({'status': 'wrong', 'type': 'sameEmail'}), content_type='application/json')
        verify_code = send_email(email)
        return HttpResponse(json.dumps({'status': 'ok', 'verifyCode': verify_code}), content_type='application/json')
        # return HttpResponse(json.dumps({'status':'ok'}), content_type='application/json')
    # 如果是点击注册
    elif type == 'logUp':
        # 判断是否重名
        check_user_by_name = exist_user_by_name(username)
        if check_user_by_name:
            return HttpResponse(json.dumps({'status': 'wrong', 'type': 'sameName'}), content_type='application/json')
        password = query_dict.get("password", "")
        create_user = add_a_user(
            username=username, password=password, email=email)
        if create_user:
            return HttpResponse(json.dumps({'status': 'ok'}), content_type='application/json')
        else:
            return HttpResponse(json.dumps({'status': 'wrong', 'type': 'unknown'}), content_type='application/json')

    # 未知操作
    else:
        return HttpResponse(json.dumps({'status': 'wrong', 'type': 'unknownOperation'}),
                            content_type='application/json')


# 登录
def log_in(request):
    query_dict = request.GET
    username = query_dict.get("username", "")
    password = query_dict.get("password", "")

    # 用户是否存在
    is_user_exist = exist_user_by_name(username)
    if not is_user_exist:
        return HttpResponse(json.dumps({'status': 'wrong', 'type': 'noUser'}), content_type='application/json')

    # 密码是否正确
    is_password_right = match_username_with_password(username, password)
    if not is_password_right:
        return HttpResponse(json.dumps({'status': 'wrong', 'type': 'wrongPassword'}), content_type='application/json')

    return HttpResponse(json.dumps({'status': 'ok'}), content_type='application/json')


# 重置密码
def reset_password(request):
    query_dict = request.GET
    reset_way = query_dict.get("resetWay", "")
    password = query_dict.get("password", "")

    # 如果是通过用户名重置
    if reset_way == 'username':
        # 用户是否存在
        username = query_dict.get("username", "")
        is_user_exist = exist_user_by_name(username)
        if is_user_exist:
            type = query_dict.get("type", "")
            if type == 'getVerifyCode':
                email = get_a_user_data(username).email
                verify_code = send_email(email)
                return HttpResponse(json.dumps({'status': 'ok', 'email': email, 'verifyCode': verify_code}),
                                    content_type='application/json')
            elif type == 'resetPassword':
                update_password_by_username(username, password)
                return HttpResponse(json.dumps({'status': 'ok'}), content_type='application/json')
            else:
                return HttpResponse(json.dumps({'status': 'wrong', 'type': 'unknownOperation'}),
                                    content_type='application/json')
        else:
            return HttpResponse(json.dumps({'status': 'wrong', 'type': 'noUser'}), content_type='application/json')

    # 如果是通过邮箱重置
    elif reset_way == 'email':
        # 用户是否存在
        email = query_dict.get("email", "")
        is_user_exist = exist_user_by_email(email)
        if is_user_exist:
            type = query_dict.get("type", "")
            if type == 'getVerifyCode':
                verify_code = send_email(email)
                return HttpResponse(json.dumps({'status': 'ok', 'verifyCode': verify_code}),
                                    content_type='application/json')
            elif type == 'resetPassword':
                update_password_by_email(email, password)
                return HttpResponse(json.dumps({'status': 'ok'}), content_type='application/json')
            else:
                return HttpResponse(json.dumps({'status': 'wrong', 'type': 'unknownOperation'}),
                                    content_type='application/json')
        else:
            return HttpResponse(json.dumps({'status': 'wrong', 'type': 'noUser'}), content_type='application/json')

    # 未知操作
    else:
        return HttpResponse(json.dumps({'status': 'wrong', 'type': 'unknownOperation'}),
                            content_type='application/json')


# 获得个人基本信息
def get_user_basic_info(request):
    query_dict = request.GET
    username = query_dict.get("username", "")
    u = get_a_user_data(username)
    user_info = {

        'status': 'ok',
        'userName': u.username,
        'mobileNumber': u.mobile_number,
        'donutNumber': u.donut_number,
        'email': u.email,
        'creditRank': u.credit_rank,
        'currentExp': u.current_exp,
        'expForUpgrade': get_exp_for_upgrade(u.credit_rank),
        'avatarImage': get_user_avatr(username),
    }
    return HttpResponse(json.dumps(user_info), content_type='application/json')


def get_task_basic_info(request):
    query_dict = request.GET
    id = query_dict.get("id", "")
    t = get_a_task_data(id)
    poster_username = get_a_user_data_by_id(t.poster).username
    task_info = {
        'status': 'ok',
        'taskName': t.task_name,
        'answerType': ANSWER_TYPE_DICT[t.answer_type],
        'description': t.description,
        'problemTotalNum': t.problem_total_number,
        'finishedProblemNum':t.finished_problem_number,
        'singleBonus': t.single_bonus,
        'starRank': t.star_rank,
        'materialType': TASK_TYPE_DICT[t.task_type],
        'posterName': poster_username,
        'posterAvatar':get_user_avatr(poster_username),
        'startTime':t.begin_time.split(" ")[0],
        'endTime':t.end_time.split(" ")[0]
    }
    return HttpResponse(json.dumps(task_info), content_type='application/json')


# 获得奖励中心信息
def get_user_bonus_info(request):
    query_dict = request.GET
    username = query_dict.get("username", "")
    u = get_a_user_data(username)
    bonus_info = {
        'status': 'ok',
        'donutToMoney': get_donut_to_money(),
        'moneyToDonut': get_money_to_donut(),
        'donutNumber': u.donut_number,
    }
    return HttpResponse(json.dumps(bonus_info), content_type='application/json')


# 获得活动中心信息
def get_user_activity_info(request):
    query_dict = request.GET
    username = query_dict.get("username", "")
    u = get_a_user_data(username)
    activity_info = {
        'status': 'ok',
        'continueSignInDays': u.continue_sign_in_days,
        'isTodaySignIn': u.is_today_sign_in,
        'donutListForClockIn': donut_for_clock_in,
    }
    return HttpResponse(json.dumps(activity_info), content_type='application/json')


# 签到接口
def clock_in(request):
    query_dict = request.GET
    username = query_dict.get("username", "")
    success_clock_in, continue_clock_in_days = update_clock_in_info(username)
    clock_in_info = {
        'continueSignInDays': continue_clock_in_days,
        'isTodaySignIn': success_clock_in,
    }
    return HttpResponse(json.dumps(clock_in_info), content_type='application/json')


# 获得设置信息
def get_user_settings_info(request):
    query_dict = request.GET
    username = query_dict.get("username", "")
    u = get_a_user_data(username)
    settings_info = {
        'status': 'ok',
        'darkMode': u.dark_mode,
    }
    return HttpResponse(json.dumps(settings_info), content_type='application/json')


# 获得已领取任务信息
# 任务信息(包括其id)通过列表传送,列表的每一项是一个字典
def get_user_received_task_info(request):
    query_dict = request.GET
    username = query_dict.get("username", "")
    page_number = query_dict.get("pageNumber", "")
    sort_choice = query_dict.get("sortChoice","")#int 0是所有 1是正在进行，2是已结束

    # 总页数（int），任务信息列表（列表，成员为字典）
    total_number, task_info_list = get_task_info_list(
        username, HAS_RECEIVED, page_number, sort_choice)

    ret = {
        'status': 'ok',
        'totalNumber': total_number,# 注意是totalNumber筛选出来的总任务数
        'taskInfoList': task_info_list
    }

    return HttpResponse(json.dumps(ret), content_type='application/json')


# 获得已发布任务信息
def get_user_released_task_info(request):
    query_dict = request.GET
    username = query_dict.get("username", "")
    page_number = query_dict.get("pageNumber", "")
    sort_choice = query_dict.get("sortChoice","")#0是所有，1是暂未发布 2是发布但未结束 3是已结束

    # 总页数（int），任务信息列表（列表，成员为字典）
    total_number, task_info_list = get_task_info_list(
        username, HAS_POSTED, page_number,sort_choice)

    ret = {
        'status': 'ok',
        'totalNumber': total_number,  # 注意是totalNumber筛选出来的总任务数，不是总页数
        'taskInfoList': task_info_list
    }
    return HttpResponse(json.dumps(ret), content_type='application/json')

def get_sorted_tasks(request):
    query_dict = request.GET
    username = query_dict.get("username", "") # 用户名用来获取等级啥的
    seach_content = query_dict.get("searchInput", "") # 搜索框输入的内容，用于模糊搜索
    only_level = eval(query_dict.get("onlyLevel", "").capitalize())
    donut_type = eval(query_dict.get("donutType", ""))
    over_type = eval(query_dict.get("overType", ""))
    new_type = eval(query_dict.get("newType", ""))
    hard_type = eval(query_dict.get("hardType", ""))
    data_type = eval(query_dict.get("chosenDataType", ""))
    answer_type = eval(query_dict.get("chosenProblemType", ""))
    page_number = eval(query_dict.get("pageNumber",""))

    total_number,task_info_list = sorted_and_selected_tasks(username, seach_content, only_level,\
                                                            donut_type, over_type, new_type,\
                                                            hard_type, data_type, answer_type,\
                                                            page_number)

    ret = {
        'status':'ok',
        "taskInfoList":task_info_list,
        "totalNumber":total_number,
    }
    return HttpResponse(json.dumps(ret), content_type='application/json')

# 修改用户名
@csrf_exempt
def update_username(request):
    query_dict = request.POST
    username = query_dict.get("username", "")
    new_username = query_dict.get("newUsername", "")
    is_new_username_exist = exist_user_by_name(new_username)
    if is_new_username_exist:
        return HttpResponse(json.dumps({'status': 'wrong', 'type': 'sameName'}), content_type='application/json')
    else:
        update_username_by_username(username, new_username)
        return HttpResponse(json.dumps({'status': 'ok', 'newUsername': new_username}), content_type='application/json')

# 修改邮箱
def update_email(request):
    query_dict = request.GET
    print(query_dict)
    username = query_dict.get("username", "")
    type = query_dict.get("type", "")
    new_email = query_dict.get("newEmail", "")
    if type == 'getVerifyCode':
        is_new_email_exist = exist_user_by_email(new_email)
        if is_new_email_exist:
            return HttpResponse(json.dumps({'status': 'wrong', 'type': 'sameEmail'}), content_type='application/json')
        else:
            verify_code = send_email(new_email)
            return HttpResponse(json.dumps({'status': 'ok', 'verifyCode': verify_code}),
                                content_type='application/json')
    elif type == 'changeEmail':
        update_email_by_username(username, new_email)
        return HttpResponse(json.dumps({'status': 'ok'}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'status': 'wrong', 'type': 'unknownOperation'}),
                            content_type='application/json')


# 修改用户头像
@csrf_exempt
def change_avatar(request):
    image = request.FILES.get('image', None)
    username = request.POST.get('username', '')
    if image == None:
        return HttpResponse(json.dumps({'status': 'wrong', 'type': 'noImage'}), content_type='application/json')
    else:
        change_user_avatar(image, username)
        return HttpResponse(json.dumps({'status': 'ok'}), content_type='application/json')


# 注销
def log_off(request):
    pass


# 修改手机号
def update_mobile(request):
    pass


# 接收前端分片上传的素材压缩包
@csrf_exempt
def get_material_zip(request):
    if request.method == "POST":  # 判断接收的值是否为POST
        query_dict = request.POST
        print(query_dict)
        username = query_dict.get("username", "")
        file_type = query_dict.get("fileType", "")
        shard_index = eval(query_dict.get("shardIndex", ""))
        shard_total = eval(query_dict.get("shardTotal", ""))
        material_type = eval(query_dict.get("materialType", ""))
        current_time = query_dict.get("currentTime", "")
        dirname = username + '_' + current_time
        path = os.path.join("./resource/task_materials", dirname)
        file = request.FILES['file']
        if not os.path.exists(path):  # 如果目录不存在就创建
            os.makedirs(path)
        path_name = os.path.join(path, "uploadPackage." + file_type)
        # time.sleep(0.5)
        handle_uploaded_file(file, path_name)
        print(shard_index, shard_total, query_dict)
        if shard_index == shard_total - 1:  # 此时要解压了
            unzip_file(path_name, path)
            os.remove(path_name)
            full_list, list_list = walk_file(path, material_type)
            # print(full_list)
            # print(list_list)
            return HttpResponse(json.dumps({'status': 'done', 'fullList': full_list, 'listList': list_list}),
                                content_type='application/json')
    return HttpResponse(json.dumps({'status': 'next'}), content_type='application/json')


# 处理前端对列表的操作（目前能想到的只有删除
@csrf_exempt
def handle_release_action(request):
    if request.method == "POST":  # 判断接收的值是否为POST
        request_body = json.loads(request.body)
        print(request_body)
        act = request_body['act']
        msg_list = request_body['msgList']
        if act == 'delete':
            for target in msg_list:
                os.remove(target['filePath'])
    return HttpResponse(json.dumps({'status': 'done'}), content_type='application/json')


# 最终前端返回的数据，request_body参数参见 https://ziyouzhiyi4.coding.net/p/naihuangbao/km/spaces/1/pages/K-16
@csrf_exempt
def release_task(request):
    request_type = request.META['CONTENT_TYPE']
    print("request_type", request_type)

    if request_type == 'application/json':
        request_body = json.loads(request.body)
        username, t_id, t_release_mode = create_task(request_body)

        # 给相应用户加上任务和状态

        if t_release_mode == NOT_YET_RELEASE or t_release_mode == TIMED_RELEASE:
            state_for_task = NOT_RELEASE
        else:
            state_for_task = RELEASE_BUT_NOT_FINISHED
        add_task_to_user(username, t_id, HAS_POSTED, state_for_task)

        return HttpResponse(json.dumps({'status': 'done'}), content_type='application/json')
    else:
        image = request.FILES.get('image', None)
        username = request.POST.get('username', '')
        file_format = image.name
        current_time = get_now_time().strftime('_%y%m%d%H%M%S.')
        path = "./resource/task_cover"
        if not os.path.exists(path):  # 如果目录不存在就创建
            os.makedirs(path)
        path_name = os.path.join(path, username + current_time + file_format)
        handle_uploaded_file(image, path_name)

        return HttpResponse(json.dumps({'status': 'get the image', 'url': path_name}), content_type='application/json')


@csrf_exempt
def submit_feedback(request):
    image_url = request.FILES.get('image', None)
    inform_email = request.POST.get('email', '')
    description = request.POST.get('textarea', '')
    feedback_type = request.POST.get('questionType', '')

    create_feedback = add_a_feedback(
        feedback_type, description, image_url, inform_email)
    if create_feedback:
        return HttpResponse(json.dumps({'status': 'ok'}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'status': 'wrong', 'type': 'unknown'}), content_type='application/json')


def perform_basic_info(request):
    query_dict = request.GET
    username = query_dict.get("username", "")
    task_id = query_dict.get("taskId","")
    # print("perform_basic_info", username)

    material_list,question_list,is_test,current_problem_index=get_current_problem(username,task_id)

    basic_info = {
        'status': 'ok',
        'materialList':material_list,
        'questionList':question_list,
        'isTest':is_test,
        'currentIndex':current_problem_index,
    }
    return HttpResponse(json.dumps(basic_info), content_type='application/json')


def perform_problem_material(request):
    query_dict = request.GET
    file_type = query_dict.get("fileType", "")
    file_path = query_dict.get("filePath", "")
    if file_type == 0:
        file_suffix = get_suffix(file_path)
        base64_str = get_problem_material(file_path)
        if file_suffix == 'jpg':
            file_suffix = 'jpeg'
        return_info = {
            'status': 'ok',
            'materialImage': "data:image/" + file_suffix + ";base64," + base64_str
        }
        return HttpResponse(json.dumps(return_info), content_type='application/json')
    pass


def uck_me(request):
    print("uck_me")
    return HttpResponse(json.dumps(fake_ans), content_type='application/json')
