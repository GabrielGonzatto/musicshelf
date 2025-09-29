from datetime import datetime

from sqlalchemy import Column, Date, Integer, Numeric, String

from service.arquivosService import Base

class Midia(Base):
    __tablename__ = "midia"

    id = Column(Integer, primary_key=True, autoincrement=True)

    # identificação e classificação
    genero = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    formato = Column(String, nullable=False)

    # dados principais
    titulo = Column(String, nullable=False)
    artista = Column(String)
    ano_lancamento = Column(Integer)
    pais = Column(String, nullable=False)

    # informações de entrada no acervo
    forma_aquisicao = Column(String, nullable=False)
    data_entrada = Column(Date, nullable=False)
    valor = Column(Numeric(10, 2))

    # estado de conservação
    conservacao_geral = Column(String)
    conservacao_encarte = Column(String)
    conservacao_midia = Column(String)

    # complementos
    descricao = Column(String)
    tags = Column(String)
    caminho_imagem = Column(String, nullable=False)



    def validar(self, titulo, artista, genero, tipo, formato, pais, forma_aquisicao, conservacao_geral, conservacao_encarte, conservacao_midia, descricao, caminho_imagem, ano_lancamento_base, data_entrada_base, valor_base, id = None):
        if not titulo: raise ValueError("O campo 'Título' é obrigatório.")
        if not genero: raise ValueError("Selecione um 'Gênero' válido.")
        if not tipo: raise ValueError("Selecione um 'Tipo' válido.")
        if not formato: raise ValueError("Selecione um 'Formato' válido.")
        if not pais: raise ValueError("O campo 'País' é obrigatório.")
        if not forma_aquisicao: raise ValueError("Selecione uma 'Forma de aquisição' válida.")
        if not data_entrada_base: raise ValueError("O campo 'Data de entrada' é obrigatório.")
        if not conservacao_midia: raise ValueError("Selecione uma 'Conservação de mídia' válida.")
        if not conservacao_encarte: raise ValueError("Selecione uma 'Conservação de encarte' válida.")
        if not conservacao_geral: raise ValueError("Selecione uma 'Conservação geral' válida.")
        if not caminho_imagem: raise ValueError("O campo 'Imagem' é obrigatório.")

        try:
            ano_lancamento = int(ano_lancamento_base)
            data_entrada = datetime.strptime(data_entrada_base, "%d/%m/%Y").date()

            valor_str = valor_base.replace(',', '.')
            valor = float(valor_str) if valor_str else 0.0

        except (ValueError, TypeError):
            raise ValueError("Verifique os campos de data e valores numéricos. Formato inválido.")

        tags_finais = f"{titulo}, {artista}, {ano_lancamento_base}, {pais}"

        return Midia(
            id=id,
            titulo=titulo,
            artista=artista,
            genero=genero,
            tipo=tipo,
            formato=formato,
            ano_lancamento=ano_lancamento,
            pais=pais,
            forma_aquisicao=forma_aquisicao,
            valor=valor,
            data_entrada=data_entrada,
            conservacao_geral=conservacao_geral,
            conservacao_encarte=conservacao_encarte,
            conservacao_midia=conservacao_midia,
            tags=tags_finais,
            descricao=descricao,
            caminho_imagem=caminho_imagem
        )
