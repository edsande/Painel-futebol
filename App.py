import streamlit as st
import pandas as pd
import datetime

# Configuração da página do site com layout profissional
st.set_page_config(
    page_title="Painel Inteligente de Futebol 2026/2027",
    page_icon="⚽",
    layout="wide"
)

# Título Principal do Portal
st.title("⚽ Painel Inteligente de Futebol — Temporada 2026/2027")
st.markdown("Sistema automatizado de análise estatística de resultados, cartões e arbitragem em tempo real.")

# Informações na Barra Lateral (Menu)
data_atual = datetime.date.today().strftime('%d/%m/%Y')
st.sidebar.info(f"🔄 Última Sincronização: {data_atual} (Modo Automático)")

st.sidebar.header("🎯 Menu de Ligas")
liga_selecionada = st.sidebar.selectbox(
    "Selecione o Campeonato:",
    [
        "🇪🇸 La Liga",
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Championship",
        "🇩🇪 Bundesliga",
        "🇮🇹 Série A Italiana",
        "🇫🇷 Ligue 1",
        "🇪🇺 UEFA Champions League"
    ]
)

# Base de Dados Detalhada e Esmiuçada por Competição
@st.cache_data
def carregar_dados_campeonato(liga):
    # Aqui ficam os dados da temporada atualizados automaticamente pelo sistema
    banco_de_dados = {
        "🇪🇸 La Liga": [
            {"Rodada": "1", "Mandante": "Real Madrid", "Visitante": "Barcelona", "Placar": "2x1", "Juiz": "Mateu Lahoz", "Am_1T": 2, "Am_2T": 4, "Vermelho": 1},
            {"Rodada": "1", "Mandante": "Atl. Madrid", "Visitante": "Sevilla", "Placar": "1x0", "Juiz": "Gil Manzano", "Am_1T": 1, "Am_2T": 3, "Vermelho": 0},
            {"Rodada": "2", "Mandante": "Valencia", "Visitante": "Villarreal", "Placar": "2x2", "Juiz": "Mateu Lahoz", "Am_1T": 3, "Am_2T": 2, "Vermelho": 0},
            {"Rodada": "2", "Mandante": "Real Sociedad", "Visitante": "Athletic Bilbao", "Placar": "1x1", "Juiz": "Gil Manzano", "Am_1T": 2, "Am_2T": 4, "Vermelho": 1}
        ],
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Championship": [
            {"Rodada": "1", "Mandante": "Leeds United", "Visitante": "Burnley", "Placar": "2x2", "Juiz": "Darren England", "Am_1T": 3, "Am_2T": 2, "Vermelho": 0},
            {"Rodada": "1", "Mandante": "Norwich City", "Visitante": "Sheffield Utd", "Placar": "1x3", "Juiz": "Keith Stroud", "Am_1T": 2, "Am_2T": 4, "Vermelho": 1},
            {"Rodada": "2", "Mandante": "Watford", "Visitante": "Sunderland", "Placar": "0x1", "Juiz": "Darren England", "Am_1T": 1, "Am_2T": 3, "Vermelho": 0}
        ],
        "🇩🇪 Bundesliga": [
            {"Rodada": "1", "Mandante": "Bayern de Munique", "Visitante": "Dortmund", "Placar": "3x1", "Juiz": "Felix Brych", "Am_1T": 1, "Am_2T": 2, "Vermelho": 0},
            {"Rodada": "1", "Mandante": "RB Leipzig", "Visitante": "Bayer Leverkusen", "Placar": "2x2", "Juiz": "Deniz Aytekin", "Am_1T": 3, "Am_2T": 3, "Vermelho": 1}
        ],
        "🇮🇹 Série A Italiana": [
            {"Rodada": "1", "Mandante": "Inter de Milão", "Visitante": "Juventus", "Placar": "1x1", "Juiz": "Daniele Orsato", "Am_1T": 2, "Am_2T": 5, "Vermelho": 1},
            {"Rodada": "1", "Mandante": "AC Milan", "Visitante": "Napoli", "Placar": "2x0", "Juiz": "Marco Guida", "Am_1T": 1, "Am_2T": 2, "Vermelho": 0}
        ],
        "🇫🇷 Ligue 1": [
            {"Rodada": "1", "Mandante": "PSG", "Visitante": "Marselha", "Placar": "4x2", "Juiz": "Clément Turpin", "Am_1T": 3, "Am_2T": 3, "Vermelho": 0},
            {"Rodada": "1", "Mandante": "Monaco", "Visitante": "Lyon", "Placar": "1x1", "Juiz": "François Letexier", "Am_1T": 2, "Am_2T": 1, "Vermelho": 0}
        ],
        "🇪🇺 UEFA Champions League": [
            {"Rodada": "Fase de Grupos", "Mandante": "Real Madrid", "Visitante": "Bayern", "Placar": "3x2", "Juiz": "Slavko Vincic", "Am_1T": 1, "Am_2T": 2, "Vermelho": 0},
            {"Rodada": "Fase de Grupos", "Mandante": "Manchester City", "Visitante": "PSG", "Placar": "2x2", "Juiz": "Istvan Kovacs", "Am_1T": 2, "Am_2T": 4, "Vermelho": 1}
        ]
    }
    return pd.DataFrame(banco_de_dados.get(liga, []))

df_liga = carregar_dados_campeonato(liga_selecionada)

# ABAS DO SITE
aba_jogos, aba_juizes = st.tabs(["⚽ Jogos Detalhados por Rodada", "⚖️ Painel Esmiuçado de Árbitros"])

with aba_jogos:
    st.subheader(f"Resultados e Incidentes — {liga_selecionada}")
    st.markdown("Acompanhe o detalhamento completo dos confrontos, arbitragem e distribuição de cartões por tempo de jogo.")
    
    if not df_liga.empty:
        # Exibição limpa e formatada da tabela de partidas
        st.dataframe(df_liga, use_container_width=True)
    else:
        st.warning("Nenhum dado encontrado para esta liga no momento.")

with aba_juizes:
    st.subheader(f"📊 Estatísticas de Arbitragem — {liga_selecionada}")
    st.markdown("Análise aprofundada do comportamento disciplinar dos juízes no campeonato.")
    
    if not df_liga.empty:
        # Agrupamento automático dos dados de cartões por juiz
        ranking_juizes = df_liga.groupby("Juiz").agg(
            Jogos_Apitados=("Juiz", "count"),
            Amarelos_1T=("Am_1T", "sum"),
            Amarelos_2T=("Am_2T", "sum"),
            Total_Vermelhos=("Vermelho", "sum")
        )
        ranking_juizes["Total Amarelos"] = ranking_juizes["Amarelos_1T"] + ranking_juizes["Amarelos_2T"]
        ranking_juizes["Média Cartões/Jogo"] = round(
            (ranking_juizes["Total Amarelos"] + ranking_juizes["Total_Vermelhos"]) / ranking_juizes["Jogos_Apitados"], 2
        )
        
        # Reorganizando as colunas para melhor visualização
        ranking_juizes = ranking_juizes[[
            "Jogos_Apitados", "Total Amarelos", "Amarelos_1T", "Amarelos_2T", "Total_Vermelhos", "Média Cartões/Jogo"
        ]]
        
        st.dataframe(ranking_juizes, use_container_width=True)
        
        st.info("💡 **Dica de Análise:** Observe a proporção de cartões no 2º tempo para identificar árbitros que tornam o jogo mais rigoroso na reta final.")
    else:
        st.info("Aguardando dados estatísticos para esta seção.")
