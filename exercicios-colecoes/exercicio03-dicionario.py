#"Escreva um programa em Python que, onde todos os valores em um dicionário são emitidos.
# Se sim, imprima True. Caso contrário, imprima Falso."

meu_dicionario = {
    'chave 1': 10,
    'chave 2': 'Annie',
    'chave 3': '',
    'chave 4': 42.5
}


    
valores_emitidos = all(meu_dicionario.values())


print("Todos os valores são verdadeiros?")
if valores_emitidos:
    print("True")
else:
    print("False")
