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

# Base de Dados estruturada contemplando Rodada 1 e Rodada 2 da Championship
@st.cache_data
def carregar_dados_oficiais():
    return {
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Championship": {
            "Geral": pd.DataFrame([
                # --- 1ª Rodada ---
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
                {"Rodada": "1", "Confronto": "West Bromwich x Burnley", "Árbitro": "Will Finnie", "Placar": "1 x 0", "Gols (1T / 2T)": "(0-0) / (1-0)", "Amarelos (1T / 2T)": "(0-0) / (1-1)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 2},
                
                # --- 2ª Rodada ---
                {"Rodada": "2", "Confronto": "Southampton x Stoke City", "Árbitro": "Stephen Martin", "Placar": "3 x 1", "Gols (1T / 2T)": "(1-0) / (2-1)", "Amarelos (1T / 2T)": "(1-1) / (2-3)", "Vermelhos (1T / 2T)": "(0-0) / (0-1)", "Total Cartões": 8},
                {"Rodada": "2", "Confronto": "Derby County x Cardiff City", "Árbitro": "Tom Nield", "Placar": "2 x 2", "Gols (1T / 2T)": "(1-1) / (1-1)", "Amarelos (1T / 2T)": "(1-0) / (4-1)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 6},
                {"Rodada": "2", "Confronto": "Blackburn x Middlesbrough", "Árbitro": "Oliver Langford", "Placar": "2 x 1", "Gols (1T / 2T)": "(2-0) / (0-1)", "Amarelos (1T / 2T)": "(2-0) / (2-1)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 5},
                {"Rodada": "2", "Confronto": "West Ham x Charlton", "Árbitro": "Sam Allison", "Placar": "1 x 2", "Gols (1T / 2T)": "(0-0) / (1-2)", "Amarelos (1T / 2T)": "(0-0) / (2-3)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 5},
                {"Rodada": "2", "Confronto": "Preston x Wolverhampton", "Árbitro": "Tony Harrington", "Placar": "1 x 3", "Gols (1T / 2T)": "(0-1) / (1-2)", "Amarelos (1T / 2T)": "(1-1) / (3-0)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 5},
                {"Rodada": "2", "Confronto": "Millwall x Norwich City", "Árbitro": "Anthony Backhouse", "Placar": "3 x 0", "Gols (1T / 2T)": "(3-0) / (0-0)", "Amarelos (1T / 2T)": "(1-2) / (0-0)", "Vermelhos (1T / 2T)": "(0-0) / (0-1)", "Total Cartões": 4},
                {"Rodada": "2", "Confronto": "Lincoln City x Portsmouth", "Árbitro": "Ed Duckworth", "Placar": "1 x 3", "Gols (1T / 2T)": "(0-1) / (1-2)", "Amarelos (1T / 2T)": "(1-0) / (2-1)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 4},
                {"Rodada": "2", "Confronto": "Swansea x Sheffield Utd", "Árbitro": "Elliot Bell", "Placar": "0 x 0", "Gols (1T / 2T)": "(0-0) / (0-0)", "Amarelos (1T / 2T)": "(0-1) / (2-1)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 4},
                {"Rodada": "2", "Confronto": "West Bromwich x Burnley", "Árbitro": "Andrew Kitchen", "Placar": "3 x 1", "Gols (1T / 2T)": "(1-1) / (2-0)", "Amarelos (1T / 2T)": "(1-1) / (0-1)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 3},
                {"Rodada": "2", "Confronto": "Birmingham x Bristol City", "Árbitro": "Will Finnie", "Placar": "2 x 2", "Gols (1T / 2T)": "(0-0) / (2-2)", "Amarelos (1T / 2T)": "(1-0) / (1-1)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 3},
                {"Rodada": "2", "Confronto": "QPR x Bolton Wanderers", "Árbitro": "Tom Reeves", "Placar": "0 x 0", "Gols (1T / 2T)": "(0-0) / (0-0)", "Amarelos (1T / 2T)": "(0-1) / (1-1)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 3},
                {"Rodada": "2", "Confronto": "Wrexham x Watford", "Árbitro": "Ruebyn Ricardo", "Placar": "1 x 1", "Gols (1T / 2T)": "(0-1) / (1-0)", "Amarelos (1T / 2T)": "(1-0) / (1-0)", "Vermelhos (1T / 2T)": "(0-0) / (0-0)", "Total Cartões": 2}
            ]),
            "Times": {
                "Watford": pd.DataFrame([
                    {"Rodada": "1", "Adversário": "Southampton", "Local": "Mandante", "Placar": "1 x 3", "Árbitro": "David Webb", "Gols (1T / 2T)": "0-2 / 1-1", "Amarelos (1T / 2T)": "3-2", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 5},
                    {"Rodada": "2", "Adversário": "Wrexham", "Local": "Visitante", "Placar": "1 x 1", "Árbitro": "Ruebyn Ricardo", "Gols (1T / 2T)": "1-0 / 0-1", "Amarelos (1T / 2T)": "1-0", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 1}
                ]),
                "Southampton": pd.DataFrame([
                    {"Rodada": "1", "Adversário": "Watford", "Local": "Visitante", "Placar": "3 x 1", "Árbitro": "David Webb", "Gols (1T / 2T)": "2-0 / 1-1", "Amarelos (1T / 2T)": "2-3", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 4},
                    {"Rodada": "2", "Adversário": "Stoke City", "Local": "Mandante", "Placar": "3 x 1", "Árbitro": "Stephen Martin", "Gols (1T / 2T)": "1-0 / 2-1", "Amarelos (1T / 2T)": "1-1", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 2}
                ]),
                "Stoke City": pd.DataFrame([
                    {"Rodada": "1", "Adversário": "West Ham", "Local": "Mandante", "Placar": "0 x 1", "Árbitro": "Josh Smith", "Gols (1T / 2T)": "0-0 / 0-1", "Amarelos (1T / 2T)": "1-0", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 1},
                    {"Rodada": "2", "Adversário": "Southampton", "Local": "Visitante", "Placar": "1 x 3", "Árbitro": "Stephen Martin", "Gols (1T / 2T)": "0-1 / 1-2", "Amarelos (1T / 2T)": "1-3", "Vermelhos (1T / 2T)": "0-1", "Total Cartões": 5}
                ]),
                "Derby County": pd.DataFrame([
                    {"Rodada": "1", "Adversário": "Bolton", "Local": "Mandante", "Placar": "2 x 0", "Árbitro": "Oliver Langford", "Gols (1T / 2T)": "1-0 / 1-0", "Amarelos (1T / 2T)": "0-0", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 0},
                    {"Rodada": "2", "Adversário": "Cardiff City", "Local": "Mandante", "Placar": "2 x 2", "Árbitro": "Tom Nield", "Gols (1T / 2T)": "1-1 / 1-1", "Amarelos (1T / 2T)": "1-0", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 1}
                ]),
                "Cardiff City": pd.DataFrame([
                    {"Rodada": "1", "Adversário": "Wrexham", "Local": "Mandante", "Placar": "1 x 1", "Árbitro": "Stephen Martin", "Gols (1T / 2T)": "0-1 / 1-0", "Amarelos (1T / 2T)": "1-0", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 1},
                    {"Rodada": "2", "Adversário": "Derby County", "Local": "Visitante", "Placar": "2 x 2", "Árbitro": "Tom Nield", "Gols (1T / 2T)": "1-1 / 1-1", "Amarelos (1T / 2T)": "4-1", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 5}
                ]),
                "Blackburn": pd.DataFrame([
                    {"Rodada": "1", "Adversário": "Bristol City", "Local": "Visitante", "Placar": "2 x 1", "Árbitro": "Lewis Smith", "Gols (1T / 2T)": "1-0 / 1-1", "Amarelos (1T / 2T)": "1-0", "Vermelhos (1T / 2T)": "0-1", "Total Cartões": 1},
                    {"Rodada": "2", "Adversário": "Middlesbrough", "Local": "Mandante", "Placar": "2 x 1", "Árbitro": "Oliver Langford", "Gols (1T / 2T)": "2-0 / 0-1", "Amarelos (1T / 2T)": "2-0", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 2}
                ]),
                "Middlesbrough": pd.DataFrame([
                    {"Rodada": "1", "Adversário": "QPR", "Local": "Mandante", "Placar": "1 x 0", "Árbitro": "Bobby Madley", "Gols (1T / 2T)": "1-0 / 0-0", "Amarelos (1T / 2T)": "0-1", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 1},
                    {"Rodada": "2", "Adversário": "Blackburn", "Local": "Visitante", "Placar": "1 x 2", "Árbitro": "Oliver Langford", "Gols (1T / 2T)": "0-2 / 1-0", "Amarelos (1T / 2T)": "2-1", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 3}
                ]),
                "West Ham": pd.DataFrame([
                    {"Rodada": "1", "Adversário": "Stoke City", "Local": "Visitante", "Placar": "1 x 0", "Árbitro": "Josh Smith", "Gols (1T / 2T)": "0-0 / 1-0", "Amarelos (1T / 2T)": "0-1 / 4-1", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 4},
                    {"Rodada": "2", "Adversário": "Charlton", "Local": "Mandante", "Placar": "1 x 2", "Árbitro": "Sam Allison", "Gols (1T / 2T)": "0-0 / 1-2", "Amarelos (1T / 2T)": "0-2", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 2}
                ]),
                "Charlton": pd.DataFrame([
                    {"Rodada": "1", "Adversário": "Wolves", "Local": "Mandante", "Placar": "1 x 1", "Árbitro": "Tim Robinson", "Gols (1T / 2T)": "0-0 / 1-1", "Amarelos (1T / 2T)": "0-0", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 0},
                    {"Rodada": "2", "Adversário": "West Ham", "Local": "Visitante", "Placar": "2 x 1", "Árbitro": "Sam Allison", "Gols (1T / 2T)": "0-0 / 2-1", "Amarelos (1T / 2T)": "0-3", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 3}
                ]),
                "Preston": pd.DataFrame([
                    {"Rodada": "1", "Adversário": "Millwall", "Local": "Mandante", "Placar": "1 x 2", "Árbitro": "Farai Hallam", "Gols (1T / 2T)": "0-1 / 1-1", "Amarelos (1T / 2T)": "3-2", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 5},
                    {"Rodada": "2", "Adversário": "Wolverhampton", "Local": "Mandante", "Placar": "1 x 3", "Árbitro": "Tony Harrington", "Gols (1T / 2T)": "0-1 / 1-2", "Amarelos (1T / 2T)": "1-3", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 4}
                ]),
                "Millwall": pd.DataFrame([
                    {"Rodada": "1", "Adversário": "Preston", "Local": "Visitante", "Placar": "2 x 1", "Árbitro": "Farai Hallam", "Gols (1T / 2T)": "1-0 / 1-1", "Amarelos (1T / 2T)": "2-3", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 5},
                    {"Rodada": "2", "Adversário": "Norwich City", "Local": "Mandante", "Placar": "3 x 0", "Árbitro": "Anthony Backhouse", "Gols (1T / 2T)": "3-0 / 0-0", "Amarelos (1T / 2T)": "1-0", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 1}
                ]),
                "Norwich City": pd.DataFrame([
                    {"Rodada": "1", "Adversário": "Portsmouth", "Local": "Mandante", "Placar": "2 x 0", "Árbitro": "Ben Speedie", "Gols (1T / 2T)": "1-0 / 1-0", "Amarelos (1T / 2T)": "0-0", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 0},
                    {"Rodada": "2", "Adversário": "Millwall", "Local": "Visitante", "Placar": "0 x 3", "Árbitro": "Anthony Backhouse", "Gols (1T / 2T)": "0-3 / 0-0", "Amarelos (1T / 2T)": "2-0", "Vermelhos (1T / 2T)": "0-1", "Total Cartões": 3}
                ]),
                "Lincoln City": pd.DataFrame([
                    {"Rodada": "1", "Adversário": "Swansea", "Local": "Visitante", "Placar": "1 x 2", "Árbitro": "Adam Herczeg", "Gols (1T / 2T)": "0-1 / 1-1", "Amarelos (1T / 2T)": "1-0 / 2-3", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 4},
                    {"Rodada": "2", "Adversário": "Portsmouth", "Local": "Mandante", "Placar": "1 x 3", "Árbitro": "Ed Duckworth", "Gols (1T / 2T)": "0-1 / 1-2", "Amarelos (1T / 2T)": "1-2", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 3}
                ]),
                "Portsmouth": pd.DataFrame([
                    {"Rodada": "1", "Adversário": "Norwich", "Local": "Visitante", "Placar": "0 x 2", "Árbitro": "Ben Speedie", "Gols (1T / 2T)": "0-1 / 0-1", "Amarelos (1T / 2T)": "0-0 / 0-3", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 3},
                    {"Rodada": "2", "Adversário": "Lincoln City", "Local": "Visitante", "Placar": "3 x 1", "Árbitro": "Ed Duckworth", "Gols (1T / 2T)": "1-0 / 2-1", "Amarelos (1T / 2T)": "0-1 / 1-1", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 3}
                ]),
                "Swansea": pd.DataFrame([
                    {"Rodada": "1", "Adversário": "Lincoln City", "Local": "Mandante", "Placar": "2 x 1", "Árbitro": "Adam Herczeg", "Gols (1T / 2T)": "1-0 / 1-1", "Amarelos (1T / 2T)": "0-1", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 1},
                    {"Rodada": "2", "Adversário": "Sheffield Utd", "Local": "Mandante", "Placar": "0 x 0", "Árbitro": "Elliot Bell", "Gols (1T / 2T)": "0-0 / 0-0", "Amarelos (1T / 2T)": "0-2", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 2}
                ]),
                "Sheffield Utd": pd.DataFrame([
                    {"Rodada": "1", "Adversário": "Birmingham", "Local": "Mandante", "Placar": "0 x 0", "Árbitro": "Gavin Ward", "Gols (1T / 2T)": "0-0 / 0-0", "Amarelos (1T / 2T)": "0-0", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 0},
                    {"Rodada": "2", "Adversário": "Swansea", "Local": "Visitante", "Placar": "0 x 0", "Árbitro": "Elliot Bell", "Gols (1T / 2T)": "0-0 / 0-0", "Amarelos (1T / 2T)": "1-1", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 2}
                ]),
                "West Bromwich": pd.DataFrame([
                    {"Rodada": "1", "Adversário": "Burnley", "Local": "Mandante", "Placar": "1 x 0", "Árbitro": "Will Finnie", "Gols (1T / 2T)": "0-0 / 1-0", "Amarelos (1T / 2T)": "0-0", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 0},
                    {"Rodada": "2", "Adversário": "Burnley", "Local": "Mandante", "Placar": "3 x 1", "Árbitro": "Andrew Kitchen", "Gols (1T / 2T)": "1-1 / 2-0", "Amarelos (1T / 2T)": "1-0", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 1}
                ]),
                "Burnley": pd.DataFrame([
                    {"Rodada": "1", "Adversário": "West Bromwich", "Local": "Visitante", "Placar": "0 x 1", "Árbitro": "Will Finnie", "Gols (1T / 2T)": "0-0 / 0-1", "Amarelos (1T / 2T)": "0-0 / 1-1", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 2},
                    {"Rodada": "2", "Adversário": "West Bromwich", "Local": "Visitante", "Placar": "1 x 3", "Árbitro": "Andrew Kitchen", "Gols (1T / 2T)": "1-1 / 0-2", "Amarelos (1T / 2T)": "1-1", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 2}
                ]),
                "Birmingham": pd.DataFrame([
                    {"Rodada": "1", "Adversário": "Sheffield Utd", "Local": "Visitante", "Placar": "0 x 0", "Árbitro": "Gavin Ward", "Gols (1T / 2T)": "0-0 / 0-0", "Amarelos (1T / 2T)": "0-0", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 0},
                    {"Rodada": "2", "Adversário": "Bristol City", "Local": "Mandante", "Placar": "2 x 2", "Árbitro": "Will Finnie", "Gols (1T / 2T)": "0-0 / 2-2", "Amarelos (1T / 2T)": "1-1", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 2}
                ]),
                "Bristol City": pd.DataFrame([
                    {"Rodada": "1", "Adversário": "Blackburn", "Local": "Mandante", "Placar": "1 x 2", "Árbitro": "Lewis Smith", "Gols (1T / 2T)": "0-1 / 1-1", "Amarelos (1T / 2T)": "2-1", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 3},
                    {"Rodada": "2", "Adversário": "Birmingham", "Local": "Visitante", "Placar": "2 x 2", "Árbitro": "Will Finnie", "Gols (1T / 2T)": "0-0 / 2-2", "Amarelos (1T / 2T)": "0-1", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 1}
                ]),
                "QPR": pd.DataFrame([
                    {"Rodada": "1", "Adversário": "Middlesbrough", "Local": "Visitante", "Placar": "0 x 1", "Árbitro": "Bobby Madley", "Gols (1T / 2T)": "0-1 / 0-0", "Amarelos (1T / 2T)": "1-0 / 1-0", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 1},
                    {"Rodada": "2", "Adversário": "Bolton Wanderers", "Local": "Mandante", "Placar": "0 x 0", "Árbitro": "Tom Reeves", "Gols (1T / 2T)": "0-0 / 0-0", "Amarelos (1T / 2T)": "0-1", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 1}
                ]),
                "Bolton Wanderers": pd.DataFrame([
                    {"Rodada": "1", "Adversário": "Derby County", "Local": "Visitante", "Placar": "0 x 2", "Árbitro": "Oliver Langford", "Gols (1T / 2T)": "0-1 / 0-1", "Amarelos (1T / 2T)": "0-3 / 0-2", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 5},
                    {"Rodada": "2", "Adversário": "QPR", "Local": "Visitante", "Placar": "0 x 0", "Árbitro": "Tom Reeves", "Gols (1T / 2T)": "0-0 / 0-0", "Amarelos (1T / 2T)": "1-1", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 2}
                ]),
                "Wrexham": pd.DataFrame([
                    {"Rodada": "1", "Adversário": "Cardiff City", "Local": "Visitante", "Placar": "1 x 1", "Árbitro": "Stephen Martin", "Gols (1T / 2T)": "1-0 / 0-1", "Amarelos (1T / 2T)": "0-1 / 1-1", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 2},
                    {"Rodada": "2", "Adversário": "Watford", "Local": "Mandante", "Placar": "1 x 1", "Árbitro": "Ruebyn Ricardo", "Gols (1T / 2T)": "0-1 / 1-0", "Amarelos (1T / 2T)": "1-0", "Vermelhos (1T / 2T)": "0-0", "Total Cartões": 1}
                ]),
                "Wolverhampton": pd.DataFrame([
                    {"Rodada": "1", "Adversário": "Charlton", "Local": "Visitante", "Placar": "1 x 1", "Árbitro": "Tim Robinson", "Gols (1T / 2T)": "0-0 / 1-1", "Amarelos (1T / 2T)": "0-
