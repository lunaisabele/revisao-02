#recer uma senha do usuario e liberar o login
senha= 1234
while senha == senha:
    login = int(input("Digite sua senha: "))
    if login != senha:
        print("Acesso negado!! Tente novamente")
    else:
        print("Acesso liberado!!!")
        break