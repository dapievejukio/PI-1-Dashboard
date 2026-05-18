import pandas as pd
import numpy as np
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

# Esta tabela nao apresenta a coluna "Tipo de violência" que na de 2013 contém, sendo assim será feito um trabalho onde o tipo de violencia sofrida será categorizado e enviado para a coluna citada para esta tabela.

condicao_para_sexual = (pns_violencia['Violência sexual (12 meses): toque/beijo/manipulação'] == 'Sim') | (pns_violencia['Violência sexual (12 meses): ameaça/forçar ato sexual'] == 'Sim') | (pns_violencia['Violência sexual na vida: toque/beijo/manipulação'] == 'Sim') | (pns_violencia['Violência sexual na vida: ameaça/forçar ato sexual'] == 'Sim')

condicao_para_fisica = (pns_violencia['Agressão física: tapa/bofetada'] == 'Sim') | (pns_violencia['Agressão física: empurrão/segurar/jogar objeto'] == 'Sim') | (pns_violencia['Agressão física: soco/chute/puxão de cabelo'] == 'Sim') | (pns_violencia['Agressão física: estrangular/asfixiar/queimar'] == 'Sim') | (pns_violencia['Agressão física com arma (faca, arma de fogo)'] == 'Sim')

condicao_para_psicologica = (pns_violencia['Ofensa/humilhação em público (12 meses)'] == 'Sim') | (pns_violencia['Gritos/xingamentos (12 meses)'] == 'Sim') | (pns_violencia['Ameaças/redes sociais (12 meses)'] == 'Sim') | (pns_violencia['Ameaça contra pessoa importante (12 meses)'] == 'Sim') | (pns_violencia['Destruiu algo seu (12 meses)'] == 'Sim')

condicoes = [
    condicao_para_sexual,
    condicao_para_fisica,
    condicao_para_psicologica,
]

valores = ['Sexual', 'Física', 'Psicológica']

pns_violencia['Tipo de violência'] = np.select(condicoes, valores, default = 'Outro')

pns_violencia['Local'] = np.where(
    pns_violencia['Tipo de violência'] == 'Psicológica', pns_violencia['Local da violência psicológica'],
    np.where(
        pns_violencia['Tipo de violência'] == 'Física', pns_violencia['Local da agressão física'],
        np.where(
            pns_violencia['Tipo de violência'] == 'Sexual', pns_violencia['Local da violência sexual'],
            None
        )
    )
)
pns_violencia['Autor'] = np.where(
    pns_violencia['Tipo de violência'] == 'Psicológica', pns_violencia['Autor da violência psicológica'],
    np.where(
        pns_violencia['Tipo de violência'] == 'Física', pns_violencia['Autor da agressão física'],
        np.where(
            pns_violencia['Tipo de violência'] == 'Sexual', pns_violencia['Autor da violência sexual'],
            None
        )
    )
)

pns_violencia.to_csv(arquivo_processed, index_label=False, encoding='utf-8-sig', sep=';')