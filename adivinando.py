import streamlit as st
import random
st.title("🕹️Adivina el numero 🎲")

numero_secreto = random.randint(1,5)
mi_numero = st.number_input("Digite un numero: ")

if st.button("Jugar 💰"):
    if numero_secreto == mi_numero:

        st.success("Felicitaciones 🥳")

    else:
        st.warning("No acertaste😞😞")