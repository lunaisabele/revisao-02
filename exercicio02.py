#Número secreto
numero_secreto = 22
palpite = 0
while palpite != numero_secreto:
    palpite = int(input("Adivinhe o número: "))
    if palpite > numero_secreto:
        print("Muito alto.")
    elif palpite < numero_secreto:
        print("Muito baixo")
    else:
        print("Acertou!")

