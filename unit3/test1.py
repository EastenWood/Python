a = []
for i in range(2, 10):
    for b in range(2, int(i**0.5) + 1):
        if i % b == 0:
            break
    else:
        a.append(i)
print("10以内的素数为：" + str(a))
