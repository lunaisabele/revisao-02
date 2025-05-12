#ler em uam sequencia de 10 numeros quantos sao maiores que 50
contador = 0
for x in range(1,11):
    nume = int(input(f"Digite {x}º numero: "))

    if nume > 50:
        contador += 1
print(f"{contador} números são maiores que 50!")