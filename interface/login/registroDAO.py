import tkinter as tk
from tkinter import messagebox
import mysql.connector

class RegistroDAO:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "infohardware"
        )
        self.cursor = self.conexao.cursor()

    def adicionar(self, registro):
        sql = "INSERT INTO registro (nome, descricao) VALUES (%s, %s)"
        self.cursor.execute(sql, (registro.nome, registro.descricao))
        self.conexao.commit()
    
    def lista(self):
        self.cursor.execute("SELECT * FROM registro")
        return self.cursor.fetchall()
    
    def atualizar(self, registro):
        sql = "UPDATE registro SET nome = %s, descricao = %s WHERE id = %s"
        self.cursor.execute(sql, (registro.nome, registro.descricao, registro.id))
        self.conexao.commit()

    def deletar(self, id):
        sql = "DELETE FROM registro WHERE id = %s"
        self.cursor.execute(sql, (id,))
        self.conexao.commit()