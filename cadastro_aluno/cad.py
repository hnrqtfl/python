import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Dicionário para armazenar os alunos
alunos = {}

# Função para cadastrar aluno
def cadastrar_aluno():
    def salvar_aluno():
        nome = entry_nome.get().strip()
        matricula = entry_matricula.get().strip()
        curso = entry_curso.get().strip()
        nascimento = entry_nascimento.get().strip()

        # Validação de dados
        if not nome or not matricula or not curso or not nascimento:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
            return
        
        if matricula in alunos:
            messagebox.showerror("Erro", "Matrícula já cadastrada.")
            return
        
        alunos[matricula] = {"nome": nome, "matricula": matricula, "curso": curso, "nascimento": nascimento}
        messagebox.showinfo("Sucesso", f"Aluno {nome} cadastrado com sucesso!")
        window_cadastro.destroy()

    window_cadastro = tk.Toplevel()
    window_cadastro.title("Cadastrar Aluno")
    
    # Labels e campos de entrada
    tk.Label(window_cadastro, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
    entry_nome = tk.Entry(window_cadastro)
    entry_nome.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(window_cadastro, text="Matrícula:").grid(row=1, column=0, padx=10, pady=5)
    entry_matricula = tk.Entry(window_cadastro)
    entry_matricula.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(window_cadastro, text="Curso:").grid(row=2, column=0, padx=10, pady=5)
    entry_curso = tk.Entry(window_cadastro)
    entry_curso.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(window_cadastro, text="Data de Nascimento (DD/MM/AAAA):").grid(row=3, column=0, padx=10, pady=5)
    entry_nascimento = tk.Entry(window_cadastro)
    entry_nascimento.grid(row=3, column=1, padx=10, pady=5)

    # Botão para salvar o aluno
    tk.Button(window_cadastro, text="Salvar", command=salvar_aluno).grid(row=4, column=1, padx=10, pady=10)
    
    
    
    window_consulta = tk.Toplevel()
    window_cadastro.title("Consultar Aluno")
    
    # Labels e campos de entrada
    tk.Label(window_consulta, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
    entry_nome = tk.Entry(window_consulta)
    entry_nome.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(window_consulta, text="Matrícula:").grid(row=1, column=0, padx=10, pady=5)
    entry_matricula = tk.Entry(window_cadastro)
    entry_matricula.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(window_consulta, text="Curso:").grid(row=2, column=0, padx=10, pady=5)
    entry_curso = tk.Entry(window_consulta)
    entry_curso.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(window_consulta, text="Data de Nascimento (DD/MM/AAAA):").grid(row=3, column=0, padx=10, pady=5)
    entry_nascimento = tk.Entry(window_cadastro)
    entry_nascimento.grid(row=3, column=1, padx=10, pady=5)
    
    # Botão Cadastrar aluno 
    tk.Button(window_cadastro, text="Cadastrar Aluno", command=cadastrar_aluno) 
    cadastrar_aluno.grid (row=1, column= 0, padx=5, pady=5)
    
    # Botão Consultar aluno
    tk.Button(window_consulta, text="", command=cadastrar_aluno) 
    cadastrar_aluno.grid (row=2, column= 0, padx=5, pady=5)

# Função para consultar aluno
def consultar_aluno():
    matricula = simpledialog.askstring("Consultar Aluno", "Digite a matrícula ou nome do aluno:")
    
    if matricula:
        matricula = matricula.strip()
        aluno = None
        if matricula in alunos:
            aluno = alunos[matricula]
        else:
            # Se não encontrar pela matrícula, tenta procurar pelo nome
            for key, value in alunos.items():
                if value["nome"].lower() == matricula.lower():
                    aluno = value
                    break
        
        if aluno:
            info = f"Nome: {aluno['nome']}\nMatrícula: {aluno['matricula']}\nCurso: {aluno['curso']}\nData de Nascimento: {aluno['nascimento']}"
            messagebox.showinfo("Aluno Encontrado", info)
        else:
            messagebox.showerror("Erro", "Aluno não encontrado.")

# Função para excluir aluno
def excluir_aluno():
    matricula = simpledialog.askstring("Excluir Aluno", "Digite a matrícula do aluno a ser excluído:")
    
    if matricula:
        matricula = matricula.strip()
        if matricula in alunos:
            del alunos[matricula]
            messagebox.showinfo("Sucesso", "Aluno excluído com sucesso!")
        else:
            messagebox.showerror("Erro", "Aluno não encontrado.")

# Função para sair
def sair():
    if messagebox.askyesno("Sair", "Deseja realmente sair?"):
        root.quit()

# Função para criar o menu principal
#def criar_menu():
    menu = tk.Menu(root)
    
    menu_cadastro = tk.Menu(menu, tearoff=0)
    menu_cadastro.add_command(label="Cadastrar Aluno", command=cadastrar_aluno)
    menu_cadastro.add_command(label="Consultar Aluno", command=consultar_aluno)
    menu_cadastro.add_command(label="Excluir Aluno", command=excluir_aluno)
    menu_cadastro.add_separator()
    menu_cadastro.add_command(label="Sair", command=sair)

    menu.add_cascade(label="", menu=menu_cadastro)
    root.config(menu=menu)

# Configuração da janela principal
root = tk.Tk()
root.title("Sistema de Cadastro de Alunos")

# Criação do menu
#criar_menu()

# Iniciar o loop da interface gráfica
root.mainloop()
