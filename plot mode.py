import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import scipy.special as sp

A = 0.07  # 振幅
a = 10  # 鼓面半径


def mode(n, k, a, A, r, phi):
    """
    振动模态对应的空间函数
    n: Bessel函数的阶
    k: 零点的指标
    a: 圆膜的半径
    A: 振幅
    r: 径向坐标
    phi: 角向坐标
    """
    zero = sp.jn_zeros(n, k)[-1]
    return A * sp.jv(n, zero * r / a) * np.cos(n * phi)


def polar_to_cartesian(r, phi):
    """
    将极坐标转化为直角坐标
    """
    return r * np.cos(phi), r * np.sin(phi)


for n in range(5):
    for k in range(1, 4):
        r = np.linspace(0, a, 2000)
        phi = np.linspace(0, 2 * np.pi, 1000)
        r, phi = np.meshgrid(r, phi)
        x, y = polar_to_cartesian(r, phi)
        u = mode(n, k, a, A, r, phi)
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        surf = ax.plot_surface(x, y, u, rstride=10, cstride=10, cmap="rainbow")
        ax.set_zlim(-0.3, 0.3)
        plt.axis("off")
        plt.title("(%s, %s)" % (n, k))
        plt.savefig("%s_%s.png" % (n, k), dpi=400)
        plt.close()
        print("%s_%s.png has finished" % (n, k))
