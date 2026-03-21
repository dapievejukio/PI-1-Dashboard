# Projeto Integrador - Low Code em Ciência de Dados 
### (Grupo 46)

## Tema do projeto
Dashboard interativo com dados do Kaggle, com pipeline de ETL (Pandas) e visualização em Streamlit.

## Integrantes
- Brunna Stival (@brunnastival)
- Caio Luna (@caioluna)
- Danubio Souza (@Danubio229)
- Franciane Giselle (@itgiselle)
- Hugo Miguel (@hugomfrosa)
- Jhon Diass (@JhonDiass)
- Júlio (@dapievejukio)

## Distribuição de tarefas (a escolher pelo grupo)
As funções abaixo serão escolhidas pelos integrantes , para fechar a Etapa 1:

- **Função A — Base Kaggle:** escolher dataset, link, contexto e justificativa. (Responsável: Jhon Diass / @JhonDiass)
- **Função B — KPIs e perguntas:** definir perguntas do dashboard + 5–8 indicadores + filtros. (Responsável: Caio Luna @caioluna)
- **Função C — Planejamento ETL:** descrever extração → transformações (Pandas) → carga (CSV/SQLite). (responsável: Franciane Giselle @itgiselle)
- **Função D — Ideia do dashboard:** layout (cards + gráficos + tabela) e visualizações.
- **Função E — Revisão final README + cronograma:** consolidar tudo e revisar coerência.
- **Função F — Repo/organização:** manter estrutura, commits e ajustes no GitHub (Responsável inicial: Júlio / @dapievejukio

## Base de dados (Kaggle)
- **Dataset:** Flor de Aço: Dados contra o Feminicídio 
- **Link:** https://www.kaggle.com/datasets/rafatrindade/feminicidio-br
- **Contexto/origem:** O objetivo desta coleta de dados é oferecer uma visão detalhada dos casos de feminicídios no Brasil, sendo possível analisar o perfil das vítimas, contexto e local para ajudar no combate contra este crime.
- **Objetivo da análise:** Sendo o mês de março marcado pelo dia internacional da mulher e termos registros de altas históricas de feminicídio no país, a escolha desse _Dataset_ tem o intuito de conscientizar o leitor com a importância da luta contra o feminicidio e a procura de ajuda ao ter conhecimento de possíveis casos no círculo social.

## Visualizações e métricas desejadas

### Análise Descritiva (compreender o cenário)
- Qual a distribuição etária e racial das vítimas?
- Como é a distribuição entre estados?
  - estado com maior índice por população;
  - estado com menor índice por população.
- Qual o tipo de violência (psicológica, física, sexual) mais declarado pelas mulheres, e quem são os principais agressores?
- Existem padrões sazonais (aumento em meses específicos, fins de semana)?

### Análise Preditiva (antecipar riscos)
- Com base na série histórica, qual a previsão de casos para o próximo ano e para os próximos cinco anos, considerando regiões e raça? (se houver tempo + variáveis)

### Análise Prescritiva (orientar decisões/ações)
- Considerando os perfis de risco identificados, qual deve ser o perfil sociodemográfico alvo de uma campanha de prevenção?
- Em quais municípios ou regiões a alocação de recursos (casas-abrigo, delegacias especializadas) teria maior potencial impacto? (se houver município/região)

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

### KPIs/Indicadores 
	•	Total de registros (casos)
	•	Casos por período (ano/mês, se existir no dataset)
	•	Casos por UF/município (se existir)
	•	Distribuição por faixa etária (se existir)
	•	Distribuição por local do crime (se existir)
	•	Top 5 categorias mais frequentes (ex.: meio, contexto, relação — conforme colunas do dataset)

### Visualizações previstas 
	•	Linha: evolução de casos por período (se houver data/ano/mês)
	•	Barras: comparação por UF/município e/ou local do crime
	•	Pizza/Barras: distribuição por faixa etária / categorias relevantes
	•	Tabela: Top N (UFs/municípios/categorias) com contagem

### Filtros previstos (dependem do dataset)
	•	Período (ano/mês) se aplicável
	•	UF/município se aplicável
	•	Faixa etária se aplicável
	•	Categoria/Tipo / conforme colunas

## Estrutura do repositório
- `app/` — aplicação Streamlit (dashboard)
- `data/raw/` — dados brutos (originais)
- `data/processed/` — dados tratados/estruturados
- `notebooks/` — análises exploratórias (Jupyter/Colab)
- `src/` — scripts do ETL e funções auxiliares

## Cronograma até 23/03/2026 (Etapa 1)
- **Semana 1:** criar repositório/estrutura + escolher dataset Kaggle + definir objetivo inicial
- **Semana 2:** planejar ETL + definir KPIs/perguntas + rascunhar layout do dashboard
- **Semana 3:** revisar README + garantir coerência (dataset ↔ ETL ↔ KPIs ↔ dashboard) + preparar entrega do link do repositório
