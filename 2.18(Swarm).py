import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

Col = ["#C6FAA8", "#C6F9A7", "#C6F9A6", "#C6F9A5", "#C7F9A4", "#C7F9A3", "#C7F9A3", "#C7F8A2", "#C8F8A1", "#C8F8A0", "#C8F89F", "#C8F89E",
"#C9F89E", "#C9F79D", "#C9F79C", "#C9F79B", "#CAF79A", "#CAF79A", "#CAF799", "#CAF698", "#CBF697", "#CBF696", "#CBF695", "#CCF695", "#CCF694",
"#CCF593", "#CCF592", "#CDF591", "#CDF591", "#CDF590", "#CDF58F", "#CEF48E", "#CEF48D", "#CEF48C", "#CEF48C", "#CFF48B", "#CFF48A", "#CFF389",
"#CFF388", "#D0F388", "#D0F387", "#D0F386", "#D0F385", "#D1F284", "#D1F283", "#D1F283", "#D2F282", "#D2F281", "#D2F280", "#D2F17F", "#D3F17F",
"#D3F17E", "#D3F17D", "#D3F17C", "#D4F17B", "#D4F07A", "#D4F07A", "#D4F079", "#D5F078", "#D5F077", "#D5F076", "#D5EF76", "#D6EF75", "#D6EF74",
"#D6EF73", "#D6EF72", "#D7EF71", "#D7EE71", "#D7EE70", "#D8EE6F", "#D8EE6E", "#D8EE6D", "#D8EE6D", "#D9ED6C", "#D9ED6B", "#D9ED6A", "#D9ED69",
"#DAED68", "#DAED68", "#DAEC67", "#DAEC66", "#DBEC65", "#DBEC64", "#DBEC64", "#DBEC63", "#DCEB62", "#DCEB61", "#DCEB60", "#DCEB5F", "#DDEB5F",
"#DDEB5E", "#DDEA5D", "#DEEA5C", "#DEEA5B", "#DEEA5B", "#DEEA5A", "#DFEA59", "#DFE958", "#DFE957", "#DFE956", "#E0E956", "#E0E955", "#E0E954",
"#E0E853", "#E1E852", "#E1E851", "#E1E851", "#E1E850", "#E2E84F", "#E2E74E", "#E2E74D", "#E3E74D", "#E3E74C", "#E3E74B", "#E3E74A", "#E4E649",
"#E4E648", "#E4E648", "#E4E647", "#E5E646", "#E5E645", "#E5E544", "#E5E544", "#E6E543", "#E6E542", "#E6E541", "#E6E540", "#E7E43F", "#E7E43F",
"#E7E43E", "#E7E43D", "#E8E43C", "#E8E43B", "#E8E33B", "#E9E33A", "#E9E339", "#E9E338", "#E9E337", "#EAE336", "#EAE236", "#EAE235", "#EAE234",
"#EBE233", "#EBE232", "#EBE232", "#EBE131", "#ECE130", "#ECE12F", "#ECE12E", "#ECE12D", "#EDE12D", "#EDE02C", "#EDE02B", "#EDE02A", "#EEE029",
"#EEE029", "#EEE028", "#EFDF27", "#EFDF26", "#EFDF25", "#EFDF24", "#F0DF24", "#F0DF23", "#F0DE22", "#F0DE21", "#F1DE20", "#F1DE20", "#F1DE1F",
"#F1DE1E", "#F2DD1D", "#F2DD1C", "#F2DD1B", "#F2DD1B", "#F3DD1A", "#F3DD19", "#F3DC18", "#F3DC17", "#F4DC17", "#F4DC16", "#F4DC15", "#F5DC14",
"#F5DB13", "#F5DB12", "#F5DB12", "#F6DB11", "#F6DB10", "#F6DB0F", "#F6DA0E", "#F7DA0E", "#F7DA0D", "#F7DA0C", "#F7DA0B", "#F8DA0A", "#F8D909",
"#F8D909", "#F8D908", "#F9D907", "#F9D906", "#F9D905", "#FAD905"]

# Make data.
X = np.arange(-5.12, 5.12, 0.01)
Y = np.arange(-5.12, 5.12, 0.01)
X, Y = np.meshgrid(X, Y)
V=0
W=0

for i in range (1,6):
    V=V+(i*np.cos((i+1)*X+1))
    W=W+(i*np.cos((i+1)*Y+1))

Z = -1*V*W

num_func_params = 2
num_swarm = 50
position = -3 + 6 * np.random.rand(num_swarm, num_func_params)
velocity = np.zeros([num_swarm, num_func_params])
personal_best_position = np.copy(position)
temp = np.copy(position)
personal_best_value = np.zeros(num_swarm)

for i in range(num_swarm):
    V=0
    W=0
    for j in range (1,6):
        V=V+(j*np.cos((j+1)*position[i][0]+1))
        W=W+(j*np.cos((j+1)*position[i][1]+1))
    personal_best_value[i] = -1*V*W

tmax = 200
c1 = 0.001
c2 = 0.002
levels = np.linspace(-1, 35, 100)
global_best = np.min(personal_best_value)
global_best_position = np.copy(personal_best_position[np.argmin(personal_best_value)])

XCol = np.zeros([tmax,num_swarm])
YCol = np.zeros([tmax,num_swarm])

for t in range(tmax):
    for i in range(num_swarm):
        V=0
        W=0
        for j in range (1,6):
            V=V+(j*np.cos((j+1)*position[i][0]+1))
            W=W+(j*np.cos((j+1)*position[i][1]+1))
        error = -1*V*W
        if personal_best_value[i] > error:
            personal_best_value[i] = error
            personal_best_position[i] = position[i]
    best = np.min(personal_best_value)
    best_index = np.argmin(personal_best_value)
    if global_best > best:
        global_best = best
        global_best_position = np.copy(personal_best_position[best_index])

    for i in range(num_swarm):
        # update velocity
        velocity[i] += c1 * np.random.rand() * (personal_best_position[i] - position[i]) \
                       + c2 * np.random.rand() * (global_best_position - position[i])
        temp[i]=position[i]
        position[i] += velocity[i]

    fig = plt.figure()
    CS = plt.contour(X, Y, Z, levels=levels, cmap=cm.gist_stern)
    plt.gca().set_xlim([-5, 5])
    plt.gca().set_ylim([-5, 5])
    for i in range (num_swarm):
        XCol[t][i]=position[i][0]
        YCol[t][i]=position[i][1]
    for i in range (t+1):
        for j in range (num_swarm):
            plt.scatter(XCol[i][j], YCol[i][j], color=Col[199-(t-i)], s=20)
    for i in range(num_swarm):
        plt.arrow(temp[i][0], temp[i][1], position[i][0]-temp[i][0], position[i][1]-temp[i][1], head_width=0.1, head_length=0.1, fc='k', ec='k', zorder=10)
        plt.scatter(position[i][0], position[i][1], color='green', s=20)
    plt.scatter(global_best_position[0], global_best_position[1], color='red', s=40)

    plt.title('{0:03d}'.format(t))
    filename = 'frame{0:03d}.png'.format(t)
    plt.savefig(filename, bbox_inches='tight')
    plt.close(fig)
    plt.cla()