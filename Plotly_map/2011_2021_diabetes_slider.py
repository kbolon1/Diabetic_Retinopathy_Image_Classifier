import os
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import chart_studio.plotly as py
import matplotlib.pyplot as plt

#access_token = os.getenv('Access_token')

#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')

df = pd.read_csv('dflatest.csv')

# min year in your dataset
year = 2011

data_slider = []

for year in df['Year'].unique():
    df_segmented =  df[(df['Year']== year)]

    for col in df_segmented.columns:
        df_segmented[col] = df_segmented.loc[:,col].astype(str)

    data_each_yr = dict(
                        type='choropleth',
                        locations = df_segmented['Country Code'],
                        z=df_segmented['Diabetes_Rate'].astype(float),
                        text = df['Country Name'],
                        locationmode='ISO-3',
                        colorscale = 'Blues',
                        autocolorscale=False,
                        reversescale=False,
                        marker_line_color='darkgray',
                        marker_line_width=0.5,
                        colorbar_tickprefix = '%',
                        colorbar_title = 'Diabetes prevalence',
                        colorbar= {'title':'Diabetes prevalence'})

    data_slider.append(data_each_yr)

steps = []
for i, year in enumerate([2011, 2021]):
    step = dict(method='restyle',
                args=['visible', [False] * len(data_slider)],
                label='Year {}'.format(year))
    step['args'][1][i] = True
    steps.append(step)

sliders = [dict(active=0, pad={"t": 1}, steps=steps)]
#print(len(data_slider))

layout = dict(title ='Prevalence of Diabetes since 2011', geo=dict(scope='world',
                       projection={'type': 'natural earth'}),
              sliders=sliders)

fig = go.Figure(data=data_slider, layout=layout)
fig.show()

