# PI-1-Dashboard

## Tema do projeto
Dashboard interativo com dados do Kaggle, com pipeline de ETL (Pandas) e visualização em Streamlit.

## Integrantes
- Júlio (@dapievejukio)
- Jhon Diass (@JhonDiass)
- Caio Luna (@caioluna)
- Danubio Souza (@Danubio229)
- Hugo Miguel (@hugomfrosa)
- Integrante 6 (a confirmar)

## Distribuição de tarefas (a escolher pelo grupo)
As funções abaixo serão escolhidas pelos integrantes , para fechar a Etapa 1:

- **Função A — Base Kaggle:** escolher dataset, link, contexto e justificativa. (Responsável: Jhon Diass / @JhonDiass)
- **Função B — KPIs e perguntas:** definir perguntas do dashboard + 5–8 indicadores + filtros.
- **Função C — Planejamento ETL:** descrever extração → transformações (Pandas) → carga (CSV/SQLite).
- **Função D — Ideia do dashboard:** layout (cards + gráficos + tabela) e visualizações.
- **Função E — Revisão final README + cronograma:** consolidar tudo e revisar coerência.
- **Função F — Repo/organização:** manter estrutura, commits e ajustes no GitHub (responsável inicial: Júlio / @dapievejukio

## Base de dados (Kaggle)
- **Dataset:** Flor de Aço: Dados contra o Feminicídio 
- **Link:** https://www.kaggle.com/datasets/rafatrindade/feminicidio-br
- **Contexto/origem (resumo):** O objetivo desta coleta de dados é oferecer uma visão detalhada dos casos de feminicídios no Brasil, sendo possível analisar o perfil das vítimas, contexto e local para ajudar no combate contra este crime.
- **Justificativa da escolha:** Como Março ser marcado pelo dia internacional da mulher e termos registros de altas históricas de feminicídio no país, a escolha dessa _Dataset_ tem o intuito de conscientizar o leitor com a importância da luta contra o feminicidio e a procura de ajuda ao ter conhecimento de possíveis casos no circulo social.

## Objetivo da análise
Construir um dashboard que permita **visualizar e explorar indicadores principais** do dataset escolhido (Kaggle), identificando padrões, comparações e tendências relevantes (ex.: evolução ao longo do tempo, distribuição por categorias, ranking de itens e variações por grupos), apoiando uma leitura rápida por meio de **KPIs, gráficos e filtros**.

## Planejamento do ETL (Pandas + carga)
O pipeline seguirá as etapas: **extração → transformação → carga**, com foco em gerar uma base limpa e estruturada para o dashboard.

### 1) Extração
- Download do dataset via Kaggle (manual ou via API, se necessário).
- Armazenamento do arquivo original em: `data/raw/` (não alterar o arquivo bruto).

### 2) Transformação (tratamentos previstos)
Tratamentos que podem ser aplicados conforme o dataset:
- remoção de duplicados;
- tratamento de valores ausentes (nulos) e padronização de preenchimentos;
- correção de tipos (datas, números, texto);
- padronização de categorias (ex.: nomes com variações, maiúsculas/minúsculas, espaços);
- criação de colunas derivadas (ex.: mês/ano, faixas, totais, médias, indicadores calculados);
- agregações para análises (ex.: total por período/categoria/região; top N; médias e taxas);
- validações básicas (ex.: valores negativos indevidos, datas fora do padrão, outliers evidentes).

### 3) Carga
- Exportação da base tratada para `data/processed/` (CSV/Parquet).
- Opcional: carga em **SQLite** para facilitar consultas e organização da base.

## Ideia inicial do dashboard (Streamlit)
O dashboard será construído no Streamlit para permitir visualização rápida e exploração dos dados.

### KPIs/Indicadores (exemplos — serão confirmados após escolher o dataset)
- total (ex.: casos, perfil, local, período etc)
- média (ex.: casos, perfil, local, período etc)
- contagem (ex.: número de registros, número de categorias)
- ranking Top 5/Top 10 (ex.: itens/regiões/categorias com maiores valores)

### Visualizações previstas (exemplos)
- gráfico de linha (evolução por tempo, se houver data/período);
- gráfico de barras (comparação por categoria/região/produto);
- tabela (Top N e detalhes filtrados);
- distribuição (histograma/boxplot) se fizer sentido para a variável principal.

### Filtros previstos (dependem do dataset)
- período (data/mês/ano) ou grupos equivalentes;
- categoria/tipo;
- região/local;
- outros filtros relevantes (ex.: faixa de preço, status, segmento).

## Estrutura do repositório
- `app/` — aplicação Streamlit (dashboard)
- `data/raw/` — dados brutos (originais)
- `data/processed/` — dados tratados/estruturados
- `notebooks/` — análises exploratórias (Jupyter/Colab)
- `src/` — scripts do ETL e funções auxiliares

## Cronograma até 23/03/2026 (Etapa 1)
- **Semana 1:** criar repo/estrutura + escolher dataset Kaggle + definir objetivo inicial
- **Semana 2:** planejar ETL + definir KPIs/perguntas + rascunhar layout do dashboard
- **Semana 3:** revisar README + garantir coerência (dataset ↔ ETL ↔ KPIs ↔ dashboard) + preparar entrega do link do repo

## Observações
- O dataset do Kaggle é obrigatório para o projeto.
- O foco da Etapa 1 é **planejamento e estruturação** (não é necessário implementar tudo agora).
