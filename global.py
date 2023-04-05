import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# 创建3D坐标系
fig = plt.figure()
ax = Axes3D(fig)

# 创建球体
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
sphere = ax.plot_surface(x, y, z, color='orange')

# 定义旋转函数
def rotate(angle):
    ax.view_init(30, angle)

# 创建动画对象
ani = FuncAnimation(fig, rotate, frames=np.arange(0, 360, 2), interval=50)

plt.show()
