# 在此处定义全局通用函数

import datetime
import random
from django.core.mail import send_mail
import os
import shutil
import zipfile
import base64
import math
import docx
from ..variables.globalConstants import *

from .databaseOperations import *
from ..variables.globalVariables import *


# 获取系统当前时间，为datetime相关类型
# 可通过成员变量获取年月日时分秒等属性，通过strftime转成字符串返回
# 参考https://www.cnblogs.com/jszfy/p/11143048.html
def get_now_time():
    return datetime.datetime.now()


# 发送邮件并返回验证码
def send_email(email):
    code_base = '0123456789'
    varify_code = ''
    for i in range(0, 6):
        varify_code += code_base[random.randrange(0, len(code_base))]

    # 发送邮件：
    # send_mail的参数分别是  邮件标题，邮件内容，发件箱(settings.py中设置过的那个)，收件箱列表(可以发送给多个人),失败静默(若发送失败，报错提示我们)
    message = "您的验证码是" + varify_code + "，10分钟内有效，请尽快填写"
    emailBox = []
    emailBox.append(email)
    send_mail('奶黄包数据标注平台邮箱验证码', message, '1596741408@qq.com', emailBox, fail_silently=False)
    return varify_code


# 管理员修改指定等级的升级所需经验
def set_exp_for_upgrade(rank, exp):
    global exp_for_upgrade
    exp_for_upgrade[rank - 1] = exp


# 管理员修改指定星级任务完成后可获得的经验值
def set_exp_by_task_rank(rank, exp):
    global exp_by_task_rank
    exp_by_task_rank[rank - 1] = exp


# 管理员修改指定星级任务的单题保底甜甜圈报酬
def set_donut_from_a_problem_by_task_rank(rank, donut):
    global donut_from_a_problem_by_task_rank
    donut_from_a_problem_by_task_rank[rank - 1] = donut


# 获取当前等级所需的升级经验
def get_exp_for_upgrade(rank):
    global exp_for_upgrade
    return exp_for_upgrade[rank - 1]


# 获取当前星级任务完成后可获得的经验
def get_exp_by_task_rank(rank):
    global exp_by_task_rank
    return exp_by_task_rank[rank - 1]


# 获取当前星级任务的单题保底甜甜圈报酬
def get_donut_from_a_problem_by_task_rank(rank):
    global donut_from_a_problem_by_task_rank
    return donut_from_a_problem_by_task_rank[rank - 1]


# 管理员设置多少甜甜圈可兑换一元
def set_donut_to_money(donut_number):
    global donut_to_money
    donut_to_money = donut_number


# 获取多少甜甜圈可兑换一元
def get_donut_to_money():
    global donut_to_money
    return donut_to_money


# 管理员设置一元人民币可兑换的甜甜圈数量
def set_money_to_donut(donut_number):
    global money_to_donut
    money_to_donut = donut_number


# 获取一元人民币可兑换的甜甜圈数量
def get_money_to_donut():
    global money_to_donut
    return money_to_donut

# 获取指定用户、指定页码、指定状态、指定筛选条件的任务列表
def get_task_info_list(username, state, page_number, sort_choice):
    u = get_a_user_data(username)
    page_number = eval(page_number)
    sort_choice = eval(sort_choice)
    all_task_to_state = u.task_info_list.all()  # 返回了字典model对象的列表

    # 存了所有的符合状态的任务的id 
    needed_task_to_state_list = [x for x in all_task_to_state if x.task_status_for_user == state]
    if sort_choice == 0:
        needed_task_to_state_list = [x.task_id for x in needed_task_to_state_list]
    else:
        needed_task_to_state_list = [x.task_id for x in needed_task_to_state_list if
                                     x.task_status_for_itself == sort_choice]

    # 反转，最新的在最前面
    needed_task_to_state_list = list(reversed(needed_task_to_state_list))

    # 总页数
    total_number = len(needed_task_to_state_list)
    total_page_number = math.ceil(total_number / TASK_NUMBER_PER_PAGE)

    begin_index = TASK_NUMBER_PER_PAGE * (page_number - 1)
    if page_number == total_page_number:  # 最后一页
        needed_task_to_state_list = needed_task_to_state_list[begin_index:]
    elif page_number < total_page_number:
        needed_task_to_state_list = needed_task_to_state_list[begin_index:begin_index + TASK_NUMBER_PER_PAGE]
    else:  # 超过页码范围
        needed_task_to_state_list = []

    task_info_list = []
    # i从0开始
    for i, t_id in enumerate(needed_task_to_state_list):
        t = get_a_task_data(t_id)
        t_info = {

            'isSpace': False,
            'id': t_id,
            'taskName': t.task_name,
            'starNum': t.star_rank,
            'donut': t.single_bonus,
            'dataType': TASK_TYPE_DICT[t.task_type],
            'problemType': ANSWER_TYPE_DICT[t.answer_type],
            'startTime': t.begin_time.split(" ")[0],
            'endTime': t.end_time.split(" ")[0],
        }
        t_info.setdefault('index', i)
        task_info_list.append(t_info)

    # 填充空白
    info_list_length = len(task_info_list)
    if info_list_length < TASK_NUMBER_PER_PAGE:
        for i in range(info_list_length, TASK_NUMBER_PER_PAGE):
            t_info = {
                'index': i,
                'isSpace': True,
            }
            task_info_list.append(t_info)

    # 返回 总页数（int），任务信息列表（列表，成员为字典）

    return total_number, task_info_list


# 修改用户头像并保存至后端
def change_user_avatar(image, username):
    avatar_url = USER_AVATAR_SAVE_PATH + username + "." + image.name
    update_avatar_url_by_username(username, avatar_url)
    with open(avatar_url, 'wb') as f:
        for line in image:
            f.write(line)

# 获得管理员用户名和密码
def get_admin_username_with_password():
    global admin_username,admin_password
    return (admin_username,admin_password)

# 获得管理员密令
def get_admin_token():
    global admin_token
    return admin_token

# 修改管理员用户名
def set_admin_username(new_name):
    global admin_username
    admin_username = new_name

# 修改管理员密码
def set_admin_password(new_password):
    global admin_password
    admin_password = new_password


# 获取用户头像base64格式
def get_user_avatr(username):
    avatar_url = get_a_user_data(username).avatar_url
    if not os.path.exists(avatar_url):
        return None
    else:
        with open(avatar_url, 'rb') as f:
            data = f.read()
            return bytes.decode(base64.b64encode(data))


# 下载前端的分块文件
def handle_uploaded_file(f, path='./temp/test.zip'):
    with open(path, 'ab+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


# 编码修正
def recode(raw: str) -> str:
    try:
        return raw.encode('cp437').decode('gbk')
    except:
        return raw.encode('utf-8').decode('utf-8')


# 解压文件
def unzip_file(zip_src, target_path) -> None:
    with zipfile.ZipFile(file=zip_src, mode='r') as file:
        # 遍历压缩包内所有内容
        for file_or_path in file.namelist():
            # 若当前节点是文件夹
            if file_or_path.endswith('/'):
                try:
                    # 基于当前文件夹节点创建多层文件夹
                    os.makedirs(os.path.join(target_path, recode(file_or_path)))
                except FileExistsError:
                    # 若已存在则跳过创建过程
                    pass
            # 否则视作文件进行写出
            else:
                # 利用shutil.copyfileobj，从压缩包io流中提取目标文件内容写出到目标路径
                with open(os.path.join(target_path, recode(file_or_path)), 'wb') as z:
                    # 这里基于Zipfile.open()提取文件内容时需要使用原始的乱码文件名
                    shutil.copyfileobj(file.open(file_or_path), z)


# # 向已存在的指定文件夹完整解压当前读入的zip文件
# def unzip_file2(zip_src, dst_dir):
#     r = zipfile.is_zipfile(zip_src)
#     if r:
#         f = zipfile.ZipFile(zip_src, 'r')  # 压缩文件位置
#         for file in f.namelist():
#             print(file, dst_dir)
#             f.extract(file, dst_dir)  # 解压位置
#         f.close()
#     else:
#         print('This is not zip')
#
#
# def unzip_file1(zip_src, dst_dir):
#     # a = zip_src.encode('cp437').decode('gbk')
#     # b = dst_dir.encode('cp437').decode('gbk')
#     # r = zipfile.is_zipfile(zip_src)
#     #
#     # if r:
#     #     f = zipfile.ZipFile(a, 'r')  # 压缩文件位置
#     #     for file in f.namelist():
#     #         f.extract(file, b)  # 解压位置
#     #     f.close()
#     # else:
#     #     print('This is not zip')
#     with zipfile.ZipFile(file=zip_src, mode='r') as zf:
#         # 解压到指定目录,首先创建一个解压目录
#         for old_name in zf.namelist():
#             # 获取文件大小，目的是区分文件夹还是文件，如果是空文件应该不好用。
#             file_size = zf.getinfo(old_name).file_size
#             # 由于源码遇到中文是cp437方式，所以解码成gbk，windows即可正常
#             # old_name = old_name.encode('gbk').decode('cp437')
#             print("old_name", old_name)
#             new_name = old_name.encode('cp437').decode('gbk')
#             print("new_name", new_name)
#             # 拼接文件的保存路径
#             new_path = os.path.join(dst_dir, new_name)
#             # 判断文件是文件夹还是文件
#             if file_size > 0:
#                 # 是文件，通过open创建文件，写入数据
#                 with open(file=new_path, mode='wb') as f:
#                     # zf.read 是读取压缩包里的文件内容
#                     try:
#                         f.write(zf.read(old_name))
#                     except:
#                         f.write(zf.read(new_name))
#             else:
#                 # 是文件夹，就创建
#                 os.mkdir(new_path)

# 将大小转化为Bytes/KB/MB/GB形式
def get_formatted_size_string(sizeInBytes):
    for (cutoff, label) in [(1024 * 1024 * 1024, "GB"), (1024 * 1024, "MB"), (1024, "KB"), ]:
        if sizeInBytes >= cutoff:
            return "%.1f %s" % (sizeInBytes * 1.0 / cutoff, label)
        if sizeInBytes == 1:
            return "1 byte"
        else:
            tempBytes = "%.1f" % (sizeInBytes or 0,)
    return (tempBytes[:-2] if tempBytes.endswith('.0') else tempBytes) + ' bytes'


# 遍历目录下所有文件并返回给前端列表
def walk_file(file, material_type):
    output_list = []
    j = 1
    output_dirs = []
    for base, dirs, _ in os.walk(file):
        print(base, dirs)
        for d in dirs:

            dirPath = os.path.join(base, d)
            sub_list = []
            i = 1
            for root, _, files in os.walk(dirPath):
                # root 表示当前正在访问的文件夹路径
                # dirs 表示该文件夹下的子目录名list
                # files 表示该文件夹下的文件list
                # 遍历文件
                for f in files:
                    file_type = os.path.splitext(f)[-1][1:]
                    file_path = os.path.join(root, f)

                    if file_type not in TYPE_SET[material_type]:
                        print(TYPE_SET[material_type], "删除了：", file_path)
                        os.remove(file_path)
                        continue
                    # 防止混合类型
                    file_type_num = material_type
                    if file_type_num == 4:
                        k = 0
                        for temp_set in TYPE_SET:
                            if file_type in temp_set:
                                file_type_num = k
                                break
                            k += 1

                    fileInfo = os.stat(file_path)
                    sub_list.append({'index': i,
                                     'fileName': f,
                                     'fileSize': get_formatted_size_string(fileInfo.st_size),
                                     'totalSize': fileInfo.st_size,
                                     'fileType': file_type_num,
                                     'filePath': file_path,
                                     'list': d,
                                     })
                    i += 1
            output_dirs.append({'index': j,
                                'listName': d,
                                'listLen': i - 1,
                                'notes': ''})
            j += 1
            output_list.append(sub_list)
            # 遍历所有的文件夹
            # for d in dirs:
            #     print(os.path.join(root, d))
    return output_list, output_dirs


def get_problem_material(avatar_url):
    if not os.path.exists(avatar_url):
        return None
    else:
        with open(avatar_url, 'rb') as f:
            data = f.read()
            return bytes.decode(base64.b64encode(data))


def get_suffix(input_str):
    temp_list = input_str.split('.')
    temp = temp_list[-1]
    return temp


def take_single_bonus(elem):
    return elem.single_bonus


def take_begin_time(elem):
    return elem.begin_time


def take_end_time(elem):
    return elem.end_time


def take_star_rank(elem):
    return elem.star_rank


def sorted_and_selected_tasks(username, seach_content, only_level, \
                              donut_type, over_type, new_type, \
                              hard_type, data_type, answer_type, page_number):
    # seach_content:搜索框输入的内容，用于模糊搜索(TODO:暂时不做)

    u = get_a_user_data(username)

    # 得到所有的任务列表
    all_task = Task.objects.all()

    # data_type:int 1:所有 2：图片 3：文本 4：视频  5：音频 6：混合
    if data_type > 1:
        all_task = all_task.filter(task_type=(data_type - 2))

    # answer_type:int 1:所有 2：单选 3：多选 4：填空 5：框图 6：混合
    if answer_type > 1:
        all_task = all_task.filter(answer_type=(answer_type - 2))

    # 必须是已经发布的任务
    all_task = [x for x in all_task if (get_now_time().strftime('%F %T') >= x.begin_time)]

    # over_type: int 1:所有 2：未结束 3：已结束
    if over_type > 1:
        if over_type == 3:
            all_task = [x for x in all_task if ((x.finished_problem_number == x.problem_total_number) \
                                                or get_now_time().strftime('%F %T') >= x.end_time)]
        else:
            all_task = [x for x in all_task if ((x.finished_problem_number < x.problem_total_number) \
                                                and get_now_time().strftime('%F %T') < x.end_time)]
    # username:用户名用来获取等级啥的
    # only_level:bool false:所有 true:只选入满足做题者等级的
    if only_level:
        all_task = [x for x in all_task if (x.star_rank <= u.credit_rank)]

    # 升序：大的在后面，sort默认升序reverse=False

    # hard_type:int 1:默认 2：从难到易 3：从易到难
    if hard_type > 1:
        if hard_type == 2:
            all_task.sort(key=take_star_rank, reverse=True)
        else:
            all_task.sort(key=take_star_rank)

    # new_type:int 1:默认 2：最新发布 3：最早结束
    if new_type > 1:
        if new_type == 2:
            all_task.sort(key=take_begin_time, reverse=True)
        else:
            all_task.sort(key=take_end_time)

    # donut_type:int 1:默认 2:从多到少 3:从少到多 
    if donut_type > 1:
        if donut_type == 2:
            all_task.sort(key=take_single_bonus, reverse=True)
        else:
            all_task.sort(key=take_single_bonus)

    total_number = len(all_task)
    total_page_number = math.ceil(total_number / TASK_NUMBER_PER_PAGE)

    begin_index = TASK_NUMBER_PER_PAGE * (page_number - 1)
    if page_number == total_page_number:  # 最后一页
        all_task = all_task[begin_index:]
    elif page_number < total_page_number:
        all_task = all_task[begin_index:begin_index + TASK_NUMBER_PER_PAGE]
    else:  # 超过页码范围
        all_task = []

    task_info_list = []
    # i从0开始
    for i, t in enumerate(all_task):
        t_info = {
            'isSpace': False,
            'id': t.id,
            'taskName': t.task_name,
            'starNum': t.star_rank,
            'donut': t.single_bonus,
            'dataType': TASK_TYPE_DICT[t.task_type],
            'problemType': ANSWER_TYPE_DICT[t.answer_type],
            'startTime': t.begin_time.split(" ")[0],
            'endTime': t.end_time.split(" ")[0],
        }
        t_info.setdefault('index', i)
        task_info_list.append(t_info)

    # 填充空白
    info_list_length = len(task_info_list)
    if info_list_length < TASK_NUMBER_PER_PAGE:
        for i in range(info_list_length, TASK_NUMBER_PER_PAGE):
            t_info = {
                'index': i,
                'isSpace': True,
            }
            task_info_list.append(t_info)

    return total_number, task_info_list


def word_to_str(path):
    """将word文本转化为字符串"""
    # 打开word文件
    file = docx.Document(path)  # 选择文件所在目录
    # 读取word文本
    text_list = [x.text for x in file.paragraphs]
    # 将list中的内容按空格拼接为str
    text_str = "\n".join(text_list)
    return text_str


def txt_to_str(path):
    data = ''
    with open(path, "r", encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip()
            data += line
            data += '\n'
    return data


def read_material_str(path, suffix):
    output = '这是一个临时的字符串'
    if suffix == 'doc' or suffix == 'docx':
        output = word_to_str(path)
    elif suffix == 'txt':
        output = txt_to_str(path)
    return output


def file_iterator(file_name, chunk_size=8192, offset=0, length=None):
    with open(file_name, "rb") as f:
        f.seek(offset, os.SEEK_SET)
        remaining = length
        while True:
            bytes_length = chunk_size if remaining is None else min(remaining, chunk_size)
            data = f.read(bytes_length)
            if not data:
                break
            if remaining:
                remaining -= len(data)
            yield data

def send_feedback_email(email,message):
    emailBox = []
    emailBox.append(email)
    send_status = send_mail('奶黄包数据标注平台反馈处理结果', message, '1596741408@qq.com', emailBox, fail_silently=False)
    return send_status

def create_a_reported_image(image,path):
    try:
        with open(path, 'wb') as f:
            for line in image:
                f.write(line)
        return True
    except:
        return False

# 领取任务
def user_receive_current_task(username,task_id):
    u = get_a_user_data(username)
    t = get_a_task_data(task_id)
    p_list = t.problem_list.all()

    # 确定测试题列表（包括资质检测和穿插题目）
    test_list = []
    for p in p_list:
        if p.is_test == True:
            test_list.append(p)
    
    # 随机打乱一下测试题列表，保证各用户使用的是同一套测试题但收到的具体测试题目顺序不同
    random.shuffle(test_list)

    # 资质测试题目数量
    before_test_number = math.ceil(len(test_list)/2)

    td = TaskDict.objects.create(task_id=task_id,task_status_for_user=HAS_RECEIVED,\
                                task_status_for_itself=NOT_FINISHED,test_problem_number=before_test_number)

    # 要做的题目列表
    normal_test_list = []
    for p in p_list:
        if len(normal_test_list) >= t.problem_number_for_single_receiver:
            break
        if p.is_test == False and p.current_state == NOT_RECEIVED:
            normal_test_list.append(p)
            p.current_state = RECEIVED_BUT_NOT_FINISHED
            p.save()

    # 要做的题目里面加上插入的测试题
    for i in range(before_test_number,len(test_list)):
        normal_test_list.append(test_list[i])

    # 随机打乱要做的题目列表
    random.shuffle(normal_test_list)

    # 确定被领取的题目列表
    received_problem_list = test_list[0:before_test_number] + normal_test_list
    for p in received_problem_list:
        p_id = Int.objects.create(int_content=p.id)
        td.received_problem_id_list.add(p_id)

    u.task_info_list.add(td)