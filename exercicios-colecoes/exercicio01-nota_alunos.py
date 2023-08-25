#Faça um Programa que peça as quatro notas de 10 alunos, 
# calcule e armazene em uma lista a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.

media_dos_alunos = []
alunos_acima_da_media = 0;

for aluno in range(10):
    media_individual = 0
    for nota in range(4):
        media_individual += float(input(f"Digite a {nota+1}ª nota do {aluno+1}º aluno: "))
    media_individual /=4
    media_dos_alunos.append(media_individual)
    
for media in media_dos_alunos:
    if media >= 7.0:
        alunos_acima_da_media+=1
        
print(media_dos_alunos)
print(alunos_acima_da_media)
        