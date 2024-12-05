import math
import numpy as np
import matplotlib.pyplot as plt

# Запрос данных у пользователя
g = 9.8  # Ускорение свободного падения, м/с^2
m = float(input("Введите массу тела (кг): "))
R = float(input("Введите радиус кольца (м): "))
a = float(input("Введите угловой размер дуги (в радианах, от π/2 до 3π/2): "))
mu = float(input("Введите коэффициент трения: "))

# Вычисления
cos_a = math.cos(a)  # Косинус угла
height = R * (1 - cos_a)  # Высота относительно нижней точки
term1 = 1 - cos_a  # Компонент потенциальной энергии
term2 = mu * a  # Учет работы трения

# Формула для скорости
v = math.sqrt(2 * g * R * (term1 + term2))

# Параметры движения после отрыва (параболическое движение)
angle = a  # Угол, с которым тело отрывается от дуги
v_x = v * math.cos(angle)  # Горизонтальная составляющая скорости
v_y = v * math.sin(angle)  # Вертикальная составляющая скорости

# Время полета
t_flight = (2 * v_y) / g

# Время и координаты
t = np.linspace(0, t_flight, num=500)  # Массив времени
x = v_x * t  # Горизонтальная координата
y = height + v_y * t - 0.5 * g * t**2  # Вертикальная координата

# Визуализация
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="Траектория тела", color="b")
plt.scatter(x[-1], y[-1], color='r', zorder=5, label="Точка отрыва")
plt.title("Траектория движения тела после отрыва от дуги")
plt.xlabel("Горизонтальное расстояние (м)")
plt.ylabel("Высота (м)")
plt.grid(True)
plt.legend()
plt.show()

# Вывод результатов
print(f"Необходимая скорость для прохождения всей дуги: {v:.2f} м/с")
