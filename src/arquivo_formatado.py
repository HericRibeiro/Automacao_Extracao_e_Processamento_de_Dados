from config import config
import pandas as pd
import os
import traceback
import logging

def cola_dados_Final():

    try:
        show = config['arquivo_Show']
        arquivoFinal = config['arquivo_Formatado']

        arquivo_origem = show
        arquivo_destino = arquivoFinal

        if not os.path.exists(arquivo_origem):
            logging.error(f"❌ Arquivo origem não encontrado: {arquivo_origem}")
            return False
            
        if not os.path.exists(arquivo_destino):
            logging.error(f"❌ Arquivo destino não encontrado: {arquivo_destino}")
            return False

        logging.info(f"📖 Lendo arquivo origem: {arquivo_origem}")
        df_origem = pd.read_excel(arquivo_origem)

        logging.info(f"📖 Lendo arquivo destino: {arquivo_destino}")
        df_destino = pd.read_excel(arquivo_destino)
        
        mapeamento_colunas = {
            'Cliente': 'NOME EMPRESA CAMPANHA',
            'Motivo': 'MOTIVO CHAMADA', 
            'Qtde de Numeros': 'QUANTIDADE TERMINAIS',
            'Data Inicio': 'DATA SOLICITAÇÃO',
            'Data Fim': 'DATA CONCLUSÃO',
            'Status': 'STATUS CAMPANHA',
            'Terminais': 'TELEFONE',
            'ID': 'ID'
        }
        
        colunas_origem_faltantes = []
        for col_origem in mapeamento_colunas.keys():
            if col_origem not in df_origem.columns:
                colunas_origem_faltantes.append(col_origem)
        
        if colunas_origem_faltantes:
            logging.error(f"❌ Colunas não encontradas no arquivo origem: {colunas_origem_faltantes}")
            logging.info(f"📋 Colunas disponíveis no arquivo origem: {list(df_origem.columns)}")
            return False

        colunas_destino_faltantes = []
        for col_destino in mapeamento_colunas.values():
            if col_destino not in df_destino.columns:
                colunas_destino_faltantes.append(col_destino)
        
        if colunas_destino_faltantes:
            logging.error(f"❌ Colunas não encontradas no arquivo destino: {colunas_destino_faltantes}")
            logging.info(f"📋 Colunas disponíveis no arquivo destino: {list(df_destino.columns)}")
            return False
        
        logging.info(f"📊 Dados origem: {len(df_origem)} linhas")
        logging.info(f"📊 Dados destino: {len(df_destino)} linhas")

        df_destino_limpo = df_destino.iloc[0:0].copy()  # Mantém só o cabeçalho

        if len(df_origem) == 0:
            logging.warning("⚠️ Arquivo origem está vazio")

            df_destino_limpo.to_excel(arquivo_destino, index=False)
            logging.info("✅ Arquivo destino limpo salvo!")
            return True
        
        # Copiar os dados linha por linha
        linhas_copiadas = 0
        for index in range(len(df_origem)):
            nova_linha = {}
            logging.info(f"🏴󠁧󠁢󠁳󠁣󠁴󠁿 ☠ Status: {index} ⚔ 🏂 ")
            # Manter todas as colunas do arquivo destino
            for col_destino in df_destino.columns:
                if col_destino in mapeamento_colunas.values():
                    # Encontrar a coluna origem correspondente
                    col_origem = None
                    for orig, dest in mapeamento_colunas.items():
                        if dest == col_destino:
                            col_origem = orig
                            break
                    
                    if col_origem:
                        nova_linha[col_destino] = df_origem.iloc[index][col_origem]
                    else:
                        nova_linha[col_destino] = None
                else:
                    # Para colunas que não estão no mapeamento, deixar vazio
                    nova_linha[col_destino] = None
            df_destino_limpo = pd.concat([df_destino_limpo, pd.DataFrame([nova_linha])], ignore_index=True)
            linhas_copiadas += 1

        df_destino_limpo.to_excel(arquivo_destino, index=False)

        logging.info(f"✅ Dados copiados com sucesso!")
        logging.info(f"📈 {linhas_copiadas} linhas processadas")
        logging.info(f"💾 Arquivo salvo: {arquivo_destino}")

        return True
        
    except Exception as e:
        logging.error(f"❌ Erro ao processar dados: {e}")
        traceback.print_exc()
        return False