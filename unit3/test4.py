a = int(input("please input a number:"))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print("闰年")
else:
    print("不是闰年")
