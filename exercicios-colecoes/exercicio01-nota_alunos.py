#Faça um Programa que peça as quatro notas de 10 alunos, 
# calcule e armazene em uma lista a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.

media_dos_alunos = []
lista_notas = []
alunos_acima_da_media = 0;

for aluno in range(10):
    lista_notas.append([])
    for nota in range(4):
        lista_notas[aluno].append(
            float(
                input(f"Digite a {nota+1}ª nota do {aluno+1}º aluno: ")
            )
        )       
    
    
for notas in lista_notas:
    media_dos_alunos.append(
        sum(notas) / len(notas)
    )
    
alunos_acima_da_media = sum(1 for media in media_dos_alunos if media >= 7.0)
        
print(media_dos_alunos)
print(alunos_acima_da_media)
        