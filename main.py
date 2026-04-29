usuarios = []

def adicionar_usuario():
    nome = input("Digite o nome do usuário: ")
    usuarios.append(nome)
    print("Usuário cadastrado com sucesso!\n")

def listar_usuarios():
    print("\nUsuários cadastrados:")
    for usuario in usuarios:
        print("-", usuario)
    print()

while True:
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_usuario()
    elif opcao == "2":
        listar_usuarios()
    elif opcao == "3":
        break
    else:
        print("Opção inválida\n")
