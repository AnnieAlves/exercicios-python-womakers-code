'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e 
calcule quanto poderia comprar de cada moeda estrangeira. 
Considere a tabela de conversão abaixo:

Dólar Americano: R$4,91
Peso Argentino: R$0,02
Dólar Australiano: R$3,18
Dólar Canadense: R$3,64
Franco Suíço: R$0,42
Euro: R$5,36
Libra Esterlina: R$6,21"



'''


    

tabela_coversao = {
    "Dólar Americano": 4.91,
    "Peso Argentino": 0.02,
    "Dólar Australiano": 3.18,
    "Dólar Canadense": 3.64,
    "Franco Suíço": 0.42,
    "Euro": 5.36,
    "Libra Esterlina": 6.21    
}


try:
    valor_carteira = float(input("Digite o valor em reais na carteira: "))
    
    print(f"Com R${valor_carteira} é possível comprar os seguintes valores de cada moeda: \n")
    for moeda, taxa in tabela_coversao.items():
        valor_convertido = valor_carteira / taxa
        print(f"{moeda}: {valor_convertido:.2f}\n")
        
except ValueError:
    print("Valor inválido. Digite apenas números")
        