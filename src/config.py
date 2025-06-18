from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

config = {
    "hoje" : datetime.now().strftime('%Y%m%d_%H%M%S'),
    "link_Portal" : os.getenv('LINK'),
    "arquivo" : os.getenv('ARQUIVO_BASE'),
    "caminho_edge_driver" : os.getenv('CAMINHO_DRIVER_NAVEGADOR'),
    "arquivo_Show": os.getenv('ARQUIVO_SHOW'),
    "arquivo_Web": os.getenv('ARQUIVO_WEB'),
    "arquivo_Formatado": os.getenv('ARQUIVO_FINAL'),
    "url_ID" : os.getenv('URL'),
    "acesso" : os.getenv('ACESSO'),
    "modulo_Pagina_Web" : os.getenv('MODULO_PAGINA_WEB'),
    "modulo_Dois_Pagina_Web" : os.getenv('MODULO_DOIS_PAGINA_WEB'),
    "caminho_arquivo_log" : os.getenv('CAMINHO_ARQUIVO_LOG'),
    "tabela" : os.getenv('TABELA'),
    "linhas_tabela" : os.getenv('LINHAS_TABELA'),
    "secao_numeros" : os.getenv('SECAO_DE_NUMEROS'),
    "linhas_numeros" : os.getenv('LINHA_SECAO_DE_NUMEROS'),
    "confirmacao_Acesso" : os.getenv('CONFIRMACAO_ACESSO'),
    "filtro_Linhas": os.getenv('FILTRO_LINHAS'),
    "filtro_Opcao_Dois": os.getenv('FILTRO_PARA_CEM'),
    "mudar_Pagina": os.getenv('MUDAR_PAGINA'),
    "scroll_Pagina": os.getenv('SCROLL_PAGINA')
}