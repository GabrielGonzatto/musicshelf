import customtkinter as ctk

from service.arquivosService import ArquivosService, SessionLocal
from service.midiaService import MidiaService
from .cadastrarMidia import CadastrarMidia
from .detalhesMidia import DetalhesMidia

class App(ctk.CTk):
    midias = None

    def __init__(self):
        super().__init__()

        self.title("MusicShelf")
        self.geometry("940x600")
        self.resizable(width=True, height=True)



        self.session = SessionLocal()

        self.midia_service = MidiaService(self.session)
        self.arquivos_service = ArquivosService()

        self.midias = self.midia_service.listar_midias_com_filtro_ordem()

        self.iconbitmap("resources/assets/logoIco.ico")

        # Váriaveis de estilo
        background_color = "#323232"
        background_color_formulario = "#323232"
        background_color_botao = "#505050"
        hover_background_color_botao = "#646464"

        corner_radius_formulario = 5
        corner_radius_botao = 20

        font_titulo = ("Arial", 30)
        font_subtitulo = ("Arial", 23)
        font_texto = ("Arial", 15)
        text_color = "#ffffff"



        # Navbar
        frame_navbar = ctk.CTkFrame(master=self, fg_color="transparent")
        frame_navbar.pack(side="top", fill="x", padx=20, pady=20)

        frame_titulo_label = ctk.CTkFrame(master=frame_navbar, fg_color="transparent")
        frame_titulo_label.pack(side="left")

        titulo = ctk.CTkLabel(master=frame_titulo_label, text_color=text_color, text="MusicShelf", font=font_titulo)
        titulo.pack()

        frame_pesquisa = ctk.CTkFrame(master=frame_navbar, fg_color="transparent")
        frame_pesquisa.pack(fill="x")
        frame_pesquisa.grid_columnconfigure(0, weight=1)

        self.pesquisa = ctk.CTkEntry(master=frame_pesquisa, placeholder_text="Pesquisar por músicas...", font=font_texto, fg_color=background_color_formulario, text_color=text_color, height=40, corner_radius=20)
        self.pesquisa.grid(row=0, column=0, sticky="ew", padx=(100, 10))

        botao_pesquisar = ctk.CTkButton(master=frame_pesquisa, image=self.arquivos_service.carregar_imagem("resources/assets/search.png", (20,20)), text="", hover_color="#646464", fg_color="#505050", corner_radius=20, height=40, width=40, command=self.listar_midias_por_pesquisa)
        botao_pesquisar.grid(row=0, column=1)



        # Filtro e ordenação
        frame_filtro_ordem = ctk.CTkFrame(master=self, fg_color=background_color)
        frame_filtro_ordem.pack(side="top", fill="x", padx=20)

        # Header
        frame_header_filtro_ordem = ctk.CTkFrame(master=frame_filtro_ordem, fg_color="transparent")
        frame_header_filtro_ordem.pack(side="top", fill="x", pady=(15,0))

        filtro_ordem_label = ctk.CTkLabel(master=frame_header_filtro_ordem, text="Filtragem e ordenação", text_color=text_color, font=font_subtitulo)
        filtro_ordem_label.pack(side="left", padx=(10, 0))

        botao_filtrar_ordenar = ctk.CTkButton(master=frame_header_filtro_ordem, text="Filtrar e ordenar", command=self.filtrar_ordenar_midias, fg_color=background_color_botao, hover_color=hover_background_color_botao, font=font_texto, text_color=text_color, height=30, corner_radius=corner_radius_botao)
        botao_filtrar_ordenar.pack(side="right", fill="x", padx=10)

        botao_limpar_filtros = ctk.CTkButton(master=frame_header_filtro_ordem, text="Limpar filtros", command=self.limpar_filtros, fg_color=background_color_botao, hover_color=hover_background_color_botao, font=font_texto, text_color=text_color, height=30, corner_radius=corner_radius_botao)
        botao_limpar_filtros.pack(side="right", fill="x", padx=10)

        # Body
        frame_body_filtro_ordem = ctk.CTkFrame(master=frame_filtro_ordem, fg_color="transparent")
        frame_body_filtro_ordem.pack(side="top", fill="x", pady=(30, 20))

        self.filtro_genero = ctk.CTkComboBox(frame_body_filtro_ordem, values=self.midia_service.listar_generos_no_banco(), corner_radius=corner_radius_formulario, state="readonly")
        self.filtro_genero.pack(side="left", padx=10)
        self.filtro_genero.set("Gênero")

        self.filtro_formato = ctk.CTkComboBox(frame_body_filtro_ordem, values=["CD", "Vinil"], corner_radius=corner_radius_formulario, state="readonly")
        self.filtro_formato.pack(side="left", padx=10)
        self.filtro_formato.set("Formato")

        self.filtro_tipo = ctk.CTkComboBox(frame_body_filtro_ordem, values=self.arquivos_service.listar_tipos(), corner_radius=corner_radius_formulario, state="readonly")
        self.filtro_tipo.pack(side="left", padx=10)
        self.filtro_tipo.set("Tipo")

        self.ordem_tipo = ctk.CTkComboBox(frame_body_filtro_ordem, values=["Ano de lançamento", "Data de entrada", "Título", "Valor"], corner_radius=corner_radius_formulario, state="readonly")
        self.ordem_tipo.pack(side="left", padx=10)
        self.ordem_tipo.set("Ordenar por")

        self.ordem = ctk.CTkComboBox(frame_body_filtro_ordem, values=["Crescente", "Decrescente"], corner_radius=corner_radius_formulario, state="readonly")
        self.ordem.pack(side="left", padx=10)
        self.ordem.set("Ordem")



        # Listagem e métricas mídias
        frame_listagem_metricas = ctk.CTkFrame(master=self, fg_color="transparent")
        frame_listagem_metricas.pack(side="top", fill="both", expand=True, padx=20, pady=20)



        # listagem mídias
        frame_listagem_midias = ctk.CTkFrame(master=frame_listagem_metricas, fg_color=background_color)
        frame_listagem_midias.pack(side="left", fill="both", expand=True, padx=(0,5))

        frame_header_listagem_midias = ctk.CTkFrame(master=frame_listagem_midias, fg_color="transparent")
        frame_header_listagem_midias.pack(side="top", fill="x")

        self.midias_label = ctk.CTkLabel(master=frame_header_listagem_midias, text="Mídias", font=font_subtitulo, text_color=text_color, fg_color="transparent")
        self.midias_label.pack(side="left", padx=10, pady=(10, 0))


        botao_cadastro = ctk.CTkButton(master=frame_header_listagem_midias, text="Cadastrar mídia", height=35, hover_color=hover_background_color_botao, fg_color=background_color_botao, text_color=text_color, corner_radius=corner_radius_botao, font=font_texto, command=self.abrir_janela_cadastro_midia)
        botao_cadastro.pack(side="right", padx=(20,0), pady=(10, 0))

        botao_exportacao = ctk.CTkButton(master=frame_header_listagem_midias, text="Exportar coleção", height=35, hover_color=hover_background_color_botao, fg_color=background_color_botao, text_color=text_color, corner_radius=corner_radius_botao, font=font_texto, command=self.midia_service.exportar_para_excel)
        botao_exportacao.pack(side="right", pady=(10, 0))

        self.scrollable_frame_midias = ctk.CTkScrollableFrame(master=frame_listagem_midias, fg_color="transparent")
        self.scrollable_frame_midias.pack(side="top", fill="both", expand=True, padx=20)

        self.listar_midias()



        # Métricas
        frame_metricas = ctk.CTkFrame(master=frame_listagem_metricas, fg_color=background_color, width=270)
        frame_metricas.pack(side="left", fill="y", padx=(5,0))
        frame_metricas.pack_propagate(False)

        frame_metricas_subtitulo_label = ctk.CTkFrame(master=frame_metricas, fg_color="transparent")
        frame_metricas_subtitulo_label.pack(side="top", fill="x")

        metricas_label = ctk.CTkLabel(master=frame_metricas_subtitulo_label, text="Métricas", text_color=text_color, font=font_subtitulo)
        metricas_label.pack(side="left", fill="x", pady=(10,0), padx=(10,0))

        # Métricas fixas
        frame_metricas_fixas = ctk.CTkFrame(master=frame_metricas, fg_color="transparent")
        frame_metricas_fixas.pack(side="top", fill="x")

        frame_metricas_texto_midias_label = ctk.CTkFrame(master=frame_metricas_fixas, fg_color="transparent")
        frame_metricas_texto_midias_label.pack(side="top", fill="x")

        metricas_midias_label = ctk.CTkLabel(master=frame_metricas_texto_midias_label, text=f"{self.midia_service.quantidade_de_midias()} Mídias - R$ {self.midia_service.valor_total_gasto_em_midias()}", text_color=text_color, font=font_texto)
        metricas_midias_label.pack(side="left", fill="x", padx=(20,0))

        frame_metricas_texto_cds_label = ctk.CTkFrame(master=frame_metricas_fixas, fg_color="transparent")
        frame_metricas_texto_cds_label.pack(side="top", fill="x")

        metricas_cds_label = ctk.CTkLabel(master=frame_metricas_texto_cds_label, text=f"{self.midia_service.quantidade_de_cds()} CDs - R$ {self.midia_service.valor_total_gasto_em_cds()}", text_color=text_color, font=font_texto)
        metricas_cds_label.pack(side="left", fill="x", padx=(20,0))

        frame_metricas_texto_vinis_label = ctk.CTkFrame(master=frame_metricas_fixas, fg_color="transparent")
        frame_metricas_texto_vinis_label.pack(side="top", fill="x")

        metricas_vinis_label = ctk.CTkLabel(master=frame_metricas_texto_vinis_label, text=f"{self.midia_service.quantidade_de_vinis()} Vinis - R$ {self.midia_service.valor_total_gasto_em_vinis()}", text_color=text_color, font=font_texto)
        metricas_vinis_label.pack(side="left", fill="x", padx=(20,0))

        barra = ctk.CTkFrame(master=frame_metricas, fg_color="#505050", height=4)
        barra.pack(side="top", fill="x", padx=10, pady=(10,0))

        # Métricas responsivas
        scrollable_frame_metricas_responsivas = ctk.CTkScrollableFrame(master=frame_metricas, fg_color="transparent")
        scrollable_frame_metricas_responsivas.pack(side="top", fill="both", expand=True)

        for genero in self.midia_service.listar_generos_no_banco():
            frame_metricas_texto_midias_por_genero_label = ctk.CTkFrame(master=scrollable_frame_metricas_responsivas, fg_color="transparent")
            frame_metricas_texto_midias_por_genero_label.pack(side="top", fill="x")

            metricas_genero_label = ctk.CTkLabel(master=frame_metricas_texto_midias_por_genero_label, text=f"{self.midia_service.quantidade_de_midias_por_genero(genero)} mídias de {genero} - R$ {self.midia_service.valor_total_gasto_por_genero(genero)}", text_color=text_color, font=font_texto)
            metricas_genero_label.pack(side="left", fill="x", padx=(14,0))

    # Funções
    def listar_midias(self):
        for widget in self.scrollable_frame_midias.winfo_children():
            widget.destroy()

        self.midias_label.configure(text=f"{len(self.midias)} Mídias")

        if not self.midias:
            label_vazio = ctk.CTkLabel(master=self.scrollable_frame_midias, text="Nenhuma mídia encontrada.", font=("Arial", 26))
            label_vazio.pack(pady=20)
            return

        for midia in self.midias:
            frame_item = ctk.CTkFrame(master=self.scrollable_frame_midias, fg_color="transparent")
            frame_item.pack(fill="x", pady=5, padx=5)

            frame_item.grid_columnconfigure(0, weight=0, minsize=120)  # Coluna da imagem (largura fixa)
            frame_item.grid_columnconfigure(1, weight=1)  # Coluna dos dados (expansível)
            frame_item.grid_columnconfigure(2, weight=0, minsize=130)  # Coluna do botão (largura fixa)

            imagem_label = ctk.CTkLabel(master=frame_item, image=self.arquivos_service.carregar_imagem(midia.caminho_imagem), text="")
            imagem_label.grid(row=0, column=0, rowspan=2, padx=10, pady=5, sticky="ns")

            midia_titulo = ctk.CTkLabel(master=frame_item, text=f"{midia.titulo} ({midia.data_entrada.strftime("%d/%m/%Y")})", font=("Arial", 21, "bold"), anchor="w")
            midia_titulo.grid(row=0, column=1, sticky="sw", padx=10)

            midia_artista = ctk.CTkLabel(master=frame_item, text=midia.artista, font=("Arial", 16), anchor="w")
            midia_artista.grid(row=1, column=1, sticky="nw", padx=10)

            botao_detalhes = ctk.CTkButton(master=frame_item, text="Detalhes", height=40, width=100, hover_color="#646464", fg_color="#505050", corner_radius=20, font=('arial', 15), command=lambda id_da_midia=midia.id: self.abrir_janela_detalhes_midia(id_da_midia))
            botao_detalhes.grid(row=0, column=2, rowspan=2, padx=10, pady=5, sticky="e")

            barra = ctk.CTkFrame(master=self.scrollable_frame_midias, fg_color="#505050", height=5)
            barra.pack(fill="x", side="top", pady=10, padx=20)


    def listar_midias_por_pesquisa(self):
        pesquisa = self.pesquisa.get()

        if pesquisa:
            self.midias = self.midia_service.listar_midias_por_pesquisa(pesquisa)
        else:
            self.midias = self.midia_service.listar_midias_com_filtro_ordem()

        self.listar_midias()

    def filtrar_ordenar_midias(self):
        genero = self.filtro_genero.get() if self.filtro_genero.get() != "Gênero" else None
        formato = self.filtro_formato.get() if self.filtro_formato.get() != "Formato" else None
        tipo = self.filtro_tipo.get() if self.filtro_tipo.get() != "Tipo" else None

        ordem_tipo = self.ordem_tipo.get() if self.ordem_tipo.get() != "Ordenar por" else "Data de entrada"
        ordem = self.ordem.get() if self.ordem.get() != "Ordem" else "Decrescente"

        self.midias = self.midia_service.listar_midias_com_filtro_ordem(genero, formato, tipo, ordem_tipo, ordem)

        self.listar_midias()

    def limpar_filtros(self):
        self.filtro_genero.set("Gênero")
        self.filtro_formato.set("Formato")
        self.filtro_tipo.set("Tipo")
        self.ordem_tipo.set("Ordenar por")
        self.ordem.set("Ordem")

        self.midias = self.midia_service.listar_midias_com_filtro_ordem()

        self.listar_midias()

    def abrir_janela_cadastro_midia(self):
        janela_cadastro = CadastrarMidia(master=self)

    def abrir_janela_detalhes_midia(self, id):
        janela_detalhes = DetalhesMidia(master=self, id_midia=id)