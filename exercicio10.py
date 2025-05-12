
frase = input("Digite uma frase: ").upper()
contador = 0
for x in frase:
    if x == "A":
        contador += 1
print(f"tem {contador} letras A!")