import tkinter as tk
from tkinter import messagebox
from registroDAO import RegistroDAO
from registro import Registro

class Cadastro:
    def __init__(self, root):
        self.dao = RegistroDAO()
        self.root = root      # q inicia o projeto python
        self.root.title("Cadastro de Peças")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")

        #frames
        self.frame_campos = tk.Frame(root, padx=10, pady=10, bg="#f0f0f0")
        self.frame_campos.pack(fill=tk.X)

        #campos
        self.label_nome = tk.Label(self.frame_campos, text="Nome da Peça", font=("Arial", 12), bg="#f0f0f0")
        self.label_nome.pack()
        self.entry_nome = tk.Entry(self.frame_campos, font=("Arial", 12))
        self.entry_nome.pack()

        self.label_descricao = tk.Label(self.frame_campos, text="Descrição da Peça", font=("Arial", 12), bg="#f0f0f0")
        self.label_descricao.pack()
        self.entry_descricao = tk.Entry(self.frame_campos, font=("Arial", 12))
        self.entry_descricao.pack()

        self.label_id = tk.Label(self.frame_campos, text="ID (para atualizar/deletar)", font=("Arial", 12), bg="#f0f0f0")
        self.label_id.pack()
        self.entry_id = tk.Entry(self.frame_campos, font=("Arial", 12))
        self.entry_id.pack()

        

        #framebotoes
        self.frame_botoes = tk.Frame(root, pady=10, bg="#f0f0f0")
        self.frame_botoes.pack()

        #botões
        
        tk.Button(self.frame_botoes, text="Adicionar", command=self.adicionar, width=12, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5)
        tk.Button(self.frame_botoes, text="Listar", command=self.listar, width=12, bg="#A3A3A3", fg="white").grid(row=0, column=1, padx=5)
        tk.Button(self.frame_botoes, text="Atualizar", command=self.atualizar, width=12, bg="#2B59C3", fg="white").grid(row=0, column=2, padx=5)
        tk.Button(self.frame_botoes, text="Deletar", command=self.deletar, width=12, bg="#E63B2E", fg="white").grid(row=0, column=3, padx=5)

        self.text_resultado = tk.Text(root, height=10, font=("Courier", 10), bd=2, relief=tk.SUNKEN)
        self.text_resultado.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def adicionar(self):
        nome = self.entry_nome.get()
        descricao = self.entry_descricao.get()
        if nome and descricao:
            registro = Registro(nome=nome, descricao=descricao)
            self.dao.adicionar(registro)
            messagebox.showinfo("Sucesso", "Peça adicionada com Sucesso!")
            self.limpar_campos()
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos!")
    
    def listar(self):
        registros = self.dao.lista()
        self.text_resultado.delete("1.0", tk.END)
        for r in registros:
            self.text_resultado.insert(tk.END, f"ID: {r[0]} | Nome: {r[1]} | Descricao: {r[2]}\n")

    def atualizar(self):
        id = self.entry_id.get()
        nome = self.entry_nome.get()
        descricao = self.entry_descricao.get()
        if id and nome and descricao:
            registro = Registro(id=int(id), nome=nome, descricao=descricao)
            self.dao.atualizar(registro)
            messagebox.showinfo("Atualizado", "Peça foi atualizada com Sucesso!")
            self.limpar_campos() 
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos e informe o ID!")

    def deletar(self):
        id = self.entry_id.get()
        if id:
            self.dao.deletar(int(id))
            messagebox.showinfo("Deletado", "Peça foi Deletada!!")
            self.limpar_campos()
        else:
            messagebox.showwarning("Erro", "Infome o ID!")
        
    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_descricao.delete(0, tk.END)
        self.entry_id.delete(0, tk.END)

#executavel
if __name__=="__main__":
    root = tk.Tk()
    cadastro = Cadastro(root)
    root.mainloop()