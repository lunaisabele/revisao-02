#Receber notas
soma = 0
for x in range(1,6):
    notas = float(input(f"Digite {x}º nota: "))
    soma += notas
media = soma/5
print(f"{media}")
if media >= 7:
    print("Aprovado!!")
elif media>=4 and media<=7:
    print("Recuperaçao")
else:
    print("Número invalido")