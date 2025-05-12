#digitar um numero inteiro e mostar sua taboada
numero = int(input("Digite um número: "))
#laço para repetir a taboada
print(f"\ntaboada {numero}\n")
for x in range(1,11):
    resultado = numero *x
    print(f"{numero} X {x} = {resultado}")
