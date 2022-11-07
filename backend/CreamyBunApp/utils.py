import os
import shutil
import zipfile


def recode(raw: str) -> str:
    """
    编码修正
    """
    try:
        return raw.encode('cp437').decode('gbk')
    except:
        return raw.encode('utf-8').decode('utf-8')


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


# 向已存在的指定文件夹完整解压当前读入的zip文件

def unzip_file2(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:
        f = zipfile.ZipFile(zip_src, 'r')  # 压缩文件位置
        for file in f.namelist():
            print(file, dst_dir)
            f.extract(file, dst_dir)  # 解压位置
        f.close()
    else:
        print('This is not zip')


def unzip_file1(zip_src, dst_dir):
    # a = zip_src.encode('cp437').decode('gbk')
    # b = dst_dir.encode('cp437').decode('gbk')
    # r = zipfile.is_zipfile(zip_src)
    #
    # if r:
    #     f = zipfile.ZipFile(a, 'r')  # 压缩文件位置
    #     for file in f.namelist():
    #         f.extract(file, b)  # 解压位置
    #     f.close()
    # else:
    #     print('This is not zip')
    with zipfile.ZipFile(file=zip_src, mode='r') as zf:
        # 解压到指定目录,首先创建一个解压目录
        for old_name in zf.namelist():
            # 获取文件大小，目的是区分文件夹还是文件，如果是空文件应该不好用。
            file_size = zf.getinfo(old_name).file_size
            # 由于源码遇到中文是cp437方式，所以解码成gbk，windows即可正常
            # old_name = old_name.encode('gbk').decode('cp437')
            print("old_name", old_name)
            new_name = old_name.encode('cp437').decode('gbk')
            print("new_name", new_name)
            # 拼接文件的保存路径
            new_path = os.path.join(dst_dir, new_name)
            # 判断文件是文件夹还是文件
            if file_size > 0:
                # 是文件，通过open创建文件，写入数据
                with open(file=new_path, mode='wb') as f:
                    # zf.read 是读取压缩包里的文件内容
                    try:
                        f.write(zf.read(old_name))
                    except:
                        f.write(zf.read(new_name))
            else:
                # 是文件夹，就创建
                os.mkdir(new_path)


def getSizeInNiceString(sizeInBytes):
    """
    Convert the given byteCount into a string like: 9.9bytes/KB/MB/GB
    """
    for (cutoff, label) in [(1024 * 1024 * 1024, "GB"), (1024 * 1024, "MB"), (1024, "KB"), ]:
        if sizeInBytes >= cutoff:
            return "%.1f %s" % (sizeInBytes * 1.0 / cutoff, label)
        if sizeInBytes == 1:
            return "1 byte"
        else:
            tempBytes = "%.1f" % (sizeInBytes or 0,)
    return (tempBytes[:-2] if tempBytes.endswith('.0') else tempBytes) + ' bytes'


def walk_file(file):
    outputList = []
    i = 0
    for root, dirs, files in os.walk(file):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        # 遍历文件
        for f in files:
            tempPath = os.path.join(root, f)
            fileInfo = os.stat(tempPath)
            outputList.append({'index': i + 1,
                               'fileName': f,
                               'fileSize': getSizeInNiceString(fileInfo.st_size),
                               'fileType': "寄了"
                               })
            i += 1
        # 遍历所有的文件夹
        for d in dirs:
            print(os.path.join(root, d))
    return outputList
