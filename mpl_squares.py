import matplotlib.pyplot as plt
"""绘制折线图"""
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
# input_values 相当于x轴，但并不是按列表中的顺序排列的
plt.plot(input_values, squares, linewidth=5)

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
plt.show()
