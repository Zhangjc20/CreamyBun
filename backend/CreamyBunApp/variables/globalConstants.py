# 在此处定义全局常量

# 用户头像储存位置
USER_AVATAR_SAVE_PATH = "./resource/user_avatar/"

# 任务发布模式
NOW_RELEASE = 0
NOT_YET_RELEASE = 1
TIMED_RELEASE = 2

# 任务自身状态常量（完成）
NOT_FINISHED = 1
HAS_FINISHED = 2

# 任务自身状态常量（发布）
NOT_RELEASE = 1
RELEASE_BUT_NOT_FINISHED = 2
FINISHED = 3

# 用户任务状态常量
HAS_RECEIVED = 1
HAS_POSTED = 2

# 问题反馈类型
FUNCTION_ADVICE = 1
INTERFACE_OPTIMIZE = 2
PRODUCT_BUG = 3
REPORT = 4  # 举报
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

# 任务类型中文
TASK_TYPE_DICT = ["图片", "文本", "视频", "音频", "混合"]

# 作答类型常量
SINGLE_CHOICE = 0
SEVERAL_CHOICES = 1
FILL_BLANK = 2
SELECT_FRAME = 3
MULTI_TASK = 4

# 作答类型中文
ANSWER_TYPE_DICT = ["单选题", "多选题", "填空题", "框图题", "混合"]

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
AUDIO_TYPE_SET = {'mp3', 'wav', 'm4a'}
ALL_TYPE_SET = IMAGE_TYPE_SET | TEXT_TYPE_SET | VIDEO_TYPE_SET | AUDIO_TYPE_SET
TYPE_SET = [IMAGE_TYPE_SET, TEXT_TYPE_SET, VIDEO_TYPE_SET, AUDIO_TYPE_SET, ALL_TYPE_SET]

fake_ans = {
    "materialList": [

        {
            "fileType": 0,
            "filePath": "./resource/task_materials\\ZDandsomSP_20221120152607\\list1\\图片 (2).jpg",
            "fileNotes": "这是一张图"
        },
        {
            "fileType": 1,
            "filePath": "./resource/task_materials\\ZDandsomSP_20221120152607\\list2\\文本 (3).txt",
            "fileNotes": "这是一文本"
        },
        {
            "fileType": 2,
            "filePath": "./resource/task_materials\\ZDandsomSP_20221120152607\\list3\\视频 (5).mp4",
            "fileNotes": "这是一视频"
        },
        {
            "fileType": 3,
            "filePath": "./resource/task_materials\\ZDandsomSP_20221120152607\\list4\\音频 (5).mp3",
            "fileNotes": "这是一音频"
        },
    ],
    "questionList": [
        {
            "questionTypeName": "单选",
            "questionType": 0,
            "questionDescription": "我是单选题",
            "optionList": [
                {
                    "index": 0,
                    "name": "A",
                    "content": "我是单选A"
                },
                {
                    "index": 1,
                    "name": "B",
                    "content": "我是单选B"
                }
            ],
            "minOptionNum": 1,
            "maxOptionNum": 1,
            "targetIndex": "",
            "mustDo": True,
            "questionAns": "",
            "index": 1
        },
        {
            "questionTypeName": "多选",
            "questionType": 1,
            "questionDescription": "我是多选题",
            "optionList": [
                {
                    "index": 0,
                    "name": "A",
                    "content": "我是多选A"
                },
                {
                    "index": 1,
                    "name": "B",
                    "content": "我是多选B"
                },
                {
                    "index": 2,
                    "name": "C",
                    "content": "我是多选C"
                },
                {
                    "index": 3,
                    "name": "D",
                    "content": "我是多选D"
                }
            ],
            "minOptionNum": 2,
            "maxOptionNum": 3,
            "targetIndex": "",
            "mustDo": False,
            "questionAns": "",
            "index": 2
        },
        {
            "questionTypeName": "填空",
            "questionType": 2,
            "questionDescription": "我是填空题",
            "optionList": [],
            "minOptionNum": 20,
            "maxOptionNum": 2000,
            "targetIndex": "",
            "mustDo": True,
            "questionAns": "",
            "index": 3
        },
        {
            "questionTypeName": "单选",
            "questionType": 3,
            "questionDescription": "我是框图题",
            "optionList": [],
            "minOptionNum": 2,
            "maxOptionNum": 10,
            "targetIndex": 1,
            "mustDo": False,
            "questionAns": "",
            "index": 4
        }
    ],
}
