class SchoolMem:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def get(self):
        print("姓名: {}, 性别: {}, 年龄: {}".format(self.name, self.gender, self.age))


class Student(SchoolMem):
    def __init__(self, name, gender, age, banji, snumber, grade):
        SchoolMem.__init__(self, name, gender, age)
        self.banji = banji
        self.snumber = snumber
        self.grade = grade

    def printInfo(self):
        SchoolMem.get(self)
        print("班级: {}, 学号: {}, 成绩: {}".format(self.banji, self.snumber, self.grade))


class Teacher(SchoolMem):
    def __init__(self, name, gender, age, keshi, gonghao, salary):
        SchoolMem.__init__(self, name, gender, age)
        self.keshi = keshi
        self.gonghao = gonghao
        self.salary = salary

    def printInfo(self):
        SchoolMem.get(self)
        print("科室: {}, 工号: {}, 工资: {}".format(self.keshi, self.gonghao, self.salary))


student1 = Student("陈根", "男", 19, "计算机2201班", "2211640101", 100)
student2 = Student("廖熙徽", "男", 19, "计算机2201班", "2211640104", 92)
teacher1 = Teacher("李老师", "女", 35, "计算机科", "T2023", 5000)
teacher2 = Teacher("郭老师", "男", 43, "数学科", "T2022", 5500)
print("学生信息：")
student1.printInfo()
student2.printInfo()
print("\n老师信息：")
teacher1.printInfo()
teacher2.printInfo()
