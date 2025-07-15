import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Функція f(x) = cos(x)
def f(x):
    return np.cos(x)

# Межі інтегрування
a = 0
b = np.pi


x = np.linspace(-0.5, 3.5, 400)
y = f(x)


fig, ax = plt.subplots()


ax.plot(x, y, 'b', linewidth=2, label='f(x) = cos(x)')

# Заповнення області під кривою між a і b
ix = np.linspace(a, b, 200)
iy = f(ix)
ax.fill_between(ix, iy, color='cyan', alpha=0.3, label='Інтеграл')


ax.axvline(a, color='gray', linestyle='--')
ax.axvline(b, color='gray', linestyle='--')

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([-1.1, 1.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title(f'Інтеграл f(x) = cos(x) від {a} до {b}')
ax.legend()
plt.grid()
plt.show()

N = 100000


x_random = np.random.uniform(a, b, N)

# Обчислення середнього значення функції
avg_f = np.mean(f(x_random))

# Розрахунок інтеграла
integral_mc = (b - a) * avg_f
print(f"Монте-Карло інтеграл cos(x) від 0 до π: {integral_mc:.5f}")

# Обчислення значення інтеграла
result, error = spi.quad(f, a, b)
print(f"Інтеграл cos(x) від 0 до π: {result:.5f}, похибка: {error:.2e}")