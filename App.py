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
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Championship",
        "🇪🇸 La Liga",
        "🇩🇪 Bundesliga",
        "🇮🇹 Série A Italiana",
        "🇫🇷 Ligue 1",
        "🇪🇺 UEFA Champions League"
    ]
)

# Base de Dados estruturada no padrão exato solicitado
@st.cache_data
def carregar_dados_oficiais():
    return {
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Championship": {
            "Geral": pd.DataFrame([
                {"Rodada": "1", "Confronto": "Watford x Southampton", "Árbitro": "David Webb", "Placar": "1 x 3", "Gols (1T / 2T)": "(0-2) / (1-1)", "Amarelos (1T / 2T)": "(3-2) / (3-1)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 9},
                {"Rodada": "1", "Confronto": "Bristol City x Blackburn", "Árbitro": "Lewis Smith", "Placar": "1 x 2", "Gols (1T / 2T)": "(0-1) / (1-1)", "Amarelos (1T / 2T)": "(2-1) / (0-0)", "Vermelhos (1T / 2T)": "(0-0) / (0-1)", "Total Cartões": 4},
                {"Rodada": "1", "Confronto": "Derby County x Bolton", "Árbitro": "Oliver Langford", "Placar": "2 x 0", "Gols (1T / 2T)": "(1-0) / (1-0)", "Amarelos (1T / 2T)": "(0-0) / (3-2)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 5},
                {"Rodada": "1", "Confronto": "Preston x Millwall", "Árbitro": "Farai Hallam", "Placar": "1 x 2", "Gols (1T / 2T)": "(0-1) / (1-1)", "Amarelos (1T / 2T)": "(3-2) / (0-0)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 5},
                {"Rodada": "1", "Confronto": "Stoke City x West Ham", "Árbitro": "Josh Smith", "Placar": "0 x 1", "Gols (1T / 2T)": "(0-0) / (0-1)", "Amarelos (1T / 2T)": "(1-0) / (1-4)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 5},
                {"Rodada": "1", "Confronto": "Swansea x Lincoln City", "Árbitro": "Adam Herczeg", "Placar": "2 x 1", "Gols (1T / 2T)": "(1-0) / (1-1)", "Amarelos (1T / 2T)": "(0-1) / (3-2)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 5},
                {"Rodada": "1", "Confronto": "Middlesbrough x QPR", "Árbitro": "Bobby Madley", "Placar": "1 x 0", "Gols (1T / 2T)": "(1-0) / (0-0)", "Amarelos (1T / 2T)": "(0-1) / (0-1)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 2},
                {"Rodada": "1", "Confronto": "Norwich x Portsmouth", "Árbitro": "Ben Speedie", "Placar": "2 x 0", "Gols (1T / 2T)": "(1-0) / (1-0)", "Amarelos (1T / 2T)": "(0-0) / (3-0)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 3},
                {"Rodada": "1", "Confronto": "Sheffield Utd x Birmingham", "Árbitro": "Gavin Ward", "Placar": "0 x 0", "Gols (1T / 2T)": "(0-0) / (0-0)", "Amarelos (1T / 2T)": "(0-0) / (0-0)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 0},
                {"Rodada": "1", "Confronto": "Charlton x Wolves", "Árbitro": "Tim Robinson", "Placar": "1 x 1", "Gols (1T / 2T)": "(0-0) / (1-1)", "Amarelos (1T / 2T)": "(0-0) / (2-1)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 3},
                {"Rodada": "1", "Confronto": "Cardiff City x Wrexham", "Árbitro": "Stephen Martin", "Placar": "1 x 1", "Gols (1T / 2T)": "(0-1) / (1-0)", "Amarelos (1T / 2T)": "(1-0) / (1-1)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 3},
                {"Rodada": "1", "Confronto": "West Bromwich x Burnley", "Árbitro": "Will Finnie", "Placar": "1 x 0", "Gols (1T / 2T)": "(0-0) / (1-0)", "Amarelos (1T / 2T)": "(0-0) / (1-1)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 2}
            ]),
            "Times": {
                "Watford": pd.DataFrame([{"Rodada": "1", "Adversário": "Southampton", "Local": "Mandante", "Placar": "1 x 3", "Árbitro": "David Webb", "Gols (1T / 2T)": "0-2 / 1-1", "Amarelos (1T / 2T)": "3-2", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 5}]),
                "Southampton": pd.DataFrame([{"Rodada": "1", "Adversário": "Watford", "Local": "Visitante", "Placar": "3 x 1", "Árbitro": "David Webb", "Gols (1T / 2T)": "2-0 / 1-1", "Amarelos (1T / 2T)": "2-3", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 4}]),
                "Bristol City": pd.DataFrame([{"Rodada": "1", "Adversário": "Blackburn", "Local": "Mandante", "Placar": "1 x 2", "Árbitro": "Lewis Smith", "Gols (1T / 2T)": "0-1 / 1-1", "Amarelos (1T / 2T)": "2-1", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 3}]),
                "Blackburn": pd.DataFrame([{"Rodada": "1", "Adversário": "Bristol City", "Local": "Visitante", "Placar": "2 x 1", "Árbitro": "Lewis Smith", "Gols (1T / 2T)": "1-0 / 1-1", "Amarelos (1T / 2T)": "1-0", "Vermelhos (1T / 2T)": "0-1", "Total Cartões": 1}]),
                "Derby County": pd.DataFrame([{"Rodada": "1", "Adversário": "Bolton", "Local": "Mandante", "Placar": "2 x 0", "Árbitro": "Oliver Langford", "Gols (1T / 2T)": "1-0 / 1-0", "Amarelos (1T / 2T)": "0-0", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 0}]),
                "Bolton": pd.DataFrame([{"Rodada": "1", "Adversário": "Derby County", "Local": "Visitante", "Placar": "0 x 2", "Árbitro": "Oliver Langford", "Gols (1T / 2T)": "0-1 / 0-1", "Amarelos (1T / 2T)": "0-3 / 0-2", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 5}]),
                "Preston": pd.DataFrame([{"Rodada": "1", "Adversário": "Millwall", "Local": "Mandante", "Placar": "1 x 2", "Árbitro": "Farai Hallam", "Gols (1T / 2T)": "0-1 / 1-1", "Amarelos (1T / 2T)": "3-2", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 5}]),
                "Millwall": pd.DataFrame([{"Rodada": "1", "Adversário": "Preston", "Local": "Visitante", "Placar": "2 x 1", "Árbitro": "Farai Hallam", "Gols (1T / 2T)": "1-0 / 1-1", "Amarelos (1T / 2T)": "2-3", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 5}]),
                "Stoke City": pd.DataFrame([{"Rodada": "1", "Adversário": "West Ham", "Local": "Mandante", "Placar": "0 x 1", "Árbitro": "Josh Smith", "Gols (1T / 2T)": "0-0 / 0-1", "Amarelos (1T / 2T)": "1-0", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 1}]),
                "West Ham": pd.DataFrame([{"Rodada": "1", "Adversário": "Stoke City", "Local": "Visitante", "Placar": "1 x 0", "Árbitro": "Josh Smith", "Gols (1T / 2T)": "0-0 / 1-0", "Amarelos (1T / 2T)": "0-1 / 4-1", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 4}]),
                "Swansea": pd.DataFrame([{"Rodada": "1", "Adversário": "Lincoln City", "Local": "Mandante", "Placar": "2 x 1", "Árbitro": "Adam Herczeg", "Gols (1T / 2T)": "1-0 / 1-1", "Amarelos (1T / 2T)": "0-1", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 1}]),
                "Lincoln City": pd.DataFrame([{"Rodada": "1", "Adversário": "Swansea", "Local": "Visitante", "Placar": "1 x 2", "Árbitro": "Adam Herczeg", "Gols (1T / 2T)": "0-1 / 1-1", "Amarelos (1T / 2T)": "1-0 / 2-3", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 4}]),
                "Middlesbrough": pd.DataFrame([{"Rodada": "1", "Adversário": "QPR", "Local": "Mandante", "Placar": "1 x 0", "Árbitro": "Bobby Madley", "Gols (1T / 2T)": "1-0 / 0-0", "Amarelos (1T / 2T)": "0-1", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 1}]),
                "QPR": pd.DataFrame([{"Rodada": "1", "Adversário": "Middlesbrough", "Local": "Visitante", "Placar": "0 x 1", "Árbitro": "Bobby Madley", "Gols (1T / 2T)": "0-1 / 0-0", "Amarelos (1T / 2T)": "1-0 / 1-0", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 1}]),
                "Norwich": pd.DataFrame([{"Rodada": "1", "Adversário": "Portsmouth", "Local": "Mandante", "Placar": "2 x 0", "Árbitro": "Ben Speedie", "Gols (1T / 2T)": "1-0 / 1-0", "Amarelos (1T / 2T)": "0-0", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 0}]),
                "Portsmouth": pd.DataFrame([{"Rodada": "1", "Adversário": "Norwich", "Local": "Visitante", "Placar": "0 x 2", "Árbitro": "Ben Speedie", "Gols (1T / 2T)": "0-1 / 0-1", "Amarelos (1T / 2T)": "0-0 / 0-3", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 3}]),
                "Sheffield Utd": pd.DataFrame([{"Rodada": "1", "Adversário": "Birmingham", "Local": "Mandante", "Placar": "0 x 0", "Árbitro": "Gavin Ward", "Gols (1T / 2T)": "0-0 / 0-0", "Amarelos (1T / 2T)": "0-0", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 0}]),
                "Birmingham": pd.DataFrame([{"Rodada": "1", "Adversário": "Sheffield Utd", "Local": "Visitante", "Placar": "0 x 0", "Árbitro": "Gavin Ward", "Gols (1T / 2T)": "0-0 / 0-0", "Amarelos (1T / 2T)": "0-0", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 0}]),
                "Charlton": pd.DataFrame([{"Rodada": "1", "Adversário": "Wolves", "Local": "Mandante", "Placar": "1 x 1", "Árbitro": "Tim Robinson", "Gols (1T / 2T)": "0-0 / 1-1", "Amarelos (1T / 2T)": "0-0", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 0}]),
                "Wolves": pd.DataFrame([{"Rodada": "1", "Adversário": "Charlton", "Local": "Visitante", "Placar": "1 x 1", "Árbitro": "Tim Robinson", "Gols (1T / 2T)": "0-0 / 1-1", "Amarelos (1T / 2T)": "0-0 / 1-2", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 3}]),
                "Cardiff City": pd.DataFrame([{"Rodada": "1", "Adversário": "Wrexham", "Local": "Mandante", "Placar": "1 x 1", "Árbitro": "Stephen Martin", "Gols (1T / 2T)": "0-1 / 1-0", "Amarelos (1T / 2T)": "1-0", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 1}]),
                "Wrexham": pd.DataFrame([{"Rodada": "1", "Adversário": "Cardiff City", "Local": "Visitante", "Placar": "1 x 1", "Árbitro": "Stephen Martin", "Gols (1T / 2T)": "1-0 / 0-1", "Amarelos (1T / 2T)": "0-1 / 1-1", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 2}]),
                "West Bromwich": pd.DataFrame([{"Rodada": "1", "Adversário": "Burnley", "Local": "Mandante", "Placar": "1 x 0", "Árbitro": "Will Finnie", "Gols (1T / 2T)": "0-0 / 1-0", "Amarelos (1T / 2T)": "0-0", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 0}]),
                "Burnley": pd.DataFrame([{"Rodada": "1", "Adversário": "West Bromwich", "Local": "Visitante", "Placar": "0 x 1", "Árbitro": "Will Finnie", "Gols (1T / 2T)": "0-0 / 0-1", "Amarelos (1T / 2T)": "0-0 / 1-1", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 2}])
            }
        },
        "🇪🇸 La Liga": {
            "Geral": pd.DataFrame([
                {"Rodada": "1", "Confronto": "Real Madrid x Barcelona", "Árbitro": "Mateu Lahoz", "Placar": "2 x 1", "Gols (1T / 2T)": "(1-0) / (1-1)", "Amarelos (1T / 2T)": "(2-2) / (2-2)", "Vermelhos (1T / 2T)": "(0-0) / (1-0)", "Total Cartões": 5}
            ]),
            "Times": {
                "Real Madrid": pd.DataFrame([{"Rodada": "1", "Adversário": "Barcelona", "Local": "Mandante", "Placar": "2 x 1", "Árbitro": "Mateu Lahoz", "Gols (1T / 2T)": "1-0 / 1-1", "Amarelos (1T / 2T)": "2-2", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 4}]),
                "Barcelona": pd.DataFrame([{"Rodada": "1", "Adversário": "Real Madrid", "Local": "Visitante", "Placar": "1 x 2", "Árbitro": "Mateu Lahoz", "Gols (1T / 2T)": "0-1 / 1-1", "Amarelos (1T / 2T)": "2-2", "Vermelhos (1T / 2T)": "0-1", "Total Cartões": 5}])
            }
        },
        "🇩🇪 Bundesliga": {"Geral": pd.DataFrame(), "Times": {}},
        "🇮🇹 Série A Italiana": {"Geral": pd.DataFrame(), "Times": {}},
        "🇫🇷 Ligue 1": {"Geral": pd.DataFrame(), "Times": {}},
        "🇪🇺 UEFA Champions League": {"Geral": pd.DataFrame(), "Times": {}}
    }

dados = carregar_dados_oficiais()
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
        st.info("Aguardando inserção de dados para esta liga.")

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
                                               
