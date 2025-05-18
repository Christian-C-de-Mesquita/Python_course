# Conjuntos: Criação e diferentes tipos de uso:

# Criação:
frutas = {"maça", "pera", "banana"}
numeros = set([5, 4, 3, 2, 1])

# Operações matemáticas:
# união( | )
# Interseção ( & )
# Diferença (-) 
# Diferença simétrica (^)
'''
conj1 = {77, 20, 48}
conj2 = {17, 20, 67}
print(conj1 | conj2)
print(conj1 & conj2)
print(conj1 - conj2)
print(conj1 ^ conj2)
'''

frutas.add('Laranja')
frutas.remove("maça")
frutas.discard("uva")
print(frutas)
frutas.clear()
print(frutas)
