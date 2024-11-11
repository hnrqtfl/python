import tkinter as tk
from tkinter import ttk

# Criar a janela principal
window = tk.Tk()
window.title("Cadastro de Usuário")

# Frame usuário
frame_usuario = ttk.Labelframe(window, text="Informações do Usuário")
frame_usuario.grid(row=0,column=0,pady=5,padx=5)

# Frame registro
frame_registro = ttk.Labelframe(window, text="Registro")
frame_registro.grid(row=2,column=0,pady=10,padx=10)

# Frame termos
frame_termos = ttk.Labelframe(window, text="Termos & Condições")
frame_termos.grid(row=3,column=0,pady=30,padx=10)

# Nome
nome_label = ttk.Label(frame_usuario, text="Nome")
nome_label.grid(row=0,column=0,padx=5,pady=5)

# Recebe nome
nome_entry = ttk.Entry(frame_usuario)
nome_entry.grid(row=1,column=0,padx=20)

# Sobrenome
last_label = ttk.Label(frame_usuario, text ="Sobrenome")
last_label.grid(row=0,column=1,padx=1,pady=5)

# Recebe sobrenome
last_entry = ttk.Entry(frame_usuario)
last_entry.grid(row=1,column=1,padx=20) 

# Título
title_label = ttk.Label(frame_usuario, text="Título")
title_label.grid(row=0,column=2,padx=1,pady=5)

# Recebe título
title_title = ttk.Combobox(frame_usuario)
title_title.grid(row=1,column=2,padx=20)

# Idade
idade_label = ttk.Label(frame_usuario, text="Idade")
idade_label.grid(row=2,column=0,pady=5)

# Recebe idade
idade_idade = ttk.Spinbox(frame_usuario)
idade_idade.grid(row=3,column=0,padx=20)

# Nacionalidade
nacio_label = ttk.Label(frame_usuario, text="Nacionalidade")
nacio_label.grid(row=2,column=1,padx=1,pady=5)

# Recebe nacionalidade
nacio_nacio = ttk.Combobox(frame_usuario)  
nacio_nacio.grid(row=3,column=1,padx=20)

# Status
status_label = ttk.Label(frame_registro, text="Status de Registro")
status_label.grid(row=4,column=0,padx=10,pady=15)

# Recebe status
status_status = ttk.Checkbutton(frame_registro,text="Cadastrado Atualmente")
status_status.grid(row=5,column=0)

# Cursos
complete_label = ttk.Label(frame_registro, text="# Cursos Completos")
complete_label.grid(row=4,column=1)

# Recebe cursos
complete_complete = ttk.Spinbox(frame_registro)
complete_complete.grid(row=5,column=1)

# Simestre
simestre_label = ttk.Label(frame_registro, text="# Semestres")
simestre_label.grid(row=4, column=2)

# Recebe simestre
simestre_simestre = ttk.Spinbox(frame_registro)
simestre_simestre.grid(row=5,column=2)

# Termos & condições
termos_label = ttk.Checkbutton(frame_termos, text="Eu aceito todos os termos e condições.")
termos_label.grid(row=6, column=0, pady=10)

# BOTÃO ENVIAR FORMULÁRIO
enviar_button = ttk.Button(text="Enviar")
enviar_button.grid(row=7, column=0)

# Iniciar o loop de eventos
window.mainloop()
