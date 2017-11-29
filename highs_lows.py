import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_072014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 查看第一行每一列的信息（表头）
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # 取出某一列或几列的所有值
    dates, highs = [], []
    for row in reader:
        current_date = datetime.striptime(row[0],"%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)

    # 根据数据绘制图形
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates,highs, c='red')
    # 设置图形的格式
    plt.title("Daily high temperatures, July", fontsize=14)
    plt.xlabel('', fontsize=16)
    # 绘制斜的日期标签
    fig.autofmt_xdate()
    plt.ylabel("Temperature(F)", fontsize=16)

    # 设置刻度标记的大小
    plt.tick_params(axis="both", which='major', labelsize=16)

    plt.show()
