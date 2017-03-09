from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-40, 40, 0.1)
Y = np.arange(-40, 40, 0.1)
X, Y = np.meshgrid(X, Y)
V=0
W=0
#Fifth function of De Jong
for i in range (-2,3):
	W=0
	for j in range (-2,3):
		W=W+(5*(i+2)+j+3+(X-16*j)**6+(Y-16*i)**6)**-1
	V=V+W

Z = (0.002+V)**-1
# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.gist_stern,
                       linewidth=0, antialiased=False)

# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()