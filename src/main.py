tarefas = []

while True:
    print("\n===== TaskTracker =====")
    print("1 - Cadastrar nova tarefa")
    print("2 - Visualizar tarefas cadastradas")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        print("\n--- Cadastro de tarefa ---")

        while True:
            titulo = input("Título: ").strip()

            if titulo:
                break

            print("Erro: o título é obrigatório.")

        descricao = input("Descrição: ").strip()

        while True:
            prioridade = input(
                "Prioridade (Alta, Média ou Baixa): "
            ).strip().lower()

            if prioridade in ("alta", "média", "media", "baixa"):
                if prioridade == "media":
                    prioridade = "média"

                prioridade = prioridade.capitalize()
                break

            print("Erro: escolha Alta, Média ou Baixa.")

        data_limite = input("Data limite (DD/MM/AAAA): ").strip()

        tarefa = {
            "titulo": titulo,
            "descricao": descricao,
            "prioridade": prioridade,
            "data_limite": data_limite,
            "status": "Pendente"
        }

        tarefas.append(tarefa)
        print("Tarefa cadastrada com sucesso!")

    elif opcao == "2":
        print("\n--- Tarefas cadastradas ---")

        if not tarefas:
            print("Não existem tarefas cadastradas.")
        else:
            for numero, tarefa in enumerate(tarefas, start=1):
                print(f"\nTarefa {numero}")
                print(f"Título: {tarefa['titulo']}")
                print(f"Descrição: {tarefa['descricao']}")
                print(f"Prioridade: {tarefa['prioridade']}")
                print(f"Data limite: {tarefa['data_limite']}")
                print(f"Status: {tarefa['status']}")

    elif opcao == "3":
        print("Encerrando o TaskTracker. Até logo!")
        break

    else:
        print("Opção inválida! Escolha 1, 2 ou 3.")