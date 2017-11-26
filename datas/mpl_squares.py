#coding: utf-8
import matplotlib.pyplot as plt
squares = [1,4,9,16,25]
# 设置图表标题，饼给坐标轴加上标签
plt.plot(squares,linewidth = 5)
plt.title("Square Numbers",fontsize = 10)
plt.xlabel("Value",fontsize = 10)
plt.ylabel("Square of Value",fontsize = 10)
#设置刻度标记的大小
plt.tick_params(axis='both',labelsize = 14)
plt.show()