import streamlit as st
import requests
from datetime import date, datetime

# ---------------------------------------------------------
# 1. CONFIGURATION DE LA PAGE
# ---------------------------------------------------------
st.set_page_config(
    page_title="Le Maestros VIP", 
    page_icon="⚡", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Style visuel Sombre & Doré (VIP)
st.markdown("""
    <style>
        .stApp { background-color: #0d1117; color: #f0f6fc; }
        .stButton>button { width: 100%; background-color: #f1c40f; color: #000; font-weight: bold; border-radius: 8px; }
        .stSelectbox, .stDateInput, .stNumberInput { background-color: #161b22; }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. CONFIGURATION DE L'API FOOTBALL
# ---------------------------------------------------------
API_KEY = "c084b5445fa0948fc566b6c0aa112228"
BASE_URL = "https://api.football-data.org/v4/"
HEADERS = {"X-Auth-Token": API_KEY}

@st.cache_data(ttl=300)
def fetch_matches_by_date(selected_date):
    """Récupère les matchs réels à une date précise via l'API"""
    date_str = selected_date.strftime("%Y-%m-%d")
    url = f"{BASE_URL}matches?dateFrom={date_str}&dateTo={date_str}"
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            return response.json().get('matches', [])
        return []
    except Exception:
        return []

# ---------------------------------------------------------
# 3. ENTÊTE DU SITE
# ---------------------------------------------------------
st.title("⚡ LE MAESTROS VIP")
st.caption("Plateforme Officielle de Pronostics, Live API & Gestion de Bankroll")
st.divider()

# ---------------------------------------------------------
# 4. NAVIGATION PAR ONGLETS (NATIVE & CLIQUABLE)
# ---------------------------------------------------------
tab_matches, tab_amicaux, tab_safes, tab_exacts, tab_leagues, tab_bankroll = st.tabs([
    "📅 Programme & Live",
    "🤝 Matchs Amicaux",
    "🛡️ Coupons Safes",
    "🎯 Scores Exacts",
    "🏆 Championnats & Coupes",
    "📊 Calculateur Bankroll"
])

# ---------------------------------------------------------
# ONGLET 1 : PROGRAMME & MATCHS REELS (CALENDRIER SUR TOUT LE MOIS)
# ---------------------------------------------------------
with tab_matches:
    st.subheader("🗓️ Calendrier des Matchs Officiels")
    
    # Sélecteur de date pour consulter tous les mois / jours de l'année
    col_date, col_info = st.columns([1, 2])
    with col_date:
        chosen_date = st.date_input("Choisir une date :", value=date.today())
    with col_info:
        st.info(f"Matchs affichés pour le : **{chosen_date.strftime('%d/%m/%Y')}**")

    matches = fetch_matches_by_date(chosen_date)

    if matches:
        for match in matches:
            home = match['homeTeam']['name']
            away = match['awayTeam']['name']
            league = match['competition']['name']
            status = match['status']
            
            home_score = match['score']['fullTime']['home']
            away_score = match['score']['fullTime']['away']
            score_display = f"{home_score} - {away_score}" if home_score is not None else "VS"

            with st.container():
                c1, c2, c3 = st.columns([3, 2, 1])
                with c1:
                    st.markdown(f"🏆 **{league}**")
                    st.markdown(f"⚽ **{home}** `{score_display}` **{away}**")
                with c2:
                    st.caption(f"Statut : {status}")
                with c3:
                    st.button("Analyser", key=f"btn_{match['id']}")
                st.divider()
    else:
        st.warning("⚠️ Aucun match officiel majeur programmé à cette date exacte sur l'API. Essayez une autre date du calendrier ou consultez l'onglet 'Matchs Amicaux'.")

# ---------------------------------------------------------
# ONGLET 2 : MATCHS AMICAUX (CLUBS & PAYS)
# ---------------------------------------------------------
with tab_amicaux:
    st.subheader("🤝 Suivi des Matchs Amicaux")
    st.write("Section dédiée aux rencontres pré-saison, tournées internationales et trêves.")

    with st.expander("🌍 Amicaux Internationaux (Sélections / Pays)", expanded=True):
        st.markdown("* ⚽ **Côte d'Ivoire vs Sénégal** *(Amical International)*")
        st.markdown("* ⚽ **Brésil vs Espagne** *(Amical International)*")
        st.caption("💡 Conseil VIP : Effectifs souvent remaniés, privilégier le marché 'Les deux équipes marquent'.")

    with st.expander("🛡️ Amicaux de Clubs (Pré-saison & Tournées)", expanded=True):
        st.markdown("* ⚽ **Real Madrid vs AC Milan** *(Tournée de Pré-Saison)*")
        st.markdown("* ⚽ **Arsenal vs Bayern Munich** *(Match Préparatoire)*")
        st.caption("💡 Les analyses complètes de ces matchs sont mises à jour dans le canal VIP.")

# ---------------------------------------------------------
# ONGLET 3 : COUPONS SAFES
# ---------------------------------------------------------
with tab_safes:
    st.subheader("🛡️ Espace Coupons Safes")
    
    st.markdown("### 📌 Ticket Safe du Jour")
    st.success("Confiance : 9/10 — Cote Globale : **1.65**")
    st.write("1. **Match 1 :** Victoire à domicile *(Cote 1.35)*")
    st.write("2. **Match 2 :** Plus de 1.5 Buts *(Cote 1.22)*")
    
    st.code("MAESTRO1X", language="text")
    st.caption("Copie ce code directement sur ton bookmaker (1xBet / Betwinner / Melbet).")

    st.divider()

    st.markdown("### 🚀 Défi Montante VIP")
    st.write("⚽ **Étape 2 :** Double chance & +1.5 buts *(Cote 1.40)*")
    st.code("MONTANTE2", language="text")

# ---------------------------------------------------------
# ONGLET 4 : SCORES EXACTS
# ---------------------------------------------------------
with tab_exacts:
    st.subheader("🎯 Espace Scores Exacts (Gros Rendement)")
    
    st.markdown("### 🔍 Pronostic Sélectionné")
    st.warning("⚠️ Mises modérées recommandées (1% de bankroll max).")
    st.write("⚽ **Grand Choc de la Semaine**")
    st.write("📊 Score prédit : **2 - 1** | Cote indicative : **8.50**")
    
    st.divider()
    
    st.markdown("### ✅ Dernières Validations")
    st.write("🟢 **Inter vs AC Milan** (Score prédit: 1-0) — *Validé (Cote 7.20)*")
    st.write("🟢 **Bayern vs Dortmund** (Score prédit: 3-1) — *Validé (Cote 11.00)*")

# ---------------------------------------------------------
# ONGLET 5 : CHAMPIONNATS & COUPES (ACCORDÉONS CLIQUABLES)
# ---------------------------------------------------------
with tab_leagues:
    st.subheader("🏆 Couverture des Compétitions Majeures")
    st.write("Clique sur un pays pour voir son championnat et ses coupes associées :")

    with st.expander("🇬🇧 **Angleterre**"):
        st.markdown("* **Premier League** *(Championnat)*")
        st.markdown("* **FA Cup** *(Coupe d'Angleterre)*")
        st.markdown("* **EFL Cup / Carabao Cup** *(Coupe de la Ligue)*")

    with st.expander("🇪🇸 **Espagne**"):
        st.markdown("* **LaLiga** *(Championnat)*")
        st.markdown("* **Copa del Rey** *(Coupe du Roi)*")
        st.markdown("* **Supercopa de España** *(Supercoupe)*")

    with st.expander("🇫🇷 **France**"):
        st.markdown("* **Ligue 1** *(Championnat)*")
        st.markdown("* **Coupe de France**")
        st.markdown("* **Trophée des Champions**")

    with st.expander("🇮🇹 **Italie**"):
        st.markdown("* **Serie A** *(Championnat)*")
        st.markdown("* **Coppa Italia** *(Coupe d'Italie)*")
        st.markdown("* **Supercoppa Italiana**")

    with st.expander("🇩🇪 **Allemagne**"):
        st.markdown("* **Bundesliga** *(Championnat)*")
        st.markdown("* **DFB-Pokal** *(Coupe d'Allemagne)*")
        st.markdown("* **DFL-Supercup**")

    with st.expander("🇪🇺 **Compétitions Européennes (UEFA)**"):
        st.markdown("* **UEFA Champions League**")
        st.markdown("* **UEFA Europa League**")
        st.markdown("* **UEFA Europa Conference League**")

# ---------------------------------------------------------
# ONGLET 6 : CALCULATEUR DE BANKROLL
# ---------------------------------------------------------
with tab_bankroll:
    st.subheader("🧮 Calculateur de Mises Intelligentes")
    st.write("Gestion stricte du capital pour une rentabilité à long terme.")

    capital = st.number_input("Entrez votre capital total (en FCFA) :", min_value=0, step=5000, value=50000)

    if capital > 0:
        safe_stake = capital * 0.05
        exact_stake = capital * 0.01

        c_safe, c_exact = st.columns(2)
        c_safe.metric("Mise Ticket Safe (5%)", f"{safe_stake:,.0f} FCFA")
        c_exact.metric("Mise Score Exact (1%)", f"{exact_stake:,.0f} FCFA")

    st.divider()
    st.markdown("### 📈 Performance du Mois")
    st.write("🟢 Taux de réussite Safes : **86%**")
    st.write("📈 ROI Mensuel : **+34.5%**")
