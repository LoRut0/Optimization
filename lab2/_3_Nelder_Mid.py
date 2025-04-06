from service.function import *
import numpy as np
from math import sqrt
from random import uniform

def nelder_mead(f, 
                x_start,
                step=0.1,
                error=1e-6,
                alpha=1., 
                gamma=2., 
                rho=-0.5, 
                sigma=0.5):
    """
    Parameters:
    - f: целевая функция
    - x_start: начальная точка (numpy-массив)
    - step: размер начального симплекса
    - error: порог улучшения
    - max_iter: максимальное число итераций (0 — бесконечно)
    - alpha, gamma, rho, sigma: параметры метода

    returns:
    - x_opt: оптимальное значение x
    - f_opt: минимальное значение функции
    - iter_count: число итераций
    """

    def check_stop(error, res, n):
        # returns true if dispersion <= error
        # false if dispersion > error
        f_mid = np.mean([f for x, f  in res], axis=0)
        f_temp = 0
        for x, f in res:
            f_temp += (f - f_mid)**2
        
        dispersion_pow2 = f_temp / (n-1)
        dispersion = sqrt(dispersion_pow2)
        return dispersion < error
    
    
    dim = len(x_start)
    prev_best = f(x_start)
    res = [[x_start, prev_best]]

    for i in range(dim):
        x = np.copy(x_start)
        x[i] += step
        res.append([x, f(x)])
    
    iter_count = 0
    while True:
        res.sort(key=lambda x: x[1])
        best = res[0][1]
        
        if (check_stop(error, res, dim)):
            break

        iter_count += 1 

        if abs(best - prev_best) - error:
            no_improve = 0
            prev_best = best
        else:
            no_improve += 1

        x0 = np.mean([x[0] for x in res[:-1]], axis=0)

        xr = x0 + alpha * (x0 - res[-1][0])
        rscore = f(xr)
        if res[0][1] <= rscore < res[-2][1]:
            res[-1] = [xr, rscore]
            continue

        if rscore < res[0][1]:
            xe = x0 + gamma * (xr - x0)
            escore = f(xe)
            if escore < rscore:
                res[-1] = [xe, escore]
            else:
                res[-1] = [xr, rscore]
            continue

        xc = x0 + rho * (res[-1][0] - x0)
        cscore = f(xc)
        if cscore < res[-1][1]:
            res[-1] = [xc, cscore]
            continue

        x1 = res[0][0]
        new_res = []
        for x, _ in res:
            x_new = x1 + sigma * (x - x1)
            new_res.append([x_new, f(x_new)])
        res = new_res

    return res[0][0], res[0][1], iter_count

for error in eps:
    print(nelder_mead(function, np.array([uniform(-1, 1), uniform(-1, 1), uniform(-1, 1)]), error=error))