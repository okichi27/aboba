import matplotlib.pyplot as plt
import numpy as np

plt.style.use('default')

x = 4 + np.random.normal(0, 1.5, 200)
fig, ax = plt.subplots()

ax.hist(x, bins=10, linewidth=0.5, edgecolor="white")

ax.set(xlim=(0, 8), xticks=np.arange(1, 10),
       ylim=(0, 56), yticks=np.linspace(0, 50, 9))

plt.show()