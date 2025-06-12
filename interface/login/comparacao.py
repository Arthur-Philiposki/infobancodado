import tkinter as tk
from fonteDAO import FonteDAO
from PIL import Image, ImageTk
import webbrowser

class Comparacao:
    def __init__(self, root):
        self.dao = FonteDAO()
        self.root = root      # q inicia o projeto python
        self.root.title("Fonte de Alimentação")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")



        canvas_ss = tk.Canvas(self.root, borderwidth=0, background="#f0f0f0")
        scrollbar_ss = tk.Scrollbar(self.root, orient="vertical", command=canvas_ss.yview)
        scroll_frame = tk.Frame(canvas_ss, background="#f0f0f0")

        scroll_frame.bind(
    "<Configure>",
    lambda e: canvas_ss.configure(
        scrollregion=canvas_ss.bbox("all")
    )
)

        canvas_ss.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas_ss.configure(yscrollcommand=scrollbar_ss.set)

        # Ativar scroll do mouse
        def _on_mousewheel(event):
            canvas_ss.yview_scroll(int(-1 * (event.delta / 120)), "units")

        def _on_mousewheel_linux(event):
            canvas_ss.yview_scroll(int(-1 * event.delta), "units")

        # Windows e MacOS
        canvas_ss.bind_all("<MouseWheel>", _on_mousewheel)
        # Linux (eventos de rolagem são diferentes)
        canvas_ss.bind_all("<Button-4>", lambda e: canvas_ss.yview_scroll(-1, "units"))
        canvas_ss.bind_all("<Button-5>", lambda e: canvas_ss.yview_scroll(1, "units"))

        canvas_ss.pack(side="left", fill="both", expand=True)
        scrollbar_ss.pack(side="right", fill="y")

        # Adiciona os widgets ao scroll_frame
        tk.Label(scroll_frame, text="Comparação das duas peças:", font=("Arial", 16, "bold"), anchor="center", justify="center").pack(pady=20)


        imagens_frame = tk.Frame(scroll_frame, bg="#f0f0f0")
        imagens_frame.pack(pady=10)


        # Primeira imagem
        imagem_path1 = r"C:\xampp\htdocs\infobancodado\img\Core.png"
        imagem1 = Image.open(imagem_path1)
        imagem1 = imagem1.resize((200, 300), Image.Resampling.LANCZOS)
        imagem_tk1 = ImageTk.PhotoImage(imagem1)

        label_imagem1 = tk.Label(imagens_frame, image=imagem_tk1, background="#f0f0f0")
        label_imagem1.image = imagem_tk1
        label_imagem1.pack(side="left", padx=10)

        # Segunda imagem
        imagem_path2 = r"C:\xampp\htdocs\infobancodado\img\ryzen.png"
        imagem2 = Image.open(imagem_path2)
        imagem2 = imagem2.resize((200, 300), Image.Resampling.LANCZOS)
        imagem_tk2 = ImageTk.PhotoImage(imagem2)

        label_imagem2 = tk.Label(imagens_frame, image=imagem_tk2, background="#f0f0f0")
        label_imagem2.image = imagem_tk2
        label_imagem2.pack(side="left", padx=10)
