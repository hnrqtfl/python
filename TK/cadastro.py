import tkinter as tk
from tkinter import ttk

# Criar a janela principal
window = tk.Tk()
window.title("Cadastro de Usuário")

# Criar um frame para conter os widgets do formulário
form_frame = ttk.Frame(window, padding="20")
form_frame.grid(row=0, column=0, sticky="nsew")

# WIDGETS INFORMAÇÕES DO USUÁRIO
nome_label = ttk.Label(form_frame, text="Nome")
nome_entry = ttk.Entry(form_frame)
last_label = ttk.Label(form_frame, text ="Sobrenome")
last_entry = ttk.Entry(form_frame)
title_label = ttk.Label(form_frame, text="Título")
title_title = ttk.Combobox(form_frame)
idade_label = ttk.Label(form_frame, text="Idade")
idade_idade = ttk.Spinbox(form_frame)
nacio_label = ttk.Label(form_frame, text="Nacionalidade")
nacio_nacio = ttk.Combobox(form_frame)  

# WIDGETS INFORMAÇÕES DO CURSO
status_label = ttk.Label(form_frame, text="Status de Registro")
status_status = ttk.Checkbutton(form_frame,text="Cadastrado Atualmente")
complete_label = ttk.Label(form_frame, text="# Cursos Completos")
complete_complete = ttk.Spinbox(form_frame)
simestre_label = ttk.Label(form_frame, text="# Semestres")
simestre_simestre = ttk.Spinbox(form_frame)

#TERMOS E CONDIÇÕES
termos_label = ttk.Checkbutton(form_frame, text="Eu aceito todos os termos e condições.")

# ORGANIZAÇÃO LAYOUT
nome_label.grid(row=0,column=0,padx=1,pady=5)
nome_entry.grid(row=1,column=0,padx=20)
last_label.grid(row=0,column=1,padx=1,pady=5)
last_entry.grid(row=1,column=1,padx=20) 
title_title.grid(row=1,column=2,padx=20)
title_label.grid(row=0,column=2,padx=1,pady=5)
idade_idade.grid(row=3,column=0,padx=20)
idade_label.grid(row=2,column=0,pady=5)
nacio_label.grid(row=2,column=1,padx=1,pady=5)
nacio_nacio.grid(row=3,column=1,padx=20)
status_label.grid(row=4,column=0,padx=10,pady=15)
status_status.grid(row=5,column=0)
complete_label.grid(row=4,column=1)
complete_complete.grid(row=5,column=1)
simestre_label.grid(row=4, column=2)
simestre_simestre.grid(row=5,column=2)
termos_label.grid(row=6, column=0, pady=10)

# BOTÃO ENVIAR FORMULÁRIO
enviar_button = ttk.Button(form_frame, text="Enviar")
enviar_button.grid(row=7, column=1)

# Iniciar o loop de eventos
window.mainloop()