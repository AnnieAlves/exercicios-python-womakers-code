#Crie um programa que tenha a função leiaInt(), 
# que vai funcionar de forma semelhante à função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. 
# Exemplo: n = leiaInt('Digite um número').

def leiaInt(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            number = int(n)
            return number
        else:
            print("\33[1;31mValor inválido. Insira um número inteiro.\33[m")

valor_int = leiaInt("Digite um número inteiro: ")
print(f"\33[1;32mO número digitado foi {valor_int}\33[m")