
#Bibliotecas
import pandas as pd
import streamlit as st
import plotly.express as px

#lendo o .CSV
df = pd.read_csv('covidVariants.csv')

#Transformando os dados de países e variantes em uma lista
paises = list(df['location'].unique())
variantes = list(df['variant'].unique())

#Formatando data e hora para padrão 'AAAA-MM-DD'
df['date'] = pd.to_datetime(df['date'], format= '%Y-%m-%d')

#Utilizando o stremlit para criar select box na barra lateral
pais = st.sidebar.selectbox('Escolha o país', ['Todos'] + paises)
variante = st.sidebar.selectbox('Escolha a variante', ['Todos'] + variantes)

if(pais != 'Todos'):
    st.header("Mostrando o resultado de: " + pais)
    df = df[df["location"] == pais]
else:
    st.subheader("Mostrando resultado para todos os países!")

if(variante != 'Todos'):
    st.header("Mostrando o resultado de: " + variante)
    df = df[df["variant"] == variante]
else:
    st.subheader("Mostrando resultado para todas as variantes!")    

dfShow = df.groupby (by = ["date"]).sum()


fig = px.line(dfShow, x = dfShow.index, y = 'num_sequences')
fig.update_layout(title = "Casos Diários COVID-19")
st.plotly_chart(fig, use_container_width= True)
    
