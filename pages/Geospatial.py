# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 23:20:03 2024

@author: daffa
"""
from dash import html, register_page,dash_table
import pandas as pd 
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output #, callback # If you need callbacks, import it here.
register_page(
    __name__,
    name='Geospatial',
    top_nav=True,
    path='/Geospatial'
)
# DATASET
df = pd.read_excel("JawaBarat.xlsx")

# MAPBOX CHART FUNCTION
def create_map_chart():
    figure = px.scatter_mapbox(
        df, 
        lat='latitude', 
        lon='longitude', 
        color='Clusters',
        title='Geospatial Analysis',
        mapbox_style="carto-positron",
        zoom=10,
        center={"lat": df['latitude'].mean(), "lon": df['longitude'].mean()},
    )
    figure.update_layout(height=720, width=1280)
    return figure

# WIDGETS
# No need for dropdown in this case

# PAGE LAYOUT
layout = html.Div(children=[
    html.H3('Geospatial Analysis'),
    dcc.Graph(id="map_chart", figure=create_map_chart())
])

# CALLBACKS
# No need for callback in this case