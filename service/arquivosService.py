import json
import os
import shutil
import uuid
from pathlib import Path

from PIL import Image
from customtkinter import CTkImage
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine(f"sqlite:///database/db/musicshelf.db")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class ArquivosService:

    # Imagens
    def cadastrar_imagem(self, caminho_imagem):
        nome_arquivo = f"{uuid.uuid4()}{Path(caminho_imagem).suffix}"
        caminho_destino = f"database/images/{nome_arquivo}"

        shutil.copy(caminho_imagem, caminho_destino)

        return f"database/images/{nome_arquivo}"

    def carregar_imagem(self, caminho_imagem, tamanho=(100,100)):
        try:
            with Image.open(caminho_imagem) as img:
                img.load()
                return CTkImage(dark_image=img, light_image=img, size=tamanho)

        except Exception:
            try:
                with Image.open("resources/assets/imageNotFound.png") as img_padrao:
                    img_padrao.load()
                    return CTkImage(dark_image=img_padrao, light_image=img_padrao, size=tamanho)

            except Exception:
                return None

    def atualizar_imagem(self, caminho_imagem_antiga, caminho_imagem_nova):
        if caminho_imagem_antiga == caminho_imagem_nova:
            return caminho_imagem_antiga
        else:
            self.deletar_imagem(caminho_imagem_antiga)
            return self.cadastrar_imagem(caminho_imagem_nova)

    def deletar_imagem(self, caminho_imagem):
        if os.path.exists(caminho_imagem):
            os.remove(caminho_imagem)



    # Váriaveis
    def listar_generos(self):
        with open("resources/assets/variaveis.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        return data["generos"]

    def listar_tipos(self):
        with open("resources/assets/variaveis.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        return data["tipos"]