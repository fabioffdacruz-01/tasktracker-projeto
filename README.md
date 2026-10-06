# TaskTracker

## Descrição

O TaskTracker é uma aplicação de linha de comando (CLI) desenvolvida em Python para auxiliar no gerenciamento de tarefas.

O sistema permite cadastrar novas tarefas, visualizar as tarefas cadastradas e encerrar a aplicação.

Cada tarefa possui título, descrição, prioridade, data limite e status. O sistema realiza validações para garantir que o título não esteja vazio e que a prioridade informada seja Alta, Média ou Baixa.

## Tecnologias Utilizadas

- Python 3
- Git
- GitHub

## Estrutura do Projeto

tasktracker-projeto/
- README.md
- .gitignore
- docs/
  - planejamento_logico.pdf
- src/
  - main.py

## Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. Abra o terminal na pasta do projeto.
3. Execute o comando:

python src/main.py

## Funcionalidades

- Cadastrar nova tarefa
- Visualizar tarefas cadastradas
- Validar título obrigatório
- Validar prioridade
- Definir automaticamente o status da nova tarefa como Pendente
- Sair da aplicação

## Projeto Acadêmico

Projeto desenvolvido para a Fase 2 — Desafio da Etapa Intermediária da disciplina Bootcamp II.