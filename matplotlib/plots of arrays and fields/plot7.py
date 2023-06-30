import matplotlib.pyplot as plt
import numpy as np

plt.style.use('grayscale')

X, Y = np.meshgrid(np.linspace(-4, 4, 256), np.linspace(-4, 4, 256))
Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)

V = np.diff(Z[1:, :], axis=1)
U = -np.diff(Z[:, 1:], axis=0)

fig, ax = plt.subplots()
ax.streamplot(X[1:, 1:], Y[1:, 1:], U, V)

plt.show()