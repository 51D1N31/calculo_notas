import streamlit as st
import pandas as pd
import numpy as np

st.title("App Streamlit Básico")
st.write("Exemplo simples para testar o Streamlit.")

# Entrada do usuário
name = st.text_input("Seu nome")
if st.button("Dizer Olá"):
    st.success(f"Olá, {name or 'usuário'}!")

# Controle para gerar dados e gráfico
n = st.slider("Número de pontos", 10, 100, 30)
data = pd.DataFrame({
    "x": np.arange(n),
    "y": np.random.randn(n).cumsum()
})
st.line_chart(data.set_index("x"))

# Mostrar tabela opcionalmente
if st.checkbox("Mostrar tabela de dados"):
    st.dataframe(data)

# Barra lateral com opção extra
st.sidebar.header("Configurações")
show_info = st.sidebar.radio("Mostrar info adicional?", ("Não", "Sim"))
if show_info == "Sim":
    st.sidebar.write("App de demonstração — Streamlit com pandas e numpy")