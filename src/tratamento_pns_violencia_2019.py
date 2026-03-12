import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
arquivo_raw = BASE_DIR / 'data' / 'raw' / 'pns_violencia_2019.csv'
arquivo_processed = BASE_DIR / 'data' / 'processed' / 'pns_violencia_2019_tratado.csv'

pns_violencia = pd.read_csv(arquivo_raw, encoding='UTF-8', sep=';')

#---Tratamento

# Estas coluna nao possui informacoes relevantes para a análise, tendo em vista que todos os registros sao "Feminino"
pns_violencia.drop(columns=['Sexo'], inplace=True)

pns_violencia.replace('Não aplicável', None, inplace=True)

pns_violencia['Faixa Etária'] = pd.cut(
    pns_violencia['Idade'],
    bins = [17, 29, 39, 49, 59, 98],
    labels = ['18-29', '30-39', '40-49', '50-59', '60+']
)

pns_violencia.to_csv(arquivo_processed, index_label=False)
