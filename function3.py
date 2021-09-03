import math


# Função de volume
# O parametro h é a altura
def function(h):

    # Função de volume a ser calculada com numero de letra do nome igual a 9
    # Retorno do resultado para um valor de h(altura)
    return math.pi * h ** 2 * (3 * 9 - h) / 3 - 3
