import tkinter as tk
from tkinter import ttk
from selecaoDAO import SelecaoDAO
from comparacao import Comparacao

class Selecao:
    def __init__(self, root):
        self.dao = SelecaoDAO()
        self.root = root      # q inicia o projeto python
        self.root.title("Seleção")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")

        label_info = tk.Label(self.root, text="Selecione os processadores para a comparação.", font=("Arial", 14, "bold"), bg="#f0f0f0")
        label_info.pack(pady=20)

        # Frame para agrupar os dois dropdowns lado a lado
        frame_dropdowns = tk.Frame(self.root, bg="#f0f0f0")
        frame_dropdowns.pack(pady=20)

        # Exemplo de lista (poderia vir de self.dao.buscar_processadores())
        opcoes = ["Opção", "Ryzen 5 3600", "Intel i5 10400"]

        # Primeiro dropdown
        self.var1 = tk.StringVar(value="Opção")
        dropdown1 = tk.OptionMenu(frame_dropdowns, self.var1, *opcoes)
        dropdown1.config(width=20, font=("Arial", 10))
        dropdown1.pack(side="left", padx=20)

        # Segundo dropdown
        self.var2 = tk.StringVar(value="Opção")
        dropdown2 = tk.OptionMenu(frame_dropdowns, self.var2, *opcoes)
        dropdown2.config(width=20, font=("Arial", 10))
        dropdown2.pack(side="left", padx=20)

        btn_avancar = tk.Button(self.root, text="Avançar", font=("Arial", 12, "bold"), command=self.abrir_comparacao) 
        btn_avancar.pack(pady=40)

    def abrir_comparacao(self):
        self.root.destroy()
        novo_root = tk.Toplevel()
        Comparacao(novo_root)
        novo_root.mainloop()