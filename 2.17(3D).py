from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X = np.arange(-5.12, 5.12, 0.01)
Y = np.arange(-5.12, 5.12, 0.01)
X, Y = np.meshgrid(X, Y)
Z = -((1+np.cos(12*np.sqrt(X**2+Y**2)))/(0.5*(X**2+Y**2)+2))

surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, alpha=0.1, linewidth=0, antialiased=False)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_autoscaley_on(False)
ax.set_ylim([-5.12,5.12])
ax.set_autoscalex_on(False)
ax.set_xlim([-5.12,5.12])
ax.set_autoscalez_on(False)
ax.set_zlim([-1,0])
num_func_params = 3
num_swarm = 50
velocity = np.zeros([num_swarm, num_func_params])
position = -4 + 8 * np.random.rand(num_swarm, num_func_params)
personal_best_position = np.copy(position)
personal_best_value = np.zeros(num_swarm)

for i in range(num_swarm):
    personal_best_value[i] = -((1+np.cos(12*np.sqrt(position[i][0]**2+position[i][1]**2)))/(0.5*(position[i][0]**2+position[i][1]**2)+2))
tmax = 200
c1 = 0.001
c2 = 0.002
levels = np.linspace(-1, 35, 100)
global_best = np.min(personal_best_value)
global_best_position = np.copy(personal_best_position[np.argmin(personal_best_value)])
for t in range (tmax):
    for i in range(num_swarm):
        error = -((1+np.cos(12*np.sqrt(position[i][0]**2+position[i][1]**2)))/(0.5*(position[i][0]**2+position[i][1]**2)+2))
        if personal_best_value[i] > error:
            personal_best_value[i] = error
            personal_best_position[i] = position[i]
    best = np.min(personal_best_value)
    best_index = np.argmin(personal_best_value)
    if global_best > best:
        global_best = best
        global_best_position = np.copy(personal_best_position[best_index])
    for i in range (num_swarm):
        velocity[i] += (c1 * np.random.rand() * (personal_best_position[i]-position[i]) \
                    +  c2 * np.random.rand() * (global_best_position - position[i]))		
        position[i] += velocity[i]
        ax.scatter(position[i][0],position[i][1],-0.5,color='green',s=20)
    ax.scatter(global_best_position[0], global_best_position[1],-0.5,color='red',s=50,zorder=1200)
    filename = 'frame{0:03d}.png'.format(t)
    plt.savefig(filename, bbox_inches='tight')
    ax.cla()
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, alpha=0.1, linewidth=0, antialiased=False)
    ax.set_autoscaley_on(False)
    ax.set_ylim([-5.12,5.12])
    ax.set_autoscalex_on(False)
    ax.set_xlim([-5.12,5.12])
    ax.set_autoscalez_on(False)
    ax.set_zlim([-1,0])