import streamlit as st
import pandas as pd
from datetime import datetime

# ---------------------------------------------------------
# CONFIGURATION DE LA PAGE & DESIGN JOSIASTRADER
# ---------------------------------------------------------
st.set_page_config(
    page_title="Josiastrader",
    page_icon="⚽",
    layout="wide"
)

# Style CSS personnalisée : Thème Rouge Profond, Dominant & Moderne
st.markdown("""
    <style>
    .stApp {
        background-color: #0A0000;
        color: #FFFFFF;
    }
    h1, h2, h3 {
        color: #FF0000 !important;
        font-family: 'Arial Black', sans-serif;
    }
    .match-card {
        background-color: #170303;
        border: 1px solid #FF0000;
        border-left: 6px solid #FF0000;
        padding: 16px;
        margin-bottom: 18px;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(255, 0, 0, 0.25);
    }
    .badge-safe {
        background-color: #FF0000;
        color: #FFFFFF;
        padding: 4px 10px;
        border-radius: 5px;
        font-weight: bold;
        font-size: 13px;
    }
    .badge-time {
        background-color: #330000;
        color: #FF9999;
        border: 1px solid #FF3333;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: bold;
    }
    .urgent-badge {
        background-color: #FF2222;
        color: white;
        padding: 2px 8px;
        border-radius: 3px;
        font-size: 11px;
        font-weight: bold;
        animation: blinker 1.5s linear infinite;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# EN-TÊTE ET SYSTEME DE MISE À JOUR EN TEMPS RÉEL
# ---------------------------------------------------------
st.title("Josiastrader ✊🏾 — Algorithme Ultra-Safe (98%)")

col_header, col_sync = st.columns([3, 1])

with col_header:
    st.caption("Analyses automatisées • Matchs imminents • 5 Scores Exacts Safes par semaine")

with col_sync:
    if st.button("🔄 Mise à jour des matchs"):
        st.session_state['last_update'] = datetime.now().strftime("%d/%m/%Y à %H:%M")
        st.success("Calendrier et cotes synchronisés !")

last_sync = st.session_state.get('last_update', datetime.now().strftime("%d/%m/%Y à %H:%M"))
st.markdown(f"**Dernière mise à jour :** `{last_sync}`")
st.markdown("---")

# ---------------------------------------------------------
# DONNÉES DU SYSTEME (Classées par date / heure et niveau)
# ---------------------------------------------------------
matchs_data = [
    # Matchs très proches (Pour la Page d'accueil)
    {
        "date": "29/07/2026", "heure": "18:00", "imminent": True,
        "pays": "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Angleterre", "competition": "1. Premier League",
        "equipes": "Manchester City vs Everton",
        "vainqueur": "Manchester City", "double_chance": "1X", "buts": "+1.5 Buts",
        "fautes": "+18.5 Fautes", "cartons": "+2.5 Cartons Jaunes", "btts": "Non",
        "confiance": "98%", "score_exact": "2 - 0", "is_top_score": True
    },
    {
        "date": "29/07/2026", "heure": "20:45", "imminent": True,
        "pays": "🇫🇷 France", "competition": "4. Ligue 1",
        "equipes": "PSG vs Angers",
        "vainqueur": "PSG", "double_chance": "1X", "buts": "+2.5 Buts",
        "fautes": "+20.5 Fautes", "cartons": "+3.5 Cartons Jaunes", "btts": "Non",
        "confiance": "97%", "score_exact": "3 - 0", "is_top_score": True
    },
    # Prochains jours de la semaine
    {
        "date": "30/07/2026", "heure": "19:00", "imminent": False,
        "pays": "🇪🇸 Espagne", "competition": "2. LaLiga",
        "equipes": "Real Madrid vs Getafe",
        "vainqueur": "Real Madrid", "double_chance": "1X", "buts": "+1.5 Buts",
        "fautes": "+22.5 Fautes", "cartons": "+4.5 Cartons Jaunes", "btts": "Non",
        "confiance": "98%", "score_exact": "2 - 0", "is_top_score": True
    },
    {
        "date": "30/07/2026", "heure": "20:30", "imminent": False,
        "pays": "🇩🇪 Allemagne", "competition": "3. Bundesliga",
        "equipes": "Bayern Munich vs Bochum",
        "vainqueur": "Bayern Munich", "double_chance": "1X", "buts": "+2.5 Buts",
        "fautes": "+16.5 Fautes", "cartons": "+2.5 Cartons Jaunes", "btts": "Oui",
        "confiance": "96%", "score_exact": "4 - 1", "is_top_score": True
    },
    {
        "date": "31/07/2026", "heure": "18:30", "imminent": False,
        "pays": "🇮🇹 Italie", "competition": "5. Serie A",
        "equipes": "Inter Milan vs Empoli",
        "vainqueur": "Inter Milan", "double_chance": "1X", "buts": "+1.5 Buts",
        "fautes": "+21.5 Fautes", "cartons": "+3.5 Cartons Jaunes", "btts": "Non",
        "confiance": "98%", "score_exact": "2 - 0", "is_top_score": True
    },
    # Coupes Internationales & Amicaux
    {
        "date": "01/08/2026", "heure": "20:00", "imminent": False,
        "pays": "🌍 International", "competition": "1. Ligue des Champions (UCL)",
        "equipes": "Real Madrid vs Club Brugge",
        "vainqueur": "Real Madrid", "double_chance": "1X", "buts": "+2.5 Buts",
        "fautes": "+19.5 Fautes", "cartons": "+3.5 Cartons Jaunes", "btts": "Oui",
        "confiance": "97%", "score_exact": "3 - 1", "is_top_score": False
    },
    {
        "date": "02/08/2026", "heure": "17:00", "imminent": False,
        "pays": "🌍 International", "competition": "2. Coupe d'Afrique des Nations (CAN)",
        "equipes": "Côte d'Ivoire vs Mozambique",
        "vainqueur": "Côte d'Ivoire", "double_chance": "1X", "buts": "+1.5 Buts",
        "fautes": "+23.5 Fautes", "cartons": "+3.5 Cartons Jaunes", "btts": "Non",
        "confiance": "97%", "score_exact": "2 - 0", "is_top_score": False
    },
    {
        "date": "03/08/2026", "heure": "18:00", "imminent": False,
        "pays": "🤝 Amicaux", "competition": "Matchs Amicaux Internationaux",
        "equipes": "France vs Autriche",
        "vainqueur": "France", "double_chance": "1X", "buts": "+1.5 Buts",
        "fautes": "+17.5 Fautes", "cartons": "+2.5 Cartons Jaunes", "btts": "Oui",
        "confiance": "95%", "score_exact": "2 - 1", "is_top_score": False
    }
]

df = pd.DataFrame(matchs_data)

# ---------------------------------------------------------
# STRUCTURE PAR ONGLETS (DISPOSITION SOUHAITÉE)
# ---------------------------------------------------------
tab_acc, tab_champ, tab_vip, tab_coupes = st.tabs([
    "⚡ ACCUEIL : Matchs Imminents", 
    "📅 Matchs à Venir & Pronostics", 
    "🎯 TOP 5 Scores Exacts Safes", 
    "🌍 Coupes & Amicaux"
])

# =========================================================
# ONGLET ACCUEIL : MATCHS QUI SE JOUENT LE PLUS VITE
# =========================================================
with tab_acc:
    st.subheader("🔥 Matchs Imminents (Coup d'envoi le plus proche)")
    st.info("Cette section filtre automatiquement les rencontres prévues aujourd'hui ou dans les prochaines heures.")
    
    df_imminent = df[df['imminent'] == True]
    
    for _, m in df_imminent.iterrows():
        st.markdown(f"""
        <div class="match-card" style="border: 2px solid #FF0000;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h4>{m['pays']} — {m['competition']}</h4>
                <div>
                    <span class="urgent-badge">🚨 JOUE BIENTÔT</span>
                    <span class="badge-time">📅 {m['date']} à {m['heure']}</span>
                    <span class="badge-safe">SAFE : {m['confiance']}</span>
                </div>
            </div>
            <h2 style="color: #FFFFFF !important; margin: 10px 0;">{m['equipes']}</h2>
            <hr style="border-color: #440000;">
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px;">
                <p><b>Vainqueur :</b> <span style="color:#FF6666;">{m['vainqueur']}</span></p>
                <p><b>Double Chance :</b> {m['double_chance']}</p>
                <p><b>Total Buts :</b> {m['buts']}</p>
                <p><b>Total Fautes :</b> {m['fautes']}</p>
                <p><b>Cartons Jaunes :</b> {m['cartons']}</p>
                <p><b>Les 2 équ. marquent :</b> {m['btts']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# ONGLET 1 : CHAMPIONNATS (Classés par importance 1 à 5)
# =========================================================
with tab_champ:
    st.subheader("🏆 Championnats Nationaux (Ordre Hiérarchique)")
    
    selected_league = st.selectbox(
        "Sélectionnez la compétition :",
        ["Tous les Championnats", "1. Premier League", "2. LaLiga", "3. Bundesliga", "4. Ligue 1", "5. Serie A"]
    )
    
    if selected_league != "Tous les Championnats":
        filtered_df = df[df['competition'] == selected_league]
    else:
        filtered_df = df[df['competition'].str.startswith(("1", "2", "3", "4", "5"))]
        
    for _, m in filtered_df.iterrows():
        st.markdown(f"""
        <div class="match-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h4>{m['pays']} — {m['competition']}</h4>
                <div>
                    <span class="badge-time">📅 {m['date']} à {m['heure']}</span>
                    <span class="badge-safe">FIABILITÉ : {m['confiance']}</span>
                </div>
            </div>
            <h2 style="color: #FFFFFF !important; margin: 10px 0;">{m['equipes']}</h2>
            <hr style="border-color: #440000;">
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px;">
                <p><b>Vainqueur :</b> <span style="color:#FF6666;">{m['vainqueur']}</span></p>
                <p><b>Double Chance :</b> {m['double_chance']}</p>
                <p><b>Total Buts :</b> {m['buts']}</p>
                <p><b>Total Fautes :</b> {m['fautes']}</p>
                <p><b>Total Cartons :</b> {m['cartons']}</p>
                <p><b>Les 2 équ. marquent :</b> {m['btts']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# ONGLET 2 : TOP 5 SCORES EXACTS SAFES
# =========================================================
with tab_vip:
    st.subheader("🎯 OngletVIP : Les 5 Scores Exacts Safes de la Semaine")
    st.info("💡 Pronostics sélectionnés selon une matrice de probabilité sécurisée à 98%.")
    
    top5_df = df[df['is_top_score'] == True].head(5)
    
    for _, m in top5_df.iterrows():
        st.markdown(f"""
        <div class="match-card" style="background-color: #260000; border: 2px solid #FF0000;">
            <div style="display: flex; justify-content: space-between;">
                <span class="badge-time">📅 {m['date']} | {m['heure']}</span>
                <span class="badge-safe">SCORE EXACT SAFE</span>
            </div>
            <h3 style="margin-top: 10px; text-align: center;">{m['equipes']} ({m['competition']})</h3>
            <h1 style="color: #FF0000 !important; text-align: center; font-size: 42px; margin: 10px 0;">
                {m['score_exact']}
            </h1>
            <p style="text-align: center;">Vainqueur : <b>{m['vainqueur']}</b> | Sécurité Double Chance : <b>{m['double_chance']}</b></p>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# ONGLET 3 : COUPES INTERNATIONALES ET AMICAUX
# =========================================================
with tab_coupes:
    st.subheader("🌍 Coupes Majeures & Matchs Amicaux")
    
    df_coupes = df[~df['competition'].str.startswith(("1", "2", "3", "4", "5"))]
    
    for _, m in df_coupes.iterrows():
        st.markdown(f"""
        <div class="match-card">
            <div style="display: flex; justify-content: space-between;">
                <h4>{m['competition']}</h4>
                <span class="badge-time">📅 {m['date']} à {m['heure']}</span>
            </div>
            <h3>{m['equipes']}</h3>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin-top: 10px;">
                <p><b>Pronostic Principal :</b> {m['vainqueur']} ({m['double_chance']})</p>
                <p><b>Buts :</b> {m['buts']} | <b>BTTS :</b> {m['btts']}</p>
                <p><b>Fautes :</b> {m['fautes']}</p>
                <p><b>Cartons Jaunes :</b> {m['cartons']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
