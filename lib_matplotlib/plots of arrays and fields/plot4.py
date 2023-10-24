import matplotlib.pyplot as plt
import numpy as np

plt.style.use('grayscale')

X, Y = np.meshgrid(np.linspace(-4, 3, 256), np.linspace(-3, 3, 256))
Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)
levels = np.linspace(Z.min(), Z.max(), 9)

fig, ax = plt.subplots()
ax.contourf(X, Y, Z, levels=levels)

plt.show()