from matplotlib import collections
import matplotlib.pyplot as plt
import random
import numpy as np

def foo(a, b):
    x = np.linspace(a + 1e-9, b - 1e-9, 100000)
    y = 2*np.log2((b - a)/2) - np.log2((x - a)*(b - x))
    return x, y

fig, ax = plt.subplots()
ax.axis('off')
ax.set_ylim([0, 8])
plt.axvline(c = 'black')
plt.axhline(c = 'black')

x, y = foo(0, 1)
plt.plot(x, y, 'black', linewidth = 0.5)

l = []
n = 1000
for i in range(n):
    l.append([(2**(-(i + 1)), i + 1), (2**(-(i + 2)), i + 1)])
    l.append([(1.0 - 2**(-(i + 1)), i + 1), (1.0 - 2**(-(i + 2)), i + 1)])
lc = collections.LineCollection(l, colors = 'black', linewidths = 0.5)
ax.add_collection(lc)
plt.show()

