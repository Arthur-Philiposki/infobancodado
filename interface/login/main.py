import tkinter as tk
from tkinter import messagebox
from login import Login
from loginDAO import LoginDAO
from cadastro import Cadastro
from visaousuario import Visaousuario

class Logins:
    def __init__(self, root):
        self.dao = LoginDAO()
        self.root = root
        self.root.title("Login de Usuário")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")

        # Frame principal centralizado
        self.main_frame = tk.Frame(root, bg="#f0f0f0")
        self.main_frame.pack(expand=True)

        # Campos de entrada
        self.label_email = tk.Label(self.main_frame, text="Email", font=("Arial", 12), bg="#f0f0f0")
        self.label_email.pack(pady=(10, 0))
        self.entry_email = tk.Entry(self.main_frame, font=("Arial", 12), width=30)
        self.entry_email.pack(pady=(0, 10))

        self.label_senha = tk.Label(self.main_frame, text="Senha", font=("Arial", 12), bg="#f0f0f0")
        self.label_senha.pack(pady=(10, 0))
        self.entry_senha = tk.Entry(self.main_frame, font=("Arial", 12), show="*", width=30)
        self.entry_senha.pack(pady=(0, 20))

        # Botão centralizado
        self.botao_logar = tk.Button(self.main_frame, text="Logar", command=self.adicionar, width=15, bg="#4CAF50", fg="white", font=("Arial", 11, "bold"))
        self.botao_logar.pack(pady=(0, 10))

    def adicionar(self):
        email = self.entry_email.get()
        senha = self.entry_senha.get()

        if email and senha:
            if email == "ag@" and senha == "1234":
                messagebox.showinfo("Sucesso", "Login bem-sucedido!")
                self.root.destroy()
                self.abrir_cadastro()
            elif email == "usuario" and senha == "1234":
                messagebox.showinfo("Sucesso", "Login bem-sucedido!")
                self.root.destroy()
                self.abrir_visaousuario()
            else:
                messagebox.showerror("Erro", "Login ou senha incorretos!")
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos!")

    def limpar_campos(self):
        self.entry_email.delete(0, tk.END)
        self.entry_senha.delete(0, tk.END)

    def abrir_cadastro(self):
        novo_root = tk.Tk()
        Cadastro(novo_root)
        novo_root.mainloop()
    
    def abrir_visaousuario(self):
        novo_root = tk.Tk()
        Visaousuario(novo_root)
        novo_root.mainloop()
#
# executável
if __name__ == "__main__":
    root = tk.Tk()
    Logins = Logins(root)
    root.mainloop()