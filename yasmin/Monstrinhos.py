# Importando a biblioteca Streamlit
import streamlit as st

# Título da aplicação
st.title("Crie Seu Próprio Monstro")

# Sidebar para opções de personalização
st.sidebar.header("Opções de Personalização")

# Caixas de seleção para características do monstro
cor = st.sidebar.selectbox("Escolha a Cor do Monstro", ["Verde", "Azul", "Vermelho"])
forma = st.sidebar.selectbox("Escolha a Forma do Monstro", ["Círculo", "Quadrado", "Triângulo"])
habilidades = st.sidebar.multiselect("Escolha as Habilidades do Monstro", ["Voar", "Invisibilidade", "Respirar Fogo"])

# Exibindo o monstro personalizado
st.subheader("Seu Monstro Personalizado:")
st.write(f"Cor: {cor}")
st.write(f"Forma: {forma}")
st.write(f"Habilidades: {', '.join(habilidades)}")
