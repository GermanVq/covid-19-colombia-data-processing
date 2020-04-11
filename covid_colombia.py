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
[1. Número total de contagiados]
"""
num_infected = data.shape[0]
print('Número total de infectado es:', num_infected)

""" 
[2. Número total de minucipios afectadas]
"""
num_cities = data.groupby('Ciudad de ubicación').size()
print('Número total de municipos afectados es:', num_cities.shape[0])


""" 
[3. Lista de minucipios afectadas sin repetir]
"""
list_infected = data['Ciudad de ubicación'].unique()
print('Lista de municipios afectados:', list_infected)

""" 
[4. Número de personas que se encuentran en atención en casa]
"""
in_house = data[data['Atención**'] == 'Casa']
print('Número de personas atentidas en casa:', in_house.shape[0])


""" 
[5. Número de personas que se encuentran recuperados]
"""
recovered = data[data['Atención**'] == 'Recuperado']
print('Número de recuperadoes es:', recovered.shape[0])

""" 
[6. Número de personas que ha fallecido]
"""

deceased = data[data['Atención**'] == 'Fallecido']
print('Número de Fallecidos es:', deceased.shape[0])


""" 
[7. Orden de Mayor a menor por tipo de caso (Importado, en estudio,
Relacionado)]
"""
type_case = data.groupby('Tipo*').size().sort_values(ascending=False)
print('Orden de mayor a menor tipo de caso', type_case)

""" 
[8. . Número de departamentos afectados]
"""
num_dep = data.groupby('Departamento o Distrito').size()
print('Número de departamentos afectados es:', num_dep.shape[0])

""" 
[9. Liste los departamentos afectados(sin repetirlos)]
"""
list_dep = data['Departamento o Distrito'].unique()
print('Lista de departamenos afectados', list_dep)

""" 
[10. Ordene de mayor a menor por tipo de atención]
"""
type_atten = data.groupby('Atención**').size().sort_values(ascending=False)
print('Orden de mayor a menor tipo de atención:', type_atten)

""" 
[11. Liste de mayor a menor los 10 departamentos con mas casos de
contagiados]
"""
dp_top10_infected = data.groupby('Departamento o Distrito').size().head(10).sort_values(ascending=False)
print('Los 10 departamentos con mas contagiados son:', dp_top10_infected)

""" 
[12. Liste de mayor a menor los 10 departamentos con mas casos de
fallecidos]
"""
dp_top10_deceased = data[data['Atención**']=='Fallecido'].groupby('Departamento o Distrito').size().head(10).sort_values(ascending=False)
print('Los 10 departamentos con mas fallecidos son:', dp_top10_deceased)

""" 
[13. Liste de mayor a menor los 10 departamentos con mas casos de
recuperados]
"""
dp_top10_recovered = data[data['Atención**']=='Recuperado'].groupby('Departamento o Distrito').size().head(10).sort_values(ascending=False)
print('Los 10 departamentos con mas recuperados son:', dp_top10_recovered)