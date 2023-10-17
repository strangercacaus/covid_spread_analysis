# Análise de Dispersão do Covid 19 por País

## Sobre:

A pandemia de Covid 19 impactou o mundo e alterou nosso modo de vida. O fator determinante para a destruição
causada pelo vírus foi a sua alta capacidade de transmissão, que fez com que em questão de meses estivesse
presente em diversas partes do planeta.

Entre os países mais atingidos no início da Pandemia, a Italia é um dos exemplos notáveis e que será abordada incialmente.
Além disso, a propagação do vírus através do mundo será exibida em um gráfico interativo.

## Objetivos:

- Determinar os 10 países com a maior taxa de dispersão do vírus durante toda a pandemia.
- Visualizar a evolução do número de casos por país ao longo da pandemia.
- Visualizar a evolução do número de mortes por país ao longo da pandemia.
- Identificar o impacto do lockdown na taxa de dispersão do vírus na Itália.
- Identificar o impacto do lockdown na taxa de mortes na Itália.
- Identificar o impacto do lockdown na taxa de dispersão do vírus no Brasil.
- Identificar o impacto do lockdown na taxa de mortes no Brasil.

## Fontes de Dados:

- Ahmad Varasteh, Github:
https://github.com/itsAbdulKhadar/COVID19-Data-Analysis-Using-Python

## Metodologia

O dataset escolhido contém valores diários da quantidade de mortes e casos confirmados para cada dia, para cada país.

As etapas de tratamento aplicadas foram as seguintes:

- Segmentação de Datasets por país de interesse (Nas análises por país)
- Eliminação de registros com 0 casos confirmados.

Nos demais casos foram calculadas as taxas de infecção (i) e a taxa de mortes (i) da seguinte maneira:

- (i) Taxa de infecção: Resultado da subtração da quantidade de pessoas infectadas em um país em um dia (d) pela quantidade de pessoas infectadas no dia anterior (d-1)
- (ii) Taxa de mortes: Resultado da subtração da quantidade de pessoas infectadas em um país em um dia (d) pela quantidade de pessoas infectadas no dia anterior (d-1)