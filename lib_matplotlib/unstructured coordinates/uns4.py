import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery-nogrid')

x = np.random.uniform(-10, 10, 256)
y = np.random.uniform(-12,15, 256)
z = (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)

fig, ax = plt.subplots()

ax.triplot(x, y)

ax.set(xlim=(-10, 11), ylim=(-13, 15))

plt.show()