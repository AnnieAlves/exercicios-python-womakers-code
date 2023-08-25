#2.Faça um Programa que peça dois números e imprima a soma.

    
try:
    number1 = float(input("Digite o primeiro número(use ponto para separar casas decimais): "))
    number2 = float(input("Digite o segundo número(use ponto para separar casas decimais): "))
    sum = number1 + number2

    print(f"A soma dos números informados é: {sum}")

except ValueError:
    print("Valor inválido!")
