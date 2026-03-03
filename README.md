# PI-1-Dashboard

## Tema do projeto
Dashboard interativo com dados do Kaggle, com pipeline de ETL (Pandas) e visualização em Streamlit.

## Integrantes e responsabilidades
> Atualizar os nomes/@ quando todos confirmarem.

1. **Júlio (@dapievejukio)** — GitHub/Repo (estrutura, permissões, organização do repositório e padronização)
2. **Jhon Diass (@JhonDiass)** — Base do Kaggle (seleção do dataset, contexto/origem e objetivo)
3. **Caio Luna (@caioluna)** — Planejamento do ETL (extração, transformação com Pandas e carga)
4. **Integrante 4 (a confirmar)** — Métricas e perguntas do dashboard (KPIs e análises)
5. **Integrante 5 (a confirmar)** — Protótipo/ideia do dashboard (layout, gráficos e filtros)
6. **Integrante 6 (a confirmar)** — Revisão do README + cronograma (consolidação final)

## Base de dados (Kaggle)
- **Dataset:** A definir (responsável: @JhonDiass)
- **Link:** A definir
- **Contexto/origem (resumo):** A definir (2–4 linhas)
- **Justificativa da escolha:** A definir (1–2 linhas)

### Critérios para escolher o dataset (orientação do grupo)
Para garantir um dashboard “forte” e um ETL realista, o dataset deve ter:
- volume de dados suficiente (não apenas poucas linhas);
- ao menos 1 dimensão temporal (data/mês/ano) **ou** algum eixo de comparação equivalente;
- pelo menos 2 campos categóricos (ex.: categoria, região, produto, tipo);
- campos numéricos para KPIs (ex.: vendas, preço, quantidade, nota, custo).

## Objetivo da análise
Construir um dashboard que permita **visualizar e explorar indicadores principais** do dataset escolhido (Kaggle), identificando padrões, comparações e tendências relevantes (ex.: evolução ao longo do tempo, distribuição por categorias, ranking de itens e variações por grupos), apoiando uma leitura rápida por meio de **KPIs, gráficos e filtros**.

> O objetivo será ajustado quando o dataset for definido, mantendo a coerência com os indicadores possíveis.

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
- total (ex.: total de vendas/ocorrências/receita)
- média (ex.: ticket médio, nota média, valor médio)
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
