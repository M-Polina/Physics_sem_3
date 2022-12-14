import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import time

aem = 1.66 * pow(10, -27)  # 1 а.е.м. = 1.66*10^(-27) кг

print("Введите положительную величину индукцию магнитного поля В (Тл):")
try:
    B = abs(float(input()))
except ValueError:
    B = 0.01

m0 = 20
print("Введите массу изотопа m (a.e.м.):")
try:
    m0 = abs(float(input()))
    m = m0 * aem
except ValueError:
    m = m0 * aem

print("Введите заряд изотопа q (10^(-19) Кл):")
try:
    q = float(input()) * pow(10, -19)
except ValueError:
    q = 1.6 * pow(10, -19)

print("Введите начальную скорость частицы v (м/с^2):")
try:
    v = abs(float(input()))
except ValueError:
    v = 1000

m_arr = []
m_arr.append(m)
t_arr = np.linspace(0, 2 * np.pi * m / q / B, num=1000, endpoint=True)


def x(t, A):
    return (-v * np.cos(A * t) / A + v / A)


def y(t, A):
    return (v * np.sin(A * t) / A)


def make_x(ind):
    A = q * B / m_arr[ind]
    x_arr = [x(t, A) for t in t_arr]
    return x_arr


def make_y(ind):
    A = q * B / m_arr[ind]
    y_arr = [y(t, A) for t in t_arr]
    return y_arr


fig = plt.figure(figsize=(13, 10))
axs = fig.subplots(1, 1)
axs.clear()
axs.minorticks_on()
axs.grid(True, which='both')
axs.grid(which='minor', color='gray', linestyle=':')

axs.plot(make_x(0), make_y(0), color='blue', label=f"m = {m0} a.e.м.")

axs.set_ylabel('y, м')
axs.set_xlabel(
    f'x, м \n B = {B} Тл, R = {q * pow(10, 19)}' + r' $ \cdot 10^{-19} $ Кл,' + f' v = {v} м/с \n Магнитное поле направлено на нас');
axs.minorticks_on()

plt.show()
