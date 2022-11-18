# 在此处定义全局常量

# 用户头像储存位置
USER_AVATAR_SAVE_PATH = "./resource/user_avatar/"

# 任务发布模式
NOW_RELEASE = 0
NOT_YET_RELEASE = 1
TIMED_RELEASE = 2

# 任务自身状态常量
NOT_FINISHED = 3
FINISHED = 4

# 用户任务状态常量
HAS_RECEIVED = 1
HAS_POSTED = 2

# 问题反馈类型
FUNCTION_ADVICE = 1
INTERFACE_OPTIMIZE = 2
PRODUCT_BUG = 3
REPORT = 4 # 举报
OTHERS = 5

# problem当前状态
NOT_RECEIVED = 1
RECEIVED_BUT_NOT_FINISHED = 2
FINISHED = 3

# 任务类型常量
IMAGE = 0
TEXT = 1
VIDEO = 2
AUDIO = 3
MIXED = 4

# 作答类型常量
SINGLE_CHOICE = 0
SEVERAL_CHOICES = 1
FILL_BLANK = 2
SELECT_FRAME = 3
MULTI_TASK = 4

# 小题类型常量
CHOICE_QUESTION = 1
FILL_BLANK_QUESTION = 2
SELECT_FRAME_QUESTION = 3

# 用户分页每页任务数量
TASK_NUMBER_PER_PAGE = 10

# 选择题最多选项数
MAX_CHOICE_NUMBER = 26

# 答案字符串最长长度
MAX_ANSWER_LENGTH = 10000

# 框图题最多可以框几个框
MAX_FRAME_NUM = 100

# 小题题干和任务描述最长长度
MAX_DESCRIPTION_LENGTH = 500

# 任务名最长长度
MAX_TASK_NAME_LENGTH = 40

# 时间字符串长度上限
MAX_TIME_STRING_LENGTH = 25

# url最长长度
MAX_URL_LENGTH = 1000

# 邮箱最长长度
MAX_EMAIL_LENGTH = 350

# 签到周期
CLOCK_IN_CYCLE = 7

IMAGE_TYPE_SET = {'jpg', 'bmp', 'png'}
TEXT_TYPE_SET = {'txt', 'docx'}
VIDEO_TYPE_SET = {'mp4'}
AUDIO_TYPE_SET = {'mp3', 'wav'}
ALL_TYPE_SET = IMAGE_TYPE_SET | TEXT_TYPE_SET | VIDEO_TYPE_SET | AUDIO_TYPE_SET
TYPE_SET = [IMAGE_TYPE_SET, TEXT_TYPE_SET, VIDEO_TYPE_SET, AUDIO_TYPE_SET, ALL_TYPE_SET]
