
from math import sqrt

def soma(numero_1, numero_2):
    print(numero_1 + numero_2)

def subtrai(numero_1, numero_2):
    print(numero_1 - numero_2)

def multiplica(numero_1, numero_2):
    print(numero_1 * numero_2)

def divide(numero_1, numero_2):
    print(numero_1 / numero_2)

def faz_potenciacao(numero_1, numero_2):
    print(numero_1 ** numero_2)

def faz_raiz_quadrada(numero_1):
    print(sqrt(numero_1))

##############################################################################################################

def verifica_operacao(numero_1, operacao, numero_2):
    if operacao == '+':
        soma(numero_1, numero_2)
    elif operacao == '-':
        subtrai(numero_1, numero_2)
    elif operacao == '*':
        multiplica(numero_1, numero_2)
    elif operacao == '/':
        divide(numero_1, numero_2)
    else:
        faz_potenciacao(numero_1, numero_2)


##############################################################################################################

numero_1 = 0
operacao = None
numero_2 = 0

print('🧮🧮 Calculadora básica 🧮🧮')


while True:
    entrada_num1 = input('Digite um número: ')

    try:
        numero_1 = float(entrada_num1)
        break
    except ValueError:
        print('❌ VOCÊ DEVE DIGITAR UM NÚMERO ❌')

##############################################################################################################

operacoes_possiveis = ['+', '-', '*', '/', '**', 'rad']

print(f'Operações possíveis: {operacoes_possiveis}')

while True:
    entrada_oper = input('Digite a operação que deseja realizar: ')

    if entrada_oper not in operacoes_possiveis:
        print('❌ DIGITE UMA OPERAÇÃO VÁLIDA ❌')
        continue
    else:
        operacao = entrada_oper
        break

##############################################################################################################

if operacao == 'rad':
    faz_raiz_quadrada(numero_1)
else:
    while True:
        entrada_num2 = input('Digite um número: ')

        try:
            numero_2 = float(entrada_num2)
            verifica_operacao(numero_1, operacao, numero_2)
            break
        except ValueError:
            print('❌ VOCÊ DEVE DIGITAR UM NÚMERO ❌')

