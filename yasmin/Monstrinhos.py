# Importando a biblioteca Streamlit
import streamlit as st

# Título da aplicação
st.title("Crie Seu Próprio Monstro")

# Sidebar para opções de personalização
st.sidebar.header("Opções de Personalização")

# Caixas de seleção para características do monstro
cor = st.sidebar.selectbox("Escolha a Cor do Monstro", ["Verde", "Azul", "Vermelho","Roxo"])
pele = st.sidebar.selectbox("Escolha a Pele do Monstro", ["Escamas", "Pelos","Gosma"])
hability = st.sidebar.selectbox("Escolha as Habilidades do Monstro", ["Voar", "Respirar Fogo","Congelar"])

# Exibindo o monstro personalizado
st.subheader("Seu Monstro Personalizado:")
st.write(f"Cor: {cor}")
st.write(f"Pele: {pele}")
st.write(f"Habilidades: {', '.join(hability)}")
if cor == "Roxo" and pele == "Escamas" and hability == "Respirar Fogo":
  st.image
