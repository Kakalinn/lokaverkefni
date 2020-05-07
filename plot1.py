import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.axis('off')
plt.axvline(c = 'black')
plt.axhline(c = 'black')
x = np.linspace(0,1,1000000)
y = 2*np.log2(1/2) - np.log2((x - 0)*(1 - x))
plt.plot(x,y, 'black')
plt.show()
