'''contador = 0

while contador <= 5:

    print(contador)
    contador += 1
'''
# Sistema de tabuáda:

tabela = int(input('Digite um número para saber sua tabela de 1 a 20: '))
contador = 1
while contador <= 20:
    multiplicacao = contador * tabela
    contador += 1
    print('{} vezes {} é igual a→ {}'.format(tabela, contador -1, multiplicacao))
