import matplotlib.pyplot as plt
import numpy as np

plt.style.use('bmh')
x = np.linspace(0, 10)
y = 3 + 2/3 * np.sin(2 * x)
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=3.0)
ax.set(xlim=(0, 10), ylim=(0, 8))

plt.show()