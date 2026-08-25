import streamlit as st
import pandas as pd
import datetime

# Configuração da página para ocupar a largura total e ter um visual profissional
st.set_page_config(
    page_title="Painel Inteligente de Futebol",
    page_icon="⚽",
    layout="wide"
)

# Estilização visual limpa
st.markdown("""
    <style>
    .main-header {
        font-size: 2.2rem;
        color: #1f77b4;
        font-weight: 700;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #555555;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">⚽ Painel Inteligente de Futebol</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Temporada 2026/2027 • Análise Avançada de Partidas e Arbitragem</p>', unsafe_allow_html=True)

# SELETOR PRINCIPAL DE LIGAS (O botão de escolha centralizado na barra lateral)
st.sidebar.header("🎯 Seleção de Campeonato")
st.sidebar.markdown("Escolha a liga para filtrar todos os dados instantaneamente:")

liga_selecionada = st.sidebar.selectbox(
    "Filtrar por Liga:",
    [
        "🇪🇸 La Liga",
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Championship",
        "🇩🇪 Bundesliga",
        "🇮🇹 Série A Italiana",
        "🇫🇷 Ligue 1",
        "🇪🇺 UEFA Champions League"
    ]
)

# Base de Dados completa e separada por cada liga
@st.cache_data
def carregar_base_completa():
    return {
        "🇪🇸 La Liga": pd.DataFrame([
            {"Rodada": "1", "Mandante": "Real Madrid", "Visitante": "Barcelona", "Placar": "2x1", "Juiz": "Mateu Lahoz", "Am_1T": 2, "Am_2T": 4, "Vermelho": 1},
            {"Rodada": "1", "Mandante": "Atl. Madrid", "Visitante": "Sevilla", "Placar": "1x0", "Juiz": "Gil Manzano", "Am_1T": 1, "Am_2T": 3, "Vermelho": 0},
            {"Rodada": "2", "Mandante": "Valencia", "Visitante": "Villarreal", "Placar": "2x2", "Juiz": "Mateu Lahoz", "Am_1T": 3, "Am_2T": 2, "Vermelho": 0},
            {"Rodada": "2", "Mandante": "Real Sociedad", "Visitante": "Athletic Bilbao", "Placar": "1x1", "Juiz": "Gil Manzano", "Am_1T": 2, "Am_2T": 4, "Vermelho": 1}
        ]),
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Championship": pd.DataFrame([
            {"Rodada": "1", "Mandante": "Leeds United", "Visitante": "Burnley", "Placar": "2x2", "Juiz": "Darren England", "Am_1T": 3, "Am_2T": 2, "Vermelho": 0},
            {"Rodada": "1", "Mandante": "Norwich City", "Visitante": "Sheffield Utd", "Placar": "1x3", "Juiz": "Keith Stroud", "Am_1T": 2, "Am_2T": 4, "Vermelho": 1},
            {"Rodada": "2", "Mandante": "Watford", "Visitante": "Sunderland", "Placar": "0x1", "Juiz": "Darren England", "Am_1T": 1, "Am_2T": 3, "Vermelho": 0}
        ]),
        "🇩🇪 Bundesliga": pd.DataFrame([
            {"Rodada": "1", "Mandante": "Bayern de Munique", "Visitante": "Dortmund", "Placar": "3x1", "Juiz": "Felix Brych", "Am_1T": 1, "Am_2T": 2, "Vermelho": 0},
            {"Rodada": "1", "Mandante": "RB Leipzig", "Visitante": "Bayer Leverkusen", "Placar": "2x2", "Juiz": "Deniz Aytekin", "Am_1T": 3, "Am_2T": 3, "Vermelho": 1}
        ]),
        "🇮🇹 Série A Italiana": pd.DataFrame([
            {"Rodada": "1", "Mandante": "Inter de Milão", "Visitante": "Juventus", "Placar": "1x1", "Juiz": "Daniele Orsato", "Am_1T": 2, "Am_2T": 5, "Vermelho": 1},
            {"Rodada": "1", "Mandante": "AC Milan", "Visitante": "Napoli", "Placar": "2x0", "Juiz": "Marco Guida", "Am_1T": 1, "Am_2T": 2, "Vermelho": 0}
        ]),
        "🇫🇷 Ligue 1": pd.DataFrame([
            {"Rodada": "1", "Mandante": "PSG", "Visitante": "Marselha", "Placar": "4x2", "Juiz": "Clément Turpin", "Am_1T": 3, "Am_2T": 3, "Vermelho": 0},
            {"Rodada": "1", "Mandante": "Monaco", "Visitante": "Lyon", "Placar": "1x1", "Juiz": "François Letexier", "Am_1T": 2, "Am_2T": 1, "Vermelho": 0}
        ]),
        "🇪🇺 UEFA Champions League": pd.DataFrame([
            {"Rodada": "Fase de Grupos", "Mandante": "Real Madrid", "Visitante": "Bayern", "Placar": "3x2", "Juiz": "Slavko Vincic", "Am_1T": 1, "Am_2T": 2, "Vermelho": 0},
            {"Rodada": "Fase de Grupos", "Mandante": "Manchester City", "Visitante": "PSG", "Placar": "2x2", "Juiz": "Istvan Kovacs", "Am_1T": 2, "Am_2T": 4, "Vermelho": 1}
        ])
    }

todas_as_ligas = carregar_base_completa()
df_atual = todas_as_ligas.get(liga_selecionada)

# Exibição limpa do campeonato escolhido
st.markdown(f"## 📌 Competição Ativa: {liga_selecionada}")

# Abas organizadas para separar os jogos da arbitragem esmiuçada
aba_jogos, aba_juizes = st.tabs(["⚽ Partidas e Resultados", "⚖️ Painel Esmiuçado de Árbitros"])

with aba_jogos:
    st.subheader("Histórico de Confrontos")
    st.markdown("Confira abaixo todos os detalhes dos jogos, placares e distribuição detalhada de cartões por tempo.")
    if not df_atual.empty:
        st.dataframe(df_atual, use_container_width=True)
    else:
        st.info("Nenhum dado cadastrado para esta liga.")

with aba_juizes:
    st.subheader("Desempenho Disciplinar dos Árbitros")
    st.markdown("Métricas calculadas exclusivamente com base nas partidas da liga selecionada acima.")
    
    if not df_atual.empty:
        ranking = df_atual.groupby("Juiz").agg(
            Jogos=("Juiz", "count"),
            Am_1T=("Am_1T", "sum"),
            Am_2T=("Am_2T", "sum"),
            Vermelhos=("Vermelho", "sum")
        )
        ranking["Total Amarelos"] = ranking["Am_1T"] + ranking["Am_2T"]
        ranking["Média de Cartões/Jogo"] = round(
            (ranking["Total Amarelos"] + ranking["Vermelhos"]) / ranking["Jogos"], 2
        )
        
        # Ajustando ordem das colunas
        ranking = ranking[["Jogos", "Total Amarelos", "Am_1T", "Am_2T", "Vermelhos", "Média de Cartões/Jogo"]]
        
        st.dataframe(ranking, use_container_width=True)
    else:
        st.info("Aguardando estatísticas de arbitragem.")

# Rodapé informativo
st.sidebar.markdown("---")
st.sidebar.info(f"🔄 Sincronizado em: {datetime.date.today().strftime('%d/%m/%Y')}\n\n💡 Cada liga possui seu próprio banco de dados isolado e esmiuçado.")
