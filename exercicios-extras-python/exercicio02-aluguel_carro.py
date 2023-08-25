#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo 
# que o carro custa R$80,00 por dia e R$0,20 por km rodado


def calcular_valor_a_pagar(km, dias):
    valor_a_pagar = (80 * dias) + (.2 * km)
    return valor_a_pagar

while True:
    try:
        km = int(input("O carro percorreu quantos km? "))
        dias = int(input("O carro foi alugado por quantos dias? "))
        
        valor_devido = calcular_valor_a_pagar(km, dias)
        print(f"O valor a ser pago é de R${valor_devido:.2f}")
        break
    
    except ValueError:
        print("Valor Inválido. Insira apenas números")
        
        