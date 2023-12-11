import numpy as np
import matplotlib.pyplot as plt
r = 2.0
a, b = (0., 0.)
x = np.arange(a-r, a+r, 0.01)
y = b + np.sqrt(r**2 - (x - a)**2)


fig = plt.figure() 
axes = fig.add_subplot(111) 
axes.plot(x, y) # 上半部
axes.plot(x, -y) # 下半部

plt.axis('equal')
plt.show()
