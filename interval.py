# Declaração de função para encontrar intervalos que contenham zero de função
def interval(function, initial, final, step):
    # Primeiro valor a ser verificado
    x1 = initial
    # Segundo valor com o passo
    x2 = initial + step

    # Laço para verificar todos os valores dentro do intervalo informado
    while x2 <= final:
        # Multiplicação de valores da função para verificar se houve alteração de sinal
        signal = function(x1) * function(x2)
        # Condições para verificação do valor do sinal
        # Quando o sinal é negativo, existe pelo menos uma raiz
        if signal < 0:
            # Caso o sinal é negativo, é feito um print com o intervalo que contém pelo menos um zero de função
            print(f'Zero de função encontrado no intervalo [{x1},{x2}]')
        elif function(x1) == 0:
            # Caso o x1 seja 0, é feito um print com o valor de x que zerou a função
            print(f'Zero de função em x={x1}')
        # Novos valores de x1 e x2
        x1 = x2
        x2 = x2 + step

    # Caso o b seja 0, é feito um print com o valor de x que zerou a função
    if function(final) == 0:
        print(f'Zero de função em x={final}')
