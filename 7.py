import random

a = random.randrange(1, 101)
c = 1
b = int(input("输入猜测的数："))

while b != a:
    c = c + 1
    if b < a:
        print(b, "小了")
    elif b > a:
        print(b, "大了")
    b = int(input("输入猜测的数："))

print(b, "恭喜你猜对了！你猜了", c, "次", sep=" ")