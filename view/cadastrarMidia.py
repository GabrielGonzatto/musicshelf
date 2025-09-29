from tkinter import filedialog

import customtkinter as ctk
from PIL import Image

from model.midia import Midia
from service.arquivosService import ArquivosService, SessionLocal
from service.midiaService import MidiaService


class CadastrarMidia(ctk.CTkToplevel):
    caminho_imagem = None

    def __init__(self, master):
        super().__init__(master)

        self.title("MusicShelf")
        self.geometry("730x800")
        self.resizable(width=True, height=True)
        self.grab_set()

        self.session = SessionLocal()

        self.midia_service = MidiaService(self.session)
        self.arquivos_service = ArquivosService()


        self.iconbitmap("resources/assets/logoIco.ico")


        # Váriaveis de estilo
        background_color = "#323232"
        background_color_formulario = "#323232"

        height_formulario = 30
        corner_radius_formulario = 5

        font_titulo = ("Arial", 30)
        font_texto = ("Arial", 15)
        text_color = "#ffffff"

        # Main frame
        scrollable_frame_formulario = ctk.CTkScrollableFrame(master=self, fg_color=background_color)
        scrollable_frame_formulario.pack(side="top", fill="both", expand=True, padx=20, pady=20)



        # MusicShelf titulo
        frame_musicshelf_label = ctk.CTkFrame(master=scrollable_frame_formulario, fg_color="transparent")
        frame_musicshelf_label.pack(side="top", fill="x")

        musicshelf_label = ctk.CTkLabel(master=frame_musicshelf_label, text="Cadastrar da mídia", text_color=text_color, font=font_titulo)
        musicshelf_label.pack(side="left", padx=(20, 0), pady=(20, 0))



        # Frame formulário
        frame_campos_formulario = ctk.CTkFrame(master=scrollable_frame_formulario, fg_color="transparent")
        frame_campos_formulario.pack(side="top", fill="both", expand=True, padx=20)



        # Título mídia
        frame_titulo_midia = ctk.CTkFrame(master=frame_campos_formulario, fg_color="transparent")
        frame_titulo_midia.pack(side="top", fill="x", pady=10)

        frame_titulo_midia_label = ctk.CTkFrame(master=frame_titulo_midia, fg_color="transparent")
        frame_titulo_midia_label.pack(side="top", fill="x")

        titulo_midia_label = ctk.CTkLabel(master=frame_titulo_midia_label, text="Título", text_color=text_color, font=font_texto)
        titulo_midia_label.pack(side="left", padx=(5, 0))

        self.titulo_midia = ctk.CTkEntry(master=frame_titulo_midia, placeholder_text="Título da mídia", font=font_texto, text_color=text_color, height=height_formulario, fg_color=background_color_formulario, corner_radius=corner_radius_formulario)
        self.titulo_midia.pack(side="top", fill="x")



        # Artista/banda mídia
        frame_artista_midia  = ctk.CTkFrame(master=frame_campos_formulario, fg_color="transparent")
        frame_artista_midia.pack(side="top", fill="x", pady=(0,10))

        frame_artista_midia_label = ctk.CTkFrame(master=frame_artista_midia, fg_color="transparent")
        frame_artista_midia_label.pack(side="top", fill="x")

        artista_midia_label = ctk.CTkLabel(master=frame_artista_midia_label, text="Artista/banda", text_color=text_color, font=font_texto)
        artista_midia_label.pack(side="left", padx=(5,0))

        self.artista_midia = ctk.CTkEntry(master=frame_artista_midia, placeholder_text="Artista/banda da mídia", font=font_texto, text_color=text_color, height=height_formulario, fg_color=background_color_formulario, corner_radius=corner_radius_formulario)
        self.artista_midia.pack(side="top", fill="x")



        # Gênero, tipo e formato mídia
        frame_genero_tipo_formato_midia = ctk.CTkFrame(master=frame_campos_formulario, fg_color="transparent")
        frame_genero_tipo_formato_midia.pack(side="top", fill="x", pady=(0, 10))

        frame_genero_tipo_formato_midia.grid_columnconfigure(0, weight=1)
        frame_genero_tipo_formato_midia.grid_columnconfigure(1, weight=1)
        frame_genero_tipo_formato_midia.grid_columnconfigure(2, weight=1)

        # Gênero
        genero_midia_label = ctk.CTkLabel(master=frame_genero_tipo_formato_midia, text="Gênero", text_color=text_color, font=font_texto)
        genero_midia_label.grid(row=0, column=0, sticky="w", padx=(5, 0))

        self.genero_midia = ctk.CTkComboBox(master=frame_genero_tipo_formato_midia, state="readonly", values=self.arquivos_service.listar_generos(), font=font_texto, text_color=text_color, height=height_formulario, fg_color=background_color_formulario, corner_radius=corner_radius_formulario)
        self.genero_midia.set("")
        self.genero_midia.grid(row=1, column=0, sticky="ew")

        # Tipo
        tipo_midia_label = ctk.CTkLabel(master=frame_genero_tipo_formato_midia, text="Tipo", text_color=text_color, font=font_texto)
        tipo_midia_label.grid(row=0, column=1, sticky="w", padx=(15, 0))

        self.tipo_midia = ctk.CTkComboBox(master=frame_genero_tipo_formato_midia, state="readonly", values=self.arquivos_service.listar_tipos(), font=font_texto, text_color=text_color, height=height_formulario, fg_color=background_color_formulario, corner_radius=corner_radius_formulario)
        self.tipo_midia.set("")
        self.tipo_midia.grid(row=1, column=1, sticky="ew", padx=10)

        # Formato
        formato_midia_label = ctk.CTkLabel(master=frame_genero_tipo_formato_midia, text="Formato", text_color=text_color, font=font_texto)
        formato_midia_label.grid(row=0, column=2, sticky="w", padx=(5, 0))

        self.formato_midia = ctk.CTkComboBox(master=frame_genero_tipo_formato_midia, state="readonly", values=["CD", "Vinil"], font=font_texto, text_color=text_color, height=height_formulario, fg_color=background_color_formulario, corner_radius=corner_radius_formulario)
        self.formato_midia.set("")
        self.formato_midia.grid(row=1, column=2, sticky="ew")



        # Ano de lançamento e país mídia
        frame_ano_lancamento_pais_midia  = ctk.CTkFrame(master=frame_campos_formulario, fg_color="transparent")
        frame_ano_lancamento_pais_midia.pack(side="top", fill="x", pady=(0,10))

        frame_ano_lancamento_pais_midia.grid_columnconfigure(0, weight=1)
        frame_ano_lancamento_pais_midia.grid_columnconfigure(1, weight=1)

        # Ano de lançamento
        ano_lancamento_midia_label = ctk.CTkLabel(master=frame_ano_lancamento_pais_midia, text="Ano de lançamento", text_color=text_color, font=font_texto)
        ano_lancamento_midia_label.grid(row=0, column=0, sticky="w", padx=(5,0))

        self.ano_lancamento_midia = ctk.CTkEntry(master=frame_ano_lancamento_pais_midia, placeholder_text="Ano de lançamento da mídia", font=font_texto, text_color=text_color, height=height_formulario, fg_color=background_color_formulario, corner_radius=corner_radius_formulario)
        self.ano_lancamento_midia.grid(row=1, column=0, sticky="ew", padx=(0,5))

        # Páis
        pais_midia_label = ctk.CTkLabel(master=frame_ano_lancamento_pais_midia, text="País", text_color=text_color, font=font_texto)
        pais_midia_label.grid(row=0, column=1, sticky="w", padx=(10,0))

        self.pais_midia = ctk.CTkEntry(master=frame_ano_lancamento_pais_midia, placeholder_text="País de prensagem da mídia", font=font_texto, text_color=text_color, height=height_formulario, fg_color=background_color, corner_radius=corner_radius_formulario)
        self.pais_midia.grid(row=1, column=1, sticky="ew", padx=(5,0))



        # Forma de aquisição, valor e data de entrada mídia
        frame_forma_aquisicao_valor_data_entrada_midia  = ctk.CTkFrame(master=frame_campos_formulario, fg_color="transparent")
        frame_forma_aquisicao_valor_data_entrada_midia.pack(side="top", fill="x", pady=(0,10))

        frame_forma_aquisicao_valor_data_entrada_midia.grid_columnconfigure(0, weight=1)
        frame_forma_aquisicao_valor_data_entrada_midia.grid_columnconfigure(1, weight=1)
        frame_forma_aquisicao_valor_data_entrada_midia.grid_columnconfigure(2, weight=1)

        # Forma de aquisição
        forma_aquisicao_midia_label = ctk.CTkLabel(master=frame_forma_aquisicao_valor_data_entrada_midia, text="Forma de aquisição", text_color=text_color, font=font_texto)
        forma_aquisicao_midia_label.grid(row=0, column=0, sticky="w", padx=(5,0))

        self.forma_aquisicao_midia = ctk.CTkComboBox(master=frame_forma_aquisicao_valor_data_entrada_midia, state="readonly", values=["Compra", "Presente"], font=font_texto, text_color=text_color, height=height_formulario, fg_color=background_color_formulario, corner_radius=corner_radius_formulario)
        self.forma_aquisicao_midia.set("")
        self.forma_aquisicao_midia.grid(row=1, column=0, sticky="ew")

        # Valor
        valor_midia_label = ctk.CTkLabel(master=frame_forma_aquisicao_valor_data_entrada_midia, text="Valor", text_color=text_color, font=font_texto)
        valor_midia_label.grid(row=0, column=1, sticky="w", padx=(15,0))

        self.valor_midia = ctk.CTkEntry(master=frame_forma_aquisicao_valor_data_entrada_midia, placeholder_text="Valor da mídia", font=font_texto, text_color=text_color, height=height_formulario, fg_color=background_color_formulario, corner_radius=corner_radius_formulario)
        self.valor_midia.grid(row=1, column=1, sticky="ew", padx=10)

        # Data de entrada
        data_entrada_midia_label = ctk.CTkLabel(master=frame_forma_aquisicao_valor_data_entrada_midia, text="Data de entrada", text_color=text_color, font=font_texto)
        data_entrada_midia_label.grid(row=0, column=2, sticky="w", padx=(5,0))

        self.data_entrada_midia = ctk.CTkEntry(master=frame_forma_aquisicao_valor_data_entrada_midia, placeholder_text="Data de entrada da mídia", font=font_texto, text_color=text_color, height=height_formulario, fg_color=background_color_formulario, corner_radius=corner_radius_formulario)
        self.data_entrada_midia.grid(row=1, column=2, sticky="ew")



        # Conservação midia, encarte e geral mídia
        frame_conservacao_midia_encarte_geral_midia = ctk.CTkFrame(master=frame_campos_formulario, fg_color="transparent")
        frame_conservacao_midia_encarte_geral_midia.pack(side="top", fill="x", pady=(0, 10))

        frame_conservacao_midia_encarte_geral_midia.grid_columnconfigure(0, weight=1)
        frame_conservacao_midia_encarte_geral_midia.grid_columnconfigure(1, weight=1)
        frame_conservacao_midia_encarte_geral_midia.grid_columnconfigure(2, weight=1)

        siglas_conservacao = ["M", "NM", "VG+", "VG", "G", "F", "P"]

        # Conservação mídia
        conservacao_midia_midia_label = ctk.CTkLabel(master=frame_conservacao_midia_encarte_geral_midia, text="Conservação da mídia", text_color=text_color, font=font_texto)
        conservacao_midia_midia_label.grid(row=0, column=0, sticky="w", padx=(5, 0))

        self.conservacao_midia_midia = ctk.CTkComboBox(master=frame_conservacao_midia_encarte_geral_midia, state="readonly", values=siglas_conservacao, font=font_texto, text_color=text_color, height=height_formulario, fg_color=background_color_formulario, corner_radius=corner_radius_formulario)
        self.conservacao_midia_midia.set("")
        self.conservacao_midia_midia.grid(row=1, column=0, sticky="ew")

        # Conservação encarte
        conservacao_encarte_midia_label = ctk.CTkLabel(master=frame_conservacao_midia_encarte_geral_midia, text="Conservação encarte", text_color=text_color, font=font_texto)
        conservacao_encarte_midia_label.grid(row=0, column=1, sticky="w", padx=(15, 0))

        self.conservacao_encarte_midia = ctk.CTkComboBox(master=frame_conservacao_midia_encarte_geral_midia, state="readonly", values=siglas_conservacao, font=font_texto, text_color=text_color, height=height_formulario, fg_color=background_color_formulario, corner_radius=corner_radius_formulario)
        self.conservacao_encarte_midia.set("")
        self.conservacao_encarte_midia.grid(row=1, column=1, sticky="ew", padx=10)

        # Conservação geral
        conservacao_geral_midia_label = ctk.CTkLabel(master=frame_conservacao_midia_encarte_geral_midia, text="Conservação geral", text_color=text_color, font=font_texto)
        conservacao_geral_midia_label.grid(row=0, column=2, sticky="w", padx=(5, 0))

        self.conservacao_geral_midia = ctk.CTkComboBox(master=frame_conservacao_midia_encarte_geral_midia, state="readonly", values=siglas_conservacao, font=font_texto, text_color=text_color, height=height_formulario, fg_color=background_color_formulario, corner_radius=corner_radius_formulario)
        self.conservacao_geral_midia.set("")
        self.conservacao_geral_midia.grid(row=1, column=2, sticky="ew")



        # Descrição mídia
        frame_descricao_midia  = ctk.CTkFrame(master=frame_campos_formulario, fg_color="transparent")
        frame_descricao_midia.pack(side="top", fill="x", pady=(0,10))

        frame_descricao_midia_label = ctk.CTkFrame(master=frame_descricao_midia, fg_color="transparent")
        frame_descricao_midia_label.pack(side="top", fill="x")

        descricao_midia_label = ctk.CTkLabel(master=frame_descricao_midia_label, text="Descrição", text_color=text_color, font=font_texto)
        descricao_midia_label.pack(side="left", padx=(5,0))

        self.descricao_midia = ctk.CTkEntry(master=frame_descricao_midia, placeholder_text="Descrição da mídia", font=font_texto, text_color=text_color, height=60, fg_color=background_color_formulario, corner_radius=corner_radius_formulario)
        self.descricao_midia.pack(side="top", fill="x")



        # Imagem mídia
        frame_imagem_botao_selecionar_imagem_midia = ctk.CTkFrame(master=frame_campos_formulario, fg_color="transparent")
        frame_imagem_botao_selecionar_imagem_midia.pack(side="top", fill="x")

        frame_imagem_midia = ctk.CTkFrame(master=frame_imagem_botao_selecionar_imagem_midia, fg_color="transparent", width=100, height=100)
        frame_imagem_midia.pack(side="left")

        self.preview_imagem_midia = ctk.CTkLabel(master=frame_imagem_midia, image=self.arquivos_service.carregar_imagem("assets/imageNotFound.png"), text="", width=100, height=100)
        self.preview_imagem_midia.pack(side="left")

        frame_botao_selecionar_imagem_midia = ctk.CTkFrame(master=frame_imagem_botao_selecionar_imagem_midia, fg_color="transparent")
        frame_botao_selecionar_imagem_midia.pack(side="left", fill="x", expand=True)

        botao_selecionar_imagem_midia = ctk.CTkButton(master=frame_botao_selecionar_imagem_midia, text="Selecionar imagem da capa",  command=self.selecionar_imagem, fg_color="#505050", hover_color="#646464", font=font_texto, text_color=text_color, height=40, corner_radius=corner_radius_formulario)
        botao_selecionar_imagem_midia.pack(side="left", fill="x", expand=True, padx=10)

        # Status e cadastro
        self.status_label = ctk.CTkLabel(master=frame_campos_formulario, text_color=text_color, text="", font=("arial", 25))
        self.status_label.pack(side="top", fill="x", pady=(0,10))

        botao_cadastrar = ctk.CTkButton(master=frame_campos_formulario, text="Cadastrar", command=self.cadastrar_midia, fg_color="#505050", hover_color="#646464", font=font_texto, text_color=text_color, height=40, corner_radius=corner_radius_formulario)
        botao_cadastrar.pack(fill="x", expand=True, padx=10)


    # Funções
    def cadastrar_midia(self):
        self.status_label.configure(text="")

        try:
            midia = Midia().validar(
                titulo=self.titulo_midia.get().strip(),
                artista=self.artista_midia.get().strip(),
                genero=self.genero_midia.get(),
                tipo=self.tipo_midia.get(),
                formato=self.formato_midia.get(),
                pais=self.pais_midia.get().strip(),
                forma_aquisicao=self.forma_aquisicao_midia.get(),
                conservacao_geral=self.conservacao_geral_midia.get(),
                conservacao_encarte=self.conservacao_encarte_midia.get(),
                conservacao_midia=self.conservacao_midia_midia.get(),
                descricao=self.descricao_midia.get().strip(),
                caminho_imagem=self.caminho_imagem,
                ano_lancamento_base=self.ano_lancamento_midia.get().strip(),
                data_entrada_base=self.data_entrada_midia.get(),
                valor_base=self.valor_midia.get(),
            )
            self.midia_service.cadastrar_midia(midia, self.master)

            self.status_label.configure(text="Mídia cadastrada com sucesso!", text_color="green")
            self.destroy()

        except ValueError as e:
            self.status_label.configure(text=e, text_color="red")
        except Exception as e:
            self.status_label.configure(text=e, text_color="red")

    def selecionar_imagem(self):
        self.caminho_imagem = filedialog.askopenfilename(
            title="Selecione uma imagem",
            filetypes=[("Arquivos de Imagem", "*.png *.jpg *.jpeg *.webp"), ("Todos os arquivos", "*.*")]
        )

        if self.caminho_imagem:
            self.preview_imagem_midia.configure(image=ctk.CTkImage(Image.open(self.caminho_imagem), size=(100, 100)), text="")







