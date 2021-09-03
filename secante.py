from function3 import function


def sec(start, end, tol, step):
    x0 = start
    x1 = end

    for _ in range(step):
        if abs((x0 - x1) / x1) <= tol:
            break
        x_sup = (x0 * function(x1) - x1 * function(x0)) / (function(x1) - function(x0))
        x0 = x1
        x1 = x_sup

    print(f'O Valor de x que zera a função é {x1}')
