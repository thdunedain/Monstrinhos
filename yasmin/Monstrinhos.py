# Importando a biblioteca Streamlit
import streamlit as st

# Título para o Jogo
st.title("Crie Seu Próprio Monstro")

# Sidebar para opções de personalização
st.sidebar.header("Opções de Personalização")

# Opções para selecionar características do monstro
cor = st.sidebar.selectbox("Escolha a Cor do Monstro", ["Verde", "Azul", "Vermelho","Roxo"])
pele = st.sidebar.selectbox("Escolha a Pele do Monstro", ["Escamas", "Pelos","Penas"])
hability = st.sidebar.selectbox("Escolha as Habilidades do Monstro", ["Respirar Fogo","Congelar"])

# Biblioteca de imagens para serem mostradas quando o monstro estiver pronto

imagens = { 
  ('Roxo', 'Escamas', 'Respirar Fogo'): "https://i.pinimg.com/736x/f5/81/11/f58111479070fbd86720b8e5a502a914.jpg",
  ('Vermelho', 'Escamas', 'Respirar Fogo'): "https://i.pinimg.com/736x/15/a4/07/15a407a3c349f4293d4a7bdfacf0f012.jpg",
  ('Azul', 'Escamas', 'Respirar Fogo'): "https://i.pinimg.com/736x/12/9b/a3/129ba31ababa4ce0b75909757229cb0c.jpg",
  ('Verde', 'Escamas', 'Respirar Fogo'): "https://i.pinimg.com/736x/95/48/2c/95482c2ae33c4df9298b59d100b17b77.jpg",
  ('Roxo', 'Penas', 'Respirar Fogo'): "https://i.pinimg.com/736x/74/9b/9c/749b9cfaaf2f89388dc5894911ea7655.jpg",
  ('Vermelho', 'Penas', 'Respirar Fogo'): "https://i.pinimg.com/736x/8c/d7/b6/8cd7b60756ac42385648175a27edc44a.jpg",
  ('Azul', 'Penas', 'Respirar Fogo'): "https://i.pinimg.com/736x/a0/39/3c/a0393cfecdfb77bc591a3a389c2bd0c7.jpg",
  ('Verde', 'Penas', 'Respirar Fogo'): "https://i.pinimg.com/736x/8c/c0/f3/8cc0f38b4c799b8d6e355dd128d18537.jpg",
  ('Roxo', 'Pelos', 'Respirar Fogo'): "https://i.pinimg.com/736x/dc/ec/0a/dcec0a9df2d12ad5d5cfe17862ca3e62.jpg",
  ('Vermelho', 'Pelos', 'Respirar Fogo'): "https://i.pinimg.com/736x/bf/04/3d/bf043d1040e07ab91904c91c55f88f73.jpg",
  ('Azul', 'Pelos', 'Respirar Fogo'): "https://i.pinimg.com/736x/b4/ab/1a/b4ab1af3bdcb54cf3d6809fb178dac8e.jpg",
  ('Verde', 'Pelos', 'Respirar Fogo'): "https://i.pinimg.com/736x/3e/90/6f/3e906f74ded301223e6f208826bb2c26.jpg",
  ('Roxo', 'Escamas', 'Congelar'): "https://i.pinimg.com/736x/96/ba/a7/96baa7c8c4b272de8f3fb84dbfc757b4.jpg",
  ('Vermelho', 'Escamas', 'Congelar'): "https://i.pinimg.com/736x/9d/72/f2/9d72f24d8c168dd743a895f865725258.jpg",
  ('Azul', 'Escamas', 'Congelar'): "https://i.pinimg.com/736x/52/1e/40/521e404af12b51a9860c2fb958129777.jpg",
  ('Verde', 'Escamas', 'Congelar'): "https://i.pinimg.com/736x/fa/41/c4/fa41c4785ce50005849bc19d841f6cf5.jpg",
  ('Roxo', 'Penas', 'Congelar'): "https://i.pinimg.com/736x/db/f4/7e/dbf47e237e001291a308c4341b18b728.jpg",
  ('Vermelho', 'Penas', 'Congelar'): "https://i.pinimg.com/736x/68/cc/b0/68ccb0fcf0890e21ca01ff54638cdf76.jpg",
  ('Azul', 'Penas', 'Congelar'): "https://i.pinimg.com/736x/3e/fa/e0/3efae0112b128d2513bfcc703c54ee02.jpg",
  ('Verde', 'Penas', 'Congelar'): "https://i.pinimg.com/736x/7e/fe/49/7efe492473155dfe9f275cc99a5608ce.jpg",
  ('Roxo', 'Pelos', 'Congelar'): "https://i.pinimg.com/736x/52/ad/24/52ad242259f601731470e440cc733b20.jpg",
  ('Vermelho', 'Pelos', 'Congelar'): "https://i.pinimg.com/736x/ac/0a/83/ac0a83c7872846ceee4014e37c6c4658.jpg",
  ('Azul', 'Pelos', 'Congelar'): "https://i.pinimg.com/736x/3c/bc/b7/3cbcb7fcde5a0f4c3a2b57e13d6f1f8b.jpg",
  ('Verde', 'Pelos', 'Congelar'): "https://i.pinimg.com/736x/8b/83/2d/8b832da7017841363089ddf78b131da5.jpg",
 
 }

# Exibindo o monstro personalizado
st.subheader("Seu Monstro Personalizado:")
st.write(f"Cor: {cor}")
st.write(f"Pele: {pele}")
st.write(f"Habilidades: {hability}")
imagem_combinacao = imagens.get((cor, pele, hability), "url_padrao_da_imagem.png")
st.image(imagem_combinacao, caption='Monstro Personalizado', use_column_width=True)

João Hallysson Alves da Silva
Yasmin de Oliveira Martins 
S2 T-1


