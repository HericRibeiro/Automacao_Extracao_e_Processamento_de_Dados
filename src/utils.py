from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium import webdriver
from config import config
import pandas as pd
import os
import pyautogui
import time
import logging

def esperar_e_clicar(driver, xpath, timeout=10):
    try:
        elemento = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", elemento)
        time.sleep(0.5)
        elemento.click()
        return True
    except Exception as e:
        logging.error(f"Erro ao clicar no elemento {xpath}: {e}")
        return False
    
def criar_driver():
    try:
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        # Usar service no caminho do driver
        if config['caminho_edge_driver'] and os.path.exists(config['caminho_edge_driver']):
            service = Service(config['caminho_edge_driver'])
            driver = webdriver.Edge(service=service, options=options)
        else:
            driver = webdriver.Edge(options=options)
        
        driver.implicitly_wait(10)
        logging.info("✅ Driver criado com sucesso")
        return driver
        
    except Exception as e:
        logging.error(f"❌ Erro ao criar driver: {e}")
        return None
    

def scroll_horizontal_pyautogui():

    try:
        pyautogui.moveTo(x= 677, y=999, duration=1) # Ajuste conforme tamanho da sua tela...
        time.sleep(2)

        pyautogui.mouseDown()
        time.sleep(2)

        pyautogui.moveTo(x=1100, y=1000, duration=1) # Ajuste conforme tamanho da sua tela...
        time.sleep(2)

        pyautogui.mouseUp()       
        time.sleep(2)

        pyautogui.moveTo(x=1300, y=900, duration=1) # Ajuste conforme tamanho da sua tela...
        time.sleep(2)

        print(f"✅ Scroll horizontal para direita executado!")
        
    except Exception as e:
        print(f"❌ Erro no scroll horizontal: {e}")
        return False


def filtro_pagina(driver):
    try:
        print("📝 Configurando página para 100 linhas!")

        driver.execute_script(config['scroll_Pagina'])
        time.sleep(2)

        if not esperar_e_clicar(driver, config['filtro_Linhas']):
            raise Exception ("❌ Erro  ao clicar no filtro de páginas!")
        
        time.sleep(3)

        if not esperar_e_clicar(driver, config['filtro_Opcao_Dois']):
            raise Exception ("❌ Erro ao selecionar 100 linhas!")
        
        print("✅ Página configurada para 100 linhas com sucesso!")
        time.sleep(3)
        return True
    
    except Exception as e:
        logging.error(f"❌ Erro ao configurar filtro de página: {e} ")
        return False


def mudar_pagina(driver):
    try:
        print("📝 Mudando para a próxima página")

        driver.execute_script(config['scroll_Pagina'])
        time.sleep(2)

        scroll_horizontal_pyautogui()        
        time.sleep(5)

        time.sleep(3)

        if not esperar_e_clicar(driver, config['mudar_Pagina']):
            raise Exception("❌ Não foi possível clicar para próxima página!")
    
        print("✅ Próxima página avançada com sucesso!")
        time.sleep(3)
        return True

    except Exception as e:
        logging.error(f"❌ Não foi possível passar a página: {e}")
        return False
    
def cola_terminais():
    terminaisPortal = config['arquivo_Web']
    show = config['arquivo_Show']

    arquivo_origem = terminaisPortal
    df_origem = pd.read_excel(arquivo_origem)
    coluna_para_copiar = df_origem['Numeros']

    arquivo_destino = show
    df_destino = pd.read_excel(arquivo_destino)
    df_destino['Terminais'] = coluna_para_copiar

    df_destino.to_excel(arquivo_destino, index=False)
    logging.info("Coluna copiada e colada com sucesso!")