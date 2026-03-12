import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
arquivo_raw = BASE_DIR / 'data' / 'raw' / 'feminicidio_serie_historica.parquet'
arquivo_processed = BASE_DIR / 'data' / 'processed' / 'feminicidio_serie_historica_tratado.csv'

serie_historica = pd.read_parquet(arquivo_raw)

# 1 ( x ) converter as variaveis DT para o formato datetime
# 2 ( x ) converter as variaveis de HORA para o formato time
# 3 ( x ) adicionando coluna de estados


# 1
serie_historica['DT_CADASTRO_OBITO'] = pd.to_datetime(serie_historica['DT_CADASTRO_OBITO'], format='%d%m%Y', errors='coerce')

serie_historica['DT_NASCIMENTO'] = pd.to_datetime(serie_historica['DT_NASCIMENTO'], format='%d%m%Y', errors='coerce')

serie_historica['DT_OBITO'] = pd.to_datetime(serie_historica['DT_OBITO'], format='%d%m%Y', errors='coerce')

# 2
def converter_hora(hora):
    hora = str(hora).upper()
    if hora == 'IGNORADO':
        return None
    hora = hora.zfill(4)
    df = pd.to_datetime(hora, format='%H%M', errors='coerce')
    return df.time() if pd.notnull(df) else None

serie_historica['HORA_OBITO'] = serie_historica['HORA_OBITO'].apply(converter_hora)

# 3
codigo_para_estado = {
    "11": "RO", "12": "AC", "13": "AM", "14": "RR",
    "15": "PA", "16": "AP", "17": "TO", "21": "MA",
    "22": "PI", "23": "CE", "24": "RN", "25": "PB",
    "26": "PE", "27": "AL", "28": "SE", "29": "BA",
    "31": "MG", "32": "ES", "33": "RJ", "35": "SP",
    "41": "PR", "42": "SC", "43": "RS", "50": "MS",
    "51": "MT", "52": "GO", "53": "DF"
}

# Transformando codigo de municipio em estado
def cnvt_mun_para_est(cod_mun):
    cod_mun = str(cod_mun)[:2]
    cod_est = codigo_para_estado.get(cod_mun)
    return cod_est

serie_historica['ESTADO_RESID'] = serie_historica['COD_MUNICIPIO_RESID'].apply(cnvt_mun_para_est)
serie_historica['ESTADO_OBITO'] = serie_historica['COD_MUNICIPIO_OBITO'].apply(cnvt_mun_para_est)


serie_historica.to_csv(arquivo_processed, index=False)