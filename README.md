# Análise de Dispersão do Covid 19 por País

## Sobre:

A pandemia de Covid 19 impactou o mundo e alterou nosso modo de vida. O fator determinante para a destruição
causada pelo vírus foi a sua alta capacidade de transmissão, que fez com que em questão de meses estivesse
presente em diversas partes do planeta.

Entre os países mais atingidos no início da Pandemia, a Italia é um dos exemplos notáveis e que será abordada incialmente.
Além disso, a propagação do vírus através do mundo será exibida em um gráfico interativo.

## Objetivos:


- Visualizar a evolução do número de casos por país ao longo da pandemia.
- Visualizar a evolução do número de mortes por país ao longo da pandemia.
- Identificar os países com a maior taxa de dispersão do vírus durante toda a pandemia.
- Identificar o impacto do lockdown na taxa de dispersão do vírus na Itália.
- Identificar o impacto do lockdown na taxa de mortes na Itália.
- Identificar o impacto do lockdown na taxa de dispersão do vírus no Brasil.
- Identificar o impacto da vacinação na taxa de mortes no Brasil.

 ---

# Visualizações de Dados

[Acesse o Notebook Python da Análise](https://deepnote.com/@cacau/analisedepropagacaodocovid19-a50281eb-904e-409c-bbad-d1ebc55ceca5)

[Acesse uma página interativa utilizando o Streamlit para filtrar os resultados Aqui](https://covidspreadanalysis-7p3iajp9xrfdvh8qcjvbng.streamlit.app/)



## Fontes de Dados:

- Ahmad Varasteh, Github:
https://github.com/itsAbdulKhadar/COVID19-Data-Analysis-Using-Python

## Metodologia

O dataset escolhido contém valores diários da quantidade de mortes e casos confirmados para cada dia, para cada país.

As etapas de tratamento aplicadas foram as seguintes:

- Segmentação de Datasets por país de interesse (Nas análises por país)
- Eliminação de registros com 0 casos confirmados.

Nos demais casos foram calculadas as taxas de infecção (i) e a taxa de mortes (i) da seguinte maneira:

- (i) Taxa de Infecção: Resultado da subtração da quantidade de pessoas infectadas em um país em um dia (d) pela quantidade de pessoas infectadas no dia anterior (d-1)
- (ii) Taxa de mortes: Resultado da subtração da quantidade de pessoas infectadas em um país em um dia (d) pela quantidade de pessoas infectadas no dia anterior (d-1)