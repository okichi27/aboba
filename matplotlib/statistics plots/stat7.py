import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery-nogrid')

x = np.random.randn(5000)
y = 1.2 * x + np.random.randn(5000) / 3

fig, ax = plt.subplots()

ax.hexbin(x, y, gridsize=10)

ax.set(xlim=(-5, 5), ylim=(-7, 7))

plt.show()