# Desenvolvendo listas e acessando-às
cores = ['1-vermelho', '2-azul', '3-amarelo', '4-verde']

# O acesso aos elementos que temos dentro das listas podem ser feitos através de números positivos ou negativos
'''print('O elemento inicial é',cores[0])
print('O elemento final é',cores[-1])'''

# Métodos de Listas:

# adicionar elementos no final da lista
cores.append('5-roxo')
print('cor adicionada no final da lista',cores)

# Inserir elementos numa posição específica da lista
cores.insert(0, '0-preto')
print('cor inserida em local específico da lista',cores)

# Remover elementos de uma lista
cores.remove('3-amarelo')
print('cor removida',cores)

# Remove e retorna o elemento em uma posição específica da lista
cor_removida = cores.pop(1)
print('removendo e retornando a cor removida', cores, cor_removida)

# Ordenar os elementos de maneira ascendente
cores.sort()
print('ordenando de maneira ascendente',cores)

# Inverte a ordem dos elementos da lista
cores.reverse()
print('elementos invertidos',cores)
