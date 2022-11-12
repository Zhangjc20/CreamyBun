# 在此处定义对数据库的操作

from ..classDefination.userClass import *
from ..classDefination.taskClass import *
from ..classDefination.questionClass import *
from ..variables.globalVariables import *

# 添加一个用户到用户列表中
def add_a_user(username,password,email):
    try:
        User.objects.create(username=username,password=password,email=email)
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

# 从用户列表中删除指定用户
def delete_a_user(username):
    User.objects.filter(username=username).delete()

# 获取指定用户的数据
# 返回的对象可以通过.获取成员变量
def get_a_user_data(username):
    return User.objects.filter(username=username).first()

# 获取指定任务的数据
def get_a_task_data(id):
    return Task.objects.filter(id=id).first()

# 通过用户名修改密码
def update_password_by_username(username,password):
    User.objects.filter(username=username).update(password=password)

# 通过用户名修改用户名
def update_username_by_username(username,new_username):
    User.objects.filter(username=username).update(username=new_username)

# 通过用户名修改邮箱
def update_email_by_username(username,new_email):
    User.objects.filter(username=username).update(email=new_email)

# 通过邮箱修改密码
def update_password_by_email(email,password):
    User.objects.filter(email=email).update(password=password)

# 通过用户名修改用户头像url
def update_avatar_url_by_username(username,avatar_url):
    User.objects.filter(username=username).update(avatar_url=avatar_url)

# 修改指定用户的手机号
def update_mobile_number_of_a_user(username,mobile_number):
    User.objects.filter(username=username).update(mobile_number=mobile_number)