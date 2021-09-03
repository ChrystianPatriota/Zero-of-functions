from function2 import function


# Função para encontrar zeros de funções utilizando o método da Bisseção
# start é o ponto incial do intervalo
# end é o ponto final do intervalo
# tol é a tolerância
# step é a quantidade de passo maximo que o método deve dar
def zeroFunction(start, end, tol, step):

    # Ponto inicial e final são salvos em outras variaveis
    numLeft = start
    numRight = end
    numMiddle = (numRight + numLeft) / 2

    # Laço para com numero de passo a ser realizado
    for _ in range(step):

        # Cálculo do valor de função dos ponto
        functionLeft = function(numLeft)
        functionMiddle = function(numMiddle)

        # Verificação se a tolerância foi ultrapassada
        if abs(numLeft - numRight) / 2 <= tol:
            break

        # Vericação para obter o novo intervalo menor que o anterior
        if functionMiddle * functionLeft < 0:
            numRight = numMiddle
        else:
            numLeft = numMiddle

        # Novo valor do meio do intervalo
        numMiddle = (numRight + numLeft) / 2

    # Print com o valor aproximado de x que pode zerar a função
    print(f'O Valor de x que zera a função é {numMiddle}')
