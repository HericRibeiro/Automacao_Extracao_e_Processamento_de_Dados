from utils import criar_driver
from utils import filtro_pagina
from utils import mudar_pagina
from utils import cola_terminais
from duplicacao import duplicar_campanha_por_terminal 
from login import login
from arquivo_formatado import cola_dados_Final
from extracao_tabela import extracao_Tabela
from acesso_modulo import acesso_modulo
from extracao_id import extracao_id
import traceback
import logging
import time

def loop():

    total_loops = 4
    sucessos = 0
    
    for i in range(total_loops):
        driver = None
        sucesso_loop = False
        
        try:
            print(f"\n{'='*50}")
            print(f"🔄 INICIANDO LOOP {i+1}/{total_loops}")
            print(f"{'='*50}")
            
            driver = criar_driver()
            if not driver:
                logging.error(f"❌ Falha ao criar driver no loop {i+1}")
                continue

            if not login(driver):
                logging.error(f"❌ Falha no login no loop {i+1}")
                continue

            if not acesso_modulo(driver):
                logging.error(f"❌ Falha ao acessar módulo no loop {i+1}")
                continue

            if i == 0:
                if not filtro_pagina(driver):
                    logging.error(f"❌ Falha ao configurar filtro no loop {i+1}")
                    continue

            elif i == 1:
                if not filtro_pagina(driver):
                    logging.error(f"❌ Falha ao configurar filtro no loop {i+1}")
                    continue
                if not mudar_pagina(driver):
                    logging.error(f"❌ Falha ao mudar página no loop {i+1}")
                    continue
                
            elif i == 2:
                if not filtro_pagina(driver):
                    logging.error(f"❌ Falha ao mudar página no loop {i+1}")
                    continue

                for pagina in range(2):
                    if not mudar_pagina(driver):
                        logging.error(f"❌ Falha ao mudar para a página {pagina+1} no loop {i+1}")
                        break

                else:
                    pass

            elif i == 3:
                if not filtro_pagina(driver):
                    logging.error(f"❌ Falha ao configurar filtro no loop {i+1}")
                    continue

                for pagina in range(3):
                    if not mudar_pagina(driver):
                        logging.error(f"❌ Falha ao mudar para a página {pagina+1} no loop {i+1}")
                        break
                
                else:
                    pass
 
            if extracao_Tabela(driver, "teste.xlsx", criar_backup=(i==0)):
                logging.info(f"✅ Loop {i+1} concluído com sucesso!")
                sucessos += 1
                sucesso_loop = True

            else:
                logging.error(f"❌ Falha na extração no loop {i+1}")

        except Exception as e:
            logging.error(f"❌ Erro no loop {i+1}: {e}")
            traceback.print_exc()
            
        finally:
            if driver:
                try:
                    driver.quit()
                    logging.info(f"🔒 Driver fechado - Loop {i+1}")

                except Exception as e:
                    logging.error(f"⚠️ Erro ao fechar driver: {e}")

            # Pausa entre loops (exceto no último)
            if i < total_loops - 1:
                tempo_pausa = 10 if sucesso_loop else 15
                logging.info(f"⏳ Aguardando {tempo_pausa} segundos antes do próximo loop...")
                time.sleep(tempo_pausa)
    
    print(f"\n{'='*50}")
    print(f"🏁 RELATÓRIO FINAL")
    print(f"{'='*50}")
    logging.info(f"✅ Loops bem-sucedidos: {sucessos}/{total_loops}")
    logging.info(f"❌ Loops falharam: {total_loops - sucessos}/{total_loops}")
    logging.info(f"📊 Taxa de sucesso: {(sucessos/total_loops)*100:.1f}%")


def executar_pos_loop():

    driver = None
    
    try:
        print(f"\n{'='*50}")
        print("🚀 INICIANDO PÓS-LOOP")
        print(f"{'='*50}")
        
        logging.info("🔧 Criando driver...")
        driver = criar_driver()
        if not driver:
            logging.error("❌ Falha ao criar driver para operações pós-loop")
            return False

        logging.info("🔑 Executando login...")
        if not login(driver):
            logging.error("❌ Falha no login pós-loop")
            return False

        logging.info("📂 Acessando módulo...")
        if not acesso_modulo(driver):
            logging.error("❌ Falha ao acessar módulo pós-loop")
            return False

        logging.info("🔍 Extraindo IDs...")
        extracao_id(driver)

        logging.info("✅ Operações com driver concluídas!")

    except Exception as e:
        logging.error(f"❌ Erro nas operações pós-loop: {e}")
        traceback.print_exc()
        return False
        
    finally:
        if driver:
            try:
                driver.quit()
                logging.info("🔒 Driver fechado - Operação pós-loop")

            except Exception as e:
                logging.error(f"⚠️ Erro ao fechar driver: {e}")

    try:
        logging.info("📋 Duplicando campanhas por terminal...")
        duplicar_campanha_por_terminal()

        logging.info("📊 Colando terminais...")
        cola_terminais()

        logging.info("Verificando arquivos...")
        cola_dados_Final()

        print(f"\n{'='*50}")
        print("🎉 TODAS AS OPERAÇÕES CONCLUÍDAS COM SUCESSO!")
        print(f"{'='*50}")
        return True
        
    except Exception as e:
        logging.error(f"❌ Erro nas operações finais: {e}")
        traceback.print_exc()
        return False