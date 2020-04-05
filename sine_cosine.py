import math
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-(2*np.pi),2*np.pi,0.1)   # start,stop,step
y = np.sin(x)
z = np.cos(x - np.pi/2)

plt.plot(x,y)
plt.plot(x,z)

plt.xlabel('numbers')
plt.ylabel('cosine or sine values')
plt.show()
