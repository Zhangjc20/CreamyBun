# 在此处定义全局通用函数

import datetime
import random
from django.core.mail import send_mail
import os
import shutil
import zipfile
from ..variables.globalConstants import *

from .databaseOperations import *
from ..variables.globalVariables import *

# 获取系统当前时间，为datetime相关类型
# 可通过成员变量获取年月日时分秒等属性，通过strftime转成字符串返回
# 参考https://www.cnblogs.com/jszfy/p/11143048.html
def get_now_time():
    return datetime.datetime.now().strftime('%F %T')


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

def handle_uploaded_file(f, path='./temp/test.zip'):
    """
    下载前端的分块文件
    """
    with open(path, 'ab+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def recode(raw: str) -> str:
    """
    编码修正
    """
    try:
        return raw.encode('cp437').decode('gbk')
    except:
        return raw.encode('utf-8').decode('utf-8')


def unzip_file(zip_src, target_path) -> None:
    """
    解压文件
    """
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


def get_formatted_size_string(sizeInBytes):
    """
    将大小转化为bytes/KB/MB/GB形式
    """
    for (cutoff, label) in [(1024 * 1024 * 1024, "GB"), (1024 * 1024, "MB"), (1024, "KB"), ]:
        if sizeInBytes >= cutoff:
            return "%.1f %s" % (sizeInBytes * 1.0 / cutoff, label)
        if sizeInBytes == 1:
            return "1 byte"
        else:
            tempBytes = "%.1f" % (sizeInBytes or 0,)
    return (tempBytes[:-2] if tempBytes.endswith('.0') else tempBytes) + ' bytes'


def walk_file(file, material_type):
    """
    遍历目录下所有文件并返回给前端列表
    """
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

                    fileInfo = os.stat(file_path)
                    sub_list.append({'index': i,
                                     'fileName': f,
                                     'fileSize': get_formatted_size_string(fileInfo.st_size),
                                     'totalSize': fileInfo.st_size,
                                     'fileType': "寄了",
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

# 检查用户名和密码是否匹配
def match_username_with_password(username,password):
    cur_user = get_a_user_data(username)
    if cur_user.password == password:
        return True
    else:
        return False 

# 管理员修改指定等级的升级所需经验
def set_exp_for_upgrade(rank,exp):
    global exp_for_upgrade
    exp_for_upgrade[rank-1]=exp

# 管理员修改指定星级任务完成后可获得的经验值
def set_exp_by_task_rank(rank,exp):
    global exp_by_task_rank
    exp_by_task_rank[rank-1]=exp

# 管理员修改指定星级任务的单题保底甜甜圈报酬
def set_donut_from_a_problem_by_task_rank(rank,donut):
    global donut_from_a_problem_by_task_rank
    donut_from_a_problem_by_task_rank[rank-1]=donut

# 获取当前等级所需的升级经验
def get_exp_for_upgrade(rank):
    global exp_for_upgrade
    return exp_for_upgrade[rank-1]

# 获取当前星级任务完成后可获得的经验
def get_exp_by_task_rank(rank):
    global exp_by_task_rank
    return exp_by_task_rank[rank-1]

# 获取当前星级任务的单题保底甜甜圈报酬
def get_donut_from_a_problem_by_task_rank(rank):
    global donut_from_a_problem_by_task_rank
    return donut_from_a_problem_by_task_rank[rank-1]

# 管理员设置多少甜甜圈可兑换一元
def set_donut_to_money(donut_number):
    global donut_to_money
    donut_to_money=donut_number


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