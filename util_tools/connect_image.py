import numpy as np
import matplotlib.pyplot as plt
x_cords=np.linspace(-100,100,500)
y_cords=np.linspace(-100,100,500)
points=[]
for y in y_cords:
    for x in x_cords:
        if ((x*0.03)**2+(y*0.03)**2-1)**3-(x*0.03)**2*(y*0.03)**3<=0:points.append({"x": x, "y": y})
hear_x=list(map(lambda point:point["x"],points))
hear_y=list(map(lambda point:point["y"],points))
plt.scatter(hear_x,hear_y,s=10,alpha=0.5,c=range(len(hear_x)),cmap="gist_rainbow")
plt.show()