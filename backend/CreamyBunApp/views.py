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
    if type == 'getEmail':
        flag = exist_user_by_email(email)
        if flag:
            return HttpResponse(json.dumps({'status': 'wrong', 'type': 'sameEmail'}), content_type='application/json')
        verify_code = send_email(email)
        return HttpResponse(json.dumps({'status': 'ok', 'verifyCode': verify_code}), content_type='application/json')
        # return HttpResponse(json.dumps({'status':'ok'}), content_type='application/json')
    
    #判断是否重名
    flag = exist_user_by_name(username)
    if flag:
        return HttpResponse(json.dumps({'status': 'wrong', 'type': 'sameName'}), content_type='application/json')
    password = query_dict.get("password", "")
    flag = add_a_user(username=username, password=password, email=email)
    if flag:
        return HttpResponse(json.dumps({'status': 'ok'}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'status': 'wrong', 'type': 'unknown'}), content_type='application/json')

# 登录
def log_in(request):
    pass

# 注销
def log_off(request):
    print(request.GET)
    pass


# 修改手机号
def update_mobile(request):
    pass


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
        path = os.path.join("./cache", dirname)
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
            return HttpResponse(json.dumps({'status': 'done', 'fullList': full_list, 'listList': list_list}), content_type='application/json')
            pass
        # query_dict = request.POST
        # file = request.FILES.get('fileName', None)
        # myFile = request.FILES["file"]
        # print(myFile)
        # inp_files = request.FILES  # 上传文件的接收方式应该是request.FILES
        # file_obj = inp_files.get('f1')  # 通过get方法获取upload.html页面提交过来的文件
        # f = open(file_obj.name, 'wb')  # 将客户端上传的文件保存在服务器上，一定要用wb二进制方式写入，否则文件会乱码
        # for line in file_obj.chunks():  # 通过chunks分片上传存储在服务器内存中,以64k为一组，循环写入到服务器中
        #     f.write(line)
        # f.close()
    return HttpResponse(json.dumps({'status': 'next'}), content_type='application/json')
