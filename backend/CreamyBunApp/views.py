import mimetypes
import os
import re
import time
from wsgiref.util import FileWrapper

from django.http import StreamingHttpResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .function.databaseOperations import *
from .variables.globalConstants import *
from .variables.globalVariables import *
from .function.universalFunctions import *
import json
import jwt



# Create your views here.

def no_log(request):
    return HttpResponse("请您先注册")

# 伪装注册用户->用于测试
def fake_log_up(request):
    query_dict = request.GET
    email = query_dict.get("email", "")
    username = query_dict.get("username", "")
    check_user_by_name = exist_user_by_name(username)
    check_user_exist_by_email = exist_user_by_email(email)
    if check_user_by_name or check_user_exist_by_email:
        return HttpResponse(json.dumps({'status': 'wrong', 'type': 'sameName'}), content_type='application/json')
    password = query_dict.get("password", "")
    create_user = add_a_user(
        username=username, password=password, email=email)
    if create_user:
        return HttpResponse(json.dumps({'status': 'ok'}), content_type='application/json')    

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

# 退出登录
def log_out(request):
    query_dict = request.GET
    username = query_dict.get("username", "")
    # remove_user_jwt(username)
    return HttpResponse(json.dumps({'status': 'ok'}),content_type='application/json')

# 登录
def log_in(request):
    query_dict = request.GET
    username = query_dict.get("username", "")
    password = query_dict.get("password", "")

    adminU, adminP = get_admin_username_with_password()
    adminT = get_admin_token()
    # 查看是否是管理员
    if username == adminU:
        if password == adminP:
            return HttpResponse(json.dumps({'status': 'ok', 'type': 'admin', 'adminToken': adminT}),
                                content_type='application/json')
        else:
            return HttpResponse(json.dumps({'status': 'wrong', 'type': 'wrongPassword'}),
                                content_type='application/json')

    # 用户是否存在
    is_user_exist = exist_user_by_name(username)
    if not is_user_exist:
        return HttpResponse(json.dumps({'status': 'wrong', 'type': 'noUser'}), content_type='application/json')

    # 密码是否正确
    is_password_right = match_username_with_password(username, password)
    if not is_password_right:
        return HttpResponse(json.dumps({'status': 'wrong', 'type': 'wrongPassword'}), content_type='application/json')

    orjwt = jwt.encode({'username':username,'time':time.strftime("%Y%m%d-%H%M%S")}, "secret", algorithm="HS256")
    orjwt = orjwt.decode(encoding="utf-8")
    if len(orjwt) > 20:
        return_jwt = orjwt[0:20]
    else:
        return_jwt = orjwt
    # add_user_jwt(username,return_jwt)
    return HttpResponse(json.dumps({'status': 'ok', 'type': 'normalUser','jwt':return_jwt}), content_type='application/json')


# 获取用户名对应用户头像
def get_avatar(request):
    query_dict = request.GET
    username = query_dict.get("username", "")
    ret = {
        'status': 'ok',
        'avatar': get_user_avatr(username)
    }
    return HttpResponse(json.dumps(ret), content_type='application/json')


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
    # if not check_jwt(username,query_dict.get("jwt", "")):
    #     return HttpResponse(json.dumps({'status':'wrong'}), content_type='application/json')
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
    }
    return HttpResponse(json.dumps(user_info), content_type='application/json')


def get_task_basic_info(request):
    query_dict = request.GET
    id = query_dict.get("id", "")
    t = get_a_task_data(id)
    poster_username = get_a_user_data_by_id(t.poster).username

    # 获取用户领了多少题目，当前做到第几题
    user_current_problem_finish_number = -1
    user_received_total_problem_number = -1
    task_status = get_task_status(t)
    tag = query_dict.get("tag","") # 表明当前是否在领取任务界面
    if tag == 'receiveTask':
        receiver_name = query_dict.get("username","")
        sort_choice = query_dict.get("sortChoice","") # int 0是所有 1是正在进行，2是已结束
        task_index = query_dict.get("index","") # 这个列表中的第几个任务
        user_current_problem_finish_number, user_received_total_problem_number,\
            task_status = get_user_received_problem_info(receiver_name,eval(sort_choice),eval(task_index))

    task_info = {
        'status': 'ok',
        'taskName': t.task_name,
        'answerType': ANSWER_TYPE_DICT[t.answer_type],
        'description': t.description,
        'problemTotalNum': t.problem_total_number,
        'finishedProblemNum': t.finished_problem_number,
        'receivedProblemNum': get_task_received_number(t),
        'singleBonus': t.single_bonus,
        'starRank': t.star_rank,
        'materialType': TASK_TYPE_DICT[t.task_type],
        'posterName': poster_username,
        'posterAvatar': get_user_avatr(poster_username),
        'startTime': t.begin_time.split(" ")[0],
        'endTime': t.end_time.split(" ")[0],
        'receiveProcess':get_task_receive_process_by_id(id),
        'coverImage': 'http://101.42.118.80:8000' + t.cover_url[1:],

        # 芝士任务状态，在领取任务界面查看时该状态对应用户领取部分的状态，其它情况下为任务整体的状态
        'taskStatus': task_status,

        'userFinishedNum':user_current_problem_finish_number,
        'userTotalNum':user_received_total_problem_number,
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
    print(u.finished_task_number)
    activity_info = {
        'status': 'ok',
        'continueSignInDays': u.continue_sign_in_days,
        'isTodaySignIn': u.is_today_sign_in,
        'donutListForClockIn': donut_for_clock_in,
        'finishTaskDonut': finish_task_donut, # 列表，共两个元素
        'finishTaskNum': u.finished_task_number, # 用户今日已完任务数
        'taskOneState': u.finish_task_one, # 该用户是否领取第一个每日任务奖励
        'taskTwoState': u.finish_task_two, # 该用户是否领取第二个每日任务奖励
    }
    return HttpResponse(json.dumps(activity_info), content_type='application/json')


# 签到接口
def clock_in(request):
    query_dict = request.GET
    username = query_dict.get("username", "")
    success_clock_in, continue_clock_in_days = update_clock_in_info(username)
    clock_in_info = {
        'status':'ok',
        'continueSignInDays': continue_clock_in_days,
        'isTodaySignIn': success_clock_in,
    }
    return HttpResponse(json.dumps(clock_in_info), content_type='application/json')

# 完成每日任务接口
def finish_daily_task(request):
    query_dict = request.GET
    username = query_dict.get("username", "")
    index = query_dict.get('index',"") # 0或1
    finish_task_one, finish_task_two = update_daily_task_info(username,eval(index))
    res = {
        'status':'ok',
        'taskOneState': finish_task_one, # 该用户是否领取第一个每日任务奖励
        'taskTwoState': finish_task_two, # 该用户是否领取第二个每日任务奖励
    }
    return HttpResponse(json.dumps(res), content_type='application/json')

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


# 获得管理员用户密码
def get_admin_username_and_password(request):
    query_dict = request.GET
    adminT = query_dict.get("adminToken", "")
    if adminT != get_admin_token():
        return HttpResponse(json.dumps({'status': "wrong"}), content_type='application/json')

    adminU, adminP = get_admin_username_with_password()
    ret = {
        'status': 'ok',
        'adminUsername': adminU,
        'adminPassword': adminP
    }
    return HttpResponse(json.dumps(ret), content_type='application/json')


# 设置管理员用户密码
def set_admin_username_and_password(request):
    query_dict = request.GET
    adminT = query_dict.get("adminToken", "")
    if adminT != get_admin_token():
        return HttpResponse(json.dumps({'status': "wrong"}), content_type='application/json')

    type = query_dict.get("type", "")
    ret = {
        'status': 'ok',
    }
    if type == "username":
        adminU = query_dict.get("newUsername", "")
        set_admin_username(adminU)
        ret['adminUsername'] = adminU
    elif type == "password":
        adminP = query_dict.get("newPassword", "")
        set_admin_password(adminP)
        ret['adminPassword'] = adminP
    return HttpResponse(json.dumps(ret), content_type='application/json')


# 获得已领取任务信息
# 任务信息(包括其id)通过列表传送,列表的每一项是一个字典
def get_examining_tasks(request):
    query_dict = request.GET
    admin_token = query_dict.get('adminToken', '')
    if admin_token != get_admin_token():
        return HttpResponse(json.dumps({'status': 'wrong'}), content_type='application/json')

    # 总个数（int），任务信息列表（列表，成员为字典）
    page_number = query_dict.get("pageNumber", "")
    total_number, task_info_list = get_reported_task_list(eval(page_number))

    ret = {
        'status': 'ok',
        'totalNumber': total_number,
        'taskInfoList': task_info_list
    }

    return HttpResponse(json.dumps(ret), content_type='application/json')


# 获得已领取任务信息
# 任务信息(包括其id)通过列表传送,列表的每一项是一个字典
def get_user_received_task_info(request):
    query_dict = request.GET
    username = query_dict.get("username", "")
    page_number = query_dict.get("pageNumber", "")
    sort_choice = query_dict.get("sortChoice", "")  # int 0是所有 1是正在进行，2是已结束

    # 总页数（int），任务信息列表（列表，成员为字典）
    total_number, task_info_list = get_task_info_list(
        username, HAS_RECEIVED, page_number, sort_choice)

    ret = {
        'status': 'ok',
        'totalNumber': total_number,  # 注意是totalNumber筛选出来的总任务数
        'taskInfoList': task_info_list
    }

    return HttpResponse(json.dumps(ret), content_type='application/json')


# 获得已发布任务信息
def get_user_released_task_info(request):
    query_dict = request.GET
    username = query_dict.get("username", "")
    page_number = query_dict.get("pageNumber", "")
    sort_choice = query_dict.get("sortChoice", "")  # 0是所有，1是暂未发布 2是发布但未结束 3是已结束

    # 总页数（int），任务信息列表（列表，成员为字典）
    total_number, task_info_list = get_task_info_list(
        username, HAS_POSTED, page_number, sort_choice)

    ret = {
        'status': 'ok',
        'totalNumber': total_number,  # 注意是totalNumber筛选出来的总任务数，不是总页数
        'taskInfoList': task_info_list
    }
    return HttpResponse(json.dumps(ret), content_type='application/json')


# 获得任务大厅排序筛选后的任务信息
def get_sorted_tasks(request):
    query_dict = request.GET
    username = query_dict.get("username", "")  # 用户名用来获取等级啥的
    seach_content = query_dict.get("searchInput", "")  # 搜索框输入的内容，用于模糊搜索
    only_level = eval(query_dict.get("onlyLevel", "").capitalize())
    donut_type = eval(query_dict.get("donutType", ""))
    over_type = eval(query_dict.get("overType", ""))
    new_type = eval(query_dict.get("newType", ""))
    hard_type = eval(query_dict.get("hardType", ""))
    data_type = eval(query_dict.get("chosenDataType", ""))
    answer_type = eval(query_dict.get("chosenProblemType", ""))
    page_number = eval(query_dict.get("pageNumber", ""))

    total_number, task_info_list = sorted_and_selected_tasks(username, seach_content, only_level, \
                                                             donut_type, over_type, new_type, \
                                                             hard_type, data_type, answer_type, \
                                                             page_number)

    ret = {
        'status': 'ok',
        "taskInfoList": task_info_list,
        "totalNumber": total_number,
    }
    return HttpResponse(json.dumps(ret), content_type='application/json')


# 获得现在甜甜圈与现金之间汇率
def get_current_rate_info(request):
    query_dict = request.GET
    adminT = query_dict.get("adminToken", "")
    if adminT != get_admin_token():
        return HttpResponse({json.dumps({'status': 'wrong'})}, content_type='application/json')

    ret = {
        'status': 'ok',
        'donutToMoney': get_donut_to_money(),
        'moneyToDonut': get_money_to_donut()
    }
    return HttpResponse(json.dumps(ret), content_type='application/json')


# 修改现在甜甜圈与现金之间汇率
def change_current_rate_info(request):
    query_dict = request.GET
    adminT = query_dict.get("adminToken", "")
    if adminT != get_admin_token():
        return HttpResponse({json.dumps({'status': 'wrong'})}, content_type='application/json')

    ret = {
        'status': 'ok',
    }
    type = query_dict.get('type', "")
    if type == "moneyToDonut":
        new_rate = eval(query_dict.get('moneyToDonut', ""))
        set_money_to_donut(new_rate)
        ret['moneyToDonut'] = new_rate
    elif type == "donutToMoney":
        new_rate = eval(query_dict.get("donutToMoney", ""))
        set_donut_to_money(new_rate)
        ret['donutToMoney'] = new_rate
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

# （TODO:暂时是伪装的没验证）修改手机号
def update_phone(request):
    query_dict = request.GET
    username = query_dict.get("username", "")
    new_phone = query_dict.get("newPhone", "")
    is_new_phone_exist = exist_user_by_mobile_number(new_phone)
    if is_new_phone_exist:
        return HttpResponse(json.dumps({'status': 'wrong', 'type': 'samePhone'}), content_type='application/json')
    else:
        update_user_by_mobile_number(username, new_phone)
        return HttpResponse(json.dumps({'status': 'ok', 'newPhone': new_phone}), content_type='application/json')

# 修改邮箱
def update_email(request):
    query_dict = request.GET
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


# （TODO:暂时不做）注销
def log_off(request):
    pass

# （TODO:待完善）充值接口，暂时是伪装充值功能
def top_up(request):
    query_dict = request.GET
    username = query_dict.get("username", "")
    money_number = eval(query_dict.get("money", ""))
    current_donut_number = user_top_up(username,money_number)
    res = {
        'status':'ok',
        'donutNum':current_donut_number,
    }
    return HttpResponse(json.dumps(res), content_type='application/json')

# （TODO:待完善）提现接口，暂时是伪装提现功能
def withdraw_money(request):
    query_dict = request.GET
    username = query_dict.get("username", "")
    money_number = eval(query_dict.get("money", ""))
    is_success, current_donut_number = user_withdraw_money(username,money_number)
    res = {
        'status':'ok',

        # 判断提现是否成功，因为有可能余额不足，这时候应该给出提示
        'withdrawStatus':is_success,

        'donutNum':current_donut_number,
    }
    return HttpResponse(json.dumps(res), content_type='application/json')

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
        path = os.path.join(TASK_MATERIAL_SAVE_PATH, dirname)
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
        username, t_id, t_release_mode, sub_donut_number = create_task(request_body)

        # 给相应用户加上任务和状态
        if t_release_mode == NOT_YET_RELEASE or t_release_mode == TIMED_RELEASE:
            state_for_task = NOT_RELEASE_YET
        else:
            state_for_task = RELEASE_BUT_NOT_OVER
        add_task_to_user(username, t_id, HAS_POSTED, state_for_task)

        # 扣钱
        sub_donut_for_user(get_a_user_data(username),sub_donut_number)

        return HttpResponse(json.dumps({'status': 'done'}), content_type='application/json')
    else:
        image = request.FILES.get('image', None)
        username = request.POST.get('username', '')
        file_format = image.name
        current_time = get_now_time().strftime('_%y%m%d%H%M%S.')
        if not os.path.exists(TASK_COVER_SAVE_PATH):  # 如果目录不存在就创建
            os.makedirs(TASK_COVER_SAVE_PATH)
        path_name = os.path.join(TASK_COVER_SAVE_PATH, username + current_time + file_format)
        handle_uploaded_file(image, path_name)

        return HttpResponse(json.dumps({'status': 'get the image', 'url': path_name}), content_type='application/json')


# 任务进行界面基本信息
def perform_basic_info(request):
    query_dict = request.GET
    username = query_dict.get("username", "")
    task_id = query_dict.get("taskId", "")
    type = query_dict.get("type", "")
    jmp_target = eval(query_dict.get("jmpTarget", ""))
    # print("perform_basic_info", username)
    print("perform_basic_info",type)
    material_list, question_list, is_test, current_problem_index, \
    current_total_problem_number, problem_state_list, answer_list = \
        get_current_problem(username, task_id, type, jmp_target)

    basic_info = {
        'status': 'ok',
        'materialList': material_list,
        'questionList': question_list,
        'isTest': is_test,
        'currentIndex': current_problem_index,
        'currentTotalProblemNum': current_total_problem_number,
        'problemStateList': problem_state_list,
        'answerList': answer_list,
    }
    return HttpResponse(json.dumps(basic_info), content_type='application/json')


# 交当前做的题的答案
@csrf_exempt
def submit_answer(request):
    request_body = json.loads(request.body)
    username = request_body["username"]
    task_id = request_body["taskId"]
    answer_list = request_body["ansList"]
    print('answer_list',answer_list)
    # 提交答案的反馈，是字典 
    test_correct_rate, pass_test, task_over = submit_current_answer(username, task_id, answer_list)

    submit_answer_feedback = {
        'status': 'ok',
        'testCorrectRate': test_correct_rate,
        'passTest': pass_test,
        'taskOver': task_over,
    }

    return HttpResponse(json.dumps(submit_answer_feedback), content_type='application/json')


# 任务总提交
@csrf_exempt
def final_submit(request):
    request_body = json.loads(request.body)
    username = request_body["username"]
    task_id = request_body["taskId"]
    
    pass_insertion_test, is_punish, today_violation_number,\
    is_upgrade, now_credit_rank, get_exp_number,\
    get_donut_number, now_donut_number = final_submit_answer(username, task_id)

    # 总提交的反馈，是字典
    final_submit_feedback = {
        'status': 'ok',
        'passInsertionTest': pass_insertion_test,       # 是否通过穿插测试

        # 是否受到了降低经验的惩罚，用于提示，未通过穿插测试时才有用，因为用户存在一个每天可以违规的次数上限
        'isPunish': is_punish,                          

        'todayViolationNum': today_violation_number,    # 今天已经违规多少次了，用于在未通过穿插测试时的提示
        'perDayViolationNum': violation_number_per_day, # 每天最多可以违规多少次
        'getExpNum': get_exp_number,                    # 做本次任务获得了多少经验，如果没通过穿插测试那就是0
        'getDonutNum': get_donut_number,                # 做本次任务获得了多少甜甜圈，没通过穿插测试是0
        'isUpgrade': is_upgrade,                        # 是否升级了
        'nowCreditRank': now_credit_rank,               # 用户当前等级
        'nowDonutNumber': now_donut_number,             # 用户当前甜甜圈数量
    }

    return HttpResponse(json.dumps(final_submit_feedback), content_type='application/json')


# 发布任务时可能会用到的一些信息
def get_release_info(request):
    query_dict = request.GET
    username = query_dict.get("username", "")
    u = get_a_user_data(username)
    re_info ={
        'status':'ok',

        # 各星级任务的单题保底甜甜圈报酬，但是本列表下标从0开始
        # 也就是说，前端donutList[0]表示1星任务对应的单题甜甜圈报酬，以此类推
        'donutList':donut_from_a_problem_by_task_rank,

        # 用户当前有多少甜甜圈，用于判断余额够不够发布，不够前端要给出提示
        'userDonutNum':u.donut_number,

        # 用户当前等级，发布任务时不能发布超过自身等级的星级任务
        'userRank':u.credit_rank, 
    }
    return HttpResponse(json.dumps(re_info), content_type='application/json')

def perform_problem_material(request):
    query_dict = request.GET
    file_type = eval(query_dict.get("fileType"))
    file_path = query_dict.get("filePath", "")
    file_suffix = get_suffix(file_path)
    if file_type == 0:
        base64_str = get_problem_material(file_path)
        if file_suffix == 'jpg':
            file_suffix = 'jpeg'
        return_info = {
            'status': 'ok',
            'materialImage': "data:image/" + file_suffix + ";base64," + base64_str
        }
        return HttpResponse(json.dumps(return_info), content_type='application/json')
    elif file_type == 1:
        content = read_material_str(file_path, file_suffix)
        return_info = {
            'status': 'ok',
            'materialContent': content
        }
        return HttpResponse(json.dumps(return_info), content_type='application/json')
    elif file_type == 2:
        return HttpResponse(json.dumps({'status': 'ok', }), content_type='application/json')
    return HttpResponse(json.dumps({'status': 'ok', }), content_type='application/json')


def stream_video(request, path):
    """将视频文件以流媒体的方式响应"""
    query_dict = request.GET
    path = path.replace('<', '/')
    print("path", path)
    # file_type = eval(query_dict.get("fileType"))
    # path = query_dict.get("filePath", "")
    # path = "./media/task_materials\\ZDandsomSP_20221120152607\\list3\\视频 (5).mp4"
    range_header = request.META.get('HTTP_RANGE', '').strip()
    range_re = re.compile(r'bytes\s*=\s*(\d+)\s*-\s*(\d*)', re.I)
    range_match = range_re.match(range_header)
    size = os.path.getsize(path)
    content_type, encoding = mimetypes.guess_type(path)
    content_type = content_type or 'application/octet-stream'
    print("stream_video")
    if range_match:
        print("if range_match:")
        first_byte, last_byte = range_match.groups()
        first_byte = int(first_byte) if first_byte else 0
        last_byte = first_byte + 1024 * 1024 * 8  # 8M 每片,响应体最大体积
        if last_byte >= size:
            last_byte = size - 1
        length = last_byte - first_byte + 1
        resp = StreamingHttpResponse(file_iterator(path, offset=first_byte, length=length), status=206,
                                     content_type=content_type)
        resp['Content-Length'] = str(length)
        resp['Content-Range'] = 'bytes %s-%s/%s' % (first_byte, last_byte, size)
    else:
        print("if range_match:")
        # 不是以视频流方式的获取时，以生成器方式返回整个文件，节省内存
        resp = StreamingHttpResponse(FileWrapper(open(path, 'rb')), content_type=content_type)
        resp['Content-Length'] = str(size)
    resp['Accept-Ranges'] = 'bytes'
    return resp


@csrf_exempt
def submit_feedback(request):
    image_url = request.FILES.get('image', None)
    inform_email = request.POST.get('email', '')
    description = request.POST.get('textarea', '')
    feedback_type = request.POST.get('questionType', '')
    create_feedback = add_a_feedback(feedback_type, description, image_url, inform_email)
    path = "./media/feedback_image"
    file_format = image_url.name
    path_name = os.path.join(path, file_format)
    handle_uploaded_file(image_url, path_name)
    print(image_url)
    if create_feedback:
        return HttpResponse(json.dumps({'status': 'ok'}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'status': 'wrong', 'type': 'unknown'}), content_type='application/json')


@csrf_exempt
def add_reported_task(request):
    image = request.FILES.get('image', None)
    description = request.POST.get('description', "")
    username = request.POST.get('username', '')
    id = request.POST.get('id', "")
    if image == None:
        create_a_reported_task(description, id, "", username)
    else:
        path = os.path.join("./media/report_image", time.strftime("%Y%m%d-%H%M%S") + image.name)
        create_a_reported_image(image, path)
        create_a_reported_task(description, id, path, username)
    return HttpResponse(json.dumps({'status': 'ok'}), content_type='application/json')


def delete_reported_task(request):
    query_dict = request.GET
    report_id = query_dict.get("reportId")
    delete_a_reported_task_all(report_id)
    return HttpResponse(json.dumps({'status': 'ok'}), content_type='application/json')


def get_reported_task(request):
    query_dict = request.GET
    report_id = query_dict.get("reportId")
    r = get_a_reported_task(report_id)
    ret = {
        'status': 'ok',
        'description': r.description,
        'image': get_reported_image(r.image_url)
    }
    return HttpResponse(json.dumps(ret), content_type='application/json')


def send_report_email(request):
    query_dict = request.GET
    type = query_dict.get("type")
    report_id = query_dict.get("reportId")
    task_id = query_dict.get("taskId")
    text = query_dict.get("textarea", '')
    send_report_back_email(type, task_id, report_id, text)
    return HttpResponse(json.dumps({'status': 'ok'}), content_type='application/json')


@csrf_exempt
def get_feedback(request):
    feedback_list = get_all_feedback()
    feedback_list = list(feedback_list)
    feedback_list_dict = [{} for _ in range(len(feedback_list))]
    for i in range(len(feedback_list)):
        feedback_list_dict[i]['advice'] = feedback_list[i].advice
        feedback_list_dict[i]['inform_email'] = feedback_list[i].inform_email
        path = "./media/feedback_image"
        path_name = os.path.join(path, feedback_list[i].image_url)
        with open(path_name, 'rb') as f:
            data = f.read()
            feedback_list_dict[i]['image_url'] = bytes.decode(base64.b64encode(data))
        feedback_list_dict[i]['description'] = feedback_list[i].description
        if feedback_list[i].feedback_type == 0:
            feedback_list_dict[i]['feedback_type'] = "功能建议"
        elif feedback_list[i].feedback_type == 1:
            feedback_list_dict[i]['feedback_type'] = "界面优化"
        elif feedback_list[i].feedback_type == 2:
            feedback_list_dict[i]['feedback_type'] = "产品bug"
        else:
            feedback_list_dict[i]['feedback_type'] = "其他问题"
    # print(feedback_list[].advice)
    # for i in range(len(feedback_list)):
    # feedback_list[i] =  feedback_list[i].__dict__
    print(feedback_list)
    if feedback_list:
        return HttpResponse(json.dumps({'feedback_list': feedback_list_dict}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'status': 'wrong', 'type': 'unknown'}), content_type='application/json')

# 发送信息处理反馈的邮件
@csrf_exempt
def handle_feedback_email(request):
    content = request.POST.get("content", "")
    email = request.POST.get("email", "")
    send_status = send_feedback_email(email, content)
    if send_status == 1:
        return HttpResponse(json.dumps({'status': 'ok', 'type': 'sameEmail'}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'status': 'wrong', 'type': 'sameEmail'}), content_type='application/json')


@csrf_exempt
def delete_feedback(request):
    content = request.POST.get("description", "")
    email = request.POST.get("email", "")
    delete_status = delete_a_feedback(email, content)
    if delete_status == 0:
        return HttpResponse(json.dumps({'status': 'wrong', 'type': 'sameEmail'}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'status': 'ok', 'type': 'sameEmail'}), content_type='application/json')


def receive_task(request):
    query_dict = request.GET
    username = query_dict.get("username", "")
    task_id = query_dict.get("taskId", "")

    # 领取任务有可能因为原来已经领取过但是没做完或者用户星级不达标而失败 
    flag, fail_type = user_receive_current_task(username, task_id)
    if flag:
        return HttpResponse(json.dumps({'status': 'ok', 'type': 'success'}), content_type='application/json')
    else:
        print(fail_type)
        # failType有'hasReceived'或者'lowRank'或者'noProblemLeft'
        return HttpResponse(json.dumps({'status': 'ok', 'type': 'fail', 'failType':fail_type}), content_type='application/json')

@csrf_exempt
def download_task_answer(request):
    task_id = request.POST.get("id", "")
    excel_data = download_task_answer_byid(task_id)
    temp = [{}]
    temp[0]['excel_data'] = bytes.decode(excel_data)
    # path_name = './task_answer.xlsx'
    # with open(path_name, 'rb') as f:
    #         data = f.read()
    #         temp[0]['excel_data'] = bytes.decode(base64.b64encode(data))
    # print(temp[0]['excel_data'])
    return HttpResponse(json.dumps({'status': 'ok','task_answer_excel': temp}), content_type='application/json')

# 发布者中断当前任务
def interrupt_task(request):
    query_dict = request.GET
    task_id = query_dict.get("taskId", "")
    left_problem_number, add_donut_number = poster_interrupt_current_task(task_id)
    res = {
        'status': 'ok',
        'leftProblemNum': left_problem_number, # 该任务剩了几题没做，用于提示
        'returnDonutNum': add_donut_number,    # 共退还多少甜甜圈，用于提示
    }
    return HttpResponse(json.dumps(res), content_type='application/json')

# 领取者放弃当前任务
def give_up_task(request):
    query_dict = request.GET
    username = query_dict.get("username","")
    task_id = query_dict.get("taskId", "") 
    receiver_give_up_task(username,task_id)
    res = {
        'status': 'ok',
    }
    return HttpResponse(json.dumps(res), content_type='application/json')

# 未发布的任务点击后立即发布
def post_task_immediately(request):
    query_dict = request.GET
    task_id = query_dict.get("taskId", "")
    is_succeed,sub_donut_number, current_donut_number = force_release_task(task_id)
    res = {
        'status': 'ok',
        'isSucceed': is_succeed, # 判断发布是否成功，这里不扣钱了，发布任务那里扣过了
        'needDonutNum': sub_donut_number, # 发布此任务需要多少甜甜圈

        # 如果发布成功，则这个是用户剩下的甜甜圈余额；如果发布失败，则为用户发布任务前的甜甜圈余额
        'leftDonutNum': current_donut_number, 
    }
    return HttpResponse(json.dumps(res), content_type='application/json')

# 管理员审核后删除任务
def delete_task(request):
    query_dict = request.GET
    task_id = query_dict.get("taskId", "")
    delete_reported_task_invalid(task_id)
    delete_violated_task(task_id)
    res = {
        'status':'ok',
    }
    return HttpResponse(json.dumps(res), content_type='application/json')
