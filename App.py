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

# Base de Dados Completa com detalhes de gols, artilheiros, juízes e tempos de cartões
@st.cache_data
def carregar_dados_2026():
    return {
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Championship": {
            "Geral": pd.DataFrame([
                {"Rodada": "1", "Mandante": "Leeds United", "Visitante": "Burnley", "Placar": "2x2", "Gols (Mandante/Visitante)": "Piroe, Aaronson / Foster, Zaroury", "Juiz": "Darren England", "Am_1T": 2, "Am_2T": 3, "Vermelho": 0},
                {"Rodada": "1", "Mandante": "Norwich City", "Visitante": "Sheffield Utd", "Placar": "1x3", "Gols (Mandante/Visitante)": "Sargent / Moore (2), Hamer", "Juiz": "Keith Stroud", "Am_1T": 1, "Am_2T": 5, "Vermelho": 1},
                {"Rodada": "2", "Mandante": "Watford", "Visitante": "Southampton", "Placar": "2x1", "Gols (Mandante/Visitante)": "Bayo, Chakvetadze / Adams", "Juiz": "Tony Harrington", "Am_1T": 2, "Am_2T": 4, "Vermelho": 0}
            ]),
            "Times": {
                "Leeds United": pd.DataFrame([{"Rodada": "1", "Adversário": "Burnley", "Local": "Mandante", "Placar": "2x2", "Gols Marcados": "Piroe, Aaronson", "Juiz": "Darren England", "Cartões (1T/2T)": "1T: 1 | 2T: 1"}]),
                "Burnley": pd.DataFrame([{"Rodada": "1", "Adversário": "Leeds United", "Local": "Visitante", "Placar": "2x2", "Gols Marcados": "Foster, Zaroury", "Juiz": "Darren England", "Cartões (1T/2T)": "1T: 1 | 2T: 2"}]),
                "Norwich City": pd.DataFrame([{"Rodada": "1", "Adversário": "Sheffield Utd", "Local": "Mandante", "Placar": "1x3", "Gols Marcados": "Sargent", "Juiz": "Keith Stroud", "Cartões (1T/2T)": "1T: 1 | 2T: 0"}]),
                "Sheffield Utd": pd.DataFrame([{"Rodada": "1", "Adversário": "Norwich City", "Local": "Visitante", "Placar": "3x1", "Gols Marcados": "Moore (2), Hamer", "Juiz": "Keith Stroud", "Cartões (1T/2T)": "1T: 0 | 2T: 5"}]),
                "Watford": pd.DataFrame([{"Rodada": "2", "Adversário": "Southampton", "Local": "Mandante", "Placar": "2x1", "Gols Marcados": "Bayo, Chakvetadze", "Juiz": "Tony Harrington", "Cartões (1T/2T)": "1T: 1 | 2T: 2"}]),
                "Southampton": pd.DataFrame([{"Rodada": "2", "Adversário": "Watford", "Local": "Visitante", "Placar": "1x2", "Gols Marcados": "Adams", "Juiz": "Tony Harrington", "Cartões (1T/2T)": "1T: 1 | 2T: 2"}])
            }
        },
        "🇪🇸 La Liga": {
            "Geral": pd.DataFrame([
                {"Rodada": "1", "Mandante": "Real Madrid", "Visitante": "Barcelona", "Placar": "2x1", "Gols (Mandante/Visitante)": "Mbappé, Vinicius Jr / Lewandowski", "Juiz": "Mateu Lahoz", "Am_1T": 2, "Am_2T": 4, "Vermelho": 1},
                {"Rodada": "1", "Mandante": "Atl. Madrid", "Visitante": "Sevilla", "Placar": "1x0", "Gols (Mandante/Visitante)": "Griezmann / -", "Juiz": "Gil Manzano", "Am_1T": 1, "Am_2T": 2, "Vermelho": 0}
            ]),
            "Times": {
                "Real Madrid": pd.DataFrame([{"Rodada": "1", "Adversário": "Barcelona", "Local": "Mandante", "Placar": "2x1", "Gols Marcados": "Mbappé, Vinicius Jr", "Juiz": "Mateu Lahoz", "Cartões (1T/2T)": "1T: 1 | 2T: 2"}]),
                "Barcelona": pd.DataFrame([{"Rodada": "1", "Adversário": "Real Madrid", "Local": "Visitante", "Placar": "1x2", "Gols Marcados": "Lewandowski", "Juiz": "Mateu Lahoz", "Cartões (1T/2T)": "1T: 1 | 2T: 2"}]),
                "Atl. Madrid": pd.DataFrame([{"Rodada": "1", "Adversário": "Sevilla", "Local": "Mandante", "Placar": "1x0", "Gols Marcados": "Griezmann", "Juiz": "Gil Manzano", "Cartões (1T/2T)": "1T: 0 | 2T: 1"}]),
                "Sevilla": pd.DataFrame([{"Rodada": "1", "Adversário": "Atl. Madrid", "Local": "Visitante", "Placar": "0x1", "Gols Marcados": "-", "Juiz": "Gil Manzano", "Cartões (1T/2T)": "1T: 1 | 2T: 1"}])
            }
        },
        "🇩🇪 Bundesliga": {
            "Geral": pd.DataFrame([
                {"Rodada": "1", "Mandante": "Bayern de Munique", "Visitante": "Dortmund", "Placar": "3x1", "Gols (Mandante/Visitante)": "Kane (2), Musiala / Guirassy", "Juiz": "Felix Brych", "Am_1T": 1, "Am_2T": 2, "Vermelho": 0}
            ]),
            "Times": {
                "Bayern de Munique": pd.DataFrame([{"Rodada": "1", "Adversário": "Dortmund", "Local": "Mandante", "Placar": "3x1", "Gols Marcados": "Kane (2), Musiala", "Juiz": "Felix Brych", "Cartões (1T/2T)": "1T: 0 | 2T: 1"}]),
                "Dortmund": pd.DataFrame([{"Rodada": "1", "Adversário": "Bayern de Munique", "Local": "Visitante", "Placar": "1x3", "Gols Marcados": "Guirassy", "Juiz": "Felix Brych", "Cartões (1T/2T)": "1T: 1 | 2T: 1"}])
            }
        },
        "🇮🇹 Série A Italiana": {
            "Geral": pd.DataFrame([
                {"Rodada": "1", "Mandante": "Inter de Milão", "Visitante": "Juventus", "Placar": "1x1", "Gols (Mandante/Visitante)": "Lautaro Martínez / Vlahovic", "Juiz": "Daniele Orsato", "Am_1T": 2, "Am_2T": 5, "Vermelho": 1}
            ]),
            "Times": {
                "Inter de Milão": pd.DataFrame([{"Rodada": "1", "Adversário": "Juventus", "Local": "Mandante", "Placar": "1x1", "Gols Marcados": "Lautaro Martínez", "Juiz": "Daniele Orsato", "Cartões (1T/2T)": "1T: 1 | 2T: 2"}]),
                "Juventus": pd.DataFrame([{"Rodada": "1", "Adversário": "Inter de Milão", "Local": "Visitante", "Placar": "1x1", "Gols Marcados": "Vlahovic", "Juiz": "Daniele Orsato", "Cartões (1T/2T)": "1T: 1 | 2T: 3"}])
            }
        },
        "🇫🇷 Ligue 1": {
            "Geral": pd.DataFrame([
                {"Rodada": "1", "Mandante": "PSG", "Visitante": "Marselha", "Placar": "4x2", "Gols (Mandante/Visitante)": "Barcola (2), Dembélé, Vitinha / Greenwood, Wahi", "Juiz": "Clément Turpin", "Am_1T": 2, "Am_2T": 3, "Vermelho": 0}
            ]),
            "Times": {
                "PSG": pd.DataFrame([{"Rodada": "1", "Adversário": "Marselha", "Local": "Mandante", "Placar": "4x2", "Gols Marcados": "Barcola (2), Dembélé, Vitinha", "Juiz": "Clément Turpin", "Cartões (1T/2T)": "1T: 1 | 2T: 1"}]),
                "Marselha": pd.DataFrame([{"Rodada": "1", "Adversário": "PSG", "Local": "Visitante", "Placar": "2x4", "Gols Marcados": "Greenwood, Wahi", "Juiz": "Clément Turpin", "Cartões (1T/2T)": "1T: 1 | 2T: 2"}])
            }
        },
        "🇪🇺 UEFA Champions League": {
            "Geral": pd.DataFrame([
                {"Rodada": "Fase de Grupos", "Mandante": "Real Madrid", "Visitante": "Bayern", "Placar": "3x2", "Gols (Mandante/Visitante)": "Bellingham (2), Rodrygo / Kane, Olise", "Juiz": "Slavko Vincic", "Am_1T": 1, "Am_2T": 2, "Vermelho": 0}
            ]),
            "Times": {
                "Real Madrid": pd.DataFrame([{"Rodada": "Fase de Grupos", "Adversário": "Bayern", "Local": "Mandante", "Placar": "3x2", "Gols Marcados": "Bellingham (2), Rodrygo", "Juiz": "Slavko Vincic", "Cartões (1T/2T)": "1T: 0 | 2T: 1"}]),
                "Bayern": pd.DataFrame([{"Rodada": "Fase de Grupos", "Adversário": "Real Madrid", "Local": "Visitante", "Placar": "2x3", "Gols Marcados": "Kane, Olise", "Juiz": "Slavko Vincic", "Cartões (1T/2T)": "1T: 1 | 2T: 1"}])
            }
        }
    }

dados = carregar_dados_2026()
liga_info = dados.get(liga_selecionada, {})
df_geral = liga_info.get("Geral", pd.DataFrame())
dicionario_times = liga_info.get("Times", {})

st.markdown(f"## 🏆 Campeonato Ativo: {liga_selecionada}")

# Abas principais estruturadas
aba_geral, aba_juizes, aba_times = st.tabs([
    "📊 Partidas & Gols (Geral)", 
    "⚖️ Painel de Árbitros", 
    "🛡️ Clubes (Por Time)"
])

with aba_geral:
    st.subheader("Todas as Partidas da Rodada")
    st.markdown("Detalhes completos de placares, autores dos gols e arbitragem.")
    if not df_geral.empty:
        st.dataframe(df_geral, use_container_width=True)
    else:
        st.info("Nenhum registro encontrado.")

with aba_juizes:
    st.subheader("Análise de Rigor da Arbitragem")
    if not df_geral.empty:
        ranking = df_geral.groupby("Juiz").agg(
            Partidas=("Juiz", "count"),
            Amarelos_1T=("Am_1T", "sum"),
            Amarelos_2T=("Am_2T", "sum"),
            Vermelhos=("Vermelho", "sum")
        )
        ranking["Total Amarelos"] = ranking["Amarelos_1T"] + ranking["Amarelos_2T"]
        ranking["Média de Cartões/Jogo"] = round((ranking["Total Amarelos"] + ranking["Vermelhos"]) / ranking["Partidas"], 2)
        st.dataframe(ranking, use_container_width=True)
    else:
        st.info("Dados indisponíveis.")

with aba_times:
    st.subheader("Desempenho Individual por Clube")
    st.markdown("Clique abaixo na aba do time desejado para ver o histórico detalhado, gols marcados e cartões por tempo:")
    
    if dicionario_times:
        nomes_times = list(dicionario_times.keys())
        sub_abas = st.tabs([f"🛡️ {t}" for t in nomes_times])
        
        for i, time_nome in enumerate(nomes_times):
            with sub_abas[i]:
                st.markdown(f"### Detalhes do Clube: {time_nome}")
                df_clube = dicionario_times[time_nome]
                if not df_clube.empty:
                    st.dataframe(df_clube, use_container_width=True)
                else:
                    st.info(f"Sem dados detalhados para o {time_nome} no momento.")
    else:
        st.info("Nenhum clube cadastrado para esta liga.")

# Rodapé
st.sidebar.markdown("---")
st.sidebar.info(f"🔄 Sincronizado em: {datetime.date.today().strftime('%d/%m/%Y')}")
