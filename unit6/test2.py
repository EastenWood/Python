class Person(object):
    __name = ""  # 私有变量--姓名
    __age = 0  # 私有变量--年龄
    __sex = ""  # 私有变量--性别

    # 基类必须继承于object，否则在派生类中将无法使用super()函数
    def __init__(self, n, a, s):
        self.setName(n)
        self.setAge(a)
        self.setSex(s)

    def setName(self, n):
        if not isinstance(n, str):
            print("姓名必须是字符串或汉字")
        self.__name = n

    def setAge(self, a):
        if not isinstance(a, int):
            print("年龄必须是整数")
        self.__age = a

    def setSex(self, s):
        if s != "man" and s != "woman" and s != "男" and s != "女":
            print('性别必须为"man" "woman" "男" "女"之一')
        self.__sex = s

    def show(self):
        print(self.__name)
        print(self.__age)
        print(self.__sex)


class Student(Person):
    __major = ""  # 私有变量--专业

    def __init__(self, n, a, s, m):
        # 调用基类构造方法初始化基类的私有数据成员
        super(Student, self).__init__(n, a, s)
        self.setMajor(m)

    # 初始化派生类的数据成员
    def setMajor(self, m):
        if not isinstance(m, str):
            print("姓名必须是字符串或汉字")
        self.__major = m

    def show(self):
        super(Student, self).show()
        print(self.__major)


if __name__ == "__main__":
    ZhangHua = Person("ZhangHua", 17, "男")
    ZhangHua.show()
    LiMei = Student("Limei", 35, "woman", "Math")
    LiMei.show()
    WangQiang = Student("王强", 30, "man", "Computer")
    WangQiang.show()
