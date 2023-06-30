import matplotlib.pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight')

x = [-3, -2, -1.6, -1.2, -.8, -.5, -.2, .1, .3, .5, .8, 1.1, 1.5, 1.9, 2.3, 3]
X, Y = np.meshgrid(x, np.linspace(-3, 3, 128))
Z = (5 + X/2 + X*5 - Y**3) * np.exp(-X**2 - Y**2)

fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z, vmin=-1, vmax=1.0)

plt.show()