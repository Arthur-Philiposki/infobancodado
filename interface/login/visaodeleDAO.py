import tkinter as tk
from tkinter import messagebox
import mysql.connector

class VisaodeleDAO:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "infohardware"
        )
        self.cursor = self.conexao.cursor()

    def adicionar(self, visaodele):
        sql = "INSERT INTO visaodele (nome, descricao) VALUES (%s, %s)"
        self.cursor.execute(sql, (visaodele.nome, visaodele.descricao))
        self.conexao.commit()
    
    def lista(self):
        self.cursor.execute("SELECT * FROM visaodele")
        return self.cursor.fetchall()
    
    def atualizar(self, visaodele):
        sql = "UPDATE visaodele SET nome = %s, descricao = %s WHERE id = %s"
        self.cursor.execute(sql, (visaodele.nome, visaodele.descricao, visaodele.id))
        self.conexao.commit()

    def deletar(self, id):
        sql = "DELETE FROM visaodele WHERE id = %s"
        self.cursor.execute(sql, (id,))
        self.conexao.commit()