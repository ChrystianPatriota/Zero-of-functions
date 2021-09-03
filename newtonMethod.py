from dxfunc3 import dxfunction
from function3 import function


def newton(start, end, tol, step):
    x0 = start
    x1 = end

    for _ in range(step):
        if abs((x1 - x0) / x1) <= tol:
            break
        x0 = x1
        x1 = x1 - function(x1) / dxfunction(x1)

    print(f'O Valor de x que zera a função é {x1}')
