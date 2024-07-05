import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def main():
    st.title("Bienvenue dans mon application")

    name_user_input = st.text_input("Entrer votre nom ")
    age_user_input = st.number_input("Entrer votre âge ")

    if st.button("Valider"):  # Ajout d'un bouton "Valider"
        if name_user_input != "" and age_user_input != 0:  # Vérification que les champs ne sont pas vides
            st.write("Bonjour", name_user_input, "vous avez", int(age_user_input), "ans")

            if age_user_input >=18 :
                st.warning("Vous etes adultes")
            else :
                st.warning("Attendtion dous etes mineurs")

    data = np.random.randn(1000)

    # Créer un histogramme avec Matplotlib
    fig, ax = plt.subplots()
    ax.hist(data, bins=30)
    ax.set_xlabel('Valeurs')
    ax.set_ylabel('Fréquence')
    ax.set_title('Histogramme')

    # Afficher l'histogramme avec Streamlit
    st.pyplot(fig)

if __name__ == "__main__":
    main()
