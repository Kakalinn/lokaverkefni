import matplotlib.pyplot as plt
import random
import numpy as np

def foo(a, b):
    x = np.linspace(a + 1e-9, b - 1e-9, 100000)
    y = 2*np.log2((b - a)/2) - np.log2((x - a)*(b - x))
    return x, y

fig, ax = plt.subplots()
ax.axis('off')
ax.set_ylim([0,10])
plt.axvline(c = 'black')
plt.axhline(c = 'black')
n = 0
h = list(np.random.sample(n))
#h.append(0)
#h.append(1)
h = sorted(h)
print(h)

for i in range(len(h)):
    plt.plot(h[i], 0, marker = '.', c = 'black')
for i in range(len(h) - 1):
    x, y = foo(h[i], h[i + 1])
    plt.plot(x, y, 'black', linewidth = 0.5)

x, y = foo(0, 1)
plt.plot(x, y, 'black', linewidth = 0.5)
x, y = foo(0, 1/2)
plt.plot(x, y, 'black', linewidth = 0.5)
x, y = foo(1/2, 1)
plt.plot(x, y, 'black', linewidth = 0.5)
plt.show()
