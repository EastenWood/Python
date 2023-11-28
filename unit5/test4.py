import os


def getcwd():
    cat = os.getcwd()  # 获取当前工作目录的路径
    return cat


def listdir(cat):
    if os.path.exists(cat):  # 如果存在，返回子目录
        return os.listdir(cat)
    else:
        return "目录" + cat + "不存在"


a = getcwd()
print(a)
print(listdir(a))
