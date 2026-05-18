import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from pathlib import Path

# ──────────────────────────────────────────────
# STYLING
# ──────────────────────────────────────────────

PALETA = {
    'vermelho':  '#c9375a',
    'laranja':   '#e8774a',
    'roxo':      '#7c6af0',
    'verde':     '#3aaa7a',
    'azul':      '#4a9de8',
    'amarelo':   '#e8c84a',
}

SEQUENCIA_CORES = [
    PALETA['vermelho'],
    PALETA['roxo'],
    PALETA['laranja'],
    PALETA['verde'],
    PALETA['azul'],
    PALETA['amarelo'],
]

TEMPLATE_GRAFICO = 'plotly_dark'

def estilo_grafico(fig, altura=400):
    fig.update_layout(
        template=TEMPLATE_GRAFICO,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=altura,
        margin=dict(t=50, b=30, l=20, r=20),
        font=dict(family='sans-serif', size=12),
        legend=dict(orientation='h', yanchor='bottom', y=-0.3, xanchor='center', x=0.5),
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(gridcolor='rgba(255,255,255,0.05)')
    return fig

st.set_page_config(
    page_title='Dashboard — Feminicídio no Brasil',
    page_icon='🌸',
    layout='wide',
)

st.markdown("""
<style>
    [data-testid="stMetricValue"] { font-size: 2rem; color: #c9375a; }
    [data-testid="stMetricLabel"] { font-size: 0.8rem; color: #aaa; }
    [data-testid="stMetricDelta"] { font-size: 0.85rem; }
    .block-container { padding-top: 2rem; }
    h1 { color: #f0eee8; }
    h2, h3 { color: #e0ddd8; }
</style>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────
# CARREGAMENTO DE DADOS
# ──────────────────────────────────────────────

BASE_DIR = Path(__file__).parent.parent
processed = BASE_DIR / 'data' / 'processed'

@st.cache_data
def carregar_dados():
    pns2013 = pd.read_csv(processed / 'pns_violencia_2013_tratado.csv', encoding='UTF-8', sep=';')
    pns2019 = pd.read_csv(processed / 'pns_violencia_2019_tratado.csv', encoding='UTF-8', sep=';')
    serie_historica = pd.read_csv(processed / 'feminicidio_serie_historica_tratado.csv', encoding='UTF-8', sep=';')
    serie_historica['ANO_OBITO'] = serie_historica['DT_OBITO'].astype(str).str[:4]
    return pns2013, pns2019, serie_historica

pns2013, pns2019, serie_historica = carregar_dados()

contagem_estados = serie_historica.groupby(['ESTADO_OBITO', 'ANO_OBITO']).size().reset_index(name='Óbitos')
contagem_estados['ANO_OBITO'] = contagem_estados['ANO_OBITO'].astype(str)
contagem_estados = contagem_estados[contagem_estados['ANO_OBITO'].isin(['2013', '2019'])]

# ──────────────────────────────────────────────
# SIDEBAR
# ──────────────────────────────────────────────

with st.sidebar:
    st.title('🌸 Flor de Ferro')
    st.caption('Dashboard interativo sobre violência e feminicídio no Brasil')
    st.divider()
    pagina = st.radio(
        'Navegar para:',
        ['Perfil & Violência', 'Série Histórica', 'Insights & Prevenção'],
    )
    st.divider()
    st.caption('Fontes: PNS 2013/2019 · SIM/DATASUS 2006–2024')

# ──────────────────────────────────────────────
# SEÇÃO 1 — PERFIL & VIOLÊNCIA
# ──────────────────────────────────────────────

def gerarGraficos1():
    st.title('Perfil & Violência')
    st.caption('Dados das Pesquisas Nacionais de Saúde (PNS) 2013 e 2019 — mulheres que relataram ter sofrido violência.')

    aba2013, aba2019 = st.tabs(['📋 PNS 2013', '📋 PNS 2019'])

    with aba2013:
        st.subheader('Dados registrados — PNS 2013')

        contagemFE = pns2013['Faixa Etária'].value_counts().reset_index()
        contagemFE.columns = ['Faixa Etária', 'Vítimas']

        cruzamento2013 = pns2013.groupby(['Faixa Etária', 'Tipo de violência']).size().reset_index(name='Vítimas')

        cruzamento_cor_raca2013 = pns2013['Cor ou raça'].value_counts().reset_index()
        cruzamento_cor_raca2013.columns = ['Cor ou raça', 'Vítimas']

        contagem_autor_2013 = pns2013['Autor da violência'].value_counts().reset_index()
        contagem_autor_2013.columns = ['Autor da violência', 'Casos']

        contagem_local_2013 = pns2013['Local da violência'].value_counts().nlargest(5).reset_index()
        contagem_local_2013.columns = ['Local da violência', 'Casos']

        col1, col2 = st.columns(2)
        with col1:
            fig = px.bar(
                contagemFE.sort_values('Faixa Etária'),
                x='Faixa Etária', y='Vítimas',
                title='Distribuição por Faixa Etária',
                color_discrete_sequence=[PALETA['roxo']],
            )
            st.plotly_chart(estilo_grafico(fig), use_container_width=True)

        with col2:
            fig = px.pie(
                cruzamento_cor_raca2013,
                values='Vítimas', names='Cor ou raça',
                title='Distribuição por Cor ou Raça',
                color_discrete_sequence=SEQUENCIA_CORES,
                hole=0.4,
            )
            st.plotly_chart(estilo_grafico(fig), use_container_width=True)

        fig = px.bar(
            cruzamento2013,
            x='Faixa Etária', y='Vítimas',
            color='Tipo de violência',
            title='Tipo de Violência por Faixa Etária',
            barmode='group',
            color_discrete_sequence=SEQUENCIA_CORES,
        )
        st.plotly_chart(estilo_grafico(fig), use_container_width=True)

        fig = px.density_heatmap(
            pns2013.sort_values('Faixa Etária'),
            x='Faixa Etária', y='Cor ou raça',
            title='Perfil Combinado: Faixa Etária × Cor ou Raça',
            color_continuous_scale=['#1a1a2e', PALETA['roxo'], PALETA['vermelho']],
        )
        st.plotly_chart(estilo_grafico(fig), use_container_width=True)

        col3, col4 = st.columns(2)
        with col3:
            fig = px.bar(
                contagem_autor_2013,
                x='Casos', y='Autor da violência',
                orientation='h',
                title='Autor da Violência',
                color_discrete_sequence=[PALETA['vermelho']],
            )
            st.plotly_chart(estilo_grafico(fig), use_container_width=True)

        with col4:
            fig = px.bar(
                contagem_local_2013,
                x='Casos', y='Local da violência',
                orientation='h',
                title='Local de Ocorrência (Top 5)',
                color_discrete_sequence=[PALETA['laranja']],
            )
            st.plotly_chart(estilo_grafico(fig), use_container_width=True)

    with aba2019:
        st.subheader('Dados registrados — PNS 2019')

        contagemFE2 = pns2019['Faixa Etária'].value_counts().reset_index()
        contagemFE2.columns = ['Faixa Etária', 'Vítimas']

        cruzamento2019 = pns2019.groupby(['Faixa Etária', 'Tipo de violência']).size().reset_index(name='Vítimas')

        cruzamento_cor_raca2019 = pns2019['Cor ou raça'].value_counts().reset_index()
        cruzamento_cor_raca2019.columns = ['Cor ou raça', 'Vítimas']

        col1, col2 = st.columns(2)
        with col1:
            fig = px.bar(
                contagemFE2.sort_values('Faixa Etária'),
                x='Faixa Etária', y='Vítimas',
                title='Distribuição por Faixa Etária',
                color_discrete_sequence=[PALETA['roxo']],
            )
            st.plotly_chart(estilo_grafico(fig), use_container_width=True)

        with col2:
            fig = px.pie(
                cruzamento_cor_raca2019,
                values='Vítimas', names='Cor ou raça',
                title='Distribuição por Cor ou Raça',
                color_discrete_sequence=SEQUENCIA_CORES,
                hole=0.4,
            )
            st.plotly_chart(estilo_grafico(fig), use_container_width=True)

        fig = px.bar(
            cruzamento2019,
            x='Faixa Etária', y='Vítimas',
            color='Tipo de violência',
            title='Tipo de Violência por Faixa Etária',
            barmode='group',
            color_discrete_sequence=SEQUENCIA_CORES,
        )
        st.plotly_chart(estilo_grafico(fig), use_container_width=True)

        fig = px.density_heatmap(
            pns2019.sort_values('Faixa Etária'),
            x='Faixa Etária', y='Cor ou raça',
            title='Perfil Combinado: Faixa Etária × Cor ou Raça',
            color_continuous_scale=['#1a1a2e', PALETA['roxo'], PALETA['vermelho']],
        )
        st.plotly_chart(estilo_grafico(fig), use_container_width=True)

        contagem_autor_2019 = pns2019['Autor'].value_counts().nlargest(5).reset_index()
        contagem_autor_2019.columns = ['Autor da violência', 'Casos']

        contagem_local_2019 = pns2019['Local'].value_counts().nlargest(5).reset_index()
        contagem_local_2019.columns = ['Local da violência', 'Casos']

        col3, col4 = st.columns(2)
        with col3:
                fig = px.bar(
                    contagem_autor_2019,
                    x='Casos', y='Autor da violência',
                    orientation='h',
                    title='Autor da Violência',
                    color_discrete_sequence=[PALETA['vermelho']],
                )
                st.plotly_chart(estilo_grafico(fig), use_container_width=True)

        with col4:
            fig = px.bar(
                contagem_local_2019,
                x='Casos', y='Local da violência',
                orientation='h',
                title='Local de Ocorrência (Top 5)',
                color_discrete_sequence=[PALETA['laranja']],
            )
            st.plotly_chart(estilo_grafico(fig), use_container_width=True)

# ──────────────────────────────────────────────
# SEÇÃO 2 — SÉRIE HISTÓRICA
# ──────────────────────────────────────────────

def gerarGraficos2():
    st.title('Série Histórica')
    st.caption('Registros de óbitos por causas externas em mulheres — SIM/DATASUS, 2006 a 2024.')

    st.info('ℹ️ Os dados desta seção referem-se a **óbitos registrados**, não a casos de violência em geral. Um óbito registrado não equivale necessariamente a um feminicídio reconhecido judicialmente.')

    geojson = requests.get(
        'https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson'
    ).json()

    contagem_casos_ano = serie_historica.groupby('ANO_OBITO').size().reset_index(name='Óbitos')

    fig_linha = px.line(
        contagem_casos_ano,
        x='ANO_OBITO', y='Óbitos',
        title='Evolução Anual de Óbitos — Brasil (2006–2024)',
        markers=True,
        color_discrete_sequence=[PALETA['vermelho']],
    )
    fig_linha.add_hline(
        y=contagem_casos_ano['Óbitos'].mean(),
        line_dash='dash',
        line_color=PALETA['roxo'],
        annotation_text=f"Média: {int(contagem_casos_ano['Óbitos'].mean())}",
        annotation_position='bottom right',
    )
    st.plotly_chart(estilo_grafico(fig_linha, altura=380), use_container_width=True)

    st.divider()
    st.subheader('Distribuição por Estado — 2013 vs 2019')
    st.caption('Os mapas abaixo comparam os óbitos por estado nos dois anos das pesquisas PNS. A escala de cores é independente entre os mapas.')

    col1, col2 = st.columns(2)
    with col1:
        fig_mapa_2013 = px.choropleth(
            contagem_estados[contagem_estados['ANO_OBITO'] == '2013'],
            geojson=geojson,
            locations='ESTADO_OBITO',
            featureidkey='properties.sigla',
            color='Óbitos',
            title='Óbitos por Estado — 2013',
            color_continuous_scale=[PALETA['roxo'], PALETA['vermelho']],
        )
        fig_mapa_2013.update_layout(geo=dict(fitbounds='locations', visible=False))
        st.plotly_chart(estilo_grafico(fig_mapa_2013, altura=420), use_container_width=True)

    with col2:
        fig_mapa_2019 = px.choropleth(
            contagem_estados[contagem_estados['ANO_OBITO'] == '2019'],
            geojson=geojson,
            locations='ESTADO_OBITO',
            featureidkey='properties.sigla',
            color='Óbitos',
            title='Óbitos por Estado — 2019',
            color_continuous_scale=[PALETA['roxo'], PALETA['vermelho']],
        )
        fig_mapa_2019.update_layout(geo=dict(fitbounds='locations', visible=False))
        st.plotly_chart(estilo_grafico(fig_mapa_2019, altura=420), use_container_width=True)

    st.divider()
    st.subheader('Sazonalidade')
    st.caption('Soma de todos os óbitos por mês ao longo de todo o período (2006–2024). Permite identificar se há padrão de concentração em épocas específicas do ano.')

    meses = {
        '01': 'Jan', '02': 'Fev', '03': 'Mar', '04': 'Abr',
        '05': 'Mai', '06': 'Jun', '07': 'Jul', '08': 'Ago',
        '09': 'Set', '10': 'Out', '11': 'Nov', '12': 'Dez',
    }
    ordem_meses = list(meses.values())

    serie_historica['MES_OBITO'] = serie_historica['DT_OBITO'].astype(str).str[5:7].map(meses)
    contagem_sazonal = serie_historica.groupby('MES_OBITO').size().reset_index(name='Óbitos')
    contagem_sazonal['MES_OBITO'] = pd.Categorical(contagem_sazonal['MES_OBITO'], categories=ordem_meses, ordered=True)
    contagem_sazonal = contagem_sazonal.sort_values('MES_OBITO')

    fig_sazonal = px.bar(
        contagem_sazonal,
        x='MES_OBITO', y='Óbitos',
        title='Sazonalidade — Óbitos por Mês (acumulado 2006–2024)',
        color_discrete_sequence=[PALETA['laranja']],
    )
    fig_sazonal.add_hline(
        y=contagem_sazonal['Óbitos'].mean(),
        line_dash='dash',
        line_color=PALETA['verde'],
        annotation_text='Média mensal',
        annotation_position='bottom right',
    )
    st.plotly_chart(estilo_grafico(fig_sazonal, altura=360), use_container_width=True)

# ──────────────────────────────────────────────
# SEÇÃO 3 — INSIGHTS & PREVENÇÃO
# ──────────────────────────────────────────────

def gerarGraficos3():
    st.title('Insights & Prevenção')
    st.caption('Indicadores-chave e orientações prescritivas baseadas nos dados analisados.')

    st.subheader('Indicadores Gerais')

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric('Total de óbitos (série)', '77.851', '2006–2024')
    with col2:
        st.metric('Pico histórico', '4.751', 'em 2017')
    with col3:
        st.metric('Último ano registrado', '3.490', '−26% desde o pico ↓', delta_color='inverse')
    with col4:
        st.metric('Não registraram ocorrência', '91,6%', 'das vítimas em 2013')

    st.divider()

    col_a, col_b = st.columns(2)

    with col_a:
        st.subheader('📍 Perfil de Maior Risco')
        st.markdown("""
Com base nos dados das PNS 2013 e 2019, o perfil com maior concentração de casos é:

- **Faixa etária:** 18 a 29 anos
- **Cor ou raça:** Parda
- **Área:** Urbana
- **Tipo de violência predominante:** Psicológica, seguida de física
- **Agressor mais citado (2013):** Pessoa desconhecida / bandido
- **Local mais citado:** Via pública (2013) e Residência (2019)

> ⚠️ A mudança no local entre 2013 e 2019 pode indicar maior exposição ao ambiente doméstico ou mudança no perfil de registro.
        """)

    with col_b:
        st.subheader('🎯 Recomendações Prescritivas')
        st.markdown("""
Com base nos padrões identificados, ações prioritárias incluem:

- **Campanhas de prevenção** direcionadas a mulheres jovens (18–29 anos), especialmente pardas e em contexto urbano
- **Ampliação de delegacias especializadas** nos estados com maior concentração histórica: SP, BA, MG, RJ e PE
- **Incentivo à denúncia** — apenas 8,4% das vítimas em 2013 registraram ocorrência, indicando grave subnotificação
- **Atenção ao ambiente doméstico** — em 2019 a residência se tornou o local mais citado, reforçando a necessidade de casas-abrigo
- **Monitoramento de janeiro e dezembro** — meses com maior volume histórico de óbitos na série
        """)

    st.divider()

    st.warning('⚠️ **Subnotificação:** A diferença entre os casos registrados nas pesquisas PNS e os óbitos da série histórica evidencia que a maioria dos casos de violência nunca chega ao sistema de saúde ou de segurança pública. Os números aqui apresentados representam apenas uma fração da realidade.')

    st.subheader('Estados com Maior Volume Histórico de Óbitos')
    top_estados = serie_historica.groupby('ESTADO_OBITO').size().nlargest(10).reset_index(name='Óbitos')
    top_estados.columns = ['Estado', 'Óbitos']

    fig = px.bar(
        top_estados,
        x='Óbitos', y='Estado',
        orientation='h',
        title='Top 10 Estados — Óbitos Acumulados (2006–2024)',
        color_discrete_sequence=[PALETA['vermelho']],
    )
    st.plotly_chart(estilo_grafico(fig, altura=380), use_container_width=True)

# ──────────────────────────────────────────────
# ROTEAMENTO
# ──────────────────────────────────────────────

match pagina:
    case 'Perfil & Violência':
        gerarGraficos1()
    case 'Série Histórica':
        gerarGraficos2()
    case 'Insights & Prevenção':
        gerarGraficos3()
