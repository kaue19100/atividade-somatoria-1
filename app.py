import streamlit as st

# python -m streamlit run  app.py

#--------------------------------------------------- sidebar
st.sidebar.image('logo.png')
st.sidebar.title('IMC - indice de massa corporal')

#--------------------------------------------------- pricipal

st.title('IMC - indice de massa corporal')

st.markdown('### bem vindo ao monitoriamento de saúde com imc !')

peso = st.text_input('qual o seu peso ? (kg)')
altura = st.text_input("Digite sua altura (m):")

if st.button('calcular imc'):
    imc = float(peso) / (float(altura) * float(altura))
    if imc < 18.5: 
        st.markdown(f'# seu imc é {imc:.2f}, ou seja, abaixo do peso segundo a (OMS).')
        st.markdown('# O melhor a se fazer é ajustar a sua alimentação e praticar exercicios')
    elif imc <= 24.9:
     st.markdown(f'O seu imc é {imc:.2f}, ou seja, você pesa o tanto ideal pra sua altura segundo a (OMS)')
     st.markdown(' O risco de problemas relacionados ao peso (como desnutrição ou obesidade) é menor.')
    elif imc <= 29.9:
        st.markdown(f'seu imc é {imc:.2f} você tem sobrepeso segundo a (OMS).')
        st.markdown('O risco de desenvolver problemas de saúde começa a aumentar especialmente se houver outros fatores associados, como: ')
        st.markdown('pressão alta; colesterol alto; pré diabetes e etc... procure um nutricionista e Reduza o consumo de ultraprocessados')
    elif imc <= 34.9:
       st.markdown(f'seu imc é {imc:.2f}. segundo a (OMS) você considerado um obeso de grau 1 ')
       st.markdown('isso já almenta os seus riscos de pegar algumas doenças, como:')
       st.markdown('diabetes tipo 2; Hipertensão arterial; Dores nas articulações e etc...')
       st.markdown('procure ajuda de especialistas e mude o seu estilo de vida.  ')
    elif imc <= 39.9: 
       st.markdown(f'seu imc é {imc:.2f}, você é considerado um obeso de grau 2 (obesidade severa)')
       st.markdown('isso já almenta os seus riscos de pegar algumas doenças, como:')
       st.markdown('diabetes tipo 2; Hipertensão arterial; Dores nas articulações e etc...')
       st.markdown('procure ajuda de especialistas e mude o seu estilo de vida.  ')
    else:
       st.markdown(f'seu imc é {imc:.2f}, você é um obeso de grau 3 ! procure ajuda.   ')
       st.markdown('isso já almenta os seus riscos de pegar algumas doenças, como:')
       st.markdown('diabetes tipo 2; Hipertensão arterial; Dores nas articulações e etc...')
       st.markdown('procure ajuda de especialistas e mude o seu estilo de vida.  ')