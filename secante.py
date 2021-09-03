from function3 import function


# Função para encontrar zeros de funções utilizando o método da Secante
# start é o ponto incial do intervalo
# end é o ponto final do intervalo
# tol é a tolerância
# step é a quantidade de passo maximo que o método deve dar
def sec(start, end, tol, step):

    # Ponto inicial e final são salvos em outras variaveis
    x0 = start
    x1 = end

    # Laço para com numero de passo a ser realizado
    for _ in range(step):

        # Verificação se a tolerância foi ultrapassada
        if abs((x0 - x1) / x1) <= tol:
            break

        # Novo ponto para o metodo verificar
        x_sup = (x0 * function(x1) - x1 * function(x0)) / (function(x1) - function(x0))

        # Troca de valores para os novos valores
        x0 = x1
        x1 = x_sup

    # Print com o valor aproximado de h que pode zerar a função
    print(f'O Valor de x que zera a função é {x1}')
