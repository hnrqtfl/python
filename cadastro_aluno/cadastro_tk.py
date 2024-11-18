'''Criar um aplicativo em Python que funcione como um sistema de cadastro de alunos para uma escola. O sistema deve permitir a inserção, consulta e exclusão de dados dos alunos.'''

'''Funcionalidades:
[ ]Menu principal: Apresentar um menu com as opções:
[ ]Cadastrar aluno: Permitir a inserção de dados do aluno, incluindo nome, matrícula, curso e data de nascimento.
[ ]Consultar aluno: Buscar um aluno por nome ou matrícula e exibir seus dados completos.
[ ]Excluir aluno: Remover um aluno do sistema por nome ou matrícula.
[ ]Sair: Encerrar o programa.
[ ]Validação de dados: Garantir que os dados inseridos sejam válidos e consistentes.
[ ]Armazenamento de dados: Armazenar os dados dos alunos em uma estrutura de dados adequada (lista, dicionário, etc.).
[ ]Interface amigável: Criar uma interface amigável e intuitiva para o usuário.'''

import tkinter as tk
from tkinter import ttk

alunos = []

def adicionar_aluno():
    aluno =input(f"Nome do aluno?:")
    alunos.append(aluno)
    print(f"Aluno {aluno} adicionado com sucesso!")
    adicionar_button = ttk.Button(frame_usuario, text="Adicionar Aluno", command=adicionar_aluno)
    adicionar_button.grid(row=0,column=1,padx=5,pady=5)

def mostrar_aluno():
    mostrar = input(f"Qual aluno deseja mostrar?:")
    if mostrar in alunos:
        print(f"{mostrar}")
    mostrar_button = ttk.Button(frame_usuario, text="Mostrar Aluno", command=mostrar_aluno)
    mostrar_button.grid(row=1,column=1,padx=5,pady=5)

def consultar_aluno():
    consulta = input(f"Consultar aluno:")
    if consulta in alunos:
        print(f"{consulta}")
    consultar_button = ttk.Button(frame_usuario, text="Consultar Aluno", command=consultar_aluno)
    consultar_button.grid(row=2,column=1,padx=5,pady=5)

def excluir_aluno():
    excluir = input(f"CPF do aluno que deseja excluir:")
    if excluir in alunos:
        print(f"Aluno {excluir} excluído com sucesso!")
    excluir_button = ttk.Button(frame_usuario, text="Excluir Aluno", command=excluir_aluno)
    excluir_button.grid(row=3,column=1,padx=5,pady=5)

def mostrar_menu():
    menu = """
    ======================
    Escolha uma opção: 
    m - (Mostrar Aluno) 
    a - (Adicionar Aluno) 
    c - (Consultar Aluno)
    e - (Excluir Aluno)
    ======================
    """
    while True:
        opcao = input(menu)
        if opcao == 'a':
            adicionar_aluno()
        elif opcao == 'm':
           mostrar_aluno()
        elif opcao == 'c':
            consultar_aluno()
        elif opcao == 'e':
           excluir_aluno()
        break
    mostrar_menu()

# Criar a janela principal
window = tk.Tk()
window.title("Cadastro de Usuário")
window.geometry("300x300")

# Frame usuário
frame_usuario = ttk.Labelframe(window, text="Menu")
frame_usuario.grid(row=2,column=0,pady=5,padx=5)

# Iniciar o loop de eventos
window.mainloop()