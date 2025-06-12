import tkinter as tk
from tkinter import messagebox
import mysql.connector

class FonteDAO:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "infohardware"
        )
        self.cursor = self.conexao.cursor()

    def adicionar(self, fontea):
        sql = "INSERT INTO fontea (nome, descricao) VALUES (%s, %s)"
        self.cursor.execute(sql, (fontea.nome, fontea.descricao))
        self.conexao.commit()
    
    def lista(self):
        self.cursor.execute("SELECT * FROM fontea")
        return self.cursor.fetchall()
    
    def atualizar(self, fontea):
        sql = "UPDATE fontea SET nome = %s, descricao = %s WHERE id = %s"
        self.cursor.execute(sql, (fontea.nome, fontea.descricao, fontea.id))
        self.conexao.commit()

    def deletar(self, id):
        sql = "DELETE FROM fontea WHERE id = %s"
        self.cursor.execute(sql, (id,))
        self.conexao.commit()