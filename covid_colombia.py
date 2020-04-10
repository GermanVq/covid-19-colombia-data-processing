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

