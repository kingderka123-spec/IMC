import streamlit as st

st.title("IMC")

poids=st.number_input("veuillez donner votre poids")

taille =st.number_input("veuillez donner votre taille")
if st.button("calcul"):
    IMC=poids/(taille**2)

    st.write(IMC)

    if IMC<18.5:
        st.warning("maigre")
    
    elif 18.5<IMC > 25:  
        st.success("poids normal")
        
    elif 25<IMC>30:
        st.warning("surpoids")
        
    elif IMC>=30 :
        st.warning("obése")
        
    else:
        st.info("La taille doit etre superieure à 0")
    