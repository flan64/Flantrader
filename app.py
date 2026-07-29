import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(
    page_title="SafePredict AI - Dashboard Pronostics",
    page_icon="⚽",
    layout="wide"
)

# Style CSS personnalisé
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0e14;
        color: #e2e8f0;
    }
    .league-title {
        color: #38bdf8;
        border-bottom: 2px solid #1e293b;
        padding-bottom: 8px;
        margin-top: 15px;
        margin-bottom: 20px;
    }
    .match-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 18px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
    }
    .match-teams {
        font-size: 1.2rem;
        font-weight: 700;
        color: #f8fafc;
        margin-bottom: 5px;
    }
    .match-meta {
        font-size: 0.85rem;
        color: #94a3b8;
        margin-bottom: 12px;
    }
    .badge-safe {
        background-color: #166534;
        color: #4ade80;
        padding: 4px 10px;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.85rem;
        display: inline-block;
    }
    .badge-confidence {
        background-color: #1e3a8a;
        color: #60a5fa;
        padding: 4px 10px;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.85rem;
        display: inline-block;
        float: right;
    }
    .stat-box {
        background-color: #0f172a;
        border-radius: 8px;
        padding: 10px;
        text-align: center;
        border: 1px solid #1e293b;
    }
    </style>
""", unsafe_allow_html=True)

# En-tête principal
st.markdown("<h1 style='text-align: center; color: #38bdf8;'>⚽ SafePredict AI - Hub Pronostics</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8;'>Analyses automatiques et pronostics haute fiabilité pour les prochains matchs</p>", unsafe_allow_html=True)
st.divider()

# Base de données des matchs à venir & analyses
MATCHES_DATA = {
    "🏆 Ligue des Champions (UCL)": [
        {
            "home": "Real Madrid", "away": "Manchester City", "date": "Prochainement • 20:00",
            "pred_principal": "Plus de 2.5 Buts", "fiabilite": "96%",
            "option_sec": "Double Chance : Real Madrid ou Nul",
            "cartons": "Plus de 3.5 Cartons", "score_exact": "2 - 1 / 2 - 2",
            "xg_h": 2.1, "xg_a": 1.9
        },
        {
            "home": "PSG", "away": "Bayern Munich", "date": "Prochainement • 20:00",
            "pred_principal": "Les deux équipes marquent", "fiabilite": "94%",
            "option_sec": "Plus de 1.5 Buts",
            "cartons": "Plus de 4.5 Cartons", "score_exact": "2 - 1 / 1 - 2",
            "xg_h": 1.8, "xg_a": 2.0
        },
        {
            "home": "Barcelona", "away": "Inter Milan", "date": "Prochainement • 20:00",
            "pred_principal": "Victoire Barcelona ou Nul", "fiabilite": "92%",
            "option_sec": "Plus de 1.5 Buts",
            "cartons": "Moins de 5.5 Cartons", "score_exact": "2 - 0 / 1 - 1",
            "xg_h": 2.2, "xg_a": 1.1
        }
    ],
    "🟠 Europa League": [
        {
            "home": "AS Roma", "away": "Porto", "date": "Jeudi • 17:45",
            "pred_principal": "Moins de 3.5 Buts", "fiabilite": "93%",
            "option_sec": "Double Chance : AS Roma ou Nul",
            "cartons": "Plus de 4.5 Cartons", "score_exact": "1 - 0 / 1 - 1",
            "xg_h": 1.4, "xg_a": 1.0
        },
        {
            "home": "Athletic Bilbao", "away": "Lazio", "date": "Jeudi • 20:00",
            "pred_principal": "Plus de 1.5 Buts", "fiabilite": "91%",
            "option_sec": "Bilbao gagne au moins une mi-temps",
            "cartons": "Plus de 3.5 Cartons", "score_exact": "2 - 1 / 1 - 1",
            "xg_h": 1.7, "xg_a": 1.2
        }
    ],
    "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League": [
        {
            "home": "Arsenal", "away": "Chelsea", "date": "Samedi • 16:30",
            "pred_principal": "Victoire Arsenal", "fiabilite": "95%",
            "option_sec": "Plus de 1.5 Buts",
            "cartons": "Plus de 3.5 Cartons", "score_exact": "2 - 0 / 3 - 1",
            "xg_h": 2.3, "xg_a": 0.9
        },
        {
            "home": "Liverpool", "away": "Manchester United", "date": "Dimanche • 16:30",
            "pred_principal": "Plus de 2.5 Buts", "fiabilite": "97%",
            "option_sec": "Liverpool gagne",
            "cartons": "Plus de 4.5 Cartons", "score_exact": "3 - 1 / 2 - 1",
            "xg_h": 2.7, "xg_a": 1.2
        }
    ],
    "🇪🇸 LaLiga": [
        {
            "home": "Atletico Madrid", "away": "Sevilla", "date": "Samedi • 20:00",
            "pred_principal": "Moins de 2.5 Buts", "fiabilite": "94%",
            "option_sec": "Atletico Madrid ou Nul",
            "cartons": "Plus de 5.5 Cartons", "score_exact": "1 - 0 / 2 - 0",
            "xg_h": 1.5, "xg_a": 0.7
        },
        {
            "home": "Villarreal", "away": "Real Betis", "date": "Dimanche • 18:30",
            "pred_principal": "Les deux équipes marquent", "fiabilite": "90%",
            "option_sec": "Plus de 2.5 Buts",
            "cartons": "Moins de 5.5 Cartons", "score_exact": "2 - 2 / 2 - 1",
            "xg_h": 1.9, "xg_a": 1.8
        }
    ],
    "🇩🇪 Bundesliga": [
        {
            "home": "Bayer Leverkusen", "away": "Dortmund", "date": "Samedi • 17:30",
            "pred_principal": "Plus de 2.5 Buts", "fiabilite": "96%",
            "option_sec": "Les deux équipes marquent",
            "cartons": "Moins de 4.5 Cartons", "score_exact": "3 - 2 / 2 - 2",
            "xg_h": 2.5, "xg_a": 2.2
        }
    ]
}

# Menu de sélection dans la barre latérale
st.sidebar.title("📌 Navigation")
selected_competition = st.sidebar.radio(
    "Choisir la compétition :",
    list(MATCHES_DATA.keys())
)

st.sidebar.divider()
st.sidebar.info("💡 **Conseil SafePredict :** Privilégiez les pronostics avec une fiabilité ≥ 92%.")

# Zone d'affichage des matchs
st.markdown(f"<h2 class='league-title'>{selected_competition}</h2>", unsafe_allow_html=True)

matches = MATCHES_DATA[selected_competition]

for match in matches:
    with st.container():
        st.markdown(f"""
        <div class="match-card">
            <div class="match-meta">📅 {match['date']} • Analyse IA</div>
            <div class="match-teams">⚽ {match['home']} vs {match['away']}</div>
            <hr style="border:0; border-top: 1px solid #334155; margin: 10px 0;">
            <div style="margin-bottom: 12px;">
                <span class="badge-safe">🎯 Sécurisé : {match['pred_principal']}</span>
                <span class="badge-confidence">🔥 Fiabilité : {match['fiabilite']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Détails supplémentaires au clic
        with st.expander(f"📊 Voir l'analyse détaillée : {match['home']} vs {match['away']}"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("<div class='stat-box'><b>Option Secondaire</b><br>" + match['option_sec'] + "</div>", unsafe_allow_html=True)
            with col2:
                st.markdown("<div class='stat-box'><b>Cartons Attendus</b><br>" + match['cartons'] + "</div>", unsafe_allow_html=True)
            with col3:
                st.markdown("<div class='stat-box'><b>Score Proposé</b><br>" + match['score_exact'] + "</div>", unsafe_allow_html=True)
            
            st.caption(f"Espérance de Buts (xG) : {match['home']} ({match['xg_h']}) - ({match['xg_a']}) {match['away']}")

st.divider()
st.caption("SafePredict AI Engine v2.0 • Les données sont mises à jour régulièrement.")
