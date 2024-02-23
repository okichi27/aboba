import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')

x = np.arange(0, 10, 2)
ay = [4, 1.25, 3, 2.75, 3.5]
by = [1, 4, 1, 3, 1]
cy = [2, 1, 2, 4, 2]
y = np.vstack([ay, by, cy])

fig, ax = plt.subplots()

ax.stackplot(x, y)

ax.set(xlim=(0, 8), xticks=np.arange(1, 10),
       ylim=(0, 10), yticks=np.arange(1, 10))

plt.show()