a = int(input("输入一个数字："))
factorial = 1
if a < 0:
    print("负数没有阶乘")
elif a == 0:
    print("0!=1")
else:
    for i in range(1, a + 1):
        factorial *= i
    print("{}!={}".format(a, factorial))
