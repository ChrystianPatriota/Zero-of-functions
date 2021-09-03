from function2 import function as func2
from function3 import function as func3
from interval import interval
from newtonMethod import newton
from secante import sec
from zerofunction import zeroFunction

# Todos as funções são executadas aqui
# Tolerância para todos os métodos é 10^-4
# Passos para todos os métodos é 10 passos
print('2 Questão')
interval(func2, -30, 30, 1)
zeroFunction(1, 2, 10 ** -4, 10)
print('3 Questão')
interval(func3, -30, 30, 1)
sec(0, 1, 10 ** -4, 10)
newton(0, 1, 10 ** -4, 10)
