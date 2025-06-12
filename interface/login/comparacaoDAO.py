import tkinter as tk
from tkinter import messagebox
import mysql.connector

class ComparacaoDAO:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "infohardware"
        )
        self.cursor = self.conexao.cursor()

    def adicionar(self, comparacaoa):
        sql = "INSERT INTO comparacaoa (nome, descricao) VALUES (%s, %s)"
        self.cursor.execute(sql, (comparacaoa.nome, comparacaoa.descricao))
        self.conexao.commit()
    
    def lista(self):
        self.cursor.execute("SELECT * FROM comparacaoa")
        return self.cursor.fetchall()
    
    def atualizar(self, comparacaoa):
        sql = "UPDATE comparacaoa SET nome = %s, descricao = %s WHERE id = %s"
        self.cursor.execute(sql, (comparacaoa.nome, comparacaoa.descricao, comparacaoa.id))
        self.conexao.commit()

    def deletar(self, id):
        sql = "DELETE FROM comparacaoa WHERE id = %s"
        self.cursor.execute(sql, (id,))
        self.conexao.commit()