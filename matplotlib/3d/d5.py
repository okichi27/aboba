from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

plt.style.use('classic')

X, Y, Z = axes3d.get_test_data(0.015)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_wireframe(X, Y, Z, rstride=15, cstride=10)

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()