import streamlit as st
import pandas as pd
import datetime

# Configuração da página em modo expandido
st.set_page_config(
    page_title="ProFootball Analytics | Ligas & Clubes",
    page_icon="⚽",
    layout="wide"
)

# Título Principal
st.markdown("# ⚽ ProFootball Analytics & Club Hub")
st.markdown("Sistema avançado de monitoramento de partidas, estatísticas de arbitragem e desempenho por clube.")

# Menu Lateral de Seleção do Campeonato
st.sidebar.header("🎯 Seleção Principal")
liga_selecionada = st.sidebar.selectbox(
    "Escolha o Campeonato:",
    [
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Championship",
        "🇪🇸 La Liga",
        "🇩🇪 Bundesliga",
        "🇮🇹 Série A Italiana",
        "🇫🇷 Ligue 1",
        "🇪🇺 UEFA Champions League"
    ]
)

# Base de Dados detalhada contendo os times de cada liga
@st.cache_data
def carregar_base_por_times():
    return {
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Championship": {
            "Geral": pd.DataFrame([
                {"Rodada": "1", "Mandante": "Leeds United", "Visitante": "Burnley", "Placar": "2x2", "Juiz": "Darren England", "Am_1T": 3, "Am_2T": 2, "Vermelho": 0},
                {"Rodada": "1", "Mandante": "Norwich City", "Visitante": "Sheffield Utd", "Placar": "1x3", "Juiz": "Keith Stroud", "Am_1T": 2, "Am_2T": 4, "Vermelho": 1},
                {"Rodada": "2", "Mandante": "Watford", "Visitante": "Southampton", "Placar": "2x1", "Juiz": "Tony Harrington", "Am_1T": 2, "Am_2T": 6, "Vermelho": 0},
                {"Rodada": "2", "Mandante": "Millwall", "Visitante": "Norwich City", "Placar": "3x0", "Juiz": "James Linington", "Am_1T": 1, "Am_2T": 1, "Vermelho": 1}
            ]),
            "Times": {
                "Leeds United": pd.DataFrame([{"Rodada": "1", "Adversário": "Burnley", "Local": "Mandante", "Placar": "2x2", "Juiz": "Darren England", "Cartões": 3}]),
                "Burnley": pd.DataFrame([{"Rodada": "1", "Adversário": "Leeds United", "Local": "Visitante", "Placar": "2x2", "Juiz": "Darren England", "Cartões": 2}]),
                "Norwich City": pd.DataFrame([
                    {"Rodada": "1", "Adversário": "Sheffield Utd", "Local": "Mandante", "Placar": "1x3", "Juiz": "Keith Stroud", "Cartões": 2},
                    {"Rodada": "2", "Adversário": "Millwall", "Local": "Visitante", "Placar": "0x3", "Juiz": "James Linington", "Cartões": 3}
                ]),
                "Watford": pd.DataFrame([{"Rodada": "2", "Adversário": "Southampton", "Local": "Mandante", "Placar": "2x1", "Juiz": "Tony Harrington", "Cartões": 4}]),
                "West Bromwich": pd.DataFrame(),
                "Sheffield Utd": pd.DataFrame([{"Rodada": "1", "Adversário": "Norwich City", "Local": "Visitante", "Placar": "3x1", "Juiz": "Keith Stroud", "Cartões": 3}]),
                "Southampton": pd.DataFrame([{"Rodada": "2", "Adversário": "Watford", "Local": "Visitante", "Placar": "1x2", "Juiz": "Tony Harrington", "Cartões": 4}]),
                "Millwall": pd.DataFrame([{"Rodada": "2", "Adversário": "Norwich City", "Local": "Mandante", "Placar": "3x0", "Juiz": "James Linington", "Cartões": 1}])
            }
        },
        "🇪🇸 La Liga": {
            "Geral": pd.DataFrame([
                {"Rodada": "1", "Mandante": "Real Madrid", "Visitante": "Barcelona", "Placar": "2x1", "Juiz": "Mateu Lahoz", "Am_1T": 2, "Am_2T": 4, "Vermelho": 1},
                {"Rodada": "1", "Mandante": "Atl. Madrid", "Visitante": "Sevilla", "Placar": "1x0", "Juiz": "Gil Manzano", "Am_1T": 1, "Am_2T": 3, "Vermelho": 0}
            ]),
            "Times": {
                "Real Madrid": pd.DataFrame([{"Rodada": "1", "Adversário": "Barcelona", "Local": "Mandante", "Placar": "2x1", "Juiz": "Mateu Lahoz", "Cartões": 3}]),
                "Barcelona": pd.DataFrame([{"Rodada": "1", "Adversário": "Real Madrid", "Local": "Visitante", "Placar": "1x2", "Juiz": "Mateu Lahoz", "Cartões": 3}]),
                "Atl. Madrid": pd.DataFrame([{"Rodada": "1", "Adversário": "Sevilla", "Local": "Mandante", "Placar": "1x0", "Juiz": "Gil Manzano", "Cartões": 2}]),
                "Sevilla": pd.DataFrame([{"Rodada": "1", "Adversário": "Atl. Madrid", "Local": "Visitante", "Placar": "0x1", "Juiz": "Gil Manzano", "Cartões": 2}])
            }
        },
        "🇩🇪 Bundesliga": {
            "Geral": pd.DataFrame([
                {"Rodada": "1", "Mandante": "Bayern de Munique", "Visitante": "Dortmund", "Placar": "3x1", "Juiz": "Felix Brych", "Am_1T": 1, "Am_2T": 2, "Vermelho": 0}
            ]),
            "Times": {
                "Bayern de Munique": pd.DataFrame([{"Rodada": "1", "Adversário": "Dortmund", "Local": "Mandante", "Placar": "3x1", "Juiz": "Felix Brych", "Cartões": 1}]),
                "Dortmund": pd.DataFrame([{"Rodada": "1", "Adversário": "Bayern de Munique", "Local": "Visitante", "Placar": "1x3", "Juiz": "Felix Brych", "Cartões": 2}])
            }
        },
        "🇮🇹 Série A Italiana": {
            "Geral": pd.DataFrame([
                {"Rodada": "1", "Mandante": "Inter de Milão", "Visitante": "Juventus", "Placar": "1x1", "Juiz": "Daniele Orsato", "Am_1T": 2, "Am_2T": 5, "Vermelho": 1}
            ]),
            "Times": {
                "Inter de Milão": pd.DataFrame([{"Rodada": "1", "Adversário": "Juventus", "Local": "Mandante", "Placar": "1x1", "Juiz": "Daniele Orsato", "Cartões": 3}]),
                "Juventus": pd.DataFrame([{"Rodada": "1", "Adversário": "Inter de Milão", "Local": "Visitante", "Placar": "1x1", "Juiz": "Daniele Orsato", "Cartões": 4}])
            }
        },
        "🇫🇷 Ligue 1": {
            "Geral": pd.DataFrame([
                {"Rodada": "1", "Mandante": "PSG", "Visitante": "Marselha", "Placar": "4x2", "Juiz": "Clément Turpin", "Am_1T": 3, "Am_2T": 3, "Vermelho": 0}
            ]),
            "Times": {
                "PSG": pd.DataFrame([{"Rodada": "1", "Adversário": "Marselha", "Local": "Mandante", "Placar": "4x2", "Juiz": "Clément Turpin", "Cartões": 2}]),
                "Marselha": pd.DataFrame([{"Rodada": "1", "Adversário": "PSG", "Local": "Visitante", "Placar": "2x4", "Juiz": "Clément Turpin", "Cartões": 4}])
            }
        },
        "🇪🇺 UEFA Champions League": {
            "Geral": pd.DataFrame([
                {"Rodada": "Grupo", "Mandante": "Real Madrid", "Visitante": "Bayern", "Placar": "3x2", "Juiz": "Slavko Vincic", "Am_1T": 1, "Am_2T": 2, "Vermelho": 0}
            ]),
            "Times": {
                "Real Madrid": pd.DataFrame([{"Rodada": "Grupo", "Adversário": "Bayern", "Local": "Mandante", "Placar": "3x2", "Juiz": "Slavko Vincic", "Cartões": 1}]),
                "Bayern": pd.DataFrame([{"Rodada": "Grupo", "Adversário": "Real Madrid", "Local": "Visitante", "Placar": "2x3", "Juiz": "Slavko Vincic", "Cartões": 2}])
            }
        }
    }

dados_completos = carregar_base_por_times()
liga_info = dados_completos.get(liga_selecionada, {})
df_geral = liga_info.get("Geral", pd.DataFrame())
dicionario_times = liga_info.get("Times", {})

st.markdown(f"## 🏆 Competição Selecionada: {liga_selecionada}")

# Abas principais da competição: Visão Geral / Árbitros / Seção dedicada aos Times
aba_geral, aba_juizes, aba_times = st.tabs([
    "📊 Visão Geral da Liga", 
    "⚖️ Painel de Árbitros", 
    "🛡️ Desempenho por Time"
])

with aba_geral:
    st.subheader("Partidas da Competição")
    if not df_geral.empty:
        st.dataframe(df_geral, use_container_width=True)
    else:
        st.info("Nenhuma partida registrada para esta liga.")

with aba_juizes:
    st.subheader("Estatísticas de Arbitragem")
    if not df_geral.empty and "Juiz" in df_geral.columns:
        ranking = df_geral.groupby("Juiz").agg(
            Jogos=("Juiz", "count"),
            Amarelos_Total=("Am_1T", lambda x: x.sum() + df_geral.loc[x.index, "Am_2T"].sum()),
            Vermelhos=("Vermelho", "sum")
        )
        ranking["Média Cartões"] = round((ranking["Amarelos_Total"] + ranking["Vermelhos"]) / ranking["Jogos"], 2)
        st.dataframe(ranking, use_container_width=True)
    else:
        st.info("Dados de arbitragem indisponíveis.")

with aba_times:
    st.subheader("Análise Detalhada por Clube")
    st.markdown("Selecione um clube abaixo para abrir o painel exclusivo de desempenho e histórico da equipe:")
    
    if dicionario_times:
        # Criando sub-abas dinâmicas para cada time da liga escolhida
        nomes_times = list(dicionario_times.keys())
        sub_abas_times = st.tabs([f"🛡️ {time}" for time in nomes_times])
        
        for i, nome_time in enumerate(nomes_times):
            with sub_abas_times[i]:
                st.markdown(f"### Histórico de Jogos: {nome_time}")
                df_time = dicionario_times[nome_time]
                
                if not df_time.empty:
                    st.dataframe(df_time, use_container_width=True)
                else:
                    st.info(f"Nenhum jogo registrado para o {nome_time} nesta rodada inicial.")
    else:
        st.info("Nenhum time cadastrado para esta competição.")

# Rodapé
st.sidebar.markdown("---")
st.sidebar.info(f"📅 Atualizado em: {datetime.date.today().strftime('%d/%m/%Y')}")
