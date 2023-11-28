# 引入 datetime 模块
import datetime


def get_oneday():
    today = (
        datetime.date.today()
    )  # datetime.date.today() 是 Python 的 datetime 模块中的一个方法，用于获取当前日期。
    someday = datetime.timedelta(
        days=5
    )  # 这一行创建了一个 datetime.timedelta 对象，表示一个时间间隔，这里的时间间隔是5天。datetime.timedelta 是 Python 的 datetime 模块中的一个类，用于表示时间间隔。
    get_day = today - someday
    return get_day


# 输出
print(get_oneday())
