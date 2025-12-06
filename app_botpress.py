"""
🎓 ASSISTANT ENSAM MEKNÈS - avec Botpress Webchat Intégré
===========================================================
Interface Streamlit avec intégration directe du webchat Botpress
Version: 3.0.0 - Multi-Pages inspiré du site officiel ENSAM
"""

import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

# ═══════════════════════════════════════════════════════════════════════════════
# 🔧 CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

st.set_page_config(
    page_title="ENSAM Meknès - École Nationale Supérieure d'Arts et Métiers",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configuration Botpress
BOTPRESS_BOT_ID = "a8711977-d355-4654-add0-e27acfebda2d"
BOTPRESS_CLIENT_ID = "335e8ae8-ecb5-474a-a795-c2125157d425"

# Initialisation de l'état de session pour la navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = "🏠 Accueil"

# ═══════════════════════════════════════════════════════════════════════════════
# 🎨 STYLES CSS AMÉLIORÉS - OPTIMISÉ LIGHT MODE
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
<style>
    /* Reset et Style général pour Light Mode */
    .main {
        background-color: #ffffff;
        padding: 0;
    }
    
    .stApp {
        background-color: #ffffff;
    }
    
    /* Supprimer les backgrounds sombres par défaut */
    [data-testid="stAppViewContainer"] {
        background-color: #ffffff;
    }
    
    /* Botpress Bubble Widget - Toujours visible */
    #bp-web-widget {
        z-index: 9999 !important;
    }
    
    .bpFabButton {
        display: block !important;
        position: fixed !important;
        bottom: 20px !important;
        right: 20px !important;
        z-index: 9999 !important;
    }
    
    /* Header principal - Light Mode */
    .main-header {
        text-align: center;
        padding: 2rem 0 1rem 0;
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        border-radius: 0 0 30px 30px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.15);
        margin: -3rem -3rem 2rem -3rem;
    }
    
    .main-title {
        color: #e94560;
        font-size: 2.8em;
        font-weight: 800;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .subtitle {
        color: #f8f9fa;
        font-size: 1.2em;
        margin-top: 0.5rem;
    }
    
    /* Cards pour les sections - Light Mode */
    .info-card {
        background: #ffffff;
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        margin: 1rem 0;
        border-left: 5px solid #e94560;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border: 1px solid #e9ecef;
    }
    
    .info-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.12);
    }
    
    .card-title {
        color: #1a1a2e;
        font-size: 1.3em;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .card-content {
        color: #495057;
        font-size: 0.95em;
        line-height: 1.6;
    }
    
    /* Stats boxes - Light Mode Compatible */
    .stat-box {
        background: linear-gradient(135deg, #e94560 0%, #0f3460 100%);
        color: white;
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 4px 15px rgba(233,69,96,0.25);
    }
    
    .stat-number {
        font-size: 2.5em;
        font-weight: 800;
        display: block;
    }
    
    .stat-label {
        font-size: 0.9em;
        opacity: 0.95;
    }
    
    /* Filière cards - Light Mode */
    .filiere-card {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        color: white;
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        margin: 0.5rem 0;
        transition: transform 0.3s ease;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
    }
    
    .filiere-card:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 20px rgba(0,0,0,0.15);
    }
    
    .filiere-icon {
        font-size: 3em;
        margin-bottom: 0.5rem;
    }
    
    .filiere-name {
        font-size: 1.1em;
        font-weight: 600;
    }
    
    /* Container du chat */
    .chat-container {
        background: white;
        border-radius: 20px;
        padding: 1rem;
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
        margin: 1rem 0;
        min-height: 600px;
    }
    
    /* Style pour le webchat Botpress */
    #webchat {
        width: 100%;
        height: 600px;
        border-radius: 15px;
        overflow: hidden;
    }
    
    /* Cacher le bouton FAB de Botpress */
    .bpFab {
        display: none !important;
    }
    
    /* Ajuster le webchat */
    #webchat .bpWebchat {
        position: unset !important;
        width: 100% !important;
        height: 100% !important;
        max-height: 100% !important;
        max-width: 100% !important;
    }
    
    /* Navigation tabs */
    .nav-tab {
        background: #1a1a2e;
        color: white;
        padding: 0.8rem 1.5rem;
        border-radius: 10px;
        margin: 0.2rem;
        cursor: pointer;
        transition: all 0.3s ease;
        border: none;
        display: inline-block;
    }
    
    .nav-tab:hover {
        background: #e94560;
    }
    
    .nav-tab.active {
        background: #e94560;
    }
    
    /* Timeline pour parcours */
    .timeline-item {
        border-left: 3px solid #e94560;
        padding-left: 20px;
        margin-bottom: 20px;
        position: relative;
    }
    
    .timeline-item::before {
        content: '';
        width: 15px;
        height: 15px;
        background: #e94560;
        border-radius: 50%;
        position: absolute;
        left: -9px;
        top: 0;
    }
    
    /* Sidebar style - Light Mode Compatible */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    [data-testid="stSidebar"] .stButton > button {
        background-color: rgba(233, 69, 96, 0.15);
        color: white !important;
        border: 1px solid rgba(233, 69, 96, 0.3);
        transition: all 0.3s ease;
    }
    
    [data-testid="stSidebar"] .stButton > button:hover {
        background-color: #e94560;
        border-color: #e94560;
        transform: translateX(5px);
    }
    
    /* Actualités card */
    .news-card {
        background: white;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        border-left: 4px solid #e94560;
        box-shadow: 0 2px 10px rgba(0,0,0,0.06);
        border: 1px solid #e9ecef;
    }
    
    .news-date {
        color: #e94560;
        font-size: 0.85em;
        font-weight: 600;
    }
    
    .news-title {
        color: #1a1a2e;
        font-size: 1.05em;
        font-weight: 600;
        margin: 0.3rem 0;
    }
    
    /* Texte et liens - Light Mode */
    p, li, span {
        color: #495057;
    }
    
    /* Divs avec contenu texte */
    .block-container p,
    .block-container li {
        color: #495057;
        line-height: 1.6;
    }
    
    a {
        color: #e94560;
        text-decoration: none;
    }
    
    a:hover {
        color: #1a1a2e;
        text-decoration: underline;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2em;
        }
        #webchat {
            height: 500px;
        }
        .main-header {
            margin: -1rem -1rem 1rem -1rem;
        }
    }
    
    /* Footer */
    .footer {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        margin-top: 2rem;
        box-shadow: 0 -4px 20px rgba(0,0,0,0.1);
    }
    
    .social-icons a {
        color: white;
        font-size: 1.5em;
        margin: 0 10px;
        text-decoration: none;
        transition: color 0.3s ease;
    }
    
    .social-icons a:hover {
        color: #e94560;
    }
    
    /* Améliorer la lisibilité des boutons Streamlit */
    .stButton > button {
        background-color: #e94560;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #1a1a2e;
        box-shadow: 0 4px 15px rgba(233, 69, 96, 0.3);
    }
    
    /* Expander - Light Mode */
    .streamlit-expanderHeader {
        background-color: #f8f9fa;
        border-radius: 8px;
        color: #1a1a2e !important;
        font-weight: 600;
    }
    
    .streamlit-expanderHeader:hover {
        background-color: #e9ecef;
    }
    
    .streamlit-expanderContent {
        background-color: #ffffff;
        border: 1px solid #e9ecef;
        border-radius: 0 0 8px 8px;
    }
    
    /* Assurer que tout le contenu est lisible en light mode */
    h1, h2, h3, h4, h5, h6 {
        color: #1a1a2e !important;
        font-weight: 700;
    }
    
    /* Titres Streamlit markdown */
    [data-testid="stMarkdownContainer"] h1,
    [data-testid="stMarkdownContainer"] h2,
    [data-testid="stMarkdownContainer"] h3 {
        color: #1a1a2e !important;
        font-weight: 700;
        padding: 0.5rem 0;
    }
    
    /* Container principal */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        background-color: #ffffff;
    }
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# 📋 FONCTIONS UTILITAIRES
# ═══════════════════════════════════════════════════════════════════════════════

def render_header():
    """Affiche le header principal"""
    st.markdown("""
    <div class="main-header">
        <h1 class="main-title">🎓 ENSAM Meknès</h1>
        <p class="subtitle">École Nationale Supérieure d'Arts et Métiers</p>
    </div>
    """, unsafe_allow_html=True)

def render_botpress_bubble():
    """Intègre le bubble Botpress (présent sur toutes les pages)"""
    botpress_bubble_html = f"""
    <script src="https://cdn.botpress.cloud/webchat/v3.3/inject.js"></script>
    <script>
        window.botpressWebChat.init({{
            "botId": "{BOTPRESS_BOT_ID}",
            "configuration": {{
                "version": "v2",
                "botName": "Assistant ENSAM Meknès",
                "botDescription": "Votre guide intelligent pour l'ENSAM Meknès",
                "website": {{}}, "email": {{}}, "phone": {{}},
                "termsOfService": {{}}, "privacyPolicy": {{}},
                "color": "#e94560",
                "variant": "solid",
                "headerVariant": "glass",
                "themeMode": "light",
                "fontFamily": "inter",
                "radius": 4,
                "feedbackEnabled": true,
                "footer": "[🎓 ENSAM Meknès](https://www.ensam-umi.ac.ma)",
                "soundEnabled": true,
                "proactiveMessageEnabled": true,
                "proactiveBubbleMessage": "Bonjour! 👋 Besoin d'aide?",
                "proactiveBubbleTriggerType": "afterDelay",
                "proactiveBubbleDelayTime": 3
            }},
            "clientId": "{BOTPRESS_CLIENT_ID}"
        }});
    </script>
    """
    components.html(botpress_bubble_html, height=0)

def render_botpress_chat():
    """Intègre le webchat Botpress en pleine page (pour la page Assistant IA)"""
    botpress_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <script src="https://cdn.botpress.cloud/webchat/v3.3/inject.js"></script>
        <style>
            body {{ margin: 0; padding: 0; overflow: hidden; }}
            #webchat {{ width: 100%; height: 600px; }}
            #webchat .bpWebchat {{
                position: unset !important;
                width: 100% !important;
                height: 100% !important;
                max-height: 100% !important;
                max-width: 100% !important;
            }}
            #webchat .bpFab {{ display: none !important; }}
        </style>
    </head>
    <body>
        <div id="webchat"></div>
        <script>
            window.botpress.on("webchat:ready", () => {{ window.botpress.open(); }});
            window.botpress.init({{
                "botId": "{BOTPRESS_BOT_ID}",
                "configuration": {{
                    "version": "v2",
                    "botName": "Assistant ENSAM Meknès",
                    "botDescription": "Votre guide intelligent pour l'ENSAM Meknès",
                    "website": {{}}, "email": {{}}, "phone": {{}},
                    "termsOfService": {{}}, "privacyPolicy": {{}},
                    "color": "#e94560", "variant": "solid",
                    "headerVariant": "glass", "themeMode": "light",
                    "fontFamily": "inter", "radius": 4,
                    "feedbackEnabled": true,
                    "footer": "[🎓 ENSAM Meknès](https://www.ensam-umi.ac.ma)",
                    "soundEnabled": true,
                    "proactiveMessageEnabled": true,
                    "proactiveBubbleMessage": "Bonjour! 👋 Besoin d'aide?",
                    "proactiveBubbleTriggerType": "afterDelay",
                    "proactiveBubbleDelayTime": 5
                }},
                "clientId": "{BOTPRESS_CLIENT_ID}",
                "selector": "#webchat"
            }});
        </script>
    </body>
    </html>
    """
    components.html(botpress_html, height=620, scrolling=False)

# ═══════════════════════════════════════════════════════════════════════════════
# 📊 SIDEBAR - Navigation
# ═══════════════════════════════════════════════════════════════════════════════

with st.sidebar:
    st.markdown("""
    <div style='text-align: center; padding: 1rem;'>
        <div style='font-size: 5rem;'>🎓</div>
        <h2 style='color: white; margin: 0;'>ENSAM Meknès</h2>
        <p style='color: #e94560; font-size: 0.9em;'>Arts et Métiers</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 🧭 Navigation")
    
    # Menu de navigation
    pages = [
        "🏠 Accueil",
        "🎓 Formations",
        "📚 Admission",
        "🔬 Recherche",
        "🏢 Entreprises",
        "👨‍🎓 Espace Étudiants",
        "💬 Assistant IA",
        "📞 Contact"
    ]
    
    for page in pages:
        if st.button(page, key=page, use_container_width=True):
            st.session_state.current_page = page
    
    st.markdown("---")
    
    st.markdown("### 📌 À propos")
    st.markdown("""
    **ENSAM Meknès** - Créée en 1997 sous les Hautes Directives Royales
    
    Formation d'ingénieurs d'État Arts et Métiers polyvalents
    """)
    
    st.markdown("---")
    
    st.markdown("### ℹ️ Informations")
    st.markdown("""
    **Contact:**
    - 📧 contact@ensam.umi.ac.ma
    - 📞 +212 5 35 46 71 71
    - 🌐 [www.ensam-umi.ac.ma](https://www.ensam-umi.ac.ma)
    
    **Adresse:**
    Marjane 2, BP 4024, Meknès, Maroc
    
    **Version:** 3.0.0
    """)

# ═══════════════════════════════════════════════════════════════════════════════
# 📄 CONTENU DES PAGES
# ═══════════════════════════════════════════════════════════════════════════════

render_header()

# Intégrer le bubble Botpress sur toutes les pages
render_botpress_bubble()

# ═══════════════════════════════════════════════════════════════════════════════
# 🏠 PAGE ACCUEIL
# ═══════════════════════════════════════════════════════════════════════════════

if st.session_state.current_page == "🏠 Accueil":
    
    # Section hero
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style='text-align: center; padding: 2rem 0;'>
            <h2 style='color: #1a1a2e; font-size: 2.5em; font-weight: 800;'>Bienvenue à l'ENSAM Meknès</h2>
            <p style='color: #495057; font-size: 1.2em;'>Le grand établissement de technologie</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Statistiques
    st.markdown("<h3 style='color: #1a1a2e; font-weight: 700; margin-top: 2rem;'>📊 L'ENSAM en chiffres</h3>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="stat-box">
            <span class="stat-number">28+</span>
            <span class="stat-label">Années d'Excellence</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-box">
            <span class="stat-number">8</span>
            <span class="stat-label">Spécialités</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-box">
            <span class="stat-number">1000+</span>
            <span class="stat-label">Étudiants</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="stat-box">
            <span class="stat-number">5000+</span>
            <span class="stat-label">Lauréats</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # À propos de l'école
    st.markdown("<h3 style='color: #1a1a2e; font-weight: 700; margin-top: 2rem;'>🎓 À propos de l'ENSAM</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class="info-card">
        <div class="card-title">École Nationale Supérieure d'Arts et Métiers de Meknès</div>
        <div class="card-content">
            L'ENSAM de Meknès, créée en 1997 sous les Hautes Directives Royales, est un établissement public 
            de l'enseignement supérieur et composant de l'Université Moulay Ismail de Meknès. 
            <br><br>
            Nous formons des <strong>ingénieurs d'État Arts et Métiers polyvalents</strong> pour répondre à la 
            demande croissante du marché d'emploi. Nos ingénieurs sont reconnus pour leur haute compétence 
            technique, leur pragmatisme et leur aptitude au travail en équipe.
            <br><br>
            <strong>Notre mission :</strong> Former des managers innovants, armés d'une haute compétence 
            technologique et entrepreneuriale, capables de s'intégrer dans des équipes multidisciplinaires 
            et multiculturelles.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Actualités
    st.markdown("<h3 style='color: #1a1a2e; font-weight: 700; margin-top: 2rem;'>📰 Actualités récentes</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="news-card">
            <div class="news-date">📅 Décembre 2025</div>
            <div class="news-title">Soutenance de Thèse : Azddine ADDADI</div>
            <p style='font-size: 0.9em; color: #666;'>
                Le Directeur de l'École annonce la soutenance de thèse de doctorat...
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="news-card">
            <div class="news-date">📅 Novembre 2025</div>
            <div class="news-title">Workshop - Modélisation & Systèmes Intelligents</div>
            <p style='font-size: 0.9em; color: #666;'>
                Approches et Applications en Ingénierie Multiphysique...
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="news-card">
            <div class="news-date">📅 Novembre 2025</div>
            <div class="news-title">Concours de recrutement MC - Génie Civil</div>
            <p style='font-size: 0.9em; color: #666;'>
                Liste des candidats convoqués pour l'entretien oral...
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="news-card">
            <div class="news-date">📅 Octobre 2025</div>
            <div class="news-title">Résultats Concours MC - Mathématiques Appliquées</div>
            <p style='font-size: 0.9em; color: #666;'>
                Publication des résultats du concours de recrutement...
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Points forts
    st.markdown("<h3 style='color: #1a1a2e; font-weight: 700; margin-top: 2rem;'>✨ Nos Points Forts</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <div class="card-title">🎯 Excellence Académique</div>
            <div class="card-content">
                Formation rigoureuse sur 5 ans avec un tronc commun Arts et Métiers 
                et 8 spécialités d'approfondissement
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <div class="card-title">🔬 Recherche & Innovation</div>
            <div class="card-content">
                Centres de recherche de pointe et partenariats avec l'industrie 
                pour une formation pratique
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="info-card">
            <div class="card-title">🌐 Insertion Professionnelle</div>
            <div class="card-content">
                Taux d'employabilité élevé grâce aux stages en entreprise 
                et au réseau Alumni
            </div>
        </div>
        """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# 🎓 PAGE FORMATIONS
# ═══════════════════════════════════════════════════════════════════════════════

elif st.session_state.current_page == "🎓 Formations":
    
    st.markdown("## 🎓 Formations à l'ENSAM Meknès")
    
    # Parcours pédagogique
    st.markdown("### 📚 Parcours Pédagogique")
    st.markdown("""
    <div class="info-card">
        <div class="card-title">Formation d'Ingénieur Arts et Métiers (5 ans - 10 semestres)</div>
        <div class="card-content">
            Le profil de l'ingénieur de demain doit être celui d'un <strong>manager innovant</strong>, 
            armé d'une haute compétence technologique et entrepreneuriale. Il devra être capable de 
            s'intégrer rapidement dans des équipes multidisciplinaires et multiculturelles.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Structure de formation
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📖 Années Préparatoires (2 ans)")
        st.markdown("""
        <div class="timeline-item">
            <h4>Objectifs</h4>
            <p>Solides bases scientifiques, technologiques et méthodologiques</p>
        </div>
        
        <div class="timeline-item">
            <h4>Matières Principales</h4>
            <ul>
                <li><strong>Mathématiques :</strong> Algèbre, Analyse, Méthodes numériques</li>
                <li><strong>Physique :</strong> Électricité, Mécanique, Thermodynamique</li>
                <li><strong>Technologie :</strong> Matériaux, Forge, Usinage, DAO</li>
                <li><strong>Soft Skills :</strong> Informatique, Langues, Communication</li>
            </ul>
        </div>
        
        <div class="timeline-item">
            <h4>Compétences Acquises</h4>
            <p>Grande capacité de travail, d'organisation, d'analyse et de synthèse</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 🎯 Cycle Ingénieur (3 ans)")
        st.markdown("""
        <div class="timeline-item">
            <h4>Phase Générale (3 semestres)</h4>
            <p>Tronc commun Arts et Métiers - Socle technologique</p>
            <ul>
                <li>Mécanique et matériaux</li>
                <li>Automatique, Électronique, Électrotechnique</li>
                <li>Énergétique</li>
                <li>Bureaux d'études</li>
                <li>Gestion des systèmes de production</li>
            </ul>
        </div>
        
        <div class="timeline-item">
            <h4>Phase d'Approfondissement (3 semestres)</h4>
            <p>Formation spécialisée dans l'une des 8 filières</p>
        </div>
        
        <div class="timeline-item">
            <h4>Stages Industriels</h4>
            <p>4 stages - Durée totale : 7 à 11 mois</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Les 8 spécialités
    st.markdown("### 🔧 Les 8 Spécialités d'Ingénierie")
    
    specialites = [
        {
            "icon": "💻",
            "name": "Génie Informatique",
            "detail": "Ingénierie Logicielle et Systèmes Intelligents (GI-ILSI)"
        },
        {
            "icon": "⚙️",
            "name": "Génie Mécanique",
            "detail": "Structures et Ingénierie des Produits (GM-SIP)"
        },
        {
            "icon": "🏭",
            "name": "Génie Mécanique",
            "detail": "Procédés de Fabrication Industrielle (GM-PFI)"
        },
        {
            "icon": "⚡",
            "name": "Génie Mécanique",
            "detail": "Énergétique (GM-E)"
        },
        {
            "icon": "🔌",
            "name": "Génie Électromécanique",
            "detail": "Commande et Management Industriel (GEM-CMI)"
        },
        {
            "icon": "🔋",
            "name": "Génie Électromécanique",
            "detail": "Énergie et Maintenance Électromécanique (GEM-EME)"
        },
        {
            "icon": "🏗️",
            "name": "Génie Industriel",
            "detail": "Ingénierie et Management (GEPS)"
        },
        {
            "icon": "🤖",
            "name": "Ingénierie Automatique",
            "detail": "Traitement de Données (IATD)"
        }
    ]
    
    col1, col2, col3, col4 = st.columns(4)
    
    for idx, spec in enumerate(specialites):
        with [col1, col2, col3, col4][idx % 4]:
            st.markdown(f"""
            <div class="filiere-card">
                <div class="filiere-icon">{spec['icon']}</div>
                <div class="filiere-name">{spec['name']}</div>
                <p style='font-size: 0.85em; margin-top: 0.5rem;'>{spec['detail']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Débouchés
    st.markdown("### 💼 Perspectives d'Emploi")
    st.markdown("""
    <div class="info-card">
        <div class="card-content">
            Les lauréats de l'ENSAM-Meknès peuvent occuper des emplois très variés :
            <br><br>
            <div style='display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem;'>
                <div>✅ Ingénieur Calcul</div>
                <div>✅ Ingénieur Production</div>
                <div>✅ Ingénieur Bureau d'Étude</div>
                <div>✅ Ingénieur Développement Industriel</div>
                <div>✅ Ingénieur Responsable Produits</div>
                <div>✅ Consultant</div>
                <div>✅ Enseignant-chercheur</div>
                <div>✅ Ingénieur-chercheur</div>
                <div>✅ Chef de Projet</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# 📚 PAGE ADMISSION
# ═══════════════════════════════════════════════════════════════════════════════

elif st.session_state.current_page == "📚 Admission":
    
    st.markdown("## 📚 Modalités d'Admission")
    
    st.markdown("""
    <div class="info-card">
        <div class="card-title">🎯 L'admission à l'ENSAM-Meknès se fait par trois voies</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Les trois voies d'admission
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <div class="card-title">📝 En 1ère Année</div>
            <div class="card-content">
                <h4>Années Préparatoires Intégrées</h4>
                <p><strong>Conditions :</strong></p>
                <ul>
                    <li>Baccalauréat Sciences & Techniques</li>
                    <li>Très bon niveau en Maths et Physique</li>
                    <li>Concours national</li>
                    <li>Étude du dossier</li>
                </ul>
                <p><strong>Formation :</strong> 5 ans (2 ans prépa + 3 ans cycle ingénieur)</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <div class="card-title">🎓 En 3ème Année</div>
            <div class="card-content">
                <h4>1ère Année Cycle Ingénieur</h4>
                <p><strong>Conditions :</strong></p>
                <ul>
                    <li>Classes Préparatoires (CPGE)</li>
                    <li>Concours National Commun (CNC)</li>
                    <li>DUT / BTS avec mention</li>
                    <li>Licence (L2 validée)</li>
                </ul>
                <p><strong>Formation :</strong> 3 ans de cycle ingénieur</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="info-card">
            <div class="card-title">🔬 En 4ème Année</div>
            <div class="card-content">
                <h4>2ème Année Cycle Ingénieur</h4>
                <p><strong>Conditions :</strong></p>
                <ul>
                    <li>Licence validée</li>
                    <li>Master 1 dans une spécialité</li>
                    <li>Dossier académique excellent</li>
                    <li>Entretien de motivation</li>
                </ul>
                <p><strong>Formation :</strong> 2 ans pour finaliser le diplôme</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Calendrier
    st.markdown("### 📅 Calendrier des Admissions")
    st.markdown("""
    <div class="info-card">
        <div class="card-content">
            <div style='display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.5rem;'>
                <div>
                    <h4>🗓️ Phase de Candidature</h4>
                    <p><strong>Janvier - Mars :</strong> Dépôt des dossiers en ligne</p>
                    <p><strong>Avril :</strong> Étude des dossiers</p>
                </div>
                <div>
                    <h4>📝 Phase de Sélection</h4>
                    <p><strong>Mai - Juin :</strong> Concours et entretiens</p>
                    <p><strong>Juillet :</strong> Publication des résultats</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Documents requis
    st.markdown("### 📄 Documents Requis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <div class="card-title">📋 Dossier de Candidature</div>
            <div class="card-content">
                <ul>
                    <li>✅ Formulaire de candidature dûment rempli</li>
                    <li>✅ Copie certifiée du Baccalauréat</li>
                    <li>✅ Relevés de notes (2 dernières années)</li>
                    <li>✅ Photocopie CIN</li>
                    <li>✅ 4 photos d'identité</li>
                    <li>✅ CV détaillé</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <div class="card-title">🎯 Critères de Sélection</div>
            <div class="card-content">
                <ul>
                    <li>📊 Excellence académique</li>
                    <li>🧮 Résultats en Mathématiques et Physique</li>
                    <li>💪 Motivation et projet professionnel</li>
                    <li>🗣️ Compétences en communication</li>
                    <li>🌟 Activités extra-scolaires</li>
                    <li>🏆 Distinctions et récompenses</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# 🔬 PAGE RECHERCHE
# ═══════════════════════════════════════════════════════════════════════════════

elif st.session_state.current_page == "🔬 Recherche":
    
    st.markdown("## 🔬 Recherche & Innovation")
    
    st.markdown("""
    <div class="info-card">
        <div class="card-title">🎯 Notre Vision Scientifique</div>
        <div class="card-content">
            L'ENSAM Meknès place la recherche et l'innovation au cœur de sa stratégie de développement,
            avec des laboratoires de pointe et des partenariats industriels solides.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Centres de recherche
    st.markdown("### 🏛️ Centres de Recherche")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <div class="card-title">🎓 CED-RISI</div>
            <div class="card-content">
                <h4>Centre d'Études Doctorales</h4>
                <p><strong>Recherche et Innovation pour les Sciences de l'Ingénieur</strong></p>
                <br>
                <p>Formation doctorale de haut niveau dans :</p>
                <ul>
                    <li>Génie Mécanique & Énergétique</li>
                    <li>Génie Électrique & Automatique</li>
                    <li>Génie Industriel & Management</li>
                    <li>Informatique & Systèmes Intelligents</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <div class="card-title">🔬 CRSIT</div>
            <div class="card-content">
                <h4>Centre de Recherche Scientifique et d'Innovation Technologique</h4>
                <br>
                <p>Axes de recherche :</p>
                <ul>
                    <li>Matériaux avancés et nano-matériaux</li>
                    <li>Énergies renouvelables</li>
                    <li>Industrie 4.0 et IoT</li>
                    <li>Intelligence Artificielle</li>
                    <li>Développement durable</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Formation doctorale
    st.markdown("### 📚 Formation Doctorale")
    
    st.markdown("""
    <div class="info-card">
        <div class="card-title">🎓 Doctorat à l'ENSAM</div>
        <div class="card-content">
            <p><strong>Durée :</strong> 3 à 6 ans</p>
            <p><strong>Structure :</strong></p>
            <ul>
                <li>Modules de formation (1ère année)</li>
                <li>Travaux de recherche encadrés</li>
                <li>Publications scientifiques</li>
                <li>Participation à des conférences internationales</li>
                <li>Soutenance de thèse</li>
            </ul>
            <br>
            <p><strong>Opportunités :</strong> Bourses d'excellence, mobilité internationale, collaboration avec l'industrie</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Publications
    st.markdown("### 📰 Publications & Thèses")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="stat-box">
            <span class="stat-number">150+</span>
            <span class="stat-label">Publications Scientifiques</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-box">
            <span class="stat-number">50+</span>
            <span class="stat-label">Thèses Soutenues</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-box">
            <span class="stat-number">20+</span>
            <span class="stat-label">Projets de Recherche</span>
        </div>
        """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# 🏢 PAGE ENTREPRISES
# ═══════════════════════════════════════════════════════════════════════════════

elif st.session_state.current_page == "🏢 Entreprises":
    
    st.markdown("## 🏢 Partenariats Entreprises")
    
    st.markdown("""
    <div class="info-card">
        <div class="card-title">🤝 Collaboration École-Entreprise</div>
        <div class="card-content">
            L'ENSAM Meknès développe des partenariats stratégiques avec le tissu industriel national 
            et international pour garantir une formation en adéquation avec les besoins du marché.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Types de partenariats
    st.markdown("### 🔗 Types de Partenariats")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <div class="card-title">🎓 Formation</div>
            <div class="card-content">
                <ul>
                    <li>Stages en entreprise</li>
                    <li>Projets industriels</li>
                    <li>Interventions de professionnels</li>
                    <li>Visites d'entreprises</li>
                    <li>Formation continue</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <div class="card-title">🔬 Recherche</div>
            <div class="card-content">
                <ul>
                    <li>Contrats de recherche</li>
                    <li>Thèses CIFRE</li>
                    <li>Transfert technologique</li>
                    <li>Brevets et innovations</li>
                    <li>Consulting technique</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="info-card">
            <div class="card-title">💼 Recrutement</div>
            <div class="card-content">
                <ul>
                    <li>Forum Entreprises</li>
                    <li>Job dating</li>
                    <li>Offres d'emploi</li>
                    <li>Présentation entreprises</li>
                    <li>Réseau Alumni</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Innovation et Entrepreneuriat
    st.markdown("### 🚀 Innovation et Entrepreneuriat")
    
    st.markdown("""
    <div class="info-card">
        <div class="card-title">💡 Incubateur ENSAM</div>
        <div class="card-content">
            <p>L'ENSAM accompagne les porteurs de projets innovants :</p>
            <ul>
                <li>🎯 Accompagnement personnalisé</li>
                <li>💰 Recherche de financement</li>
                <li>🏢 Mise à disposition d'espaces de travail</li>
                <li>👥 Mentorat par des professionnels</li>
                <li>🌐 Mise en réseau</li>
                <li>📚 Formations en entrepreneuriat</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Politique partenariale
    st.markdown("### 🎯 Politique Partenariale")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <div class="card-title">🌟 Nos Partenaires</div>
            <div class="card-content">
                <p><strong>Secteurs d'activité :</strong></p>
                <ul>
                    <li>⚙️ Automobile et Aéronautique</li>
                    <li>⚡ Énergie et Environnement</li>
                    <li>🏭 Industrie manufacturière</li>
                    <li>💻 Technologies de l'information</li>
                    <li>🏗️ BTP et Génie Civil</li>
                    <li>🔬 R&D et Innovation</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <div class="card-title">📝 Devenir Partenaire</div>
            <div class="card-content">
                <p><strong>Contactez-nous pour :</strong></p>
                <ul>
                    <li>📋 Conventions de partenariat</li>
                    <li>🎓 Accueillir des stagiaires</li>
                    <li>🔬 Projets de R&D collaboratifs</li>
                    <li>💼 Recruter nos lauréats</li>
                    <li>🏆 Sponsoring d'événements</li>
                    <li>👨‍🏫 Interventions pédagogiques</li>
                </ul>
                <br>
                <p><strong>📧 Contact :</strong> partenariats@ensam.umi.ac.ma</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# 👨‍🎓 PAGE ESPACE ÉTUDIANTS
# ═══════════════════════════════════════════════════════════════════════════════

elif st.session_state.current_page == "👨‍🎓 Espace Étudiants":
    
    st.markdown("## 👨‍🎓 Espace Étudiants")
    
    # Liens rapides
    st.markdown("### 🔗 Liens Utiles")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <div class="card-title">📅 Emploi du Temps</div>
            <div class="card-content">
                <p>Consultez votre emploi du temps en ligne</p>
                <br>
                <a href="http://www.ensam-umi.ac.ma/?p=5074" target="_blank" 
                   style="background: #e94560; color: white; padding: 10px 20px; 
                          border-radius: 5px; text-decoration: none; display: inline-block;">
                    Accéder ➜
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <div class="card-title">👤 Compte Académique</div>
            <div class="card-content">
                <p>Accédez à votre espace personnel</p>
                <br>
                <a href="https://my.umi.ac.ma/#/myumi/login" target="_blank" 
                   style="background: #e94560; color: white; padding: 10px 20px; 
                          border-radius: 5px; text-decoration: none; display: inline-block;">
                    Se connecter ➜
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="info-card">
            <div class="card-title">🌐 Site ENSAM</div>
            <div class="card-content">
                <p>Visitez le site officiel</p>
                <br>
                <a href="https://www.ensam-umi.ac.ma" target="_blank" 
                   style="background: #e94560; color: white; padding: 10px 20px; 
                          border-radius: 5px; text-decoration: none; display: inline-block;">
                    Visiter ➜
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Clubs et associations
    st.markdown("### 🎭 Clubs et Associations")
    
    st.markdown("""
    <div class="info-card">
        <div class="card-title">🌟 Vie Associative Dynamique</div>
        <div class="card-content">
            <p>L'ENSAM encourage la vie associative et parascolaire à travers de nombreux clubs :</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    clubs = [
        {"icon": "🎨", "name": "Club Culturel", "desc": "Arts, théâtre, musique"},
        {"icon": "⚽", "name": "Club Sportif", "desc": "Football, basketball, athlétisme"},
        {"icon": "🤖", "name": "Club Robotique", "desc": "Robotique et mécatronique"},
        {"icon": "💻", "name": "Club Informatique", "desc": "Développement et IA"},
        {"icon": "🌱", "name": "Club Environnement", "desc": "Développement durable"},
        {"icon": "📸", "name": "Club Média", "desc": "Photo, vidéo, communication"}
    ]
    
    col1, col2, col3 = st.columns(3)
    
    for idx, club in enumerate(clubs):
        with [col1, col2, col3][idx % 3]:
            st.markdown(f"""
            <div class="info-card">
                <div style="font-size: 2em; text-align: center;">{club['icon']}</div>
                <div class="card-title" style="text-align: center;">{club['name']}</div>
                <div class="card-content" style="text-align: center;">{club['desc']}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Compétitions
    st.markdown("### 🏆 Compétitions et Événements")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <div class="card-title">🎓 Compétitions Académiques</div>
            <div class="card-content">
                <ul>
                    <li>🤖 Concours de robotique</li>
                    <li>💡 Hackathons et challenges innovation</li>
                    <li>📊 Compétitions de gestion de projet</li>
                    <li>🏗️ Concours de conception mécanique</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <div class="card-title">🌟 Événements</div>
            <div class="card-content">
                <ul>
                    <li>🎤 Journées portes ouvertes</li>
                    <li>🏢 Forum Entreprises</li>
                    <li>🔬 Séminaires scientifiques</li>
                    <li>🎉 Gala de l'ENSAM</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# 💬 PAGE ASSISTANT IA
# ═══════════════════════════════════════════════════════════════════════════════

elif st.session_state.current_page == "💬 Assistant IA":
    
    st.markdown("## 💬 Assistant Intelligent ENSAM")
    
    st.markdown("""
    <div class="info-card">
        <div class="card-title">🤖 Votre Assistant Personnel</div>
        <div class="card-content">
            Posez toutes vos questions sur l'ENSAM Meknès : formations, admissions, vie étudiante, 
            contacts des professeurs, et bien plus encore !
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Afficher le chatbot
    render_botpress_chat()
    
    # Instructions
    with st.expander("ℹ️ Comment utiliser l'assistant"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **📝 Poser une question:**
            1. Tapez votre question dans le chat ci-dessus
            2. Appuyez sur Entrée ou cliquez sur le bouton d'envoi
            3. L'assistant vous répondra instantanément
            
            **🎯 Catégories disponibles:**
            - Contacts des professeurs
            - Informations sur les filières
            - Programmes d'études
            - Documents administratifs
            - Vie étudiante et clubs
            """)
        
        with col2:
            st.markdown("""
            **💡 Exemples de questions:**
            - "Comment contacter le professeur X?"
            - "Quelles sont les 8 spécialités?"
            - "Comment s'inscrire en 1ère année?"
            - "Quels sont les clubs disponibles?"
            - "Comment obtenir une attestation?"
            
            **✨ Fonctionnalités:**
            - Réponses en temps réel
            - Historique de conversation
            - Support multimédia
            """)

# ═══════════════════════════════════════════════════════════════════════════════
# 📞 PAGE CONTACT
# ═══════════════════════════════════════════════════════════════════════════════

elif st.session_state.current_page == "📞 Contact":
    
    st.markdown("## 📞 Nous Contacter")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <div class="card-title">📍 Coordonnées</div>
            <div class="card-content">
                <h4>École Nationale Supérieure d'Arts et Métiers</h4>
                <p><strong>Adresse :</strong><br>
                Marjane 2, B.P. 15290 Al-Mansour<br>
                Meknès, Maroc</p>
                
                <p><strong>📞 Téléphone :</strong><br>
                +212 5 35 46 71 71</p>
                
                <p><strong>📠 Fax :</strong><br>
                +212 5 35 46 71 73</p>
                
                <p><strong>📧 Email :</strong><br>
                contact@ensam.umi.ac.ma</p>
                
                <p><strong>🌐 Site Web :</strong><br>
                <a href="https://www.ensam-umi.ac.ma" target="_blank">www.ensam-umi.ac.ma</a></p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card">
            <div class="card-title">🕐 Horaires d'Ouverture</div>
            <div class="card-content">
                <p><strong>Lundi - Vendredi :</strong> 8h00 - 17h00</p>
                <p><strong>Samedi :</strong> Fermé</p>
                <p><strong>Dimanche :</strong> Fermé</p>
                <br>
                <p style="font-size: 0.9em; color: #666;">
                    * Horaires susceptibles de modification pendant les vacances
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <div class="card-title">📧 Services</div>
            <div class="card-content">
                <p><strong>Direction :</strong><br>
                direction@ensam.umi.ac.ma</p>
                
                <p><strong>Scolarité :</strong><br>
                scolarite@ensam.umi.ac.ma</p>
                
                <p><strong>Admissions :</strong><br>
                admissions@ensam.umi.ac.ma</p>
                
                <p><strong>Stages :</strong><br>
                stages@ensam.umi.ac.ma</p>
                
                <p><strong>Partenariats :</strong><br>
                partenariats@ensam.umi.ac.ma</p>
                
                <p><strong>Recherche :</strong><br>
                recherche@ensam.umi.ac.ma</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card">
            <div class="card-title">🌐 Réseaux Sociaux</div>
            <div class="card-content" style="text-align: center; padding: 1rem 0;">
                <p><a href="https://www.facebook.com/ensam.umi" target="_blank" style="color: #e94560; text-decoration: none; font-size: 1.1em;">📘 Facebook</a></p>
                <p><a href="https://www.instagram.com/fameensam" target="_blank" style="color: #e94560; text-decoration: none; font-size: 1.1em;">📷 Instagram</a></p>
                <p><a href="https://www.twitter.com/ensammeknes" target="_blank" style="color: #e94560; text-decoration: none; font-size: 1.1em;">🐦 Twitter</a></p>
                <p><a href="https://www.youtube.com/ensammaroc" target="_blank" style="color: #e94560; text-decoration: none; font-size: 1.1em;">▶️ YouTube</a></p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Plan d'accès
    st.markdown("### 🗺️ Plan d'Accès")
    st.markdown("""
    <div class="info-card">
        <div class="card-content">
            <p>L'ENSAM Meknès est située à Marjane 2, facilement accessible depuis le centre-ville de Meknès.</p>
            <p><strong>En voiture :</strong> Suivre les indications vers Marjane 2</p>
            <p><strong>En transport en commun :</strong> Lignes de bus desservant le quartier Marjane</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# 📌 FOOTER
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("---")
st.markdown(f"""
<div class="footer">
    <h3 style='margin: 0; color: #e94560;'>🎓 ENSAM Meknès</h3>
    <p style='margin: 0.5rem 0;'>École Nationale Supérieure d'Arts et Métiers</p>
    <p style='margin: 0.5rem 0; font-size: 0.95em;'>
        Marjane 2, BP 15290 Al-Mansour, Meknès, Maroc<br>
        Tel: +212 5 35 46 71 71 | Email: contact@ensam.umi.ac.ma
    </p>
    <div class="social-icons" style="margin: 1rem 0;">
        <a href="https://www.facebook.com/ensam.umi" target="_blank">📘</a>
        <a href="https://www.instagram.com/fameensam" target="_blank">📷</a>
        <a href="https://www.twitter.com/ensammeknes" target="_blank">🐦</a>
        <a href="https://www.youtube.com/ensammaroc" target="_blank">▶️</a>
    </div>
    <p style='margin: 1rem 0 0 0; font-size: 0.85em; opacity: 0.8;'>
        © {datetime.now().year} ENSAM Meknès - Tous droits réservés | v3.0.0
    </p>
</div>
""", unsafe_allow_html=True)
