import tkinter as tk
from tkinter import ttk, scrolledtext

class Notepad(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Notepad com Múltiplas Guias")
        self.geometry("600x400")

        # Criar um Notebook para as guias
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True)

        # Botão para adicionar novas guias
        self.add_tab_button = ttk.Button(self, text="Nova Guia", command=self.add_tab)
        self.add_tab_button.pack(side='bottom', fill='x')

        # Adiciona uma guia inicial
        self.add_tab()

    def add_tab(self):
        # Cria uma nova guia
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Nova Guia")

        # Adiciona um widget de texto na nova guia
        text_area = scrolledtext.ScrolledText(tab, wrap=tk.WORD)
        text_area.pack(fill='both', expand=True)

if __name__ == "__main__":
    app = Notepad()
    app.mainloop()