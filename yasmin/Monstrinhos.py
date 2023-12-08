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

imagens = { 
  ('Roxo', 'Escamas', 'Respirar Fogo'): " imagem"
  ('Vermelho', 'Escamas', 'Respirar Fogo'): " imagem"
  ('Azul', 'Escamas', 'Respirar Fogo'): " imagem"
  ('Verde', 'Escamas', 'Respirar Fogo'): " imagem"
  ('Roxo', 'Gosma', 'Respirar Fogo'): " imagem"
  (Vermelho', 'Gosma', 'Respirar Fogo'): " imagem"
  ('Azul', 'Gosma', 'Respirar Fogo'): " imagem"
  ('Verde', 'Gosma', 'Respirar Fogo'): " imagem"
  ('Roxo', 'Pelos', 'Respirar Fogo'): " imagem"
  ('Vermelho', 'Pelos', 'Respirar Fogo'): " imagem"
  ('Azul', 'Pelos', 'Respirar Fogo'): " imagem"
  ('Verde', 'Pelos', 'Respirar Fogo'): " imagem"
  ('Roxo', 'Escamas', 'Congelar'): " imagem"
  ('Vermelho', 'Escamas', 'Congelar'): " imagem"
  ('Azul', 'Escamas', 'Congelar'): " imagem"
  ('Verde', 'Escamas', 'Congelar'): " imagem"
  ('Roxo', 'Gosma', 'Congelar'): " imagem"
  ('Vermelho', 'Gosma', 'Congelar'): " imagem"
  ('Azul', 'Gosma', 'Congelar'): " imagem"
  ('Verde', 'Gosma', 'Congelar'): " imagem"
  ('Roxo', 'Pelos', 'Congelar'): " imagem"
  ('Vermelho', 'Pelos', 'Congelar'): " imagem"
  ('Azul', 'Pelos', 'Congelar'): " imagem"
  ('Verde', 'pelos', 'Congelar'): " imagem"
  ('Roxo', 'Escamas', 'Voar'): " imagem"
  ('Vermelho', 'Escamas', 'Voar'): " imagem"
  ('Azul', 'Escamas', 'Voar'): " imagem"
  ('Verde', 'Escamas', 'Voar'): " imagem"
  ('Roxo', 'Gosma', 'Voar'): " imagem"
  ('Vermelho', 'Gosma', 'Voar'): " imagem"
  ('Azul', 'Gosma', 'Voar'): " imagem"
  ('Verde', 'Gosma', 'Voar'): " imagem"
  ('Roxo', 'Pelos', 'Voar'): " imagem"
  ('Vermelho', 'Pelos', 'Voar'): " imagem"
  ('Azul', 'Pelos', 'Voar'): " imagem"
  ('Verde', 'Pelos', 'Voar'): " imagem"
 }

# Exibindo o monstro personalizado
st.subheader("Seu Monstro Personalizado:")
st.write(f"Cor: {cor}")
st.write(f"Pele: {pele}")
st.write(f"Habilidades: {', '.join(hability)}")
