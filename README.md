# CreamyBun
# git 使用
+ 已经在远程仓库的文件加入gitignore不可行，需要git rm -r --cached ./backend/CreamyBunApp/migrations/之后才有用
+ git status --ignored查看被忽略的文件
# 前端配色：蓝色#5EABBF #FBE484

# 前端命名统一
+ css多单词命名用-连接，如nav-bar
+ js文件变量命名，采用小驼峰
+ js文件常量命名，采用全大写的命名
+ js文件函数命名，采用小驼峰，前缀应当为动词，如handleClick
+ 说明Camel Case 小驼峰式命名法：首字母小写。eg：studentInfo、userInfo、productInfo
+ 类 & 构造函数命名方法：大驼峰式命名法，首字母大写。
+ 类的成员公共属性和方法：跟变量和函数的命名一样；私有属性和方法：前缀为_(下划线)，后面跟公共属性和方法一样的命名方式

# 后端命名统一
+ 文件名：小驼峰
+ 类命名：大驼峰
+ 变量名：全小写，多单词用下划线隔开，私有类成员使用单一下划线前缀标识
+ 函数名：全小写，多单词用下划线隔开
+ 常量：全大写，多单词用下划线隔开

# 后端注释规范
+ 函数若要注释，以一行或多行#开头的形式写在函数定义的上一行或上若干行
+ 变量若要注释，直接写在本行末尾
+ 若变量所在行过长或变量注释有多行，则注释写在变量上一行或上若干行，此时变量和注释与代码其它部分须上下各空一行，表示分割
+ 

# 前端注释规范
+ //　用来显示一个解释的评论
+ // ->　用来显示表达式的结果
+ // > 用来显示console的输出结果
+ 多行注释：/**/

# 部署注意事项
+ 服务器 http://101.42.118.80/ 密码 lu4l5xft.0
+ 前端vue.config.js跨域配置仅作用于开发模式，以后axios中地址请直接写全
+ 重新部署步骤：
+ + 后端部分删除CreamyBunApp下migrations/除了__init__.py
+ + 前端部分先将bighw内代码更新（不要求改compose文件夹，可更改frontend和backend），在frontend目录下运行npm run build,该目录下会生成dist文件夹，将该文件夹放到compose/nginx/之内即可
+ ubuntu@VM-0-17-ubuntu: cd /home/ubuntu/bighw/frontend
+ ubuntu@VM-0-17-ubuntu:~/bighw/frontend$ npm run build
+ ubuntu@VM-0-17-ubuntu:~/bighw/frontend$ cp -r dist/ ../compose/nginx/
+ ubuntu@VM-0-17-ubuntu:~/bighw/frontend$ cd ..
+ ubuntu@VM-0-17-ubuntu:~/bighw$ sudo docker-compose build
+ ubuntu@VM-0-17-ubuntu:~/bighw$ sudo docker-compose up (-d) #此时需要等全部部署完才生效，一分钟以内可完成 -d代表在后台运行
+ 先运行sudo docker-compose build，成功后运行sudo docker-compose up
+ 如果需要查看数据库输入以下指令
+ docker-compose exec db /bin/bash
+ mysql -u dbuser -p;
+ 用户名dbuser 密码password
+ 其他操作和原先后端操作一样