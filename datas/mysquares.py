#coding: utf-8
import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
s = [1,4,9,16,25]
plt.plot(input_values,s,linewidth = 5)
plt.title("Square Numbers",fontsize = 15)
plt.xlabel("Value",fontsize = 15)
plt.ylabel("Squares of values",fontsize = 15)
plt.plot()
plt.show()