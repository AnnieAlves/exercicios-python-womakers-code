#Escreva um script que pergunte ao usuário se ele deseja converter uma temperatura 
# de graus Celsius para Fahrenheit ou vice-versa. Para cada opção, crie uma função.
# Crie uma terceira função que é um menu para o usuário escolher a opção desejada, 
# onde esse menu chama a função de conversão correta

def menu_escolha():
    print("#CONVERSOR DE TEMPERATURA#\n\n")
    print("Escolha uma opção de conversão: \n\n")
    print("1 - Celsius para Farenheit \n")
    print("2- Fahrenheit para Celsius \n")    
    
    while True:
        
        resposta = input()
        if resposta == '1':
            celsius_para_fahrenheit()
            break  
        elif resposta == '2':
            fahrenheit_para_celsius()
            break
        else:
            print("\nOpção inválida. Escolha 1 ou 2.\n")
            



def celsius_para_fahrenheit():
    
    while True:
        valor = input("\nDigite a temperatura em graus Celsius: ")
        valor = valor.replace(',','.')   
    
        try:
            temperatura = float(valor)
            temperatura_convertida = (temperatura * 9/5) + 32
            
            print(f"\n{temperatura:.1f}ºC equivale a {temperatura_convertida:.1f}ºF")
            break
        
        except ValueError:
            print("\nValor inválido. Digite apenas números")
            
            
            
def fahrenheit_para_celsius():
    
    while True:
        valor = input("\nDigite a temperatura em graus Fahrenheit: ")
        valor = valor.replace(',','.')  
        
        try:
            temperatura = float(valor)
            temperatura_convertida = (temperatura - 32) * 5/9
            
            print(f"\n{temperatura:.1f}ºF equivale a {temperatura_convertida:.1f}ºC")
            break
        
        except ValueError:
            print("\nValor inválido. Digite apenas números")
    
    

menu_escolha()