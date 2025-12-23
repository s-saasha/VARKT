import matplotlib.pyplot as plt
import math

DIR = 'Graphics'

#CONSTS

x = [0]
y = [0]
m = [171000]
vx = [0]
vy = [0]
v = [0]
l = [0]
ro = [1.2754]
dl = 0.66
dm = 1200
dt = 0.01
t = [0]
u = 2965
G = 6.67 * 10 ** -11
M = 5.3 * 10 ** 22
R = 600000
k = 0.5
h = [0]
teta = [0]

def gethras():
    global m, v, k, u, dm, vx, vy, G, M, R, x, y, ro, teta
    h = m[-1] * v[-1] ** 2 / (2 * ((u * dm + k * ro[-1] * v[-1] ** 2) * math.cos((math.pi / 2) if vy[-1] == 0 else math.atan(vx[-1] / vy[-1])) - m[-1] * G * M * math.cos(teta[-1]) * dt / (x[-1] ** 2 + (y[-1] + R) ** 2)))
    return h


while m[-1] > math.exp(500 / u) * 75400:
    dvy = u * dm * math.cos(math.radians(l[-1])) * dt / m[-1] - k * ro[-1] * vy[-1] ** 2 * math.cos((math.pi / 2) if vy[-1] == 0 else math.atan(vx[-1] / vy[-1])) * dt / m[-1] - G * M * math.cos(teta[-1]) * dt / (x[-1] ** 2 + (y[-1] + R) ** 2)
    dvx = u * dm * math.sin(math.radians(l[-1])) * dt / m[-1] - k * ro[-1] * vx[-1] ** 2 * math.sin((math.pi / 2) if vy[-1] == 0 else math.atan(vx[-1] / vy[-1])) * dt / m[-1] - G * M * math.sin(teta[-1]) * dt / (x[-1] ** 2 + (y[-1] + R) ** 2)
    ro.append(ro[0] * math.exp(-h[-1]/8000))
    h.append(math.sqrt((x[-1] ** 2 + (y[-1] + R) ** 2)) - R)
    x.append(x[-1] + vx[-1] * dt)
    y.append(y[-1] + vy[-1] * dt)
    teta.append(math.atan(x[-2] / (y[-2] + R)))
    v.append(math.sqrt(vx[-1] ** 2 + vy[-1] ** 2))
    vx.append(vx[-1] + dvx)
    vy.append(vy[-1] + dvy)
    l.append(l[-1] + dl * dt)
    m.append(m[-1] - dm * dt)
    t.append(t[-1] + dt)


while h[-1] > h[-2]:
    dvy = -k * ro[-1] * vy[-1] ** 2 * math.cos((math.pi / 2) if vy[-1] == 0 else math.atan(vx[-1] / vy[-1])) * dt / m[-1] - G * M * math.cos(teta[-1]) * dt / (x[-1] ** 2 + (y[-1] + R) ** 2)
    dvx = -k * ro[-1] * vx[-1] ** 2 * math.sin((math.pi / 2) if vy[-1] == 0 else math.atan(vx[-1] / vy[-1])) * dt / m[-1] - G * M * math.sin(teta[-1]) * dt / (x[-1] ** 2 + (y[-1] + R) ** 2)
    ro.append(ro[0] * math.exp(-h[-1] / 8000))
    h.append(math.sqrt((x[-1] ** 2 + (y[-1] + R) ** 2)) - R)
    x.append(x[-1] + vx[-1] * dt)
    y.append(y[-1] + vy[-1] * dt)
    teta.append(math.atan(x[-2] / (y[-2] + R)))
    v.append(math.sqrt(vx[-1] ** 2 + vy[-1] ** 2))
    vx.append(vx[-1] + dvx)
    vy.append(vy[-1] + dvy)
    m.append(m[-1])
    t.append(t[-1] + dt)
    
k = 17.5
m[-1] = m[-1] - 24600

while h[-1] > gethras():
    dvy = k * ro[-1] * vy[-1] ** 2 * math.cos((math.pi / 2) if vy[-1] == 0 else math.atan(vx[-1] / vy[-1])) * dt / m[-1] - G * M * math.cos(teta[-1]) * dt / (x[-1] ** 2 + (y[-1] + R) ** 2)
    dvx = k * ro[-1] * vx[-1] ** 2 * math.sin((math.pi / 2) if vy[-1] == 0 else math.atan(vx[-1] / vy[-1])) * dt / m[-1] - G * M * math.sin(teta[-1]) * dt / (x[-1] ** 2 + (y[-1] + R) ** 2)
    ro.append(ro[0] * math.exp(-h[-1] / 8000))
    h.append(math.sqrt((x[-1] ** 2 + (y[-1] + R) ** 2)) - R)
    x.append(x[-1] + vx[-1] * dt)
    y.append(y[-1] + vy[-1] * dt)
    teta.append(math.atan(x[-2] / (y[-2] + R)))
    v.append(math.sqrt(vx[-1] ** 2 + vy[-1] ** 2))  
    vx.append(vx[-1] + dvx)
    vy.append(vy[-1] + dvy)
    m.append(m[-1])
    t.append(t[-1] + dt)


while h[-1] < h[-2]:
    dvy = u * dm * math.cos((math.pi / 2) if vy[-1] == 0 else math.atan(vx[-1] / vy[-1])) * dt / m[-1] + k * ro[-1] * vy[-1] ** 2 * math.cos((math.pi / 2) if vy[-1] == 0 else math.atan(vx[-1] / vy[-1])) * dt / m[-1] - G * M * math.cos(teta[-1]) * dt / (x[-1] ** 2 + (y[-1] + R) ** 2)
    dvx = u * dm * math.sin((math.pi / 2) if vy[-1] == 0 else math.atan(vx[-1] / vy[-1])) * dt / m[-1] + k * ro[-1] * vx[-1] ** 2 * math.sin((math.pi / 2) if vy[-1] == 0 else math.atan(vx[-1] / vy[-1])) * dt / m[-1] - G * M * math.sin(teta[-1]) * dt / (x[-1] ** 2 + (y[-1] + R) ** 2)
    ro.append(ro[0] * math.exp(-h[-1] / 8000))
    h.append(math.sqrt((x[-1] ** 2 + (y[-1] + R) ** 2)) - R)
    x.append(x[-1] + vx[-1] * dt)
    y.append(y[-1] + vy[-1] * dt)
    teta.append(math.atan(x[-2] / (y[-2] + R)))
    v.append(math.sqrt(vx[-1] ** 2 + vy[-1] ** 2))
    vx.append(vx[-1] + dvx)
    vy.append(vy[-1] + dvy) 
    m.append(m[-1] - dm * dt)
    t.append(t[-1] + dt)

    
with open("data1.csv", "r") as f:
    velocities = []
    times = []
    for line in f.readlines():
        line = line.split(',')
        times.append(float(line[0]))
        velocities.append(float(line[2]))


# Создаём график
plt.figure(figsize=(10, 6))

# Гладкая кривая
plt.plot(times, velocities, 'tab:orange', linewidth=2, label='Данные из игры')
plt.plot(t, v, 'b-', linewidth=2, label='Физмодель')

# Настройка графика
plt.xlabel('Время t, с', fontsize=12)
plt.ylabel('Скорость v, м/с', fontsize=12)
plt.title('Изменение скорости ракеты на начальном участке полёта', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.xlim(0, 600)
plt.ylim(0, 3000)

# Сохраняем график в файл
plt.tight_layout()
plt.savefig(f'{DIR}/speed', dpi=300, bbox_inches='tight')
plt.close()  # Закрываем фигуру

with open("data1.csv", "r") as f:
    heights = []
    times = []
    for line in f.readlines():
        line = line.split(',')
        times.append(float(line[0]))
        heights.append(float(line[1]))

plt.figure(figsize=(10, 6))

plt.plot(times, heights, 'tab:orange', linewidth=2, label='Данные из игры')
plt.plot(t, h, 'b-', linewidth=2, label='Физмодель')

# Настройка графика
plt.xlabel('Время t, с', fontsize=12)
plt.ylabel('Высота h, м', fontsize=12)
plt.title('Изменение высоты ракеты на начальном участке полёта', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.xlim(0, 600)
plt.ylim(0, 270000)

# Сохраняем график в файл
plt.tight_layout()
plt.savefig(f'{DIR}/height', dpi=300, bbox_inches='tight')
plt.close()  # Закрываем фигуру

with open("data1.csv", "r") as f:
    weights = []
    times = []
    for line in f.readlines():
        line = line.split(',')
        times.append(float(line[0]))
        weights.append(float(line[3]))

plt.figure(figsize=(10, 6))

plt.plot(times, weights, 'tab:orange', linewidth=2, label='Данные из игры')
plt.plot(t, m, 'b-', linewidth=2, label='Физмодель')

# Настройка графика
plt.xlabel('Время t, с', fontsize=12)
plt.ylabel('Масса m, кг', fontsize=12)
plt.title('Изменение массы ракеты на начальном участке полёта', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.xlim(0, 600)
plt.ylim(0, 300000)

# Сохраняем график в файл
plt.tight_layout()
plt.savefig(f'{DIR}/mass', dpi=300, bbox_inches='tight')
plt.close()  # Закрываем фигуру
