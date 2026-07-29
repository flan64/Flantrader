import streamlit as st
import requests

# Configuration de la page Streamlit
st.set_page_config(page_title="Le Maestros VIP", page_icon="⚡", layout="wide")

# ---------------------------------------------------------
# CONFIGURATION DE L'API FOOTBALL
# ---------------------------------------------------------
API_KEY = "c084b5445fa0948fc566b6c0aa112228"  
BASE_URL = "https://api.football-data.org/v4/"

headers = {"X-Auth-Token": API_KEY}

@st.cache_data(ttl=600)  # Actualise les données toutes les 10 minutes
def get_todays_matches():
    """Récupère les matchs réels du jour"""
    url = f"{BASE_URL}matches"
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json().get('matches', [])
        else:
            return []
    except Exception:
        return []

# ---------------------------------------------------------
# INTERFACE UTILISATEUR
# ---------------------------------------------------------
st.title("⚡ LE MAESTROS VIP")
st.caption("Pronostics, Live API & Gestion de Bankroll")
st.divider()

# Onglets de navigation
tab_live, tab_safes, tab_exacts, tab_leagues, tab_stats = st.tabs([
    "🔴 Matchs du Jour (Live)",
    "🛡️ Coupons Safes", 
    "🎯 Scores Exacts", 
    "🏆 Championnats & Coupes", 
    "📊 Stats & Mises"
])

# ---------------------------------------------------------
# 1. MATCHS EN DIRECT & DU JOUR (API)
# ---------------------------------------------------------
with tab_live:
    st.subheader("⚽ Programme & Matchs Réels d'Aujourd'hui")
    
    matches = get_todays_matches()
    
    if matches:
        for match in matches:
            home_team = match['homeTeam']['name']
            away_team = match['awayTeam']['name']
            competition = match['competition']['name']
            status = match['status']
            
            # Formatage du score s'il existe
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
        st.info("Aucun match majeur programmé pour aujourd'hui ou limite d'appels atteinte.")

# ---------------------------------------------------------
# 2. COUPONS SAFES
# ---------------------------------------------------------
with tab_safes:
    st.subheader("📌 Ticket Safe du Jour")
    st.write("Espace réservé à tes sélections à haute fiabilité.")
    
    st.code("MAESTRO1X", language="text")
    st.caption("💡 Code coupon rapide à partager à tes membres.")

# ---------------------------------------------------------
# 3. SCORES EXACTS
# ---------------------------------------------------------
with tab_exacts:
    st.subheader("🎯 Espace Scores Exacts")
    st.info("Publie ici tes prédictions de scores à forte cote.")

# ---------------------------------------------------------
# 4. CHAMPIONNATS & COUPES
# ---------------------------------------------------------
with tab_leagues:
    st.subheader("🏆 Championnats & Coupes Couverts")

    with st.expander("🇬🇧 Angleterre"):
        st.write("• Premier League")
        st.write("• FA Cup")
        st.write("• EFL Cup (Carabao Cup)")

    with st.expander("🇪🇸 Espagne"):
        st.write("• LaLiga")
        st.write("• Copa del Rey")
        st.write("• Supercopa de España")

    with st.expander("🇫🇷 France"):
        st.write("• Ligue 1")
        st.write("• Coupe de France")

    with st.expander("🇮🇹 Italie"):
        st.write("• Serie A")
        st.write("• Coppa Italia")

    with st.expander("🇩🇪 Allemagne"):
        st.write("• Bundesliga")
        st.write("• DFB-Pokal")

    with st.expander("🇪🇺 Europe (UEFA)"):
        st.write("• UEFA Champions League")
        st.write("• UEFA Europa League")
        st.write("• UEFA Europa Conference League")

# ---------------------------------------------------------
# 5. CALCULATEUR DE BANKROLL
# ---------------------------------------------------------
with tab_stats:
    st.subheader("🧮 Calculateur de Mise Automatique")
    capital = st.number_input("Capital Total (FCFA) :", min_value=0, step=1000, value=50000)
    
    if capital > 0:
        col_s1, col_s2 = st.columns(2)
        col_s1.metric("Mise Safe (5%)", f"{capital * 0.05:,.0f} FCFA")
        col_s2.metric("Mise Score Exact (1%)", f"{capital * 0.01:,.0f} FCFA")
