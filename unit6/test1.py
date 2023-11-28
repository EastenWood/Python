class Animal:
    def __init__(self, name):  # 定义构造方法
        self.name = name

    def run(self):
        print("正在跑步")


class cat(Animal):
    def __init__(self, name):  # 重写构造方法
        Animal.__init__(self, name)  # 调用父类的构造方法

    def printName(self):
        print("猫的名字:%s" % self.name)


cat1 = cat("lxh")
cat1.printName()
cat1.run()
