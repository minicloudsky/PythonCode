#coding: utf-8
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [1,4,9,16,25]
plt.scatter(x,y,s = 100)
plt.title("Square Number")
plt.xlabel("x",fontsize = 15)
plt.ylabel("y",fontsize = 15)
plt.show()