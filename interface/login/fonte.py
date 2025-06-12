import tkinter as tk
from fonteDAO import FonteDAO
from PIL import Image, ImageTk
import webbrowser

class Fonte:
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
        tk.Label(scroll_frame, text="Fonte de Alimentação", font=("Arial", 16, "bold")).pack(pady=20)

        tk.Label(scroll_frame, text="Função:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(10, 2))
        tk.Label(scroll_frame, text="A fonte de um computador, também chamada de fonte de alimentação ou PSU (Power Supply Unit), é um componente crucial que fornece energia elétrica, ela ajusta a tensão e corrente para valores adequados aos componentes internos do PC, como a placa-mãe, o processador, o disco rígido, a placa de vídeo, entre outros.", font=("Arial", 12), wraplength=480, justify="left").pack(anchor="w", padx=10, pady=2)

        tk.Label(scroll_frame, text="Tipos:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(10, 2))
        tk.Label(scroll_frame, text="Atx: Fontes comuns em desktops, com conectores específicos para vários componentes.", font=("Arial", 12), wraplength=480, justify="left").pack(anchor="w", padx=10, pady=2)
        tk.Label(scroll_frame, text="Sfx: Fontes menores, ideais para gabinetes compactos.", font=("Arial", 12), wraplength=480, justify="left").pack(anchor="w", padx=10, pady=2)
        tk.Label(scroll_frame, text="Modulares: Permitem conectar apenas os cabos necessários, ajudando na organização.", font=("Arial", 12), wraplength=480, justify="left").pack(anchor="w", padx=10, pady=2)
        tk.Label(scroll_frame, text="Semi-Modulares: Têm alguns cabos fixos e outros que podem ser conectados conforme necessário.", font=("Arial", 12), wraplength=480, justify="left").pack(anchor="w", padx=10, pady=2)

        tk.Label(scroll_frame, text="Instalação:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(10, 2))
        tk.Label(scroll_frame, text="Com o espaço livre, posicione a nova fonte no compartimento correto do gabinete. Em gabinetes padrão, ela geralmente fica na parte superior ou inferior traseira. Alinhe os furos de fixação da fonte com os furos do gabinete e prenda-a firmemente usando os parafusos que vieram com a fonte. Com a fonte fixada, comece a conectar os cabos aos componentes.", font=("Arial", 12), wraplength=480, justify="left").pack(anchor="w", padx=10, pady=2)
        tk.Label(scroll_frame, text="Conecte o cabo principal (geralmente de 20 ou 24 pinos) à placa-mãe, certificando-se de que está bem encaixado. Em seguida, conecte o cabo de alimentação do processador (normalmente de 4 ou 8 pinos), que fica próximo ao processador. Se tiver uma placa de vídeo dedicada, ligue o(s) conector(es) PCIe, que geralmente possuem 6 ou 8 pinos. Conecte também os cabos SATA ou Molex aos dispositivos de armazenamento, como HDs e SSDs, além de outros periféricos que possam precisar de energia, como ventiladores.", font=("Arial", 12), wraplength=480, justify="left").pack(anchor="w", padx=10, pady=2)
        tk.Label(scroll_frame, text="Após conectar todos os cabos necessários, organize-os para melhorar o fluxo de ar dentro do gabinete. Muitos gabinetes possuem compartimentos específicos para roteamento de cabos na parte traseira, o que facilita essa organização. Use abraçadeiras ou presilhas para fixar os cabos e evitar que fiquem soltos. Depois de tudo conectado e organizado, coloque a tampa do gabinete de volta, parafuse-a e conecte o cabo de alimentação da fonte à tomada. Verifique se a chave seletora de voltagem da fonte está ajustada corretamente para a voltagem da sua região (110V ou 220V), caso a fonte não seja bivolt automática.", font=("Arial", 12), wraplength=480, justify="left").pack(anchor="w", padx=10, pady=2)

        # Caminho da imagem
        imagem_path = r"C:\xampp\htdocs\infobancodado\img\fonte.png"

        # Carrega a imagem e redimensiona se necessário
        imagem = Image.open(imagem_path)
        
        imagem = imagem.resize((200, 200), Image.Resampling.LANCZOS)  # redimensionar se desejar
        imagem_tk = ImageTk.PhotoImage(imagem)

        # Exibe a imagem
        label_imagem = tk.Label(scroll_frame, image=imagem_tk, background="#f0f0f0")
        label_imagem.image = imagem_tk  # manter referência para não ser coletada pelo garbage collector
        label_imagem.pack(pady=10)

        def abrir_video():
             webbrowser.open("https://youtu.be/81AA-Y5cXGY")

        botao_video = tk.Button(scroll_frame, text="▶️ Tutorial de Instalação", font=("Arial", 12, "bold"), command=abrir_video, bg="#dcd1e7")
        botao_video.pack(pady=10)
