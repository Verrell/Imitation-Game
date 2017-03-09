from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-5.12, 5.12, 0.01)
Y = np.arange(-5.12, 5.12, 0.01)
X, Y = np.meshgrid(X, Y)
V=0
W=0
#Shubert's Function
for i in range (1,6):
	V=V+(i*np.cos((i+1)*X+1))
	W=W+(i*np.cos((i+1)*Y+1))

Z = -1*V*W
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