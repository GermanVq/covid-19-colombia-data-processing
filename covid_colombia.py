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
dp_top10_infected = data.groupby('Departamento o Distrito').size().sort_values(ascending=False).head(10)
print('Los 10 departamentos con mas contagiados son:', dp_top10_infected)

""" 
[12. Liste de mayor a menor los 10 departamentos con mas casos de
fallecidos]
"""
dp_top10_deceased = data[data['Atención**']=='Fallecido'].groupby('Departamento o Distrito').size().sort_values(ascending=False).head(10)
print('Los 10 departamentos con mas fallecidos son:', dp_top10_deceased)

""" 
[13. Liste de mayor a menor los 10 departamentos con mas casos de
recuperados]
"""
dp_top10_recovered = data[data['Atención**']=='Recuperado'].groupby('Departamento o Distrito').size().sort_values(ascending=False).head(10)
print('Los 10 departamentos con mas recuperados son:', dp_top10_recovered)

""" 
[14. Liste de mayor a menor los 10 municipios con mas casos de
contagiados]
"""
mp_top10_infected = data.groupby('Ciudad de ubicación').size().sort_values(ascending=False).head(10)
print('Los 10 Municipios con mas infectados son:', mp_top10_infected)

""" 
[15. Liste de mayor a menor los 10 municipios con mas casos de
fallecidos]
"""
mp_top10_deceased = data[data['Atención**']=='Fallecido'].groupby('Ciudad de ubicación').size().sort_values(ascending=False).head(10)
print('Los 10 municipios con mas fallecidos son:', mp_top10_deceased)

""" 
[16. Liste de mayor a menor los 10 municipios con mas casos de
recuperados]
"""
mp_top10_recovered = data[data['Atención**']=='Recuperado'].groupby('Ciudad de ubicación').size().sort_values(ascending=False).head(10)
print('Los 10 municipios con mas recuperados son:', mp_top10_recovered)

""" 
[17. Liste agrupado por departamento y en orden de Mayor a menor las
ciudades con mas casos de contagiados]
"""
dp_mp = data.groupby(['Departamento o Distrito','Ciudad de ubicación']).size().sort_values(ascending=False)
print('Lista de  Departamenos agrupudos de mayor a menor con ciudades con mas casos: ', dp_mp)

""" 
[18. Número de Mujeres y hombres contagiados por ciudad por
departamento]
"""
dp_men_women_infected = data.groupby(['Departamento o Distrito','Ciudad de ubicación','Sexo']).size()
print('Numero de hombre y mujeres infectados por Ciudad de cada departamento es:', dp_men_women_infected)

""" 
[19. Liste el promedio de edad de contagiados por hombre y mujeres por
ciudad por departamento]
"""

prom_ed = data.groupby(['Departamento o Distrito', 'Ciudad de ubicación','Sexo']).mean()
prom_ed.drop('ID de caso', axis = 1)
""" 
[20. Liste de mayor a menor el número de contagiados por país de procedencia]
"""
country_p = data.groupby('País de procedencia').size().sort_values(ascending = False)
print('Lista de paises de mayor a menos de contagiados por:', country_p)


""" 
[21. Liste de mayor a menor las fechas donde se presentaron mas
contagios]
"""
diagnosis_date = data.groupby('Fecha de diagnóstico').size().sort_values(ascending = False)
print('Fechas de mayor a menor con mas infectados:', diagnosis_date)

""" 
[22. Diga cual es la tasa de mortalidad y recuperación que tiene toda 
Colombia]
"""
z = data.groupby('Atención**').size().sort_values(ascending = False)
k = z / z.sum() * 100
print('Tasa de mortalidad en toda colombia es:',k.iloc[4:5])
print('Tasa de recuperados en toda colombia es:',k.iloc[2:3])

""" 
[23. Liste la tasa de mortalidad y recuperación que tiene cada
departamento]
"""
z = data.groupby(['Departamento o Distrito','Atención**']).size()
k = z / z.sum() * 100


""" 
[24. Liste la tasa de mortalidad y recuperación que tiene cada ciudad]
"""
z = data.groupby(['Ciudad de ubicación','Atención**']).size()
k = z / z.sum() * 100

""" 
[25. Liste por cada ciudad la cantidad de personas por atención]
"""
data.groupby(['Ciudad de ubicación','Atención**']).size()


""" 
[26. Liste el promedio de edad por sexo por cada ciudad de contagiados]
"""
prom_ed = data.groupby(['Ciudad de ubicación','Sexo']).mean()
prom_ed.drop('ID de caso', axis = 1)


""" 
[27. Grafique las curvas de contagio, muerte y recuperación de toda
Colombia acumulados]
"""

""" 
[28. Grafique las curvas de contagio, muerte y recuperación de los 10
departamentos con mas casos de contagiados acumulados]
"""

""" 
[29. Grafique las curvas de contagio, muerte y recuperación de las 10
ciudades con mas casos de contagiados acumulados]
"""


""" 
[30. Liste de mayor a menor la cantidad de fallecidos por edad en toda
Colombia.]
"""
a_deceased = data[data['Atención**'] == 'Fallecido'].groupby('Edad').size().sort_values(ascending = False)
print('Liste de mayor a menor la cantidad de fallecidos por edad en toda Colombia: ', a_deceased)


""" 
[31. Liste el porcentaje de personas por atención de toda Colombia]
"""
list_at = data.groupby('Atención**').size()
sm = data.groupby('Atención**').size().sum()
res = (list_at.iloc[0:7]*100)/sm
print('Porcentajes por atención:', res)