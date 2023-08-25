quantidade_respostas_positivas = 0

veredito = {
    2: "Suspeito(a)",
    3: "Cumplíce",
    4: "Cumplíce",
    5: "Assassino(a)"
}

perguntas = [
        "\nTelefonou para a vítima?",
        "\nEsteve no local do crime?",
        "\nMora perto da vítima?",
        "\nDevia para a vítima?",
        "\nJá trabalhou com a vítima?"
    ]

print("Respondas as perguntas a seguir com 's' para sim e n para 'não'")

for pergunta in perguntas:
    resposta = input(f"\n{pergunta} ").lower()
    if resposta == 's':
        quantidade_respostas_positivas += 1

if quantidade_respostas_positivas in veredito:
    print(f"\nVeredito: {veredito[quantidade_respostas_positivas]}")
else:
    print("Veredito: Inocente")
    
