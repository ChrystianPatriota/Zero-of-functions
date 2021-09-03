from function2 import function


def zeroFunction(initial, final, tol, loop):

    numLeft = initial
    numRight = final
    numMiddle = (numRight + numLeft) / 2

    for _ in range(loop):

        functionLeft = function(numLeft)
        functionMiddle = function(numMiddle)

        if abs(numLeft - numRight)/2 <= tol:
            break

        if functionMiddle*functionLeft < 0:
            numRight = numMiddle
        else:
            numLeft = numMiddle
        numMiddle = (numRight + numLeft) / 2

    print(f'O Valor de x que zera a função é {numMiddle}')
