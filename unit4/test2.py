def gcd(x, y):
    """求两个数的最大公约数"""
    while x % y != 0:
        r = x % y
        x, y = y, r
    return y


def lcm(x, y):
    """求两个数的最小公倍数"""
    return x * y // gcd(x, y)


num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))
print("{} 和 {} 的最大公约数为 {}".format(num1, num2, gcd(num1, num2)))
print("{} 和 {} 的最小公倍数为 {}".format(num1, num2, lcm(num1, num2)))
