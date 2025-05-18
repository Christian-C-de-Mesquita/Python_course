# funções com números

print('Funções de retorno não são inicialmente muito iterativas, mas creio que serão bastante utilizadas')
def multiplicacao(a, b):
    return a * b

resultado = multiplicacao(8, 18)
print(resultado) # imprime 144


print("Funções anônimas ou lambdas são aquelas que são mais concisas e fáceis de se estruturar, necessiatando menos linhas de código")
quadrado = lambda x: x ** 2
print(quadrado(5))  # Imprime 25

def area_retangulo(base, altura):
    """
    Calcula a área de um retângulo.


    Args:
        base (float): A base do retângulo.
        altura (float): A altura do retângulo.


    Returns:
        float: A área do retângulo.
    """
    return base * altura