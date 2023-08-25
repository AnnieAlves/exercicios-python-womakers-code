#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado.
# Por exemplo, 127 -> 721."



###Primeira abordagem: Sem conversão para do input para int,
# o que posibilita o usuário digitar valores não numéricos

''' def inverter_numero(n):
            return str(n[::-1])
        
numero = input("Digite um número inteiro: ")
print(f"O reverso do número {numero} é {inverter_numero(numero)}" ) '''

#Abordagem com tratamento de exceções:

while True:
    def inverter_numero(n):
        numero_para_string = str(n)
        return str(numero_para_string[::-1])
        
    try:
        numero = int(input("\nDigite um número inteiro: "))
        
        
        print(f"O reverso do número {numero} é {inverter_numero(numero)}" )
        break
    
    except ValueError:        
        print("\nInsira apenas números inteiros")
        
