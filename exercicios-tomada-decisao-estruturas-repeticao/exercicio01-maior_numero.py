#1 Faça um Programa que peça dois números e imprima o maior deles.

while True:
    try:
        number1 = int(input("Digite um número inteiro: "))
        number2 = int(input("Digite outro número inteiro: "))
        
        maxNumber = max(number1, number2)
        
        print(f"Entre os números digitados, o maior é: {maxNumber}")
        break
        
    except ValueError:
        print("Números inválidos. Por favor digite apenas números inteiros")
    
    