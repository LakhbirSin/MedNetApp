import streamlit as st
import pandas as pd
from PIL import Image
from Data import predict


# Ajoute un bouton pour charger une nouvelle image
uploaded_files = st.file_uploader("Choisissez une image au format PNG ou JPG", accept_multiple_files=True, type=["png", "jpg","jpeg"])
if st.button("Upload"):
    if uploaded_files is not None:
        # Crée les colonnes pour afficher les informations de l'image
        image_col, name_col, detect_col, id_col = st.columns(4)
        
        image_list = []
        image_names = []
        for uploaded_file in uploaded_files:
            # Charge chaque image sélectionnée
            image_list.append(uploaded_file)
            # Ajoute le nom de l'image à la liste
            image_names.append(uploaded_file.name)
            
        # Affiche les informations par défaut
        with image_col:
            st.markdown("<h3 style ='font-size:1rem; margin-bottom:50px'>Image</h3>", unsafe_allow_html=True)
            for image in image_list:
                image_col.image(image, use_column_width=True)
        
        with name_col:
            st.markdown("<h3 style ='font-size:1rem; margin-bottom:110px'>Description image</h3>", unsafe_allow_html=True)
            for name in image_names:
                    st.markdown(f"<h3 style ='font-size:1rem; margin-bottom:120px'>{name}</h3>", unsafe_allow_html=True)

        # Affiche les noms des images sélectionnées
        # name_col.write(", ".join(image_names))

        # Fait la prédiction sur chaque image et récupère les résultats
        id_cols = []
        for uploaded_file in uploaded_files:
            id_col = predict(uploaded_file)
            id_cols.append(id_col)
            
        with detect_col:
            st.markdown("<h3 style ='font-size:1rem; margin-bottom:100px'>Classe de rayons X détectée :</h3>", unsafe_allow_html=True)
            for id in id_cols:
                    st.markdown(f"<h3 style ='font-size:1rem; margin-bottom:120px'>{id}</h3>", unsafe_allow_html=True)
                    # Affiche les résultats de la prédiction
                    # detect_col.write(str(id_cols))