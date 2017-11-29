import matplotlib.pyplot as plt

"""绘制散点图"""

# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25]
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

# 点默认为蓝色点和黑色轮廓，可通过edgecolor='none'去除轮廓,自定义颜色 c=
plt.scatter(x_values, y_values,c=(0,0,0.8), edgecolors='none', s=200)

# 使用颜色映射
# plt.scatter(x_values, y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none', s=200)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=10)
plt.ylabel("Square of Value", fontsize=10)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
# 自动保存图表到文件  1，当前目录  2，裁剪多余的空白区域
plt.savefig('squares_plot.png',bbox_inches='tight')
