

# Configure o Streamlit e o Ngrok
from pyngrok import conf, ngrok
import subprocess

# Substitua 'SEU_AUTHTOKEN' pelo token copiado do painel do Ngrok
conf.get_default().auth_token = '2piU8aYaI7Zme8uMNVmdaOk9rOH_6whRM18khwa9SzpjPn9AT'

# Crie o código do aplicativo Streamlit em um arquivo
app_code = """
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

"""

# Salve o código em um arquivo chamado app.py
with open("app.py", "w") as f:
    f.write(app_code)

# Execute o aplicativo Streamlit
process = subprocess.Popen(['streamlit', 'run', 'app.py', '--server.port', '8501'])

# Exponha o aplicativo publicamente usando o ngrok
# Especificamos o tipo de túnel como HTTP e configuramos explicitamente a porta
public_url = ngrok.connect(8501, "http")
print(f"App Streamlit está disponível publicamente em: {public_url}")
