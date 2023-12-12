# Importando a biblioteca Streamlit
import streamlit as st

# Título da aplicação
st.title("Crie Seu Próprio Monstro")

# Sidebar para opções de personalização
st.sidebar.header("Opções de Personalização")

# Caixas de seleção para características do monstro
cor = st.sidebar.selectbox("Escolha a Cor do Monstro", ["Verde", "Azul", "Vermelho","Roxo"])
pele = st.sidebar.selectbox("Escolha a Pele do Monstro", ["Escamas", "Pelos","Penas"])
hability = st.sidebar.selectbox("Escolha as Habilidades do Monstro", ["Respirar Fogo","Congelar"])

imagens = { 
  ('Roxo', 'Escamas', 'Respirar Fogo'): "https://i.pinimg.com/736x/f5/81/11/f58111479070fbd86720b8e5a502a914.jpg",
  ('Vermelho', 'Escamas', 'Respirar Fogo'): "blob:https://web.whatsapp.com/c8a5963e-bb0c-4da4-9153-107d7aceb6d8",
  ('Azul', 'Escamas', 'Respirar Fogo'): "blob:https://web.whatsapp.com/503010be-8a81-43c8-8361-d3b872b98048",
  ('Verde', 'Escamas', 'Respirar Fogo'): "blob:https://web.whatsapp.com/a52ef481-38b5-4513-b27c-1e2c7b683ea4",
  ('Roxo', 'Penas', 'Respirar Fogo'): "blob:https://web.whatsapp.com/f882caab-4596-4e6b-8e6f-54d4c67abf7a",
  ('Vermelho', 'Penas', 'Respirar Fogo'): "blob:https://web.whatsapp.com/21934ed6-b556-445d-8886-4894c3ef9790",
  ('Azul', 'Penas', 'Respirar Fogo'): "blob:https://web.whatsapp.com/f658faec-43e8-4cb6-b7d2-c49db518dfcd",
  ('Verde', 'Penas', 'Respirar Fogo'): "blob:https://web.whatsapp.com/6a8a44d2-eff5-46da-bebe-3d00a787dcc1",
  ('Roxo', 'Pelos', 'Respirar Fogo'): "blob:https://web.whatsapp.com/ddbb5f9d-10d0-4204-8a9c-821b0ef0f0eb",
  ('Vermelho', 'Pelos', 'Respirar Fogo'): "blob:https://web.whatsapp.com/10594871-1899-4c29-8108-8618c19722e5",
  ('Azul', 'Pelos', 'Respirar Fogo'): "blob:https://web.whatsapp.com/82260ba3-3224-421e-8f1b-2e22b4429a60",
  ('Verde', 'Pelos', 'Respirar Fogo'): "OnlineImageTools",
  ('Roxo', 'Escamas', 'Congelar'): "blob:https://web.whatsapp.com/9a85c5b2-90b4-477e-a28d-4e1dfb85e1be",
  ('Vermelho', 'Escamas', 'Congelar'): "blob:https://web.whatsapp.com/db07affb-627a-4d40-9299-d05f5ddaff38",
  ('Azul', 'Escamas', 'Congelar'): "blob:https://web.whatsapp.com/35bcff70-bf0b-4224-b6b0-613f8fe0750e",
  ('Verde', 'Escamas', 'Congelar'): "blob:https://web.whatsapp.com/459dbecc-f018-4897-8392-3bed7f93d320",
  ('Roxo', 'Penas', 'Congelar'): "blob:https://web.whatsapp.com/d9474d65-a380-46fd-9370-68b4fb6a4ed6",
  ('Vermelho', 'Penas', 'Congelar'): "blob:https://web.whatsapp.com/5dc82388-564a-4470-9798-28a00e55fe42",
  ('Azul', 'Penas', 'Congelar'): "blob:https://web.whatsapp.com/0c33b4e5-b2bd-4c61-8e48-81b5b403afdf",
  ('Verde', 'Penas', 'Congelar'): "blob:https://web.whatsapp.com/2891e6c8-8474-49b8-bc35-7015b820d0a3",
  ('Roxo', 'Pelos', 'Congelar'): "blob:https://web.whatsapp.com/e253cbb3-5b16-4903-bb03-67612e7897b4",
  ('Vermelho', 'Pelos', 'Congelar'): "blob:https://web.whatsapp.com/272d7fc6-2570-4076-a994-5d9fc5fe0fd7",
  ('Azul', 'Pelos', 'Congelar'): "blob:https://web.whatsapp.com/d189011a-88c4-45f4-8b1c-03f9ac77f4ab",
  ('Verde', 'Pelos', 'Congelar'): "blob:https://web.whatsapp.com/7629e0ed-fd65-47f0-8c64-9e5920420077",
 
 }

# Exibindo o monstro personalizado
st.subheader("Seu Monstro Personalizado:")
st.write(f"Cor: {cor}")
st.write(f"Pele: {pele}")
st.write(f"Habilidades: {hability}")
imagem_combinacao = imagens.get((cor, pele, hability), "url_padrao_da_imagem.png")
st.image(imagem_combinacao, caption='Monstro Personalizado', use_column_width=True)
