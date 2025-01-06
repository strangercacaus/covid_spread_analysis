import ssl
import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt

# Setar tamanho da tabela a ser apresentada

st.set_page_config(layout="wide", page_title="Propagação da Covid 19")

# Baixar fonte de dados atualizada

ssl._create_default_https_context = ssl._create_unverified_context
dataset_url = "https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv"
df = pd.read_csv(dataset_url)
df.to_csv("../data/covid_dataset.csv")

# Ler fonte de dados atualizada

df = pd.read_csv("../data/covid_dataset.csv", decimal=",")
df = df[df.Confirmed > 0]

# Definir tema do painel:
theme = None
cc_scale = "Plotly3"
cd_scale = px.colors.qualitative.Alphabet

# Tratar coluna Data para usar nos filtros dos gráficos

df["filter_date"] = pd.to_datetime(df["Date"])
min_date = df["filter_date"].min().date()
max_date = df["filter_date"].max().date()
df["filter_date"] = df["filter_date"].dt.date

# Tratar coluna de países para usar nos filtros dos gráficos

countries_list = df["Country"].unique().tolist()

# Criação dos filtros na sidebar

st.sidebar.header("Filtros")
start_date = st.sidebar.date_input(
    "Data inicial", min_date, min_value=min_date, max_value=max_date
)
end_date = st.sidebar.date_input(
    "Data final", max_date, min_value=min_date, max_value=max_date
)
selected_country = st.sidebar.selectbox(
    "País", countries_list
)

# Garantir que a data inicial seja menor ou igual à data fina

if start_date > end_date:
    st.sidebar.error("A data inicial deve ser menor ou igual à data final.")

# Filtrar dados conforme  as datas e países selecionados

if start_date:
    df = df[df["filter_date"] >= start_date]

if end_date:
    df = df[df["filter_date"] <= end_date]

# Seta as posições das colunas
col1, col2 = st.columns(2)
col3 = st.columns(1)[0]
col4 = st.columns(1)[0]
col5 = st.columns(1)[0]

# # Evolução do número de casos por país.

fig = px.choropleth(
    df,
    locations = 'Country',
    locationmode='country names',
    color='Confirmed',
    animation_frame = 'Date',
    title='Evolução no número de casos de COVID-19 ao redor do mundo.',
    labels={
        "Date":"Data",
        "Confirmed":"Número de Casos"
        }
    )

col1.plotly_chart(fig, use_container_width=True)

# Evolução do número de mortes por país.

fig = px.choropleth(
    df,
    locations = 'Country',
    locationmode='country names',
    color='Deaths',
    animation_frame = 'Date',
    title='Evolução no número de mortes por COVID-19 ao redor do mundo.',
    labels={
        "Date":"Data",
        "Deaths":"Número de Mortes"
        }
    )
col2.plotly_chart(fig, use_container_width=True)

# Calculando a Taxa de Infecção máxima para todos os países
# Criando uma lista com o nome de todos os países do dataset

countries = list(df['Country'].unique())

# Calculando a Maior taxa de Infeçcão para cada país e adicionando a uma lista
max_infection_rates = []
for c in countries:
    MIR = df[df.Country == c].Confirmed.diff().max()
    max_infection_rates.append(MIR)

# Criando um dataframe apenas para a Maior Taxa de Infecção (MIR) 
df_MIR = pd.DataFrame()

# Populando a coluna Country com a lista de nomes dos paises
df_MIR['País'] = countries

# Populando a coluna MIR com os valores de Maior Taxa de Infecção
df_MIR['MIR'] = max_infection_rates

# Ordenando os valores do dataframe do maior MIR para o Menor
df_MIR = df_MIR.sort_values(by=['MIR'])

# Selecionando apenas os 20 primeiros países
df_top10 = df_MIR.tail(20)

# Criando o gráfico de barras
fig = fig = px.bar(
    df_top10,
    x='País',
    y='MIR',
    title = '10 Maiores taxas de Infecção Global (Máxima de casos notificados em um dia)',
    labels={
        'MIR':'Maior Taxa de Infecção','variable':'Variável'
    }) 

col3.plotly_chart(fig, use_container_width=True)

# Visualizando a intensidade da transmissão ao longo do tempo

if selected_country:
    df_filtered = df[df.Country == selected_country].copy()
    df_filtered = df_filtered[['Date','Confirmed']]
    # Calculando a Taxa de Infeção
    df_filtered['Taxa de Infecção'] = df_filtered['Confirmed'].diff()

    # Calculando a Taxa de Infeção Normalizada
    df_filtered['Taxa de Infecção (Normalizada)'] = (df_filtered['Taxa de Infecção'] / df_filtered['Taxa de Infecção'].max()) * 100

    # Calculando o Número de Casos Confirmados Normalizado.
    df_filtered['Confirmados (Normalizado)'] = (df_filtered['Confirmed'] / df_filtered['Confirmed'].max()) *100
    
    fig = px.line(
        df_filtered,
        x= 'Date',
        y = ['Confirmados (Normalizado)','Taxa de Infecção (Normalizada)'],
        title=f'Coeficiente de Infecção e Número de Casos em {selected_country}',
        labels={'Date':'Data',
                'variable':'Variavel:',
                'value':'Valor'})
else: fig = None

col4.plotly_chart(fig, use_container_width=True)