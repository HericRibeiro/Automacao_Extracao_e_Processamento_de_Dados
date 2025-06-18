from config import config
from utils import esperar_e_clicar
import time
import pyautogui
import logging

def acesso_modulo(driver):
    try:
        logging.info("📂 Acessando módulo...")
        
        if not esperar_e_clicar(driver, config['modulo_Pagina_Web']):
            logging.error("❌ Falha ao acessar módulo inicial")
            return False
            
        time.sleep(3)
        
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(3)
        
        pyautogui.press('pagedown')
        time.sleep(2)
        
        if esperar_e_clicar(driver, config['modulo_Dois_Pagina_Web']):
            logging.info("✅ Módulo acessado com sucesso")
            time.sleep(10)
            return True
        else:
            logging.error("❌ Falha ao acessar sub-módulo")
            return False
            
    except Exception as e:
        logging.error(f"❌ Erro ao acessar os módulos: {e}")
        return False