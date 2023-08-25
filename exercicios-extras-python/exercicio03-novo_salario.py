#"Faça um algoritmo que leia o salário de um 
# funcionário e mostre seu novo salário. 
# Se o salário for até R$1000,00, o funcionário terá 20% de aumento. 
# Entre R$1001,00 até R$2800,00, o funcionário terá 10% de aumento.
# Acima de R$2801,00, o funcionário terá 5% de aumento."

while True:
    try:
        salario_atual = input("Insira o seu salário atual, em reais: ")
        salario_atual = salario_atual.replace(',','.')
        salario_atual = float(salario_atual)
        
        if salario_atual <= 1000:
            novo_salario = salario_atual * 1.2
        elif salario_atual <= 2800:
            novo_salario = salario_atual * 1.1
        else:
            novo_salario = salario_atual * 1.05
            
        print(f"Seu novo salário será de R${novo_salario:.2f}")
        break
            
    except ValueError:
        print("Por gentileza, insira apenas números")
        