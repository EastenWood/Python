def transform_1(s):  # 小写转大写
    a = ""
    for c in s:
        if "a" <= c <= "z":
            c = chr(ord(c) - 32)
        a += c
    return a


def transform_2(s):  # 大写转小写
    a = ""
    for c in s:
        if "A" <= c <= "Z":
            c = chr(ord(c) + 32)
        a += c
    return a


ba = input()
print(transform_1(ba))
print(transform_2(ba))
