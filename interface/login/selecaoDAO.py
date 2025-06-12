import tkinter as tk
from tkinter import messagebox
import mysql.connector

class SelecaoDAO:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "infohardware"
        )
        self.cursor = self.conexao.cursor()

    def adicionar(self, selecaoa):
        sql = "INSERT INTO selecaoa (nome, descricao) VALUES (%s, %s)"
        self.cursor.execute(sql, (selecaoa.nome, selecaoa.descricao))
        self.conexao.commit()
    
    def lista(self):
        self.cursor.execute("SELECT * FROM selecaoa")
        return self.cursor.fetchall()
    
    def atualizar(self, selecaoa):
        sql = "UPDATE selecaoa SET nome = %s, descricao = %s WHERE id = %s"
        self.cursor.execute(sql, (selecaoa.nome, selecaoa.descricao, selecaoa.id))
        self.conexao.commit()

    def deletar(self, id):
        sql = "DELETE FROM selecaoa WHERE id = %s"
        self.cursor.execute(sql, (id,))
        self.conexao.commit()