#3. Faça um Programa que peça a temperatura em graus Celsius,
# converta e mostre em graus Fahrenheit.

while True:
    try:
        temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))
        temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32  
        print(f"{temperatura_celsius:.1f}ºC equivale a {temperatura_fahrenheit}ºF") 
        break
    except ValueError:
        print("Por favor, digite apenas números. Use ponto para separar casas decimais")
