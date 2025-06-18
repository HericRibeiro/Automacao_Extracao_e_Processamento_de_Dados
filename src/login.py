from utils import esperar_e_clicar
from config import config
import traceback
import logging
import time

def login(driver):
    try:
        logging.info("🔑 Iniciando login...")
        driver.get(config['link_Portal'])
        time.sleep(5)
        driver.maximize_window()
        
        if esperar_e_clicar(driver, config['acesso']):
            esperar_e_clicar(driver, config['confirmacao_Acesso'])
            logging.info("✅ Login realizado com sucesso")
            time.sleep(10)
            return True
        else:
            logging.error("❌ Falha no login")
            return False
         
    except Exception as e:
        logging.error(f"❌ Erro no login: {e}")
        traceback.print_exc()
        return False