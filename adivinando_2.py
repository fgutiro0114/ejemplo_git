import streamlit as st
import tkinter as tk
nombre = st.text_input("Digite su nombre")
edad = st.number_input("Digite su nombre", min_value = 1, max_value= 20, step=1)
                       

if edad >= 18:
    st.write(f"{nombre} es mayor de edad")
else:
    st.write(f"{nombre} es menor de edad")