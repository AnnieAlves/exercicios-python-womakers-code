#"Escreva um programa em Python que, onde todos os valores em um dicionário são emitidos.
# Se sim, imprima True. Caso contrário, imprima Falso."

meu_dicionario = {
    'chave 1': 10,
    'chave 2': 'Annie',
    'chave 3': None,
    'chave 4': 42.5
}


for chave, valor in meu_dicionario.items():
    print(f"A {chave} tem valor?", valor is not None)
