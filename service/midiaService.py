from sqlalchemy import asc, desc, func

import pandas as pd

from model.midia import Midia
from .arquivosService import ArquivosService

class MidiaService:
    def __init__(self, session):
        self.session = session

        self.arquivos_service = ArquivosService()



    # Excel
    def exportar_para_excel(self):
        try:
            midias = self.session.query(Midia).order_by(asc(Midia.data_entrada)).all()

            if not midias:
                return

            dados_para_planilha = [
                {
                    "Título": midia.titulo,
                    "Artista/Banda": midia.artista,
                    "Gênero": midia.genero,
                    "Tipo": midia.tipo,
                    "Formato": midia.formato,
                    "Data de Entrada": midia.data_entrada.strftime("%d/%m/%Y"),
                    "Forma de aquisição": midia.forma_aquisicao,
                    "Valor": midia.valor,
                    "Descrição": midia.descricao,
                }
                for midia in midias
            ]


            df = pd.DataFrame(dados_para_planilha)
            df.to_excel("resources/xls/relatorio_de_midias.xls", index=False, engine='openpyxl')

        except Exception as e:
            print(f"Ocorreu um erro ao exportar para Excel: {e}")



    # CRUD mídia
    def cadastrar_midia(self, midia:Midia, master):
        midia.caminho_imagem = self.arquivos_service.cadastrar_imagem(midia.caminho_imagem)

        self.session.add(midia)
        self.session.commit()

        master.filtrar_ordenar_midias()

    def listar_midias_com_filtro_ordem(self, genero=None, formato=None, tipo=None, ordem_tipo='Data de entrada', ordem='Decrescente'):
        query = self.session.query(Midia)

        colunas_ordenacao = {
            'Data de entrada': Midia.data_entrada,
            'Título': Midia.titulo,
            'Valor': Midia.valor,
            'Ano de lançamento': Midia.ano_lancamento,
        }
        coluna_a_ordenar = colunas_ordenacao.get(ordem_tipo, Midia.data_entrada)

        if ordem == 'Decrescente':
            query = query.order_by(desc(coluna_a_ordenar))
        else:
            query = query.order_by(asc(coluna_a_ordenar))

        if genero:
            query = query.filter(Midia.genero == genero)

        if formato:
            query = query.filter(Midia.formato == formato)

        if tipo:
            query = query.filter(Midia.tipo == tipo)

        return query.all()

    def listar_midias_por_pesquisa(self, pesquisa):
        return self.session.query(Midia).filter(Midia.tags.ilike(f"%{pesquisa}%")).all()

    def listar_midia(self, id):
        return self.session.query(Midia).filter(Midia.id == id).first()

    def editar_midia(self, midia: Midia, caminho_imagem_antiga, caminho_imagem_nova, master):
        midia.caminho_imagem = self.arquivos_service.atualizar_imagem(caminho_imagem_antiga, caminho_imagem_nova)

        self.session.merge(midia)
        self.session.commit()

        master.session.expire_all()

        master.filtrar_ordenar_midias()

    def deletar_midia(self, midia:Midia):
        self.arquivos_service.deletar_imagem(midia.caminho_imagem)

        self.session.delete(midia)
        self.session.commit()



    # Consultas gerais
    def listar_generos_no_banco(self):
        return [resultado[0] for resultado in self.session.query(Midia.genero).distinct().order_by(Midia.genero).all()]

    def quantidade_de_midias_por_genero(self, genero):
        return self.session.query(Midia).filter(Midia.genero == genero).count()

    def valor_total_gasto_por_genero(self, genero):
        return self.session.query(func.sum(Midia.valor)).filter(Midia.forma_aquisicao == "Compra", Midia.genero == genero).scalar() or 0.0

    def quantidade_de_midias(self):
        return self.session.query(Midia).count()

    def valor_total_gasto_em_midias(self):
        return self.session.query(func.sum(Midia.valor)).filter(Midia.forma_aquisicao == "Compra").scalar() or 0.0

    def quantidade_de_cds(self):
        return self.session.query(Midia).filter(Midia.formato == "CD").count()

    def valor_total_gasto_em_cds(self):
        return self.session.query(func.sum(Midia.valor)).filter(Midia.forma_aquisicao == "Compra", Midia.formato == "CD").scalar() or 0.0
    def quantidade_de_vinis(self):
        return self.session.query(Midia).filter(Midia.formato == "Vinil").count()

    def valor_total_gasto_em_vinis(self):
        return self.session.query(func.sum(Midia.valor)).filter(Midia.forma_aquisicao == "Compra", Midia.formato == "Vinil").scalar() or 0.0