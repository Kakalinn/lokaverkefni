#approc regions
from matplotlib import collections
import matplotlib.pyplot as plt
import random
import numpy as np
from math import sin, cos

fig, ax = plt.subplots()
ax.axis('off')
ax.set_xlim([-1.1, 1.1])
ax.set_ylim([-1.1, 1.1])
plt.axvline(c = 'black')
plt.axhline(c = 'black')


l = []
alpha = 0.7
circle1 = plt.Circle((0, 0), alpha, color = 'black', fill = False)
ax.add_artist(circle1)

n = 100000
for i in range(n):
    l.append([(alpha*cos(i), alpha*sin(i)), (1.0, 0.0)])
lc = collections.LineCollection(l, colors = 'black', linewidths = 0.5)
ax.add_collection(lc)

plt.show()

