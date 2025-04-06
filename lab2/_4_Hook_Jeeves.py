from service.function import *
import numpy as np
from random import uniform

import numpy as np
from typing import Callable, Tuple

def exploratory_search(f, x, delta):
    # Исследовательский поиск
    x_new = np.copy(x)
    for i in range(len(x)):
        f_curr = f(x_new)

        # Пробуем сдвиг вперёд
        x_temp = np.copy(x_new)
        x_temp[i] += delta[i]
        if f(x_temp) < f_curr:
            x_new = x_temp
            continue

        # Пробуем сдвиг назад
        x_temp[i] -= 2 * delta[i]
        if f(x_temp) < f_curr:
            x_new = x_temp

    return x_new


def hooke_jeeves(
    f,
    x0,
    delta_init = 0.5,
    alpha = 2.0,
    error = 1e-6):
    """
    Метод Хука–Дживса в соответствии с пошаговым описанием.
    """
    n = len(x0)
    delta = np.full(n, delta_init)    # начальные приращения Δ_i
    x_prev = np.copy(x0)              # x^{K-1}
    x_curr = exploratory_search(f, x_prev, delta)  # x^K после первичной разведки

    iter_count = 0

    while np.any(delta > error):
        iter_count += 1

        # Шаг 3: если исследовательский поиск успешен (x_curr лучше x_prev) — шаг 5
        if f(x_curr) < f(x_prev):
            # Шаг 5: поиск по образцу
            x_p = x_curr + (x_curr - x_prev)

            # Шаг 6: исследование в точке x_p
            x_new = exploratory_search(f, x_p, delta)

            # Шаг 7: проверка успеха
            if f(x_new) < f(x_curr):
                x_prev = x_curr
                x_curr = x_new
            else:
                x_prev = np.copy(x_curr)
        else:
            # Шаг 4: если исследовательский поиск неудачен
            # уменьшаем приращения
            delta = delta / alpha
            # и возвращаемся к шагу 2 (исследуем текущую базовую точку)
            x_curr = exploratory_search(f, x_prev, delta)

    return x_curr, f(x_curr), iter_count

for error in eps:
    print(hooke_jeeves(function, np.array([uniform(-1, 1), uniform(-1, 1), uniform(-1, 1)]), error=error))
    