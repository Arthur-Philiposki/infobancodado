import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from visaodeleDAO import VisaodeleDAO
from PIL import Image, ImageTk




class Visaousuario:
    def __init__(self, root):
        self.dao = VisaodeleDAO()
        self.root = root      # q inicia o projeto python
        self.root.title("INFOHARDWARE")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")

        # Criar o Notebook (abas)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)

        # Criar as páginas (abas)
        self.page1 = tk.Frame(self.notebook)
        self.page2 = tk.Frame(self.notebook)
        self.page3 = tk.Frame(self.notebook)
        self.page4 = tk.Frame(self.notebook)
        self.page5 = tk.Frame(self.notebook)
        self.page6 = tk.Frame(self.notebook)
        self.page7 = tk.Frame(self.notebook)

        # Adicionar as páginas ao notebook
        self.notebook.add(self.page1, text='Home')
        self.notebook.add(self.page2, text='Peças')
        self.notebook.add(self.page3, text='Comparação')
        self.notebook.add(self.page4, text='Criação PC')
        self.notebook.add(self.page5, text='Sobre o Site')
        self.notebook.add(self.page6, text='Quanto a Nós')
        self.notebook.add(self.page7, text='Serviços')

        # Adicionar conteúdo à HOME
        frame_horizontal = tk.Frame(self.page1)
        frame_horizontal.pack(pady=10)

        self.label1 = tk.Label(self.page1, text="Peças, Montagem e muito mais, sem limites!", font=("Arial", 16, "bold"))
        self.label1.pack(pady=20)

        # campo de entrada
        self.entry = tk.Entry(self.page1, font=("Arial", 12))
        self.entry.pack(pady=10)

        # Botão
        self.button1 = tk.Button(self.page1, text="Buscar", command=self.show_message1)
        self.button1.pack(pady=10)

#------------------------------------------------------------------------------------------------------------

        # Adicionar conteúdo à PEÇAS


        canvas_ss = tk.Canvas(self.page2, borderwidth=0, background="#f0f0f0")
        scrollbar_ss = tk.Scrollbar(self.page2, orient="vertical", command=canvas_ss.yview)
        scroll_frame = tk.Frame(canvas_ss, background="#f0f0f0")

        # Atualiza área de rolagem
        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas_ss.configure(scrollregion=canvas_ss.bbox("all"))
        )

        canvas_ss.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas_ss.configure(yscrollcommand=scrollbar_ss.set)

        # Scroll do mouse (Windows/macOS/Linux)
        canvas_ss.bind_all("<MouseWheel>", lambda e: canvas_ss.yview_scroll(int(-1 * (e.delta / 120)), "units"))
        canvas_ss.bind_all("<Button-4>", lambda e: canvas_ss.yview_scroll(-1, "units"))  # Linux
        canvas_ss.bind_all("<Button-5>", lambda e: canvas_ss.yview_scroll(1, "units"))   # Linux

        canvas_ss.pack(side="left", fill="both", expand=True)
        scrollbar_ss.pack(side="right", fill="y")

        # CONTEÚDO na scroll_frame
        label_p1 = tk.Label(scroll_frame,
            text="Aqui, você poderá visualizar informações de componentes que compõem o computador.", font=("Arial", 12, "bold"),
            wraplength=480,
            justify="center",
            bg="#f0f0f0"
        )
        label_p1.pack(pady=20)

        frame_pecas = tk.Frame(scroll_frame, bg="#1e1e1e", bd=10, relief="groove")
        frame_pecas.pack(pady=20)

        label_titulo = tk.Label(frame_pecas, text="Qual a Peça?", font=("Arial", 14, "bold"),
                                fg="#f0f0f0", bg="#1e1e1e")
        label_titulo.pack(pady=5)

        botoes_pecas = [
            "Placa de Video", "Placa-Mãe", "Processador", "Memoria RAM",
            "Armazenamento", "Fonte de Alimentação", "Cooler", "Gabinete"
        ]

        for texto in botoes_pecas:
            if texto == "Fonte de Alimentação":
                btn = tk.Button(frame_pecas, text=texto, font=("Arial", 10, "bold"), width=20, command=self.abrir_fonte)
            else:
                btn = tk.Button(frame_pecas, text=texto, font=("Arial", 10, "bold"), width=20)
            btn.pack(pady=2)

        


#------------------------------------------------------------------------------------------------------------

        # Adicionar conteúdo à COMPARACAO


        frame_comparacao = tk.Frame(self.page3, bg="#f0f0f0")
        frame_comparacao.pack(fill="both", expand=True)

        tk.Label(frame_comparacao, text="Selecione qual peça quer fazer a comparação.", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=20)

        frame_selecao = tk.Frame(frame_comparacao, bg="#1e1e1e", bd=10, relief="groove")
        frame_selecao.pack(pady=20)

        botoes_selecao = ["Placa de Video", "Processador"]

        for texto in botoes_selecao:
            if texto == "Processador":
                btn = tk.Button(frame_selecao, text=texto, font=("Arial", 10, "bold"), width=20, command=self.abrir_selecao)
            else:
                btn = tk.Button(frame_selecao, text=texto, font=("Arial", 10, "bold"), width=20)
            btn.pack(pady=2)

#------------------------------------------------------------------------------------------------------------

        # Adicionar conteúdo à CRIACAO PC
        self.label2 = tk.Label(self.page4, text="Bem-vindo à CRIACAO PC!", font=("Arial", 16))
        self.label2.pack(pady=20)

        self.button2 = tk.Button(self.page4, text="Mostrar Mensagem", command=self.show_message2)
        self.button2.pack(pady=10)

#------------------------------------------------------------------------------------------------------------

        # Adicionar conteúdo à SOBRE SITE

        canvas_ss = tk.Canvas(self.page5, borderwidth=0, background="#f0f0f0")
        scrollbar_ss = tk.Scrollbar(self.page5, orient="vertical", command=canvas_ss.yview)
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
        tk.Label(scroll_frame, text="Sobre a Infohardware", font=("Arial", 16, "bold")).pack(pady=20)

        tk.Label(scroll_frame, text="Missão:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(10, 2))
        tk.Label(scroll_frame, text="Proporcionar conhecimento acessível e prático sobre hardware e montagem de computadores, capacitando os usuários a solucionarem problemas e montarem computadores com excelência.", font=("Arial", 12), wraplength=480, justify="left").pack(anchor="w", padx=10, pady=2)

        tk.Label(scroll_frame, text="Visão:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(10, 2))
        tk.Label(scroll_frame, text="Ser a referência nacional em educação de hardware, capacitando pessoas a entenderem e dominarem a área de montagem de PCs.", font=("Arial", 12), wraplength=480, justify="left").pack(anchor="w", padx=10, pady=2)

        tk.Label(scroll_frame, text="Valores:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(10, 2))
        tk.Label(scroll_frame, text="Capacitar os usuários a compreenderem a área de hardware, de maneira simples e compreensiva, possibilitando-os a realizarem seus objetivos em relação a montagem de computadores.", font=("Arial", 12), wraplength=480, justify="left").pack(anchor="w", padx=10, pady=2)

        tk.Label(scroll_frame, text="Objetivos:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(10, 2))
        tk.Label(scroll_frame, text="Temos como objetivo a transmissão do conhecimento de maneira simples e educativa, com o intuito de resolver a dor de usuários que possuem receio de montarem seus próprios computadores por falta de conhecimento. Nosso foco é quebrar tais barreiras através do conhecimento, proporcionando ao usuário um aprendizado de qualidade e maestria.", font=("Arial", 12), wraplength=480, justify="left").pack(anchor="w", padx=10, pady=2)

        tk.Label(scroll_frame, text="Segmentos:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(10, 2))
        tk.Label(scroll_frame, text="Segmento: Edtech.", font=("Arial", 12), wraplength=480, justify="left").pack(anchor="w", padx=10, pady=2)

        tk.Label(scroll_frame, text="Significado das cores:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(10, 2))
        tk.Label(scroll_frame, text="Roxo: essa cor está intimamente relacionada à sabedoria, independência e criatividade...", font=("Arial", 12), wraplength=480, justify="left").pack(anchor="w", padx=10, pady=2)
        tk.Label(scroll_frame, text="Preto: O preto é a cor mais poderosa e neutra. Tende a ser associada à elegância e força...", font=("Arial", 12), wraplength=480, justify="left").pack(anchor="w", padx=10, pady=2)
        tk.Label(scroll_frame, text="Branco: Significa paz e pureza.", font=("Arial", 12), wraplength=480, justify="left").pack(anchor="w", padx=10, pady=2)

        tk.Label(scroll_frame, text="Logo para aplicativo:", font=("Arial", 16, "bold")).pack(pady=20)

        # Caminho da imagem
        imagem_path = r"C:\xampp\htdocs\infobancodado\img\LogoM.png"

        # Carrega a imagem e redimensiona se necessário
        imagem = Image.open(imagem_path)
        
        imagem = imagem.resize((200, 200), Image.Resampling.LANCZOS)  # redimensionar se desejar
        imagem_tk = ImageTk.PhotoImage(imagem)

        # Exibe a imagem
        label_imagem = tk.Label(scroll_frame, image=imagem_tk, background="#f0f0f0")
        label_imagem.image = imagem_tk  # manter referência para não ser coletada pelo garbage collector
        label_imagem.pack(pady=10)

        tk.Label(scroll_frame, text="Logo para site:", font=("Arial", 16, "bold")).pack(pady=20)

        imagem_path = r"C:\xampp\htdocs\infobancodado\img\Info.png"


        imagem = Image.open(imagem_path)
        
        imagem = imagem.resize((300, 50), Image.Resampling.LANCZOS)
        imagem_tk = ImageTk.PhotoImage(imagem)

        label_imagem = tk.Label(scroll_frame, image=imagem_tk, background="#f0f0f0")
        label_imagem.image = imagem_tk  
        label_imagem.pack(pady=10)

#------------------------------------------------------------------------------------------------------------

        # Adicionar conteúdo à QUANTO NOS
        self.label6 = tk.Label(self.page6, text="Composto Por:", font=("Arial", 16, "bold"))
        self.label6.pack(pady=20)

        self.label1 = tk.Label(self.page6, text="Quem sou?", font=("Arial", 12, "bold"))
        self.label1.pack(anchor="w", padx=10, pady=(10, 2))
        self.label2 = tk.Label(self.page6, text="Meu nome é Arthur Gabriel Philiposki Agner. (Idealizador, designer, desenvolvedor)", font=("Arial", 12))
        self.label2.pack(anchor="w", padx=10, pady=2)

        self.label3 = tk.Label(self.page6, text="Trabalho", font=("Arial", 12, "bold"))
        self.label3.pack(anchor="w", padx=10, pady=(10, 2))
        self.label4 = tk.Label(self.page6, text="Projeto desenvolvido para a disciplina de Startup Model Intermediante da Faculdade Senac - Ponta Grossa ;)", font=("Arial", 12), wraplength=480, justify="left")
        self.label4.pack(anchor="w", padx=10, pady=2)

#------------------------------------------------------------------------------------------------------------

        # Adicionar conteúdo à SERVICOS
        self.label_s1 = tk.Label(self.page7, text="Serviços", font=("Arial", 16, "bold"))
        self.label_s1.pack(pady=20)

        self.label_s2 = tk.Label(self.page7, text="O que o Site Oferece:", font=("Arial", 12, "bold"))
        self.label_s2.pack(anchor="w", padx=10, pady=(10, 2))

        self.label_s3 = tk.Label(self.page7, text="A Infohardware desempenha funções como vídeos, textos didáticos, comparação de peças e criação de PC.",font=("Arial", 12),
            wraplength=480,
            justify="left"
        )
        self.label_s3.pack(anchor="w", padx=10, pady=2)

#------------------------------------------------------------------------------------------------------------

    # Função para mostrar mensagem na HOME
    def show_message1(self):
        messagebox.showinfo("HOME", "Realizou Busca")

    # Função para mostrar mensagem na PEÇAS
    def show_message2(self):
        messagebox.showinfo("PEÇAS", "Você clicou no botão da PEÇAS")

    # Função para mostrar mensagem na COMPARACAO
    def show_message3(self):
        messagebox.showinfo("COMPARACAO", "Você clicou no botão da COMPARACAO")

    # Função para mostrar mensagem na CRIACAO PC
    def show_message4(self):
        messagebox.showinfo("CRIACAO PC", "Você clicou no botão da CRIACAO PC")

    




    def abrir_fonte(self):
        import fonte
        nova_janela = tk.Toplevel(self.root)
        fonte.Fonte(nova_janela)
    
    def abrir_selecao(self):
        import selecao
        nova_janela = tk.Toplevel(self.root)
        selecao.Selecao(nova_janela)



#executavel
if __name__=="__main__":
    root = tk.Tk()
    visaousuario = Visaousuario(root)
    root.mainloop()