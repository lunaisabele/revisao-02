#Receber 5 nomes
nomes=[]
for x in range(5):
    nome = input("Digite um nome: ").upper()
    nomes.append(nome)
#printar apenas os nomes que começam com a letra "A"
for i in nomes:
    if "A"in i[0]:
        print(i)

