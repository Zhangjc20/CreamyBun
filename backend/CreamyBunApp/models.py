from django.db import models
#导入uuid
import uuid
from .classDefination.universalClass import *
from .variables.globalVariables import *

# Create your models here.
from django.contrib.auth.models import AbstractUser , UserManager as _UserManager

class UserManager(_UserManager):
    def create_user(self, email, firstname, lastname, phone,password=None):
        user = self.model(
            email = self.normalize_email(email),
            firstname = firstname,
            lastname = lastname,
            phone = phone,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
 
    def create_superuser(self, email,firstname,lastname,phone,password=None):
        user = self.create_user(
            email=email,
            password=password,
            firstname = firstname,
            lastname = lastname,
            phone = phone,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
 
class User(AbstractUser):
    jwt = models.CharField(max_length=20, default="password")
    id = models.CharField(max_length=200, default=uuid.uuid4,unique=True,primary_key=True)
    firstname = models.CharField(null=False, max_length=100)
    lastname = models.CharField(null=False, max_length=100)
    date_joined = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False) 
    username = models.CharField(max_length=12, default="username",unique=True)
    password = models.CharField(max_length=18, default="password")
    email = models.CharField(max_length=MAX_EMAIL_LENGTH, default="email")
    avatar_url = models.CharField(max_length=MAX_URL_LENGTH, default="image")
    mobile_number = models.CharField(max_length=11, default="")
    donut_number = models.IntegerField(default=0)
    credit_rank = models.IntegerField(default=1)
    current_exp = models.IntegerField(default=0)
    dark_mode = models.BooleanField(default=False)
    today_violation = models.IntegerField(default=0)  # 该用户当天已违规次数
    is_today_sign_in = models.BooleanField(default=False)  # 用户当天是否已经签到
    continue_sign_in_days = models.IntegerField(default=0)  # 用户当前连续签到天数

    # 该用户所拥有的所有任务信息，该列表增加的成员为字典类型，表示{任务id:任务状态（已领取或已发布）}
    # 该列表在数据库中的存储格式为字典，如“{1:HAS_POSTED} {2:HAS_RECEIVED}”
    # 新增二级检索常量，包括发布状态或者完成状态
    task_info_list = models.ManyToManyField(TaskDict)
 
    objects = UserManager()
 
    def __str__(self):
        return self.email + ", " + self.firstname
 
    def has_perm(self, perm, obj = None):
        return self.is_admin
 
    def has_module_perms(self, app_label):
        return True
    # 定时重置签到数据接口
    def reset_clock_in_info(self):
        if self.is_today_sign_in == False or self.continue_sign_in_days == CLOCK_IN_CYCLE:
            self.continue_sign_in_days = 0
            self.save()
        self.is_today_sign_in = False
        self.save()

    # 定时重置当天违规次数接口
    def reset_violation(self):
        self.today_violation = 0
        self.save()

    # 检验密码是否匹配
    def validate_password(self, password):
        if self.password == password:
            return True
        else:
            return False

    # 未通过穿插测试惩罚接口
    def punish_for_insertion_test(self):
        self.today_violation += 1
        self.save()
        flag = False
        if self.today_violation > violation_number_per_day:
            flag = True
            temp_exp = self.current_exp
            sub_exp = self.credit_rank * punish_sub_rank_rate
            self.current_exp -= sub_exp
            if self.current_exp < 0:
                self.credit_rank -= 1
                self.current_exp = exp_for_upgrade[self.credit_rank] - sub_exp +temp_exp
                if self.credit_rank == 0:
                    self.credit_rank = 1
                    self.current_exp = 0
        self.save()
        return flag, self.today_violation

    def add_exp_and_upgrade(self,exp_number):
        is_upgrade = False
        credit_rank = -1 # 没升级是-1，升级了是当前等级
        self.current_exp += exp_number

        # 如果升级了
        if self.credit_rank < max_credit_rank and self.current_exp >= exp_for_upgrade[self.credit_rank]:
            is_upgrade = True
            self.current_exp -= exp_for_upgrade[self.credit_rank]
            self.credit_rank += 1
            credit_rank = self.credit_rank
        
        self.save()
        return is_upgrade, credit_rank
