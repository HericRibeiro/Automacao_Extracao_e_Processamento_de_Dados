import pandas as pd
import logging

def duplicar_campanha_por_terminal():
    df = pd.read_excel('extracao_tabela.xlsx')
    logging.info(f"Linhas no arquivo original: {len(df)}")

    linhas_novas = []

    for i in range(len(df)):
        Cliente = df.iloc[i, 0]
        Motivo = df.iloc[i, 1]
        Qtde_de_Numeros = df.iloc[i, 2]
        DataInicio = df.iloc[i, 3]
        DataFim = df.iloc[i, 4]
        Status = df.iloc[i, 5]
        id = df.iloc[i, 7]
        
        for j in range(Qtde_de_Numeros):
            linhas_novas.append({
                'Cliente': Cliente,
                'Motivo': Motivo,
                'Qtde de Numeros': Qtde_de_Numeros,
                'Data Inicio': DataInicio,
                'Data Fim': DataFim,
                'Status': Status,
                'Terminais': None,
                'ID': id
            })

    DadosDuplicados = pd.DataFrame(linhas_novas)
    logging.info(f"Total de linhas criadas: {len(DadosDuplicados)}")
    DadosDuplicados.to_excel('Show.xlsx', index=False)
    logging.info("✅ Arquivo 'Show.xlsx' salvo com sucesso!")