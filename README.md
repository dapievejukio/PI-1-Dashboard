# Projeto Integrador - Low Code em Ciência de Dados  
### (Grupo 46)

## Tema do projeto
Dashboard interativo com dados do Kaggle, com pipeline de ETL (Pandas) e visualização em Streamlit.

## Integrantes
- Brunna Stival (@brunnastival)
- Caio Luna (@caioluna)
- Danubio Souza (@Danubio229)
- Franciane Giselle (@itgiselle)
- Glauco Campos (@turistech)
- Hugo Miguel (@hugomfrosa)
- Jhon Diass (@JhonDiass)
- Júlio (@dapievejukio)

## Distribuição de tarefas (a escolher pelo grupo)
As funções abaixo serão escolhidas pelos integrantes, para fechar a Etapa 1:

- **Função A — Base Kaggle:** escolher dataset, link, contexto e justificativa. (Responsável: Jhon Diass / @JhonDiass)
- **Função B — KPIs e perguntas:** definir perguntas do dashboard + 5–8 indicadores + filtros. (Responsáveis: Caio Luna @caioluna, Glauco Campos @turistech)
- **Função C — Planejamento ETL:** descrever extração → transformações (Pandas) → carga (CSV/SQLite). (Responsável: Franciane Giselle @itgiselle)
- **Função D — Ideia do dashboard:** layout (cards + gráficos + tabela) e visualizações.
- **Função E — Revisão final README + cronograma:** consolidar tudo e revisar coerência.
- **Função F — Repositório/organização:** manter estrutura, commits e ajustes no GitHub (Responsável inicial: Júlio / @dapievejukio)

## Base de dados (Kaggle)
- **Dataset:** Flor de Aço: Dados contra o Feminicídio  
- **Link:** https://www.kaggle.com/datasets/rafatrindade/feminicidio-br  
- **Arquivo principal do projeto (para o dashboard):** `pns_violencia_2019.csv` (PNS 2019 – mulheres entrevistadas que relataram algum tipo de violência)  
- **Contexto/origem:** Conjunto filtrado de microdados da Pesquisa Nacional de Saúde (2019) com informações sobre tipo de agressão, autor/agressor, local da ocorrência e possíveis consequências para a saúde.  
- **Justificativa da escolha:** Como março é marcado pelo Dia Internacional da Mulher e o tema tem alta relevância social no Brasil, escolhemos esse dataset para apoiar um dashboard de conscientização e análise de padrões dos **relatos de violência**, ajudando a visualizar perfil, contexto e fatores associados.

## Objetivo da análise
Construir um dashboard em Streamlit para **visualizar e explorar indicadores** dos relatos de violência contra mulheres (PNS 2019), destacando distribuição por UF e área (urbano/rural), perfil (idade e cor/raça), tipo de violência, autor/agressor e local da ocorrência, com filtros que facilitem comparação e leitura rápida.

## Visualizações e métricas desejadas

### Análise Descritiva (compreender o cenário)
- Qual a distribuição etária e de cor/raça das mulheres que relataram violência?
- Como é a distribuição por UF e por área (urbano/rural)?
- Qual o tipo de violência (psicológica, física, sexual) mais frequente?
- Quem aparece com mais frequência como autor/agressor (conforme colunas do dataset)?
- Quais são os locais mais citados para a ocorrência? (casa, via pública, outros, etc.)
- A vítima registrou ocorrência/denúncia? (se existir a variável)
- **Opcional (se existir dado de tempo):** há padrão por mês/dia da semana/fim de semana?

### Análise Preditiva (antecipar riscos) — opcional
- **Opcional (se houver variável temporal suficiente):** previsão de registros para o próximo ano / próximos anos.

### Análise Prescritiva (orientar ações) — opcional
- Com base nos perfis observados, qual perfil deveria ser priorizado em campanhas de prevenção (conforme variáveis disponíveis)?
- **Opcional (se houver município/região detalhada e/ou integração externa):** quais regiões teriam maior potencial de impacto para ações e recursos.

> Observação: itens marcados como “Opcional” dependem das colunas existentes no arquivo e/ou integração com bases externas.

## Planejamento do ETL (Pandas + carga)
O pipeline seguirá as etapas: **extração → transformação → carga**, com foco em gerar uma base limpa e estruturada para o dashboard.

### 1) Extração
- Download do dataset via Kaggle (manual ou via API, se necessário).
- Armazenamento do arquivo original em: `data/raw/` (não alterar o arquivo bruto).

### 2) Transformação (tratamentos previstos)
Tratamentos planejados (de acordo com as colunas disponíveis):
- remoção de duplicados;
- tratamento de valores ausentes (nulos) e padronização de preenchimentos;
- correção de tipos (números, texto e variáveis categóricas);
- padronização de categorias (ex.: maiúsculas/minúsculas, espaços, valores equivalentes);
- criação de colunas derivadas úteis (ex.: faixas etárias);
- agregações para análises (ex.: contagem por UF/área/idade/raça/tipo/local/autor);
- validações básicas (ex.: valores fora de faixa, categorias inconsistentes).

### 3) Carga
- Exportação da base tratada para `data/processed/` (CSV).
- Opcional: carga em **SQLite** para facilitar consultas e organização da base.

## Ideia inicial do dashboard (Streamlit)
O dashboard será construído no Streamlit para permitir visualização rápida e exploração dos dados.

### KPIs/Indicadores (iniciais)
- Total de registros (mulheres que relataram violência)
- Top 5 UFs por contagem
- Urbano vs Rural
- Faixa etária com maior concentração
- Cor/raça mais frequente
- Tipo de violência mais frequente
- Autor/agressor mais frequente (se existir)
- Local de ocorrência mais frequente (se existir)

### Visualizações previstas
- Barras: Top UFs por contagem
- Barras empilhadas: UF x tipo de violência (se existir)
- Histograma: distribuição de idade
- Barras: cor/raça
- Barras: autor/agressor (se existir)
- Barras: local da ocorrência (se existir)
- Tabela: resumo filtrável (UF, área, idade, raça, tipo, autor, local)

### Filtros previstos
- UF
- Área (urbano/rural)
- Faixa etária
- Cor/raça
- Tipo de violência (se existir)
- Autor/agressor (se existir)
- Local da ocorrência (se existir)

## Estrutura do repositório
- `app/` — aplicação Streamlit (dashboard)
- `data/raw/` — dados brutos (originais)
- `data/processed/` — dados tratados/estruturados
- `notebooks/` — análises exploratórias (Jupyter/Colab)
- `src/` — scripts do ETL e funções auxiliares

## Cronograma até 23/03/2026 (Etapa 1)
- **Semana 1:** criar repositório/estrutura + escolher dataset Kaggle + definir objetivo e perguntas
- **Semana 2:** planejar ETL + definir KPIs e filtros + rascunhar visualizações do dashboard
- **Semana 3:** revisar README + garantir coerência (dataset ↔ ETL ↔ KPIs ↔ dashboard) + preparar entrega do link do repositório
