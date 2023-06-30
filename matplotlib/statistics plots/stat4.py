import matplotlib.pyplot as plt
import numpy as np

plt.style.use('default')

D = np.random.normal((3, 5, 4), (0.7, 1.00, 0.5), (200, 3))

fig, ax = plt.subplots()

vp = ax.violinplot(D, [2, 4.5, 6.9], widths=2,
                   showmeans=False, showmedians=False, showextrema=False)
for body in vp['bodies']:
    body.set_alpha(0.7)
ax.set(xlim=(0, 9), xticks=np.arange(1, 9),
       ylim=(0, 9), yticks=np.arange(1, 9))

plt.show()