import tkinter as tk
from tkinter import messagebox
import mysql.connector

class LoginDAO:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "infohardware"
        )
        self.cursor = self.conexao.cursor()

    def adicionar(self, login):
        sql = "INSERT INTO login (email, senha) VALUES (%s, %s)"
        self.cursor.execute(sql, (login.email, login.senha))
        self.conexao.commit()
    
    def lista(self):
        self.cursor.execute("SELECT * FROM login")
        return self.cursor.fetchall()
    
    def atualizar(self, login):
        sql = "UPDATE login SET email = %s, senha = %s WHERE id = %s"
        self.cursor.execute(sql, (login.email, login.senha, login.id))
        self.conexao.commit()

    def deletar(self, id):
        sql = "DELETE FROM login WHERE id = %s"
        self.cursor.execute(sql, (id,))
        self.conexao.commit()