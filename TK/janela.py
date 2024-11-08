import tkinter as tk

# Criação da janela principal
janela = tk.Tk()
janela.title("Minha Primeira Janela")
janela.geometry("780x360")

# Crição de um rótulo
greeting = tk.Label(text="Hello, Tkinter", 
     foreground="red",  # Altera a cor do texto
     background="black", # Altera a cor de fundo
     height=10, # Altera altura do botão 
     width=50  # Altera largura do botão 
) 
greeting.pack(pady=5)

# Criação de um botão
button = tk.Button(janela, text="Clique Aqui",
    foreground="black",  # Altera a cor do texto
    background="red", # Altera a cor de fundo
    height=1, # Altera altura do botão 
    width=50, # Altera largura do botão
    command=lambda: greeting.config(text="Botão clicado!"))
button.pack(pady=5)   

button2 = tk.Button(janela, text="Adicionar",
    foreground="black",  # Altera a cor do texto
    background="red", # Altera a cor de fundo
    height=1, # Altera altura do botão 
    width=50, # Altera largura do botão
    command=lambda: greeting.config(text=entry.get))
button2.pack(pady=5)   

entry = tk.Entry(fg="black", bg="red", width=60)
entry.pack(pady=5) 

# Iniciando o loop principal
janela.mainloop()
