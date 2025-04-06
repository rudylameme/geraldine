import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Titres Restaurant", layout="centered")
st.title("🍽️ Application de calcul des titres restaurant")

st.markdown("""
Cette application permet de :
- Charger 3 fichiers : Absences, Déplacements, Bénéficiaires (.xlsx ou .ods)
- Identifier automatiquement la ligne début de tableau
- Préparer le calcul des titres restaurant
""")

# Fonction de lecture dynamique (auto .xlsx / .ods)
def load_excel(file):
    if file.name.endswith(".ods"):
        return pd.read_excel(file, engine="odf")
    else:
        return pd.read_excel(file, engine="openpyxl")

# Auto-détection de la ligne d'en-tête
def detect_table(file):
    for header_row in range(10):
        try:
            df = pd.read_excel(file, engine="odf" if file.name.endswith(".ods") else "openpyxl", header=header_row)
            if any(col.lower() in ["nom", "agent", "date", "motif"] for col in df.columns.str.lower()):
                return df
        except:
            continue
    st.error("❌ Impossible d'identifier le début du tableau. Merci de vérifier le format du fichier.")
    return None

# Upload des fichiers
uploaded_absences = st.file_uploader("Fichier 1 : Absences", type=["xlsx", "ods"])
uploaded_deplacements = st.file_uploader("Fichier 2 : Déplacements", type=["xlsx", "ods"])
uploaded_beneficiaires = st.file_uploader("Fichier 3 : Bénéficiaires", type=["xlsx", "ods"])

if st.button("📊 Calculer les titres restaurant"):
    if not uploaded_absences or not uploaded_deplacements or not uploaded_beneficiaires:
        st.warning("⚠️ Merci de charger les 3 fichiers.")
    else:
        df_abs = detect_table(uploaded_absences)
        df_dep = detect_table(uploaded_deplacements)
        df_ben = detect_table(uploaded_beneficiaires)

        if df_abs is not None and df_dep is not None and df_ben is not None:
            st.success("🚀 Fichiers chargés avec succès")

            with st.expander("🔍 Aperçu des absences"):
                st.dataframe(df_abs.head(15))
            with st.expander("🔍 Aperçu des déplacements"):
                st.dataframe(df_dep.head(15))
            with st.expander("🔍 Aperçu des bénéficiaires"):
                st.dataframe(df_ben.head(15))

            st.info("✅ Prêt à ajouter la logique métier (filtres, arrondis, calculs...)")

            # Ici tu pourras ajouter la logique :
            # - filtrer df_abs selon motifs et jours
            # - arrondir les 0.5 à 1
            # - croiser avec df_dep pour soustraire les jours
            # - produire une synthèse par agent

            # Exemple : st.dataframe(resultat_final)

        else:
            st.error("❌ Erreur de chargement de l'un des fichiers.")
