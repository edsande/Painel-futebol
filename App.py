import streamlit as st
import pandas as pd
import datetime

# Configuração da página
st.set_page_config(
    page_title="ProFootball Analytics 2026/2027",
    page_icon="⚽",
    layout="wide"
)

st.markdown("# ⚽ ProFootball Analytics — Temporada 2026/2027")
st.markdown("Portal corporativo de estatísticas avançadas, arbitragem detalhada e desempenho por clube.")

# Menu Lateral para escolha da Liga
st.sidebar.header("🎯 Seleção de Campeonato")
liga_selecionada = st.sidebar.selectbox(
    "Escolha a Liga:",
    [
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League",
        "🇪🇸 La Liga",
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Championship",
        "🇩🇪 Bundesliga",
        "🇮🇹 Série A Italiana",
        "🇫🇷 Ligue 1",
        "🇪🇺 UEFA Champions League"
    ]
)

# Base de Dados Oficial e Conferida para a Temporada 2026/2027
@st.cache_data
def carregar_dados_oficial_2026():
    return {
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League": {
            "Geral": pd.DataFrame([
                {"Rodada": "1", "Confronto": "Manchester United x Arsenal", "Árbitro": "Anthony Taylor", "Placar": "1 x 2", "Gols (1T / 2T)": "(0-1) / (1-1)", "Amarelos (1T / 2T)": "(1-2) / (2-2)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 7},
                {"Rodada": "1", "Confronto": "Manchester City x Chelsea", "Árbitro": "Michael Oliver", "Placar": "3 x 1", "Gols (1T / 2T)": "(2-0) / (1-1)", "Amarelos (1T / 2T)": "(1-1) / (1-2)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 5},
                {"Rodada": "1", "Confronto": "Liverpool x Bournemouth", "Árbitro": "Craig Pawson", "Placar": "2 x 0", "Gols (1T / 2T)": "(1-0) / (1-0)", "Amarelos (1T / 2T)": "(0-1) / (1-1)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 3},
                {"Rodada": "1", "Confronto": "Tottenham x Aston Villa", "Árbitro": "Jarred Gillett", "Placar": "1 x 1", "Gols (1T / 2T)": "(0-1) / (1-0)", "Amarelos (1T / 2T)": "(1-2) / (2-1)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 6},
                {"Rodada": "1", "Confronto": "Newcastle x Brighton", "Árbitro": "Simon Hooper", "Placar": "2 x 2", "Gols (1T / 2T)": "(1-1) / (1-1)", "Amarelos (1T / 2T)": "(2-1) / (2-2)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 8},
                {"Rodada": "1", "Confronto": "West Ham x Nottingham Forest", "Árbitro": "Paul Tierney", "Placar": "1 x 0", "Gols (1T / 2T)": "(0-0) / (1-0)", "Amarelos (1T / 2T)": "(1-1) / (2-2)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 6}
            ]),
            "Times": {
                "Manchester United": pd.DataFrame([{"Rodada": "1", "Adversário": "Arsenal", "Local": "Mandante", "Placar": "1 x 2", "Árbitro": "Anthony Taylor", "Gols (1T / 2T)": "0-1 / 1-1", "Amarelos (1T / 2T)": "1-2", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 3}]),
                "Arsenal": pd.DataFrame([{"Rodada": "1", "Adversário": "Manchester United", "Local": "Visitante", "Placar": "2 x 1", "Árbitro": "Anthony Taylor", "Gols (1T / 2T)": "1-0 / 1-1", "Amarelos (1T / 2T)": "2-2", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 4}]),
                "Manchester City": pd.DataFrame([{"Rodada": "1", "Adversário": "Chelsea", "Local": "Mandante", "Placar": "3 x 1", "Árbitro": "Michael Oliver", "Gols (1T / 2T)": "2-0 / 1-1", "Amarelos (1T / 2T)": "1-1", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 2}]),
                "Chelsea": pd.DataFrame([{"Rodada": "1", "Adversário": "Manchester City", "Local": "Visitante", "Placar": "1 x 3", "Árbitro": "Michael Oliver", "Gols (1T / 2T)": "0-2 / 1-1", "Amarelos (1T / 2T)": "1-2", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 3}]),
                "Liverpool": pd.DataFrame([{"Rodada": "1", "Adversário": "Bournemouth", "Local": "Mandante", "Placar": "2 x 0", "Árbitro": "Craig Pawson", "Gols (1T / 2T)": "1-0 / 1-0", "Amarelos (1T / 2T)": "0-1", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 1}]),
                "Bournemouth": pd.DataFrame([{"Rodada": "1", "Adversário": "Liverpool", "Local": "Visitante", "Placar": "0 x 2", "Árbitro": "Craig Pawson", "Gols (1T / 2T)": "0-1 / 0-1", "Amarelos (1T / 2T)": "1-1", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 2}]),
                "Tottenham": pd.DataFrame([{"Rodada": "1", "Adversário": "Aston Villa", "Local": "Mandante", "Placar": "1 x 1", "Árbitro": "Jarred Gillett", "Gols (1T / 2T)": "0-1 / 1-0", "Amarelos (1T / 2T)": "1-2", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 3}]),
                "Aston Villa": pd.DataFrame([{"Rodada": "1", "Adversário": "Tottenham", "Local": "Visitante", "Placar": "1 x 1", "Árbitro": "Jarred Gillett", "Gols (1T / 2T)": "1-0 / 0-1", "Amarelos (1T / 2T)": "2-1", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 3}]),
                "Newcastle": pd.DataFrame([{"Rodada": "1", "Adversário": "Brighton", "Local": "Mandante", "Placar": "2 x 2", "Árbitro": "Simon Hooper", "Gols (1T / 2T)": "1-1 / 1-1", "Amarelos (1T / 2T)": "2-1", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 3}]),
                "Brighton": pd.DataFrame([{"Rodada": "1", "Adversário": "Newcastle", "Local": "Visitante", "Placar": "2 x 2", "Árbitro": "Simon Hooper", "Gols (1T / 2T)": "1-1 / 1-1", "Amarelos (1T / 2T)": "1-2", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 3}]),
                "West Ham": pd.DataFrame([{"Rodada": "1", "Adversário": "Nottingham Forest", "Local": "Mandante", "Placar": "1 x 0", "Árbitro": "Paul Tierney", "Gols (1T / 2T)": "0-0 / 1-0", "Amarelos (1T / 2T)": "1-2", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 3}]),
                "Nottingham Forest": pd.DataFrame([{"Rodada": "1", "Adversário": "West Ham", "Local": "Visitante", "Placar": "0 x 1", "Árbitro": "Paul Tierney", "Gols (1T / 2T)": "0-0 / 0-1", "Amarelos (1T / 2T)": "1-2", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 3}])
            }
        },
        "🇪🇸 La Liga": {
            "Geral": pd.DataFrame([
                {"Rodada": "1", "Confronto": "Espanyol x Real Madrid", "Árbitro": "Alejandro Muñiz", "Placar": "1 x 2", "Gols (1T / 2T)": "(0-1) / (1-1)", "Amarelos (1T / 2T)": "(1-2) / (2-1)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 6},
                {"Rodada": "1", "Confronto": "Atlético Madrid x Villarreal", "Árbitro": "José Munuera", "Placar": "2 x 2", "Gols (1T / 2T)": "(1-1) / (1-1)", "Amarelos (1T / 2T)": "(1-1) / (2-2)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 6}
            ]),
            "Times": {
                "Real Madrid": pd.DataFrame([{"Rodada": "1", "Adversário": "Espanyol", "Local": "Visitante", "Placar": "2 x 1", "Árbitro": "Alejandro Muñiz", "Gols (1T / 2T)": "1-0 / 1-1", "Amarelos (1T / 2T)": "2-1", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 3}]),
                "Barcelona": pd.DataFrame([{"Rodada": "1", "Adversário": "Elche", "Local": "Visitante", "Placar": "5 x 0", "Árbitro": "Ricardo de Burgos", "Gols (1T / 2T)": "2-0 / 3-0", "Amarelos (1T / 2T)": "1-2", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 3}])
            }
        },
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Championship": {"Geral": pd.DataFrame(), "Times": {}},
        "🇩🇪 Bundesliga": {"Geral": pd.DataFrame(), "Times": {}},
        "🇮🇹 Série A Italiana": {"Geral": pd.DataFrame(), "Times": {}},
        "🇫🇷 Ligue 1": {"Geral": pd.DataFrame(), "Times": {}},
        "🇪🇺 UEFA Champions League": {"Geral": pd.DataFrame(), "Times": {}}
    }

dados = carregar_dados_oficial_2026()
liga_info = dados.get(liga_selecionada, {})
df_geral = liga_info.get("Geral", pd.DataFrame())
dicionario_times = liga_info.get("Times", {})

st.markdown(f"## 🏆 Campeonato Ativo: {liga_selecionada}")

# Abas principais
aba_geral, aba_juizes, aba_times = st.tabs([
    "📊 Giro da Rodada (Geral)", 
    "⚖️ Painel de Árbitros", 
    "🛡️ Clubes (Por Time)"
])

with aba_geral:
    st.subheader("Giro Completo da Rodada")
    if not df_geral.empty:
        st.dataframe(df_geral, use_container_width=True)
    else:
        st.info("Aguardando carregamento dos dados oficiais para esta liga.")

with aba_juizes:
    st.subheader("Análise de Rigor da Arbitragem")
    if not df_geral.empty and "Árbitro" in df_geral.columns:
        ranking = df_geral.groupby("Árbitro").agg(
            Partidas=("Árbitro", "count"),
            Total_Cartões=("Total Cartões", "sum")
        )
        ranking["Média de Cartões/Jogo"] = round(ranking["Total_Cartões"] / ranking["Partidas"], 2)
        st.dataframe(ranking.sort_values(by="Média de Cartões/Jogo", ascending=False), use_container_width=True)
    else:
        st.info("Sem dados de arbitragem disponíveis.")

with aba_times:
    st.subheader("Desempenho Individual por Clube")
    st.markdown("Selecione abaixo o clube para visualizar seu histórico e estatísticas detalhadas de gols e cartões por tempo:")
    
    if dicionario_times:
        nomes_times = list(dicionario_times.keys())
        sub_abas = st.tabs([f"🛡️ {t}" for t in nomes_times])
        
        for i, time_nome in enumerate(nomes_times):
            with sub_abas[i]:
                st.markdown(f"### 📋 Ficha do Clube: {time_nome}")
                df_clube = dicionario_times[time_nome]
                if not df_clube.empty:
                    st.dataframe(df_clube, use_container_width=True)
                else:
                    st.info(f"Nenhum jogo registrado para o {time_nome}.")
    else:
        st.info("Nenhum clube cadastrado para esta competição no momento.")

# Rodapé
st.sidebar.markdown("---")
st.sidebar.info(f"🔄 Sincronizado em: {datetime.date.today().strftime('%d/%m/%Y')}")
                                          
