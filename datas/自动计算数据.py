#coding: utf-8
import matplotlib.pyplot as plt
x_value = list(range(1,1001))
y = [x**2 for x in x_value]
# c为数据点颜色
plt.scatter(x_value,y,s = 40,edgecolors='none',c = 'red')
plt.title("Square Number")
plt.xlabel("x",fontsize = 15)
plt.ylabel("y",fontsize = 15)
# 设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])
plt.show()