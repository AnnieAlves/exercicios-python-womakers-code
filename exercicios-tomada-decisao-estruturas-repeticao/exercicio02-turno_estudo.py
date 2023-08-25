'''
Faça um Programa que pergunte em que turno você estuda. 
Peça para digitar M - matutino, V - vespertino ou N - noturno. 
Imprima a mensagem "Bom dia!", "Boa tarde!" ou "Boa noite!" ou 
"Valor inválido!", conforme o caso.
'''

turno = input("Em que período você estuda? Digite M para matutino, V para vespertino ou N para noturno: ").upper()

if turno == 'M':
    print("Bom Dia!")
elif turno == 'V':
    print("Boa Tarde!")
elif turno == 'N':
    print("Boa Noite!")
else:
    print("Valor inválido!")