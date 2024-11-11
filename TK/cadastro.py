import tkinter as tk
from tkinter import ttk

# Criar a janela principal
window = tk.Tk()
window.title("Cadastro de Usuário")

# Criar um frame para conter os widgets do formulário
frame = ttk.LabelFrame(window, text="Informações do Usuário")
frame.grid(row=0,column=0, pady=5, padx=5)

# Nome
nome_label = ttk.Label(frame, text="Nome")
nome_label.grid(row=0,column=0,padx=1,pady=5)

# Recebe nome
nome_entry = ttk.Entry(frame)
nome_entry.grid(row=1,column=0,padx=20)

# Sobrenome
last_label = ttk.Label(frame, text ="Sobrenome")
last_label.grid(row=0,column=1,padx=1,pady=5)

# Recebe sobrenome
last_entry = ttk.Entry(frame)
last_entry.grid(row=1,column=1,padx=20) 

# Título
title_label = ttk.Label(frame, text="Título")
title_label.grid(row=0,column=2,padx=1,pady=5)

# Recebe título
title_title = ttk.Combobox(frame)
title_title.grid(row=1,column=2,padx=20)

# Idade
idade_label = ttk.Label(frame, text="Idade")
idade_label.grid(row=2,column=0,pady=5)

# Recebe idade
idade_idade = ttk.Spinbox(frame)
idade_idade.grid(row=3,column=0,padx=20)

# Nacionalidade
nacio_label = ttk.Label(frame, text="Nacionalidade")
nacio_label.grid(row=2,column=1,padx=1,pady=5)

# Recebe nacionalidade
nacio_nacio = ttk.Combobox(frame)  
nacio_nacio.grid(row=3,column=1,padx=20)

# Status
status_label = ttk.Label(frame, text="Status de Registro")
status_label.grid(row=4,column=0,padx=10,pady=15)

# Recebe status
status_status = ttk.Checkbutton(frame,text="Cadastrado Atualmente")
status_status.grid(row=5,column=0)

# Cursos
complete_label = ttk.Label(frame, text="# Cursos Completos")
complete_label.grid(row=4,column=1)

# Recebe cursos
complete_complete = ttk.Spinbox(frame)
complete_complete.grid(row=5,column=1)

# Simestre
simestre_label = ttk.Label(frame, text="# Semestres")
simestre_label.grid(row=4, column=2)

# Recebe simestre
simestre_simestre = ttk.Spinbox(frame)
simestre_simestre.grid(row=5,column=2)

# Termos & condições
termos_label = ttk.Checkbutton(frame, text="Eu aceito todos os termos e condições.")
termos_label.grid(row=6, column=0, pady=10)

# BOTÃO ENVIAR FORMULÁRIO
enviar_button = ttk.Button(frame, text="Enviar")
enviar_button.grid(row=7, column=1)

# Iniciar o loop de eventos
window.mainloop()