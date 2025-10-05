# dashboard_defense_brics_avance.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Configuration de la page
st.set_page_config(
    page_title="Analyse Stratégique Avancée - BRICS",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé avancé
st.markdown("""
<style>
    .main-header {
        font-size: 2.8rem;
        background: linear-gradient(45deg, #FF9933, #0055A4, #008000, #DA0000, #FFB81C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .metric-card {
        background: linear-gradient(135deg, #FF9933, #FF671F);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .section-header {
        color: #0055A4;
        border-bottom: 3px solid #FF9933;
        padding-bottom: 0.8rem;
        margin-top: 2rem;
        font-size: 1.8rem;
        font-weight: bold;
    }
    .china-card {
        background: linear-gradient(135deg, #DE2910, #FFDE00);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    .russia-card {
        background: linear-gradient(135deg, #0033A0, #D52B1E);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .india-card {
        background: linear-gradient(135deg, #FF9933, #138808);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .brazil-card {
        background: linear-gradient(135deg, #009C3B, #FFDF00);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .safrica-card {
        background: linear-gradient(135deg, #007A4D, #FFB81C);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .cooperation-card {
        background: linear-gradient(135deg, #4B0082, #8A2BE2);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

class DefenseBricsDashboardAvance:
    def __init__(self):
        self.branches_options = self.define_branches_options()
        self.programmes_options = self.define_programmes_options()
        self.member_capabilities = self.define_member_capabilities()
        self.cooperation_projects = self.define_cooperation_projects()
        
    def define_branches_options(self):
        return [
            "BRICS - Vue d'Ensemble", "Chine", "Russie", "Inde", 
            "Brésil", "Afrique du Sud", "Coopérations BRICS",
            "Nouveaux Membres (2024)"
        ]
    
    def define_programmes_options(self):
        return [
            "Coopération Militaire BRICS", "Exercices Conjoints", 
            "Transferts de Technologie", "Défense Anti-Missile",
            "Marine BRICS", "Cybersécurité Collective",
            "Industrie de Défense Intégrée"
        ]
    
    def define_member_capabilities(self):
        return {
            "Chine": {
                "budget": 230.0,
                "personnel": 2035,
                "nucleaire": "Oui",
                "porte_avions": 3,
                "icbm": "DF-41, DF-31AG",
                "technologies": "Hypersonique, IA, Cyber"
            },
            "Russie": {
                "budget": 65.0,
                "personnel": 1014,
                "nucleaire": "Oui", 
                "porte_avions": 1,
                "icbm": "RS-28 Sarmat, RS-24 Yars",
                "technologies": "Hypersonique, Guerre électronique"
            },
            "Inde": {
                "budget": 73.0,
                "personnel": 1455,
                "nucleaire": "Oui",
                "porte_avions": 2,
                "icbm": "Agni-V, Agni-VI",
                "technologies": "Missiles, Spatial, Cyber"
            },
            "Brésil": {
                "budget": 22.0,
                "personnel": 334,
                "nucleaire": "Non",
                "porte_avions": 0,
                "forces": "Amazonie, Surveillance maritime",
                "technologies": "Sous-marins, Systèmes de surveillance"
            },
            "Afrique du Sud": {
                "budget": 3.0,
                "personnel": 72,
                "nucleaire": "Non",
                "forces": "Forces spéciales, Paix ONU",
                "technologies": "Cybersécurité, Renseignement"
            }
        }
    
    def define_cooperation_projects(self):
        return {
            "Exercice Naval BRICS": {"pays": "Tous", "type": "Exercice conjoint", "statut": "Actif", "frequence": "Annuel"},
            "Système de Communication Sécurisé": {"pays": "Chine/Russie/Inde", "type": "Communication", "statut": "Développement", "objectif": "2026"},
            "Centre Cyber BRICS": {"pays": "Chine/Russie", "type": "Cybersécurité", "statut": "Opérationnel", "localisation": "Moscou/Pékin"},
            "Développement Missilistique": {"pays": "Chine/Russie/Inde", "type": "Technologie", "statut": "Coopération", "domaines": "Hypersonique, Croisière"},
            "Surveillance Spatiale": {"pays": "Chine/Russie", "type": "Espace", "statut": "Partage données", "satellites": "Reconnaissance"}
        }
    
    def generate_advanced_data(self, selection):
        """Génère des données avancées et détaillées pour les BRICS"""
        annees = list(range(2000, 2028))
        
        config = self.get_advanced_config(selection)
        
        data = {
            'Annee': annees,
            'Budget_Defense_Mds': self.simulate_advanced_budget(annees, config),
            'Personnel_Milliers': self.simulate_advanced_personnel(annees, config),
            'PIB_Militaire_Pourcent': self.simulate_military_gdp_percentage(annees),
            'Exercices_Militaires': self.simulate_advanced_exercises(annees, config),
            'Readiness_Operative': self.simulate_advanced_readiness(annees),
            'Capacite_Dissuasion': self.simulate_advanced_deterrence(annees),
            'Temps_Mobilisation_Jours': self.simulate_advanced_mobilization(annees),
            'Exercices_Conjoints': self.simulate_joint_exercises(annees),
            'Developpement_Technologique': self.simulate_tech_development(annees),
            'Capacite_Navale': self.simulate_naval_capacity(annees),
            'Couverture_AD': self.simulate_air_defense_coverage(annees),
            'Cooperation_Structured': self.simulate_structured_cooperation(annees),
            'Cyber_Capabilities': self.simulate_cyber_capabilities(annees),
            'Production_Armements': self.simulate_weapon_production(annees)
        }
        
        # Données spécifiques aux programmes
        if 'cooperation' in config.get('priorites', []):
            data.update({
                'Projets_Cooperation': self.simulate_cooperation_projects(annees),
                'Echanges_Technologiques': self.simulate_tech_exchanges(annees),
                'Exercices_BRICS': self.simulate_brics_exercises(annees)
            })
        
        if 'nucleaire' in config.get('priorites', []):
            data.update({
                'Stock_Ogives_Nucleaires': self.simulate_nuclear_arsenal(annees),
                'Portee_Missiles_Km': self.simulate_missile_range(annees),
                'Triade_Nucleaire': self.simulate_nuclear_triad(annees)
            })
        
        if 'marine' in config.get('priorites', []):
            data.update({
                'Porte_Avions': self.simulate_aircraft_carriers(annees),
                'Sous_Marins': self.simulate_submarines(annees),
                'Projection_Maritime': self.simulate_maritime_projection(annees)
            })
        
        if 'innovation' in config.get('priorites', []):
            data.update({
                'Recherche_Defense': self.simulate_defense_research(annees),
                'Technologies_Emergentes': self.simulate_emerging_tech(annees),
                'Exportations_Armes': self.simulate_weapon_exports(annees)
            })
        
        return pd.DataFrame(data), config
    
    def get_advanced_config(self, selection):
        """Configuration avancée avec plus de détails pour les BRICS"""
        configs = {
            "BRICS - Vue d'Ensemble": {
                "type": "alliance_multipolaire",
                "budget_base": 400.0,
                "personnel_base": 4900,
                "exercices_base": 180,
                "priorites": ["cooperation", "nucleaire", "marine", "innovation", "cyber"],
                "doctrines": ["Multipolarité", "Souveraineté stratégique", "Défense collective"],
                "objectifs": "Contrepoids à l'hégémonie occidentale"
            },
            "Chine": {
                "type": "puissance_mondiale",
                "budget_base": 230.0,
                "personnel_base": 2035,
                "priorites": ["marine", "missiles", "cyber", "espace"],
                "capacites": ["Force de frappe nucléaire", "Marine bleue", "Guerre électronique"],
                "doctrine": "Défense active périphérique"
            },
            "Russie": {
                "type": "puissance_nucleaire",
                "budget_base": 65.0,
                "personnel_base": 1014,
                "priorites": ["nucleaire", "missiles", "cyber", "asymetrique"],
                "capacites": ["Triade nucléaire", "Systèmes hypersoniques", "Guerre hybride"],
                "doctrine": "Dissuasion stratégique élargie"
            },
            "Coopérations BRICS": {
                "type": "cooperation_strategique",
                "budget_base": 15.0,
                "priorites": ["exercices_conjoints", "transfert_technologie", "intelligence_collective"],
                "projets": ["Exercices navals", "Centre cyber", "Systèmes C4ISR"],
                "objectifs": "Autonomie stratégique collective"
            }
        }
        
        return configs.get(selection, {
            "type": "membre_brics",
            "personnel_base": 300,
            "exercices_base": 25,
            "priorites": ["defense_generique"]
        })
    
    def simulate_advanced_budget(self, annees, config):
        """Simulation avancée du budget avec variations géopolitiques"""
        budget_base = config.get('budget_base', 350.0)
        budgets = []
        for annee in annees:
            base = budget_base * (1 + 0.055 * (annee - 2000))
            # Variations selon événements géopolitiques
            if 2008 <= annee <= 2010:  # Crise financière
                base *= 1.08  # Les BRICS ont moins souffert
            elif annee >= 2014:  # Formation BRICS formelle
                base *= 1.1
            elif annee >= 2020:  # Pandémie et tensions
                base *= 1.12
            elif annee >= 2022:  # Expansion géopolitique
                base *= 1.15
            budgets.append(base)
        return budgets
    
    def simulate_advanced_personnel(self, annees, config):
        """Simulation avancée des effectifs"""
        personnel_base = config.get('personnel_base', 4500)
        return [personnel_base * (1 + 0.008 * (annee - 2000)) for annee in annees]
    
    def simulate_military_gdp_percentage(self, annees):
        """Pourcentage du PIB consacré à la défense"""
        return [2.2 + 0.12 * (annee - 2000) for annee in annees]
    
    def simulate_advanced_exercises(self, annees, config):
        """Exercices militaires avec saisonnalité"""
        base = config.get('exercices_base', 120)
        return [base + 6 * (annee - 2000) + 8 * np.sin(2 * np.pi * (annee - 2000)/4) for annee in annees]
    
    def simulate_advanced_readiness(self, annees):
        """Préparation opérationnelle avancée"""
        readiness = []
        for annee in annees:
            base = 65 + 1.8 * (annee - 2000)
            if annee >= 2008:  # Émergence BRICS
                base += 6
            if annee >= 2014:  # Coopération renforcée
                base += 5
            if annee >= 2020:  # Modernisation accélérée
                base += 4
            readiness.append(min(base, 90))
        return readiness
    
    def simulate_advanced_deterrence(self, annees):
        """Capacité de dissuasion avancée"""
        deterrence = []
        for annee in annees:
            base = 60  # Début modeste
            if annee >= 2006:
                base += 3  # Montée en puissance
            if annee >= 2014:
                base += 5  # Coordination BRICS
            if annee >= 2020:
                base += 7  # Capacités avancées
            deterrence.append(min(base, 88))
        return deterrence
    
    def simulate_advanced_mobilization(self, annees):
        """Temps de mobilisation avancé"""
        return [max(50 - 1.5 * (annee - 2000), 15) for annee in annees]
    
    def simulate_joint_exercises(self, annees):
        """Exercices conjoints BRICS"""
        exercises = []
        for annee in annees:
            if annee < 2010:
                exercises.append(2)
            elif annee < 2015:
                exercises.append(5 + (annee - 2010))
            else:
                exercises.append(10 + 2 * (annee - 2015))
        return exercises
    
    def simulate_tech_development(self, annees):
        """Développement technologique global"""
        return [min(55 + 2.8 * (annee - 2000), 88) for annee in annees]
    
    def simulate_naval_capacity(self, annees):
        """Capacité navale combinée"""
        return [min(45 + 3.2 * (annee - 2000), 85) for annee in annees]
    
    def simulate_air_defense_coverage(self, annees):
        """Couverture de défense anti-aérienne"""
        return [min(50 + 2.5 * (annee - 2000), 86) for annee in annees]
    
    def simulate_structured_cooperation(self, annees):
        """Coopération structurée BRICS"""
        return [min(20 + 4 * (annee - 2009), 75) for annee in annees if annee >= 2009] + [0] * (2009 - min(annees))
    
    def simulate_cyber_capabilities(self, annees):
        """Capacités cybernétiques"""
        return [min(50 + 3.5 * (annee - 2000), 87) for annee in annees]
    
    def simulate_weapon_production(self, annees):
        """Production d'armements (indice)"""
        return [min(60 + 2.8 * (annee - 2000), 89) for annee in annees]
    
    def simulate_cooperation_projects(self, annees):
        """Projets de coopération BRICS"""
        return [min(2 + 3 * (annee - 2009), 25) for annee in annees if annee >= 2009] + [0] * (2009 - min(annees))
    
    def simulate_tech_exchanges(self, annees):
        """Échanges technologiques"""
        return [min(10 + 4 * (annee - 2009), 60) for annee in annees if annee >= 2009] + [0] * (2009 - min(annees))
    
    def simulate_brics_exercises(self, annees):
        """Exercices spécifiques BRICS"""
        return [min(1 + 2 * (annee - 2014), 15) for annee in annees if annee >= 2014] + [0] * (2014 - min(annees))
    
    def simulate_nuclear_arsenal(self, annees):
        """Arsenal nucléaire combiné"""
        return [min(3000 + 100 * (annee - 2000), 6000) for annee in annees]
    
    def simulate_missile_range(self, annees):
        """Portée moyenne des missiles (km)"""
        return [min(2000 + 150 * (annee - 2000), 8000) for annee in annees]
    
    def simulate_nuclear_triad(self, annees):
        """Capacité de triade nucléaire"""
        return [min(40 + 3 * (annee - 2000), 85) for annee in annees]
    
    def simulate_aircraft_carriers(self, annees):
        """Porte-avions opérationnels"""
        return [min(1 + 0.3 * (annee - 2000), 6) for annee in annees]
    
    def simulate_submarines(self, annees):
        """Sous-marins stratégiques"""
        return [min(10 + 2 * (annee - 2000), 50) for annee in annees]
    
    def simulate_maritime_projection(self, annees):
        """Projection maritime"""
        return [min(30 + 3 * (annee - 2000), 80) for annee in annees]
    
    def simulate_defense_research(self, annees):
        """Recherche défense"""
        return [min(40 + 3.2 * (annee - 2000), 84) for annee in annees]
    
    def simulate_emerging_tech(self, annees):
        """Technologies émergentes"""
        return [min(35 + 4 * (annee - 2000), 82) for annee in annees]
    
    def simulate_weapon_exports(self, annees):
        """Exportations d'armes (milliards USD)"""
        return [min(5 + 1.5 * (annee - 2000), 30) for annee in annees]
    
    def display_advanced_header(self):
        """En-tête avancé avec plus d'informations"""
        st.markdown('<h1 class="main-header">🌍 ANALYSE STRATÉGIQUE AVANCÉE - BRICS</h1>', 
                   unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
            <div style='text-align: center; background: linear-gradient(135deg, #FF9933, #0055A4, #008000); 
            padding: 1rem; border-radius: 10px; color: white; margin: 1rem 0;'>
            <h3>🛡️ COOPÉRATION STRATÉGIQUE DES BRICS - BRÉSIL, RUSSIE, INDE, CHINE, AFRIQUE DU SUD</h3>
            <p><strong>Analyse multidimensionnelle des capacités militaires et de la coopération stratégique (2000-2027)</strong></p>
            </div>
            """, unsafe_allow_html=True)
    
    def create_advanced_sidebar(self):
        """Sidebar avancé avec plus d'options"""
        st.sidebar.markdown("## 🎛️ PANEL DE CONTRÔLE AVANCÉ")
        
        # Sélection du type d'analyse
        type_analyse = st.sidebar.radio(
            "Mode d'analyse:",
            ["Vue d'Ensemble BRICS", "Analyse par Pays", "Coopérations Stratégiques", "Scénarios Géopolitiques"]
        )
        
        if type_analyse == "Vue d'Ensemble BRICS":
            selection = st.sidebar.selectbox("Niveau d'analyse:", self.branches_options)
        elif type_analyse == "Analyse par Pays":
            selection = st.sidebar.selectbox("Pays membre:", ["Chine", "Russie", "Inde", "Brésil", "Afrique du Sud"])
        elif type_analyse == "Coopérations Stratégiques":
            selection = st.sidebar.selectbox("Programme de coopération:", self.programmes_options)
        else:
            selection = "Scénarios Géopolitiques"
        
        # Options avancées
        st.sidebar.markdown("### 🔧 OPTIONS AVANCÉES")
        show_geopolitical = st.sidebar.checkbox("Contexte géopolitique", value=True)
        show_cooperation = st.sidebar.checkbox("Analyse des coopérations", value=True)
        show_technical = st.sidebar.checkbox("Détails techniques", value=True)
        threat_assessment = st.sidebar.checkbox("Évaluation des menaces", value=True)
        
        # Paramètres de simulation
        st.sidebar.markdown("### ⚙️ PARAMÈTRES DE SIMULATION")
        scenario = st.sidebar.selectbox("Scénario:", ["Coopération Renforcée", "Expansion BRICS+", "Confrontation avec l'Occident", "Autonomie Stratégique"])
        
        return {
            'selection': selection,
            'type_analyse': type_analyse,
            'show_geopolitical': show_geopolitical,
            'show_cooperation': show_cooperation,
            'show_technical': show_technical,
            'threat_assessment': threat_assessment,
            'scenario': scenario
        }
    
    def display_strategic_metrics(self, df, config):
        """Métriques stratégiques avancées"""
        st.markdown('<h3 class="section-header">🎯 TABLEAU DE BORD STRATÉGIQUE BRICS</h3>', 
                   unsafe_allow_html=True)
        
        derniere_annee = df['Annee'].max()
        data_actuelle = df[df['Annee'] == derniere_annee].iloc[0]
        data_2000 = df[df['Annee'] == 2000].iloc[0]
        
        # Première ligne de métriques
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div class="metric-card">
                <h4>💰 BUDGET DÉFENSE TOTAL 2027</h4>
                <h2>{:.0f} Md$</h2>
                <p>📈 {:.1f}% du PIB BRICS</p>
            </div>
            """.format(data_actuelle['Budget_Defense_Mds'], data_actuelle['PIB_Militaire_Pourcent']), 
            unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="metric-card">
                <h4>👥 EFFECTIFS TOTAUX</h4>
                <h2>{:,.0f}K</h2>
                <p>⚔️ +{:.1f}% depuis 2000</p>
            </div>
            """.format(data_actuelle['Personnel_Milliers'], 
                     ((data_actuelle['Personnel_Milliers'] - data_2000['Personnel_Milliers']) / data_2000['Personnel_Milliers']) * 100), 
            unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="china-card">
                <h4>☢️ PUISSANCE NUCLÉAIRE</h4>
                <h2>{:.0f}%</h2>
                <p>🚀 {} ogives stratégiques</p>
            </div>
            """.format(data_actuelle['Capacite_Dissuasion'], 
                     int(data_actuelle.get('Stock_Ogives_Nucleaires', 0))), 
            unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div class="cooperation-card">
                <h4>🤝 COOPÉRATION BRICS</h4>
                <h2>{:.0f}%</h2>
                <p>🔧 {} projets conjoints</p>
            </div>
            """.format(data_actuelle['Cooperation_Structured'], 
                     int(data_actuelle.get('Projets_Cooperation', 0))), 
            unsafe_allow_html=True)
        
        # Deuxième ligne de métriques
        col5, col6, col7, col8 = st.columns(4)
        
        with col5:
            reduction_temps = ((data_2000['Temps_Mobilisation_Jours'] - data_actuelle['Temps_Mobilisation_Jours']) / 
                             data_2000['Temps_Mobilisation_Jours']) * 100
            st.metric(
                "⏱️ Temps Mobilisation",
                f"{data_actuelle['Temps_Mobilisation_Jours']:.1f} jours",
                f"{reduction_temps:+.1f}%"
            )
        
        with col6:
            croissance_navale = ((data_actuelle['Capacite_Navale'] - data_2000['Capacite_Navale']) / 
                               data_2000['Capacite_Navale']) * 100
            st.metric(
                "🌊 Puissance Navale",
                f"{data_actuelle['Capacite_Navale']:.1f}%",
                f"{croissance_navale:+.1f}%"
            )
        
        with col7:
            if 'Portee_Missiles_Km' in df.columns:
                croissance_portee = ((data_actuelle['Portee_Missiles_Km'] - data_2000.get('Portee_Missiles_Km', 2000)) / 
                                   data_2000.get('Portee_Missiles_Km', 2000)) * 100
                st.metric(
                    "🎯 Portée Missiles Moyenne",
                    f"{data_actuelle['Portee_Missiles_Km']:,.0f} km",
                    f"{croissance_portee:+.1f}%"
                )
        
        with col8:
            st.metric(
                "📊 Préparation Opérationnelle",
                f"{data_actuelle['Readiness_Operative']:.1f}%",
                f"+{(data_actuelle['Readiness_Operative'] - data_2000['Readiness_Operative']):.1f}%"
            )
    
    def create_comprehensive_analysis(self, df, config):
        """Analyse complète multidimensionnelle"""
        st.markdown('<h3 class="section-header">📊 ANALYSE MULTIDIMENSIONNELLE BRICS</h3>', 
                   unsafe_allow_html=True)
        
        # Graphiques principaux
        col1, col2 = st.columns(2)
        
        with col1:
            # Évolution des capacités principales
            fig = go.Figure()
            
            capacites = ['Readiness_Operative', 'Capacite_Dissuasion', 'Cyber_Capabilities', 'Cooperation_Structured']
            noms = ['Préparation Opér.', 'Dissuasion Strat.', 'Capacités Cyber', 'Coopération BRICS']
            couleurs = ['#FF9933', '#0055A4', '#4B0082', '#008000']
            
            for i, (cap, nom, couleur) in enumerate(zip(capacites, noms, couleurs)):
                if cap in df.columns:
                    fig.add_trace(go.Scatter(
                        x=df['Annee'], y=df[cap],
                        mode='lines', name=nom,
                        line=dict(color=couleur, width=4),
                        hovertemplate=f"{nom}: %{{y:.1f}}%<extra></extra>"
                    ))
            
            fig.update_layout(
                title="📈 ÉVOLUTION DES CAPACITÉS STRATÉGIQUES BRICS (2000-2027)",
                xaxis_title="Année",
                yaxis_title="Niveau de Capacité (%)",
                height=500,
                template="plotly_white",
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Analyse des coopérations stratégiques
            strategic_data = []
            strategic_names = []
            
            if 'Exercices_Conjoints' in df.columns:
                strategic_data.append(df['Exercices_Conjoints'])
                strategic_names.append('Exercices Conjoints')
            
            if 'Projets_Cooperation' in df.columns:
                strategic_data.append(df['Projets_Cooperation'])
                strategic_names.append('Projets Coopération')
            
            if 'Echanges_Technologiques' in df.columns:
                strategic_data.append(df['Echanges_Technologiques'])
                strategic_names.append('Échanges Technologiques')
            
            if strategic_data:
                fig = make_subplots(specs=[[{"secondary_y": True}]])
                
                for i, (data, nom) in enumerate(zip(strategic_data, strategic_names)):
                    fig.add_trace(
                        go.Scatter(x=df['Annee'], y=data, name=nom,
                                 line=dict(width=4)),
                        secondary_y=(i > 0)
                    )
                
                fig.update_layout(
                    title="🤝 COOPÉRATIONS STRATÉGIQUES - ÉVOLUTION COMPARÉE",
                    height=500,
                    template="plotly_white"
                )
                st.plotly_chart(fig, use_container_width=True)
    
    def create_geopolitical_analysis(self, df, config):
        """Analyse géopolitique avancée"""
        st.markdown('<h3 class="section-header">🌍 CONTEXTE GÉOPOLITIQUE BRICS</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Architecture géopolitique
            st.markdown("""
            <div class="china-card">
                <h4>🏛️ ARCHITECTURE GÉOPOLITIQUE BRICS</h4>
                <p><strong>Chine:</strong> Puissance économique et militaire mondiale émergente</p>
                <p><strong>Russie:</strong> Puissance nucléaire et énergétique historique</p>
                <p><strong>Inde:</strong> Démocratie émergente et puissance régionale</p>
                <p><strong>Brésil:</strong> Leader latino-américain et puissance verte</p>
                <p><strong>Afrique du Sud:</strong> Porte d'entrée africaine et leader régional</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Analyse des relations internationales
            st.markdown("""
            <div class="cooperation-card">
                <h4>🌐 RELATIONS INTERNATIONALES</h4>
                <p><strong>Occident:</strong> Relations complexes - coopération et compétition</p>
                <p><strong>Global Sud:</strong> Leadership et partenariats renforcés</p>
                <p><strong>Organisations:</strong> ONU, OCS, G20 - recherche de réforme</p>
                <p><strong>Économie:</strong> NDB - Alternative aux institutions de Bretton Woods</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Expansion BRICS+
            expansion_data = {
                'Année': [2009, 2011, 2015, 2017, 2021, 2023, 2024],
                'Membres': [5, 5, 5, 5, 5, 5, 11],
                'PIB_Mondial': [18, 19, 23, 24, 26, 27, 32]  # %
            }
            expansion_df = pd.DataFrame(expansion_data)
            
            fig = px.line(expansion_df, x='Année', y='Membres', 
                         title="📈 EXPANSION DES BRICS - MEMBRES ET INFLUENCE",
                         labels={'Membres': 'Nombre de Membres'},
                         markers=True)
            fig.add_trace(go.Scatter(x=expansion_df['Année'], y=expansion_df['PIB_Mondial'], 
                                   mode='lines+markers', name='Part du PIB Mondial (%)',
                                   yaxis='y2'))
            fig.update_layout(yaxis2=dict(title='Part du PIB Mondial (%)', overlaying='y', side='right'))
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
            
            # Indice de coopération stratégique
            cooperation = [min(20 + 4 * (annee - 2009), 75) for annee in df['Annee'] if annee >= 2009] + [0] * (2009 - min(df['Annee']))
            annees_coop = [annee for annee in df['Annee'] if annee >= 2009] + [2009] * (2009 - min(df['Annee']))
            
            fig = px.area(x=annees_coop, y=cooperation,
                         title="🕊️ COOPÉRATION STRATÉGIQUE BRICS",
                         labels={'x': 'Année', 'y': 'Niveau de Coopération (%)'})
            fig.update_traces(fillcolor='rgba(255, 153, 51, 0.3)', line_color='#FF9933')
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
    
    def create_member_analysis(self, df, config):
        """Analyse des capacités des membres"""
        st.markdown('<h3 class="section-header">🇧🇷🇷🇺🇮🇳🇨🇳🇿🇦 CAPACITÉS DES MEMBRES BRICS</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Contributions des membres
            contributions_data = []
            for pays, data in self.member_capabilities.items():
                contributions_data.append({
                    'Pays': pays,
                    'Budget (Md$)': data['budget'],
                    'Personnel (K)': data['personnel'],
                    'Nucléaire': data['nucleaire'],
                    'Technologies': data['technologies']
                })
            
            contributions_df = pd.DataFrame(contributions_data)
            
            fig = px.bar(contributions_df, x='Pays', y='Budget (Md$)',
                        title="💰 CONTRIBUTIONS BUDGÉTAIRES DES MEMBRES",
                        color='Budget (Md$)',
                        color_continuous_scale='viridis')
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Cartographie des capacités spécialisées
            st.markdown("""
            <div class="russia-card">
                <h4>🎯 SPÉCIALISATIONS STRATÉGIQUES</h4>
                <p><strong>Chine:</strong> Production massive, cyber, espace, marine</p>
                <p><strong>Russie:</strong> Armes nucléaires, hypersoniques, énergie</p>
                <p><strong>Inde:</strong> Missiles, spatial, puissance régionale</p>
                <p><strong>Brésil:</strong> Amazonie, surveillance, sous-marins</p>
                <p><strong>Afrique du Sud:</strong> Renseignement, paix, ressources</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Avantages comparatifs
            advantages_data = {
                'Domaine': ['Production Industrielle', 'Technologie Nucléaire', 'Missiles', 
                           'Marine', 'Cybersécurité', 'Renseignement'],
                'Chine': [9, 8, 9, 8, 9, 7],
                'Russie': [6, 9, 9, 7, 8, 8],
                'Inde': [7, 7, 8, 6, 7, 6],
                'Brésil': [5, 0, 4, 5, 5, 5],
                'Afrique du Sud': [3, 0, 3, 3, 6, 7]
            }
            advantages_df = pd.DataFrame(advantages_data)
            
            fig = go.Figure(data=[
                go.Bar(name='Chine', x=advantages_df['Domaine'], y=advantages_df['Chine']),
                go.Bar(name='Russie', x=advantages_df['Domaine'], y=advantages_df['Russie']),
                go.Bar(name='Inde', x=advantages_df['Domaine'], y=advantages_df['Inde']),
                go.Bar(name='Brésil', x=advantages_df['Domaine'], y=advantages_df['Brésil']),
                go.Bar(name='Afrique du Sud', x=advantages_df['Domaine'], y=advantages_df['Afrique du Sud'])
            ])
            fig.update_layout(title="📊 AVANTAGES COMPARATIFS STRATÉGIQUES (0-10)",
                             barmode='group', height=400)
            st.plotly_chart(fig, use_container_width=True)
    
    def create_technical_analysis(self, df, config):
        """Analyse technique détaillée"""
        st.markdown('<h3 class="section-header">🔬 ANALYSE TECHNIQUE AVANCÉE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Analyse des systèmes d'armes
            systems_data = {
                'Système': ['DF-41 (Chine)', 'RS-28 Sarmat (Russie)', 'Agni-V (Inde)', 
                           'J-20 (Chine)', 'Su-57 (Russie)', 'Sous-marin Type 094 (Chine)',
                           'Sous-marin Arihant (Inde)', 'Frégate Classe Kolkata (Inde)'],
                'Portée/Puissance': [15000, 18000, 5000, 5500, 3500, 12000, 3500, 7500],
                'Pays': ['Chine', 'Russie', 'Inde', 'Chine', 'Russie', 'Chine', 'Inde', 'Inde'],
                'Statut': ['Opérationnel', 'Opérationnel', 'Opérationnel', 'Opérationnel', 'Opérationnel', 'Opérationnel', 'Opérationnel', 'Opérationnel']
            }
            systems_df = pd.DataFrame(systems_data)
            
            fig = px.scatter(systems_df, x='Portée/Puissance', y='Pays', 
                           size='Portée/Puissance', color='Pays',
                           hover_name='Système', log_x=True,
                           title="🚀 SYSTÈMES D'ARMES DES BRICS",
                           size_max=30)
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Analyse de la modernisation
            modernization_data = {
                'Domaine': ['Forces Nucléaires', 'Forces Conventionnelles', 
                          'Marine', 'Défense Aérienne', 'Cybersécurité'],
                'Niveau 2000': [60, 45, 40, 35, 30],
                'Niveau 2027': [85, 75, 78, 72, 80]
            }
            modern_df = pd.DataFrame(modernization_data)
            
            fig = go.Figure()
            fig.add_trace(go.Bar(name='2000', x=modern_df['Domaine'], y=modern_df['Niveau 2000'],
                                marker_color='#FF9933'))
            fig.add_trace(go.Bar(name='2027', x=modern_df['Domaine'], y=modern_df['Niveau 2027'],
                                marker_color='#0055A4'))
            
            fig.update_layout(title="📈 MODERNISATION DES CAPACITÉS MILITAIRES BRICS",
                             barmode='group', height=500)
            st.plotly_chart(fig, use_container_width=True)
            
            # Innovations technologiques
            st.markdown("""
            <div class="cooperation-card">
                <h4>🚀 INNOVATIONS TECHNOLOGIQUES BRICS</h4>
                <p><strong>Chine:</strong> DF-ZF hypersonique, J-20 furtif, drones de combat</p>
                <p><strong>Russie:</strong> Avangard hypersonique, S-500, guerre électronique</p>
                <p><strong>Inde:</strong> Missiles BrahMos, programme spatial, cyber défense</p>
                <p><strong>Brésil:</strong> Systèmes de surveillance, sous-marins conventionnels</p>
                <p><strong>Afrique du Sud:</strong> Renseignement électronique, maintien de la paix</p>
            </div>
            """, unsafe_allow_html=True)
    
    def create_cooperation_analysis(self, config):
        """Analyse des coopérations BRICS"""
        st.markdown('<h3 class="section-header">🤝 ANALYSE DES COOPÉRATIONS BRICS</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Projets de coopération
            cooperation_data = []
            for projet, details in self.cooperation_projects.items():
                cooperation_data.append({
                    'Projet': projet,
                    'Pays': details['pays'],
                    'Type': details['type'],
                    'Statut': details['statut']
                })
            
            cooperation_df = pd.DataFrame(cooperation_data)
            
            fig = px.treemap(cooperation_df, path=['Type', 'Projet'],
                            title="🌳 CARTE DES PROJETS DE COOPÉRATION BRICS",
                            color='Type')
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Avantages de la coopération
            st.markdown("""
            <div class="china-card">
                <h4>🏆 AVANTAGES DE LA COOPÉRATION BRICS</h4>
                <p><strong>Économies d'échelle:</strong> Marché combiné de 3.2 milliards de personnes</p>
                <p><strong>Complémentarité:</strong> Technologies russes + production chinoise</p>
                <p><strong>Réduction des coûts:</strong> R&D partagée et production collaborative</p>
                <p><strong>Autonomie stratégique:</strong> Réduction de la dépendance occidentale</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Domaines de coopération future
            future_coop_data = {
                'Domaine': ['Défense Anti-Missile', 'Guerre Cyber', 'Espace Militaire', 
                           'Renseignement', 'Recherche Technologique', 'Exercices Conjoints'],
                'Potentiel': [8, 9, 7, 8, 9, 8]  # sur 10
            }
            future_coop_df = pd.DataFrame(future_coop_data)
            
            fig = px.bar(future_coop_df, x='Domaine', y='Potentiel',
                        title="🔮 POTENTIEL DE COOPÉRATION FUTURE",
                        color='Potentiel',
                        color_continuous_scale='reds')
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
    
    def create_threat_assessment(self, df, config):
        """Évaluation avancée des menaces"""
        st.markdown('<h3 class="section-header">⚠️ ÉVALUATION STRATÉGIQUE DES MENACES</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Matrice des menaces
            threats_data = {
                'Type de Menace': ['Pression Occidentale', 'Sanctions Économiques', 
                                 'Guerre Cyber', 'Instabilité Régionale', 
                                 'Conflits Frontaliers', 'Crise Énergétique'],
                'Probabilité': [0.8, 0.7, 0.9, 0.6, 0.5, 0.4],
                'Impact': [0.7, 0.8, 0.6, 0.5, 0.7, 0.8],
                'Niveau Préparation': [0.7, 0.6, 0.8, 0.5, 0.6, 0.5]
            }
            threats_df = pd.DataFrame(threats_data)
            
            fig = px.scatter(threats_df, x='Probabilité', y='Impact', 
                           size='Niveau Préparation', color='Type de Menace',
                           title="🎯 MATRICE RISQUES - PROBABILITÉ VS IMPACT",
                           size_max=30)
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Capacités de réponse
            response_data = {
                'Scénario': ['Sanctions Économiques', 'Pression Militaire', 
                           'Guerre Cyber', 'Crise Énergétique', 'Instabilité Politique'],
                'Chine': [0.8, 0.7, 0.9, 0.6, 0.5],
                'Russie': [0.6, 0.9, 0.8, 0.7, 0.4],
                'Inde': [0.7, 0.6, 0.7, 0.5, 0.6],
                'Coopération': [0.9, 0.8, 0.8, 0.7, 0.7]
            }
            response_df = pd.DataFrame(response_data)
            
            fig = go.Figure(data=[
                go.Bar(name='Chine', x=response_df['Scénario'], y=response_df['Chine']),
                go.Bar(name='Russie', x=response_df['Scénario'], y=response_df['Russie']),
                go.Bar(name='Inde', x=response_df['Scénario'], y=response_df['Inde']),
                go.Bar(name='Coopération', x=response_df['Scénario'], y=response_df['Coopération'])
            ])
            fig.update_layout(title="🛡️ CAPACITÉS DE RÉPONSE PAR ACTEUR",
                             barmode='group', height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        # Recommandations stratégiques
        st.markdown("""
        <div class="cooperation-card">
            <h4>🎯 RECOMMANDATIONS STRATÉGIQUES BRICS</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div><strong>• Renforcement coopération:</strong> Commandement militaire commun</div>
                <div><strong>• Autonomie technologique:</strong> Chaînes d'approvisionnement alternatives</div>
                <div><strong>• Dissuasion intégrée:</strong> Coordination des capacités nucléaires</div>
                <div><strong>• Cybersécurité collective:</strong> Centre de cyber défense BRICS</div>
                <div><strong>• Industrie de défense:</strong> Production collaborative d'armements</div>
                <div><strong>• Expansion BRICS+:</strong> Intégration de nouveaux membres</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def create_cooperation_database(self):
        """Base de données des coopérations BRICS"""
        st.markdown('<h3 class="section-header">🤝 BASE DE DONNÉES DES COOPÉRATIONS BRICS</h3>', 
                   unsafe_allow_html=True)
        
        cooperation_data = []
        for nom, specs in self.cooperation_projects.items():
            cooperation_data.append({
                'Projet': nom,
                'Pays Participants': specs['pays'],
                'Type': specs['type'],
                'Statut': specs['statut'],
                'Détails': specs.get('objectif', specs.get('localisation', specs.get('domaines', 'N/A')))
            })
        
        cooperation_df = pd.DataFrame(cooperation_data)
        
        # Affichage interactif
        col1, col2 = st.columns([2, 1])
        
        with col1:
            fig = px.treemap(cooperation_df, path=['Type', 'Projet'],
                            title="🤝 CARTE DES COOPÉRATIONS BRICS",
                            color='Type')
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("""
            <div class="china-card">
                <h4>📋 PROJETS DE COOPÉRATION</h4>
            """, unsafe_allow_html=True)
            
            for projet in cooperation_data:
                st.markdown(f"""
                <div style="background: rgba(255,255,255,0.1); padding: 0.5rem; margin: 0.2rem 0; border-radius: 5px;">
                    <strong>{projet['Projet']}</strong><br>
                    🌍 {projet['Pays Participants']} • 🎯 {projet['Type']}<br>
                    📊 {projet['Statut']} • 📝 {projet['Détails']}
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    def run_advanced_dashboard(self):
        """Exécute le dashboard avancé complet"""
        # Sidebar avancé
        controls = self.create_advanced_sidebar()
        
        # Header avancé
        self.display_advanced_header()
        
        # Génération des données avancées
        df, config = self.generate_advanced_data(controls['selection'])
        
        # Navigation par onglets avancés
        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
            "📊 Tableau de Bord", 
            "🔬 Analyse Technique", 
            "🌍 Contexte Géopolitique", 
            "🇧🇷🇷🇺🇮🇳🇨🇳🇿🇦 Membres BRICS",
            "⚠️ Évaluation Menaces",
            "🤝 Coopérations BRICS",
            "💎 Synthèse Stratégique"
        ])
        
        with tab1:
            self.display_strategic_metrics(df, config)
            self.create_comprehensive_analysis(df, config)
        
        with tab2:
            self.create_technical_analysis(df, config)
        
        with tab3:
            if controls['show_geopolitical']:
                self.create_geopolitical_analysis(df, config)
        
        with tab4:
            self.create_member_analysis(df, config)
        
        with tab5:
            if controls['threat_assessment']:
                self.create_threat_assessment(df, config)
        
        with tab6:
            if controls['show_cooperation']:
                self.create_cooperation_database()
        
        with tab7:
            self.create_strategic_synthesis(df, config, controls)
    
    def create_strategic_synthesis(self, df, config, controls):
        """Synthèse stratégique finale"""
        st.markdown('<h3 class="section-header">💎 SYNTHÈSE STRATÉGIQUE - BRICS</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="china-card">
                <h4>🏆 POINTS FORTS STRATÉGIQUES</h4>
                <div style="margin-top: 1rem;">
                    <div class="russia-card" style="margin: 0.5rem 0;">
                        <strong>🌍 Poids Démographique et Économique</strong>
                        <p>40% de la population mondiale et 30% du PIB mondial en parité de pouvoir d'achat</p>
                    </div>
                    <div class="india-card" style="margin: 0.5rem 0;">
                        <strong>☢️ Puissance Nucléaire Combinée</strong>
                        <p>Trois puissances nucléaires avec capacités de seconde frappe crédibles</p>
                    </div>
                    <div class="brazil-card" style="margin: 0.5rem 0;">
                        <strong>🚀 Diversité des Capacités</strong>
                        <p>Complémentarité des forces : technologie russe + production chinoise + puissance indienne</p>
                    </div>
                    <div class="safrica-card" style="margin: 0.5rem 0;">
                        <strong>🤝 Solidarité Sud-Sud</strong>
                        <p>Leadership dans le Global Sud avec légitimité politique étendue</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="cooperation-card">
                <h4>🎯 DÉFIS ET VULNÉRABILITÉS</h4>
                <div style="margin-top: 1rem;">
                    <div class="cooperation-card" style="margin: 0.5rem 0;">
                        <strong>💸 Divergences Économiques</strong>
                        <p>Écarts de développement importants entre les membres</p>
                    </div>
                    <div class="cooperation-card" style="margin: 0.5rem 0;">
                        <strong>🌐 Conflits d'Intérêts</strong>
                        <p>Tensions frontalières et rivalités historiques entre certains membres</p>
                    </div>
                    <div class="cooperation-card" style="margin: 0.5rem 0;">
                        <strong>🔧 Dépendance Technologique</strong>
                        <p>Dépendance persistante aux technologies occidentales dans certains domaines</p>
                    </div>
                    <div class="cooperation-card" style="margin: 0.5rem 0;">
                        <strong>⚡ Coordination Limitée</strong>
                        <p>Absence de structure militaire intégrée comparable à l'OTAN</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Perspectives futures
        st.markdown("""
        <div class="metric-card">
            <h4>🔮 PERSPECTIVES STRATÉGIQUES 2027-2035</h4>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 1rem;">
                <div>
                    <h5>🌍 EXPANSION GÉOPOLITIQUE</h5>
                    <p>• BRICS+ avec 15+ membres<br>• Institutions financières alternatives<br>• Système de paiement commun<br>• Alliances stratégiques élargies</p>
                </div>
                <div>
                    <h5>🛡️ COOPÉRATION MILITAIRE</h5>
                    <p>• Commandement militaire commun<br>• Exercices navals réguliers<br>• Système de défense anti-missile<br>• Centre cyber BRICS</p>
                </div>
                <div>
                    <h5>🚀 INNOVATION TECHNOLOGIQUE</h5>
                    <p>• Chaînes d'approvisionnement autonomes<br>• Recherche-développement collaborative<br>• Standards technologiques BRICS<br>• Supériorité dans domaines clés</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Recommandations finales
        st.markdown("""
        <div class="china-card">
            <h4>🎖️ RECOMMANDATIONS STRATÉGIQUES FINALES</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div>
                    <h5>🛡️ RENFORCEMENT INTERNE</h5>
                    <p>• Institutionnalisation de la coopération militaire<br>
                    • Harmonisation des doctrines et équipements<br>
                    • Développement de l'industrie de défense intégrée<br>
                    • Renforcement des capacités cyber collectives</p>
                </div>
                <div>
                    <h5>🌍 LEADERSHIP GLOBAL</h5>
                    <p>• Expansion stratégique du BRICS+<br>
                    • Développement d'institutions alternatives<br>
                    • Promotion du multilatéralisme réformé<br>
                    • Construction d'un ordre mondial multipolaire</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Lancement du dashboard avancé
if __name__ == "__main__":
    dashboard = DefenseBricsDashboardAvance()
    dashboard.run_advanced_dashboard()