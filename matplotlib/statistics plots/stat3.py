import matplotlib.pyplot as plt
import numpy as np

plt.style.use('fast')

x = [2, 4, 6]
y = [3.6, 7, 9.2]
yerr = [0.6, 1.5, 0.3]
fig, ax = plt.subplots()

ax.errorbar(x, y, yerr, fmt='o', linewidth=2, capsize=6)

ax.set(xlim=(0, 10), xticks=np.arange(1, 10),
       ylim=(0, 10), yticks=np.arange(1, 10))

plt.show()