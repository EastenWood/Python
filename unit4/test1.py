# 斐波那契数列
def Fib(num):
    fib = [1]
    for i in range(num):
        if i < 2:
            fib.append(i + 1)
        else:
            fib.append(sum(fib[-2:]))
    return fib


n = int(input("输入一个数字："))
print(*Fib(n), sep=",")
