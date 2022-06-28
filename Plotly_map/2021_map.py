import os
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

#access_token = os.getenv('Access_token')

#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')

df = pd.read_csv('d_2021.csv')


fig = go.Figure(data=go.Choropleth(
    locations = df['Country_Code'],
    z = df['2021'],
    text = df['Country_Name'],
    colorscale = 'Blues',
    autocolorscale=False,
    reversescale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_tickprefix = '%',
    colorbar_title = 'Diabetes prevalence,<br>2021',
))

fig.update_layout(
    title_text='Prevalence of Diabetes in 2021',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    annotations = [dict(
        x=0.55,
        y=0.1,
        xref='paper',
        yref='paper',
        text='Source: <a href="https://datacatalog.worldbank.org/search/dataset/0037652/Health-Nutrition-and-Population-Statistics">\
            THE WORLD BANK</a>',
        showarrow = False
    )]
)

fig.show()