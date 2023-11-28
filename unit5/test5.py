import csv  # 提供了用于读取和写入 CSV 文件的功能

csvfile = open("sec.csv", "w", newline="")  # newline='' 参数指定在写入 CSV 文件时不添加额外的换行符。
wri = csv.writer(
    csvfile, dialect="excel"
)  # 创建了一个 csv.writer 对象 wri，用于向 CSV 文件中写入数据。dialect='excel' 参数指定使用的是 Excel 方言。
wri.writerow(["a", "1", "2", "3"])
wri.writerow(["b", "4", "5", "6"])
wri.writerow(["c", "7", "8", "9"])
csvfile.close()
