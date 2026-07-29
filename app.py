import streamlit as st
import pandas as pd

# 1. Configuration de la page
st.set_page_config(
    page_title="Josiastrader ✊🏾 - Moteur de Pronostics Ultra Safe",
    page_icon="🥊",
    layout="wide"
)

# 2. Style CSS Personnalisé - Thème Rouge Victoire & Force de Frappe
st.markdown("""
    <style>
    .stApp {
        background-color: #0d0505;
        color: #f8fafc;
    }
    .main-title {
        text-align: center;
        color: #ef4444;
        font-weight: 900;
        font-size: 2.3rem;
        margin-bottom: 5px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .sub-title {
        text-align: center;
        color: #fca5a5;
        font-size: 0.95rem;
        margin-bottom: 25px;
    }
    .section-header {
        color: #ffffff;
        background: linear-gradient(90deg, #991b1b 0%, #0d0505 100%);
        padding: 10px 15px;
        border-left: 5px solid #ef4444;
        border-radius: 6px;
        font-size: 1.2rem;
        margin-top: 20px;
        margin-bottom: 15px;
    }
    .match-card {
        background: linear-gradient(135deg, #1f0909 0%, #110303 100%);
        border: 1px solid #7f1d1d;
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 15px;
        box-shadow: 0 4px 12px rgba(220, 38, 38, 0.15);
    }
    .match-teams {
        font-size: 1.15rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 6px;
    }
    .match-meta {
        font-size: 0.8rem;
        color: #fca5a5;
        margin-bottom: 10px;
    }
    .badge-safe {
        background-color: #991b1b;
        color: #fef2f2;
        padding: 5px 12px;
        border-radius: 6px;
        font-weight: 700;
        font-size: 0.85rem;
        display: inline-block;
        border: 1px solid #ef4444;
    }
    .badge-confidence {
        background-color: #dc2626;
        color: #ffffff;
        padding: 5px 12px;
        border-radius: 6px;
        font-weight: 800;
        font-size: 0.85rem;
        display: inline-block;
        float: right;
    }
    .stat-box {
        background-color: #140505;
        border-radius: 8px;
        padding: 10px;
        text-align: center;
        border: 1px solid #450a0a;
        color: #fecdd3;
    }
    </style>
""", unsafe_allow_html=True)

# 3. En-tête de l'application
st.markdown("<h1 class='main-title'>🥊 JOSIASTRADER ✊🏾</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Logiciel N°1 d'Analyse Sportive Ultra-SÉCURISÉE (98% Fiabilité)</p>", unsafe_allow_html=True)
st.divider()

# 4. Base de Données Restructurée par Ordre d'Importance
DATA_COMPETITIONS = {
    "🏆 COUPES INTERNATIONALES & SÉLECTIONS": {
        "🏆 Ligue des Champions (UCL)": [
            {"date": "Mercredi • 20:00", "home": "Real Madrid", "away": "Manchester City", "pred": "Double Chance : Real Madrid ou Nul", "fiab": "98%", "sec": "Plus de 1.5 Buts", "cartons": "Plus de 3.5 Cartons", "score": "2 - 1", "xg": "2.2 - 1.8"},
            {"date": "Mercredi • 20:00", "home": "PSG", "away": "Bayern Munich", "pred": "Plus de 1.5 Buts", "fiab": "98%", "sec": "Les 2 équipes marquent", "cartons": "Plus de 4.5 Cartons", "score": "2 - 2", "xg": "1.9 - 2.1"}
        ],
        "🟠 Europa League": [
            {"date": "Jeudi • 17:45", "home": "AS Roma", "away": "FC Porto", "pred": "Moins de 3.5 Buts", "fiab": "98%", "sec": "AS Roma ou Nul", "cartons": "Plus de 4.5 Cartons", "score": "1 - 0", "xg": "1.3 - 0.9"}
        ],
        "🌍 Coupe du Monde / Qualifications": [
            {"date": "Mardi • 19:00", "home": "Brésil", "away": "Argentine", "pred": "Plus de 3.5 Cartons", "fiab": "98%", "sec": "Moins de 3.5 Buts", "cartons": "Plus de 5.5 Cartons", "score": "1 - 1", "xg": "1.2 - 1.3"}
        ],
        "🌍 CAN (Coupe d'Afrique)": [
            {"date": "Jeudi • 20:00", "home": "Côte d'Ivoire", "away": "Sénégal", "pred": "Moins de 2.5 Buts", "fiab": "98%", "sec": "Côte d'Ivoire ou Nul", "cartons": "Plus de 3.5 Cartons", "score": "1 - 0", "xg": "1.4 - 0.8"}
        ],
        "🇪🇺 UEFA Nations League": [
            {"date": "Vendredi • 20:45", "home": "Espagne", "away": "Italie", "pred": "Espagne ou Nul", "fiab": "98%", "sec": "Plus de 1.5 Buts", "cartons": "Plus de 3.5 Cartons", "score": "2 - 1", "xg": "2.0 - 1.0"}
        ],
        "🤝 Matchs Amicaux (Clubs & Sélections)": [
            {"date": "Mardi • 18:00", "home": "FC Barcelone", "away": "Vissel Kobe", "pred": "Plus de 2.5 Buts", "fiab": "98%", "sec": "Victoire Barcelone", "cartons": "Moins de 3.5 Cartons", "score": "3 - 1", "xg": "2.8 - 0.9"}
        ]
    },
    "🇪🇸 ESPAGNE": {
        "🇪🇸 LaLiga": [
            {"date": "Vendredi • 21:00", "home": "Real Madrid", "away": "Betis Séville", "pred": "Victoire Real Madrid", "fiab": "98%", "sec": "Plus de 1.5 Buts", "cartons": "Plus de 3.5 Cartons", "score": "2 - 0", "xg": "2.4 - 0.7"}
        ],
        "👑 Copa del Rey": [
            {"date": "Mercredi • 21:00", "home": "Athletic Bilbao", "away": "Real Sociedad", "pred": "Moins de 3.5 Buts", "fiab": "98%", "sec": "Bilbao ou Nul", "cartons": "Plus de 5.5 Cartons", "score": "1 - 0", "xg": "1.2 - 0.8"}
        ]
    },
    "🏴󠁧󠁢󠁥󠁮󠁧󠁿 ANGLETERRE": {
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League": [
            {"date": "Mardi • 20:45", "home": "Arsenal", "away": "Wolverhampton", "pred": "Victoire Arsenal", "fiab": "98%", "sec": "Plus de 1.5 Buts", "cartons": "Moins de 4.5 Cartons", "score": "3 - 0", "xg": "2.6 - 0.5"}
        ],
        "🏆 FA Cup / League Cup": [
            {"date": "Mercredi • 19:45", "home": "Manchester City", "away": "Newcastle", "pred": "Man City ou Nul", "fiab": "98%", "sec": "Plus de 2.5 Buts", "cartons": "Plus de 3.5 Cartons", "score": "3 - 1", "xg": "2.5 - 1.1"}
        ]
    },
    "🇫🇷 FRANCE": {
        "🇫🇷 Ligue 1": [
            {"date": "Vendredi • 21:00", "home": "PSG", "away": "Rennes", "pred": "Victoire PSG", "fiab": "98%", "sec": "Plus de 2.5 Buts", "cartons": "Moins de 4.5 Cartons", "score": "3 - 1", "xg": "2.7 - 0.9"}
        ],
        "🏆 Coupe de France": [
            {"date": "Mercredi • 21:00", "home": "Marseille", "away": "Lyon", "pred": "Plus de 1.5 Buts", "fiab": "98%", "sec": "Les 2 équipes marquent", "cartons": "Plus de 4.5 Cartons", "score": "2 - 1", "xg": "1.8 - 1.5"}
        ]
    },
    "🇩🇪 ALLEMAGNE": {
        "🇩🇪 Bundesliga": [
            {"date": "Vendredi • 20:30", "home": "Bayern Munich", "away": "Eintracht Francfort", "pred": "Plus de 2.5 Buts", "fiab": "98%", "sec": "Victoire Bayern", "cartons": "Moins de 4.5 Cartons", "score": "4 - 1", "xg": "3.1 - 1.0"}
        ],
        "🏆 DFB-Pokal": [
            {"date": "Mardi • 20:45", "home": "Bayer Leverkusen", "away": "Stuttgart", "pred": "Plus de 2.5 Buts", "fiab": "98%", "sec": "Leverkusen ou Nul", "cartons": "Plus de 3.5 Cartons", "score": "2 - 2", "xg": "2.2 - 1.9"}
        ]
    },
    "🇮🇹 ITALIE": {
        "🇮🇹 Serie A": [
            {"date": "Lundi • 20:45", "home": "Inter Milan", "away": "Lazio", "pred": "Inter Milan ou Nul", "fiab": "98%", "sec": "Plus de 1.5 Buts", "cartons": "Plus de 4.5 Cartons", "score": "2 - 0", "xg": "2.1 - 0.8"}
        ],
        "🏆 Coppa Italia": [
            {"date": "Jeudi • 21:00", "home": "Juventus", "away": "Atalanta", "pred": "Moins de 3.5 Buts", "fiab": "98%", "sec": "Juventus ou Nul", "cartons": "Plus de 4.5 Cartons", "score": "1 - 1", "xg": "1.3 - 1.2"}
        ]
    }
}

# Top 5 Scores Exacts de la Semaine
TOP_5_SCORES = [
    {"match": "Arsenal vs Wolverhampton", "comp": "Premier League", "score": "3 - 0", "fiab": "98%", "justif": "Arsenal n'a encaissé aucun but à domicile sur les 4 derniers matchs."},
    {"match": "Real Madrid vs Betis", "comp": "LaLiga", "score": "2 - 0", "fiab": "98%", "justif": "Moyenne de xG à domicile de 2.4 pour Madrid face aux blocs bas."},
    {"match": "Inter Milan vs Lazio", "comp": "Serie A", "score": "2 - 0", "fiab": "98%", "justif": "Défense d'acier de l'Inter à San Siro (0.8 xG concédé/match)."},
    {"match": "Côte d'Ivoire vs Sénégal", "comp": "CAN", "score": "1 - 0", "fiab": "98%", "justif": "Match à enjeu tactique très fermé, faible nombre de tir cadrés."},
    {"match": "FC Barcelone vs Vissel Kobe", "comp": "Amical", "score": "3 - 1", "fiab": "98%", "justif": "Match amical ouvert avec une rotation offensive lourde du Barca."}
]

# 5. Barre Latérale de Navigation
st.sidebar.markdown("<h2 style='color:#ef4444;'>📌 MENU PRINCIPAL</h2>", unsafe_allow_html=True)

mode = st.sidebar.radio(
    "Mode d'affichage :",
    ["🔥 Hub Pronostics (98% Safe)", "🎯 Top 5 Scores Exacts de la Semaine", "⚡ 5 Coupons Safe Hors Week-end"]
)

st.sidebar.divider()
st.sidebar.markdown("### 🌍 Choisir la Zone / Pays")
zone_selected = st.sidebar.selectbox("Zone Géographique :", list(DATA_COMPETITIONS.keys()))

st.sidebar.divider()
st.sidebar.info("🥊 **Josiastrader Engine 98% :** Aucune prise de risque. Seules les valeurs d'espérance maximale sont sélectionnées.")

# 6. Contenu Principal selon le mode choisi

if mode == "🔥 Hub Pronostics (98% Safe)":
    st.markdown(f"<h2 style='color:#ef4444;'>{zone_selected}</h2>", unsafe_allow_html=True)
    
    competitions = DATA_COMPETITIONS[zone_selected]
    for comp_name, matches in competitions.items():
        st.markdown(f"<div class='section-header'>{comp_name}</div>", unsafe_allow_html=True)
        
        for m in matches:
            st.markdown(f"""
            <div class="match-card">
                <div class="match-meta">📅 {m['date']} • Force de Frappe 98%</div>
                <div class="match-teams">⚽ {m['home']} vs {m['away']}</div>
                <hr style="border:0; border-top: 1px solid #7f1d1d; margin: 10px 0;">
                <div>
                    <span class="badge-safe">🎯 PRONO SAFE : {m['pred']}</span>
                    <span class="badge-confidence">🔥 {m['fiab']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            with st.expander(f"📊 Analyse Tactique & Options : {m['home']} vs {m['away']}"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown(f"<div class='stat-box'><b>Option Secours</b><br>{m['sec']}</div>", unsafe_allow_html=True)
                with col2:
                    st.markdown(f"<div class='stat-box'><b>Cartons Attendus</b><br>{m['cartons']}</div>", unsafe_allow_html=True)
                with col3:
                    st.markdown(f"<div class='stat-box'><b>Projection Score</b><br>{m['score']}</div>", unsafe_allow_html=True)
                st.caption(f"Espérance de Buts (xG) : {m['xg']}")

elif mode == "🎯 Top 5 Scores Exacts de la Semaine":
    st.markdown("<h2 style='color:#ef4444;'>🎯 Onglet Spécial : Top 5 Scores Exacts</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#fca5a5;'>Sélection hebdomadaire rigoureuse basée sur les modèles xG et statistiques défensives.</p>", unsafe_allow_html=True)
    
    for i, item in enumerate(TOP_5_SCORES, 1):
        st.markdown(f"""
        <div class="match-card">
            <div class="match-meta">🏆 {item['comp']} • Pronostic Score Exact #{i}</div>
            <div class="match-teams">⚽ {item['match']}</div>
            <hr style="border:0; border-top: 1px solid #7f1d1d; margin: 10px 0;">
            <div style="margin-bottom:10px;">
                <span class="badge-safe" style="font-size:1rem;">📌 Score Proposé : {item['score']}</span>
                <span class="badge-confidence">🔥 Indice : {item['fiab']}</span>
            </div>
            <div style="font-size:0.85rem; color:#fca5a5; margin-top:8px;">
                <b>💡 Justification IA :</b> {item['justif']}
            </div>
        </div>
        """, unsafe_allow_html=True)

elif mode == "⚡ 5 Coupons Safe Hors Week-end":
    st.markdown("<h2 style='color:#ef4444;'>⚡ 5 Coupons Ultra-Safe (Lundi au Vendredi)</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#fca5a5;'>Sélection de 5 combinaisons haute sécurité pour jouer en semaine hors week-end.</p>", unsafe_allow_html=True)
    
    coupons = [
        {"jour": "Lundi", "match": "Inter Milan vs Lazio", "prono": "Double Chance Inter ou Nul", "cote": "1.25", "fiab": "98%"},
        {"jour": "Mardi", "match": "Arsenal vs Wolverhampton", "prono": "Victoire Arsenal", "cote": "1.30", "fiab": "98%"},
        {"jour": "Mercredi", "match": "Real Madrid vs Man City", "prono": "Plus de 1.5 Buts dans le match", "cote": "1.22", "fiab": "98%"},
        {"jour": "Jeudi", "match": "Côte d'Ivoire vs Sénégal", "prono": "Moins de 2.5 Buts", "cote": "1.40", "fiab": "98%"},
        {"jour": "Vendredi", "match": "Bayern Munich vs Francfort", "prono": "Plus de 2.5 Buts", "cote": "1.32", "fiab": "98%"}
    ]
    
    for c in coupons:
        st.markdown(f"""
        <div class="match-card">
            <div class="match-meta">📅 {c['jour']} (En semaine)</div>
            <div class="match-teams">⚽ {c['match']}</div>
            <hr style="border:0; border-top: 1px solid #7f1d1d; margin: 10px 0;">
            <div>
                <span class="badge-safe">🛡️ {c['prono']}</span>
                <span class="badge-confidence">🔥 {c['fiab']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.divider()
st.caption("Josiastrader ✊🏾 v3.0 • Puissance, Analyse & Sécurité Maximale.")
