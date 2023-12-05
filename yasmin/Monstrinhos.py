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
  st.image(https://cdn.gencraft.com/prod/user/7ce7e7e6-3fef-495f-abf0-dc1cea44387d/8c6fc0b2-b4c2-46cb-8dc6-de04a293fe11/image/image0_0.jpg?Expires=1701885309&Signature=GLrywWbnl-RwpKWHuaOeqaQLyZeY-bsMO-f9GhneiC2FhK9NBKxKiVSd8YM~QJp4wJmhYXZ3CwWBI~v5suY3SH8gOv4UALRS7DVyz2WakYhAGHF0eo2rh6aPx1RL29s5eiZKhhbvr-pbcAGtM~9ciLmWrUnNWcBvuHkdkBSNV7cHFyKNyJbLk5gEnlJuYOij2QrB0sBFuGbLlnG52GM~2qhf~oWacvxVNprsRR25ASlAUexJvmS7uWixmuC-avU9lSBbhIuWokxRC4TnyR-Zw8-fFEoTkLuD7AevenLNjgl9CHmhL8gm7ek-CUPROh8YQEpfpxAj2in29YetV0peBQ__&Key-Pair-Id=K3RDDB1TZ8BHT8
