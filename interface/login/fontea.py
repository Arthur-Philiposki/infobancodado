import tkinter as tk
from tkinter import messagebox
import mysql.connector

class Fontea:

    def __init__(self, id=None, nome="", descricao=""):
        self.id = id
        self.nome = nome
        self.descricao = descricao