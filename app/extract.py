# Importar módulos de tratamento de dados
import pandas as pd
import numpy as np


# Definindo URL do DataSet
dataset_url = "https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv"



#Importando arquivo diretamente da URL e salvando como CSV
df = pd.read_csv(dataset_url)
df.to_csv('data/covid_dataset.csv')