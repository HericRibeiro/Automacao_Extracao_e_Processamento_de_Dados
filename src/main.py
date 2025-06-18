from processamento import loop
from processamento import executar_pos_loop
from logger import setup_logging
import logging
import traceback

def main():

    try:
        setup_logging()
        logging.info("🔄 Iniciando processo de extração...")
        loop()
        
        print(f"\n{'='*60}")
        print("✅ LOOP DE EXTRAÇÃO FINALIZADO")
        print("🚀 INICIANDO OPERAÇÕES SUBSEQUENTES...")
        print(f"{'='*60}")
        
        if executar_pos_loop():
            logging.info("\n🎊 PROCESSO COMPLETO FINALIZADO COM SUCESSO!")

        else:
            logging.error("\n❌ ERRO NAS OPERAÇÕES PÓS-LOOP")

    except Exception as e:
        logging.error(f"❌ Erro geral no processo da função main: {e}")
        traceback.print_exc()


if __name__ == "__main__":
    main()