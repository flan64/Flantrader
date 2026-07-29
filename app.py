<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Le Maestros VIP - Pronostics Football</title>
    <style>
        :root {
            --bg-dark: #0d1117;
            --card-bg: #161b22;
            --accent-gold: #f1c40f;
            --accent-green: #2ea44f;
            --accent-blue: #3182ce;
            --accent-red: #e53e3e;
            --text-main: #f0f6fc;
            --text-muted: #8b949e;
            --border-color: #30363d;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: var(--bg-dark);
            color: var(--text-main);
            padding-bottom: 30px;
        }

        /* Header */
        header {
            background: linear-gradient(135deg, #1f2937, #111827);
            padding: 20px;
            text-align: center;
            border-bottom: 2px solid var(--accent-gold);
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .logo {
            font-size: 1.8rem;
            font-weight: bold;
            color: var(--accent-gold);
            letter-spacing: 1.5px;
        }

        .tagline {
            font-size: 0.85rem;
            color: var(--text-muted);
            margin-top: 4px;
        }

        /* Navigation Bar */
        nav {
            display: flex;
            justify-content: space-around;
            background-color: var(--card-bg);
            border-bottom: 1px solid var(--border-color);
            overflow-x: auto;
        }

        .nav-btn {
            background: none;
            border: none;
            color: var(--text-muted);
            padding: 15px 12px;
            font-size: 0.95rem;
            font-weight: 600;
            cursor: pointer;
            white-space: nowrap;
            transition: all 0.3s ease;
            border-bottom: 3px solid transparent;
        }

        .nav-btn.active {
            color: var(--accent-gold);
            border-bottom-color: var(--accent-gold);
        }

        /* Main Container */
        .container {
            max-width: 800px;
            margin: 20px auto;
            padding: 0 15px;
        }

        .tab-content {
            display: none;
        }

        .tab-content.active {
            display: block;
        }

        /* UI Cards */
        .card {
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 18px;
            margin-bottom: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        }

        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 8px;
        }

        .badge {
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: bold;
            text-transform: uppercase;
        }

        .badge-safe { background-color: var(--accent-green); color: #fff; }
        .badge-exact { background-color: var(--accent-gold); color: #000; }
        .badge-vip { background-color: #8b5cf6; color: #fff; }

        /* Betting Items */
        .match-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin: 10px 0;
            font-size: 0.95rem;
        }

        .odds {
            font-weight: bold;
            color: var(--accent-gold);
            background-color: rgba(241, 196, 15, 0.1);
            padding: 3px 8px;
            border-radius: 5px;
        }

        .code-box {
            background-color: #0d1117;
            border: 1px dashed var(--accent-gold);
            padding: 10px;
            border-radius: 8px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 15px;
        }

        .btn-copy {
            background-color: var(--accent-gold);
            color: #000;
            border: none;
            padding: 6px 12px;
            border-radius: 6px;
            font-weight: bold;
            cursor: pointer;
        }

        /* Championnats Accordion */
        .country-group {
            margin-bottom: 12px;
        }

        .country-header {
            width: 100%;
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            color: var(--text-main);
            padding: 12px 15px;
            text-align: left;
            font-size: 1rem;
            font-weight: 600;
            border-radius: 8px;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
        }

        .competitions-list {
            display: none;
            background-color: #0d1117;
            padding: 10px 20px;
            border-radius: 0 0 8px 8px;
            border: 1px solid var(--border-color);
            border-top: none;
        }

        .competitions-list li {
            list-style: none;
            padding: 8px 0;
            border-bottom: 1px solid #21262d;
            font-size: 0.9rem;
            color: var(--text-muted);
        }

        .competitions-list li:last-child {
            border-bottom: none;
        }

        /* Calculator */
        .calc-input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border-radius: 6px;
            border: 1px solid var(--border-color);
            background-color: #0d1117;
            color: #fff;
        }
    </style>
</head>
<body>

    <header>
        <div class="logo">⚡ LE MAESTROS VIP</div>
        <div class="tagline">Pronostics Experts & Gestion Rigoureuse</div>
    </header>

    <nav>
        <button class="nav-btn active" onclick="switchTab('safes')">🛡️ Coupons Safes</button>
        <button class="nav-btn" onclick="switchTab('exacts')">🎯 Scores Exacts</button>
        <button class="nav-btn" onclick="switchTab('competitions')">🏆 Compétitions</button>
        <button class="nav-btn" onclick="switchTab('stats')">📊 Stats & Mises</button>
    </nav>

    <div class="container">

        <!-- TAB 1: COUPONS SAFES -->
        <div id="safes" class="tab-content active">
            <div class="card">
                <div class="card-header">
                    <h3>📌 Ticket Safe du Jour</h3>
                    <span class="badge badge-safe">Confiance : 9/10</span>
                </div>
                <div class="match-row">
                    <span>Real Madrid vs Getafe (Victoire Real)</span>
                    <span class="odds">1.35</span>
                </div>
                <div class="match-row">
                    <span>Man. City vs Wolves (Over 1.5 Buts)</span>
                    <span class="odds">1.22</span>
                </div>
                <hr style="border-color: var(--border-color); margin: 10px 0;">
                <div class="match-row">
                    <strong>Cote Totale : 1.65</strong>
                    <span style="color: var(--accent-green); font-weight: bold;">Mise conseillée : 5%</span>
                </div>
                <div class="code-box">
                    <span>Code Bookmaker : <strong id="code-safe">MAESTRO1X</strong></span>
                    <button class="btn-copy" onclick="copyCode('code-safe')">Copier</button>
                </div>
            </div>

            <div class="card">
                <div class="card-header">
                    <h3>🚀 Défi Montante - Étape 2</h3>
                    <span class="badge badge-vip">VIP</span>
                </div>
                <div class="match-row">
                    <span>PSG vs Rennes (PSG ou Nul & +1.5 buts)</span>
                    <span class="odds">1.40</span>
                </div>
                <div class="code-box">
                    <span>Code Bookmaker : <strong id="code-montante">MONTANTE2</strong></span>
                    <button class="btn-copy" onclick="copyCode('code-montante')">Copier</button>
                </div>
            </div>
        </div>

        <!-- TAB 2: SCORES EXACTS -->
        <div id="exacts" class="tab-content">
            <div class="card">
                <div class="card-header">
                    <h3>🎯 Score Exact Sélectionné</h3>
                    <span class="badge badge-exact">Analyse Tactique</span>
                </div>
                <div class="match-row">
                    <span>Arsenal vs Chelsea</span>
                    <span class="odds">Cote: 8.50</span>
                </div>
                <div class="match-row">
                    <span style="color: var(--text-muted);">Score Prédict : <strong>2 - 1</strong></span>
                    <span style="color: var(--accent-gold);">Indice : Favori</span>
                </div>
            </div>

            <div class="card">
                <div class="card-header">
                    <h3>✅ Dernières Validations</h3>
                    <span class="badge badge-safe">Historique</span>
                </div>
                <div class="match-row">
                    <span>Inter vs AC Milan (Prédit: 1-0)</span>
                    <span style="color: var(--accent-green);">Validé 🟢 (Cote 7.20)</span>
                </div>
                <div class="match-row">
                    <span>Bayern vs Dortmund (Prédit: 3-1)</span>
                    <span style="color: var(--accent-green);">Validé 🟢 (Cote 11.00)</span>
                </div>
            </div>
        </div>

        <!-- TAB 3: CHAMPIONNATS & COUPES -->
        <div id="competitions" class="tab-content">
            <h3 style="margin-bottom: 15px;">Couverture par Pays & Compétitions</h3>

            <div class="country-group">
                <button class="country-header" onclick="toggleAccordion('anglet')">
                    <span>🇬🇧 Angleterre</span> <span>▼</span>
                </button>
                <ul id="anglet" class="competitions-list">
                    <li>Premier League (Championnat)</li>
                    <li>FA Cup (Coupe d'Angleterre)</li>
                    <li>EFL Cup (Carabao Cup)</li>
                </ul>
            </div>

            <div class="country-group">
                <button class="country-header" onclick="toggleAccordion('espagne')">
                    <span>🇪🇸 Espagne</span> <span>▼</span>
                </button>
                <ul id="espagne" class="competitions-list">
                    <li>LaLiga (Championnat)</li>
                    <li>Copa del Rey (Coupe du Roi)</li>
                    <li>Supercopa de España</li>
                </ul>
            </div>

            <div class="country-group">
                <button class="country-header" onclick="toggleAccordion('france')">
                    <span>🇫🇷 France</span> <span>▼</span>
                </button>
                <ul id="france" class="competitions-list">
                    <li>Ligue 1 (Championnat)</li>
                    <li>Coupe de France</li>
                    <li>Trophée des Champions</li>
                </ul>
            </div>

            <div class="country-group">
                <button class="country-header" onclick="toggleAccordion('italie')">
                    <span>🇮🇹 Italie</span> <span>▼</span>
                </button>
                <ul id="italie" class="competitions-list">
                    <li>Serie A (Championnat)</li>
                    <li>Coppa Italia</li>
                    <li>Supercoppa Italiana</li>
                </ul>
            </div>

            <div class="country-group">
                <button class="country-header" onclick="toggleAccordion('allemagne')">
                    <span>🇩🇪 Allemagne</span> <span>▼</span>
                </button>
                <ul id="allemagne" class="competitions-list">
                    <li>Bundesliga (Championnat)</li>
                    <li>DFB-Pokal (Coupe d'Allemagne)</li>
                    <li>DFL-Supercup</li>
                </ul>
            </div>

            <div class="country-group">
                <button class="country-header" onclick="toggleAccordion('europe')">
                    <span>🇪🇺 Europe (UEFA)</span> <span>▼</span>
                </button>
                <ul id="europe" class="competitions-list">
                    <li>UEFA Champions League</li>
                    <li>UEFA Europa League</li>
                    <li>UEFA Europa Conference League</li>
                </ul>
            </div>
        </div>

        <!-- TAB 4: STATS & CALCULATEUR DE BANKROLL -->
        <div id="stats" class="tab-content">
            <div class="card">
                <h3>🧮 Calculateur de Mise Conseillée</h3>
                <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 5px;">Entrez votre capital total pour obtenir le montant exact à miser :</p>
                <input type="number" id="bankroll" class="calc-input" placeholder="Capital Total (ex: 50000)" oninput="calculateStake()">
                
                <div style="margin-top: 15px;">
                    <div class="match-row">
                        <span>Ticket Safe (5%) :</span>
                        <strong id="stake-safe" style="color: var(--accent-green);">0 FCFA</strong>
                    </div>
                    <div class="match-row">
                        <span>Score Exact / Fun (1%) :</span>
                        <strong id="stake-exact" style="color: var(--accent-gold);">0 FCFA</strong>
                    </div>
                </div>
            </div>

            <div class="card">
                <h3>📈 Bilans & Performance du Mois</h3>
                <div class="match-row" style="margin-top: 10px;">
                    <span>Taux de Réussite Safes :</span>
                    <strong style="color: var(--accent-green);">86%</strong>
                </div>
                <div class="match-row">
                    <span>ROI Mensuel Moyen :</span>
                    <strong style="color: var(--accent-gold);">+34.5%</strong>
                </div>
            </div>
        </div>

    </div>

    <script>
        // Navigation par onglets
        function switchTab(tabId) {
            document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
            document.querySelectorAll('.nav-btn').forEach(btn => btn.classList.remove('active'));
            
            document.getElementById(tabId).classList.add('active');
            event.currentTarget.classList.add('active');
        }

        // Accordéon pour les compétitions
        function toggleAccordion(id) {
            const list = document.getElementById(id);
            if (list.style.display === "block") {
                list.style.display = "none";
            } else {
                list.style.display = "block";
            }
        }

        // Copier les codes promo/bookmakers
        function copyCode(elementId) {
            const codeText = document.getElementById(elementId).innerText;
            navigator.clipboard.writeText(codeText);
            alert("Code " + codeText + " copié dans le presse-papier !");
        }

        // Calculateur de mise automatique
        function calculateStake() {
            const bankroll = parseFloat(document.getElementById('bankroll').value);
            if (!isNaN(bankroll) && bankroll > 0) {
                document.getElementById('stake-safe').innerText = (bankroll * 0.05).toFixed(0) + " FCFA";
                document.getElementById('stake-exact').innerText = (bankroll * 0.01).toFixed(0) + " FCFA";
            } else {
                document.getElementById('stake-safe').innerText = "0 FCFA";
                document.getElementById('stake-exact').innerText = "0 FCFA";
            }
        }
    </script>
</body>
</html>
