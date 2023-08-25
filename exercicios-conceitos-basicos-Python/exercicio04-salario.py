'''4. Faça um Programa que pergunte quanto você ganha por hora 
e o número de horas trabalhadas no mês.Calcule e mostre o total
 do seu salário no referido mês.'''

while True:
    try:
        ganho_por_hora = float(input("Digite o quanto você ganha por hora, em reais: "))
        horas_por_mes = float(input("Digite a quantidade de horas trabalhadas por mês: "))
        
        salario_mes = ganho_por_hora * horas_por_mes
        
        print(f"Seu salário mensal é de R${salario_mes:.2f}")
        break
    except ValueError:
        print("Valor inválido. Por favor, insira um número válido")