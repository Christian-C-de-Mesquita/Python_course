# Aprendendo sobre os dicionários (criação e uso)
carros = {"nome": "Ferrari", "valor": 250.000, "modelo": "SF90 Stradale"}
print(carros["nome"]) #imprime "Ferrari"
print(carros["valor"]) #imprime 250.000
print(carros["modelo"]) #imprime "SF90 Stradale"

print(carros.keys()) # Imprime dict_keys(["nome", "valor", "modelo"])
print(carros.values()) # Imprime dict.values["Ferrari","250.000","SD90 Stradale"]
print(carros.items()) # Imprime dict.items[('nome', 'Ferrari'), ('valor', 250.0), ('modelo', 'SF90 Stradale')]
carros.update({"nome": "Ferrari SF90 Stradale"}) #faz a alteração de informações
print(carros)
