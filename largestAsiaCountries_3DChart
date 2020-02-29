import plotly as py
from plotly import tools
import plotly.graph_objs as go
import numpy as np
import pandas as pd

#set up offline mode
py.offline.init_notebook_mode(connected=True)

df = pd.read_csv('/Users/saranking/Documents/DASE4770/3DChart/Population.csv')

countries = ['China', 'India', 'Indonesia', 'Pakistan', 'Bangladesh']
fill_colors = ['#006a4e', '#006600', '#FF0000', '#ff9933', '#ffde00']
gf = df.groupby('country')

data = []

for country, fill_color in zip(countries[::-1], fill_colors):
    group = gf.get_group(country)
    years = group['year'].tolist()
    length = len(years)
    country_coords = [country] * length
    pop = group['pop'].tolist()
    zeros = [0] * length
    
    data.append(dict(
        type='scatter3d',
        mode='lines',
        x=years + years[::-1] + [years[0]],  
        y=country_coords * 2 + [country_coords[0]],
        z=pop + zeros + [pop[0]],
        name='',
        surfaceaxis=1, 
        surfacecolor=fill_color,
        line=dict(
            color='black',
            width=4
        ),
    ))

layout = dict(
    title='Top Five Largest Asia Countries by Population',
    showlegend=False,
    scene=dict(
        xaxis=dict(title=''),
        yaxis=dict(title=''),
        zaxis=dict(title=''),
        camera=dict(
            eye=dict(x=-1.7, y=-1.7, z=0.5)
        )
    )
)

fig = dict(data=data, layout=layout)
py.offline.plot(fig, filename='3DChart.html')
