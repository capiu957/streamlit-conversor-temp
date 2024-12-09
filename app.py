

import streamlit as st

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

st.title("Conversor de Temperatura")
st.write("Este aplicativo converte temperaturas de Celsius para Fahrenheit.")

# Entrada do usuário
celsius = st.number_input("Insira a temperatura em Celsius:", value=0.0)

# Cálculo e exibição do resultado
fahrenheit = celsius_to_fahrenheit(celsius)
st.write(f"A temperatura em Fahrenheit é: {fahrenheit:.2f} °F")
