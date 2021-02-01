dicionario = dict()
lista_telefonica = list()

lista_telefonica = [("Yan", "21 97886-5443"), ("Pedro", "43 92223-2313")]

dicionario = dict(lista_telefonica)

print(dicionario.keys())

for chave in dicionario.keys():
    print(chave)
    print(f'Para o outcome {chave} a probabilidade é {dicionario[chave]}')

print(dicionario)
lista_telefonica.append((32, 0))
dicionario = dict(lista_telefonica)
print(dicionario)

lista_nova = list(dicionario.items())
print(lista_nova)