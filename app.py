import streamlit as st
import requests
from datetime import datetime, date

# Configuration de la page Streamlit
st.set_page_config(page_title="Le Maestros VIP", page_icon="⚡", layout="wide")

# ---------------------------------------------------------
# CONFIGURATION DE L'API FOOTBALL
# ---------------------------------------------------------
API_KEY = "c084b5445fa0948fc566b6c0aa112228"  
BASE_URL = "https://api.football-data.org/v4/"
headers = {"X-Auth-Token": API_KEY}

@st.cache_data(ttl=300)
def get_matches_by_date(selected_date):
    """Récupère les matchs pour une date précise (YYYY-MM-DD)"""
    date_str = selected_date.strftime("%Y-%m-%d")
    url = f"{BASE_URL}matches?dateFrom={date_str}&dateTo={date_str}"
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json().get('matches', [])
        return []
    except Exception:
        return []

# ---------------------------------------------------------
# INTERFACE UTILISATEUR
# ---------------------------------------------------------
st.title("⚡ LE MAESTROS VIP")
st.caption("Pronostics, Live API, Calendrier & Gestion de Bankroll")
st.divider()

# Navigation par Onglets
tab_live, tab_amicaux, tab_safes, tab_exacts, tab_leagues, tab_stats = st.tabs([
    "📅 Programme Matchs",
    "🤝 Matchs Amicaux",
    "🛡️ Coupons Safes", 
    "🎯 Scores Exacts", 
    "🏆 Championnats", 
    "📊 Stats & Mises"
])

# ---------------------------------------------------------
# 1. MATCHS PAR DATE (PROGRAMME)
# ---------------------------------------------------------
with tab_live:
    st.subheader("⚽ Choisir une Date dans le Mois")
    
    # Calendrier interactif
    chosen_date = st.date_input("Sélectionner la date :", value=date.today())
    
    st.write(f"### Matchs du {chosen_date.strftime('%d/%m/%Y')}")
    matches = get_matches_by_date(chosen_date)
    
    if matches:
        for match in matches:
            home_team = match['homeTeam']['name']
            away_team = match['awayTeam']['name']
            competition = match['competition']['name']
            status = match['status']
            
            home_score = match['score']['fullTime']['home']
            away_score = match['score']['fullTime']['away']
            score_str = f"{home_score} - {away_score}" if home_score is not None else "VS"

            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"🏆 **{competition}**")
                st.write(f"⚽ **{home_team}** `{score_str}` **{away_team}**")
            with col2:
                st.caption(f"Statut : {status}")
            st.divider()
    else:
        st.info("ℹ️ Aucun match officiel majeur répertorié à cette date. Consultez l'onglet 'Matchs Amicaux' ou sélectionnez une autre date du calendrier ci-dessus.")

# ---------------------------------------------------------
# 2. MATCHS AMICAUX (PAYS & CLUBS)
# ---------------------------------------------------------
with tab_amicaux:
    st.subheader("🤝 Espace Matchs Amicaux")
    st.write("Suivi des rencontres amicales de pré-saison et trêves internationales.")

    with st.expander("🌍 Amicaux Internationaux (Sélections / Pays)", expanded=True):
        st.write("• **Brésil vs Espagne** *(Amical International)*")
        st.write("• **Côte d'Ivoire vs Sénégal** *(Amical International)*")
        st.caption("💡 Mises recommandées : Prudence sur les amicaux de sélection (effectifs remaniés).")

    with st.expander("🛡️ Amicaux de Clubs (Pré-saison)", expanded=True):
        st.write("• **Arsenal vs AC Milan** *(Tournée d'été)*")
        st.write("• **FC Barcelone vs Juventus** *(Match Préparatoire)*")
        st.caption("💡 Analyse tactique disponible dans le canal VIP.")

# ---------------------------------------------------------
# 3. COUPONS SAFES
# ---------------------------------------------------------
with tab_safes:
    st.subheader("📌 Ticket Safe du Jour")
    st.write("Sélections sécurisées à haute confiance.")
    st.code("MAESTRO1X", language="text")

# ---------------------------------------------------------
# 4. SCORES EXACTS
# ---------------------------------------------------------
with tab_exacts:
    st.subheader("🎯 Espace Scores Exacts")
    st.info("Prédictions de scores à forte valeur.")

# ---------------------------------------------------------
# 5. CHAMPIONNATS & COUPES
# ---------------------------------------------------------
with tab_leagues:
    st.subheader("🏆 Championnats & Coupes Couverts")

    with st.expander("🇬🇧 Angleterre"):
        st.write("• Premier League | FA Cup | EFL Cup")

    with st.expander("🇪🇸 Espagne"):
        st.write("• LaLiga | Copa del Rey | Supercopa")

    with st.expander("🇫🇷 France"):
        st.write("• Ligue 1 | Coupe de France")

    with st.expander("🇮🇹 Italie"):
        st.write("• Serie A | Coppa Italia")

    with st.expander("🇩🇪 Allemagne"):
        st.write("• Bundesliga | DFB-Pokal")

    with st.expander("🇪🇺 Europe (UEFA)"):
        st.write("• Champions League | Europa League | Conference League")

# ---------------------------------------------------------
# 6. CALCULATEUR
# ---------------------------------------------------------
with tab_stats:
    st.subheader("🧮 Calculateur de Mise")
    capital = st.number_input("Capital Total (FCFA) :", min_value=0, step=1000, value=50000)
    if capital > 0:
        col_s1, col_s2 = st.columns(2)
        col_s1.metric("Mise Safe (5%)", f"{capital * 0.05:,.0f} FCFA")
        col_s2.metric("Mise Score Exact (1%)", f"{capital * 0.01:,.0f} FCFA")
