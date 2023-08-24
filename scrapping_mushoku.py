# Importando bibliotecas necessárias
from bs4 import BeautifulSoup
import requests

# Criando variáveis com URL do site
url_volume = "https://centralnovel.com/mushoku-tensei-jobless-reincarnation-volume-"
url_capitulo = "-capitulo-"

# Criando variáveis incrementais de volume e capítulo
numero_volume = 1
numero_capitulo = 1.0


while numero_capitulo <= 15:
    # Iniciando tentativa
    try:
        # Tratando número do cap por ser FLOAT
        if str(numero_capitulo).find(".0") >= 0:
            # Criando variável para armazenar número do capítulo em STRING
            numero_capitulo_modificado = str(numero_capitulo).split(".")[0]

            # Criando requisição da URL
            requisicao = requests.get(
                url_volume
                + str(numero_volume)
                + url_capitulo
                + str(numero_capitulo_modificado)
            )
        else:
            # Criando variável para armazenar número do capítulo em STRING
            numero_capitulo_modificado = (
                str(numero_capitulo).split(".")[0]
                + "-"
                + str(numero_capitulo).split(".")[1]
            )

            # Criando requisição da URL
            requisicao = requests.get(
                url_volume
                + str(numero_volume)
                + url_capitulo
                + numero_capitulo_modificado
            )

        # Parseando HTML
        soup = BeautifulSoup(requisicao.text, "html.parser")

        # Acessando título com NÚMERO do capítulo
        titulo_capitulo_numero = soup.find("h1", {"class": "entry-title"}).get_text()

        # Acessando título com NOME do capítulo
        titulo_capitulo_nome = soup.find("div", {"class": "cat-series"}).get_text()

        # Criando documento
        open(
            f"./capitulos/Capitulo {numero_capitulo_modificado} - {titulo_capitulo_nome}.txt",
            "w",
        )

        # Adicionando paragrafos ao documento
        with open(
            f"./capitulos/Capitulo {numero_capitulo_modificado} - {titulo_capitulo_nome}.txt",
            "a",
        ) as documento:
            for paragrafo in soup.findAll("p"):
                documento.write(paragrafo.get_text())
                documento.write("\n\n")
    except:
        print(
            "ERRO NO CAPÌTULO " + str(numero_capitulo_modificado) + ", POIS NÂO EXISTE"
        )
        pass

    # Incrementando
    numero_capitulo += 0.5
