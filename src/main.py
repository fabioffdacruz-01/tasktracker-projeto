tarefas = []

while True:
    print("\n===== TaskTracker =====")
    print("1 - Cadastrar nova tarefa")
    print("2 - Visualizar tarefas cadastradas")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        print("Cadastro de tarefas em desenvolvimento.")
    elif opcao == "2":
        print("Visualização de tarefas em desenvolvimento.")
    elif opcao == "3":
        print("Encerrando o TaskTracker. Até logo!")
        break
    else:
        print("Opção inválida! Escolha 1, 2 ou 3.")