import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt 

#Setar tamanho da tabela a ser apresentada
st.set_page_config(layout="wide")

#Ler arquivo .csv
df = pd.read_csv("https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv", decimal=",")

#Tratar coluna Data para usar nos filtros dos gráficos
#df["Date"] = pd.to_datetime(df["Date"])
#df = df.sort_values("Date")
#df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
#month = st.sidebar.selectbox("Mês", df["Month"].unique())
#df_filtered = df[df["Month"] == month]

#Seta as posições das colunas
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

#Gráfico 1 - Faturamento por dia.
df = df[df.Confirmed > 0].copy()
df[df.Country == 'Brazil']
fig = px.choropleth(
    df,
    locations = 'Country',
    locationmode='country names',
    color='Confirmed',
    animation_frame = 'Date',
    title='Dispersão do vírus da COVID-19',
    labels={
        "Date":"Data",
        "Confirmed":"Número de Casos"
        }
    )
col1.plotly_chart(fig, use_container_width=True)

#Gráfico 2 - Faturamento por tipo do produto.
fig = px.choropleth(
    df,
    locations = 'Country',
    locationmode='country names',
    color='Deaths',
    animation_frame = 'Date',
    title='Dispersão das mortes da COVID-19',
    labels={
        "Date":"Data",
        "Deaths":"Número de Mortes"
        }
    )
col2.plotly_chart(fig, use_container_width=True)

#Gráfico 3 - Faturamento de cada filial.
df_brasil = df[df.Country == 'Brazil'].copy()
df_brasil = df_brasil[['Date','Confirmed']]
df_brasil['Infection Rate'] = df_brasil['Confirmed'].diff()
df_brasil['Taxa de Infecção'] = (df_brasil['Infection Rate'] / df_brasil['Infection Rate'].max()) * 100
df_brasil['Casos Confirmados'] = (df_brasil['Confirmed'] / df_brasil['Confirmed'].max()) *100
fig = px.line(
    df_brasil,
    x= 'Date',
    y = ['Casos Confirmados','Taxa de Infecção'],
    title='Coeficiente de Infecção e Número de Casos no Brasil (Normalizado)',
    labels={'Confirmed Cases Normalized':'Casos Confirmados',
            'Infection Rate Normalized':'Taxa de Infecção',
            'Date':'Data',
            'variable':'Variavel:',
            'value':'Valor'})
col3.plotly_chart(fig, use_container_width=True)

#Gráfico 4 - Faturamento por tipo de pagamento.
countries = list(df['Country'].unique())
max_infection_rates = []
for c in countries:
    MIR = df[df.Country == c].Confirmed.diff().max()
    max_infection_rates.append(MIR)
df_MIR = pd.DataFrame()
df_MIR['Country'] = countries
df_MIR['MIR'] = max_infection_rates
df_MIR = df_MIR.sort_values(by=['MIR'])
df_MIR.head()
df_top10 = df_MIR.tail(20)
fig = px.bar(
    df_top10,
    x='Country',
    y='MIR',
#    log_y=True,
    title = '10 Maiores taxas de Infecção Global (Máxima de casos notificados em um dia)',
    labels={
        'Country':'País',
        'MIR':'Maior Taxa de Infecção'
    })
col4.plotly_chart(fig, use_container_width=True)
