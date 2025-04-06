import streamlit as st
import pandas as pd

st.set_page_config(page_title="Titres Restaurant", layout="centered")

st.title("🍽️ Application de calcul des titres restaurant")

uploaded_absences = st.file_uploader("Fichier 1 : Absences", type=["xlsx", "ods"])
uploaded_deplacements = st.file_uploader("Fichier 2 : Déplacements", type=["xlsx", "ods"])
uploaded_beneficiaires = st.file_uploader("Fichier 3 : Bénéficiaires", type=["xlsx", "ods"])

if st.button("🧮 Calculer les titres restaurant"):
    if not (uploaded_absences and uploaded_deplacements and uploaded_beneficiaires):
        st.warning("Merci d'importer les 3 fichiers.")
    else:
        df_abs = pd.read_excel(uploaded_absences, engine="openpyxl")
        df_dep = pd.read_excel(uploaded_deplacements, engine="openpyxl")
        df_ben = pd.read_excel(uploaded_beneficiaires, engine="openpyxl")

        st.success("Fichiers chargés avec succès !")

        st.subheader("✅ Exemple de prétraitement des absences")
        st.write(df_abs.head(10))

        st.subheader("✅ Exemple de prétraitement des déplacements")
        st.write(df_dep.head(10))

        st.subheader("✅ Liste des bénéficiaires")
        st.write(df_ben.head(10))
