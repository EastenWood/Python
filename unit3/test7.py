# 水仙花数
for n in range(100, 1000):
    a = n % 10  # 个位
    b = (n % 100) // 10  # 十位
    c = n // 100  # 百位
    if a**3 + b**3 + c**3 == n:
        print(n, end=" ")
