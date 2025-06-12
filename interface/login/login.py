import tkinter as tk
from tkinter import messagebox
import mysql.connector

class Login:

    def __init__(self, id=None, email="", senha=""):
        self.id = id
        self.email = email
        self.senha = senha
        