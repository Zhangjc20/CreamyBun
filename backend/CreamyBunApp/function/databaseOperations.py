# 在此处定义对数据库的操作

from ..classDefination.userClass import *
from ..classDefination.questionClass import *

def add_a_user(username,password,email):
    try:
        User.objects.create(username=username,password=password,email=email)
        return True
    except:
        return False

def exist_user_by_name(username):
    try:
        User.objects.get(username=username)
        return True
    except:
        return False

def exist_user_by_email(email):
    try:
        User.objects.get(email=email)
        return True
    except:
        return False

def delete_a_user(username):
    User.objects.filter(username=username).delete()

# 返回的对象可以通过.获取成员变量
def get_a_user_data(username):
    return User.objects.filter(username=username).first()

def update_mobile_number_of_a_user(username,mobile_number):
    User.objects.filter(username=username).update(mobile_number=mobile_number)

def make_a_choice_question(index,question_type,description,must_do,option_list,min_option_num,max_option_num):
    ChoiceQuestion.objects.create(index=index,question_type=question_type,\
                                description=description,must_do=must_do,\
                                min_option_num=min_option_num,max_option_num=max_option_num)
