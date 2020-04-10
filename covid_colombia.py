# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 11:54:44 2020

@author: German Vega
"""
import pandas as pd
import numpy as np
import matplotlib as mpl

url = "covid_colombia_09_04_2020.csv"
data = pd.read_csv(url)

""" 
[1. número total de contagiados]
"""
num_infected = data.shape[0]

""" 
[2. número total de minucipios afectadas]
"""
num_cities = data.groupby('Ciudad de ubicación').size()
num_cities.shape[0]

""" 
[3. Lista de minucipios afectadas sin repetir]
"""
list_infected = data['Ciudad de ubicación'].unique()

""" 
[4. Número de personas que se encuentran en atención en casa]
"""
in_house = data[data['Atención**'] == 'Casa']
in_house.shape[0]

""" 
[5. Número de personas que se encuentran recuperados]
"""
recovered = data[data['Atención**'] == 'Recuperado']
recovered.shape[0]