try:
    f = open(r"text.txt", "w")
    while True:
        s = input()
        if s.upper() == "E":
            break
        f.write(s + "\n")
except KeyboardInterrupt:
    print("输入Ctrl+Z时程序终止！")
finally:
    print("正常关闭文件！")
f.close()
