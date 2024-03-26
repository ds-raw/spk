# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 23:22:36 2024

@author: daffa
"""
from dash import html, register_page,dash_table
import pandas as pd 
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output #, callback # If you need callbacks, import it here.
register_page(
    __name__,
    name='Relationship',
    top_nav=True,
    path='/Relationship'
)
####################### DATASET #############################
df = pd.read_excel("JawaBarat.xlsx")

####################### SCATTER CHART #############################
def create_scatter_chart(x_axis="Peruntukan", y_axis="LT (m2)", color_axis="Clusters"):
    return px.scatter(data_frame=df, x=x_axis, y=y_axis, color=color_axis,height=600)

####################### WIDGETS #############################
columns = ["LT (m2)","Kondisi Wilayah Sekitar", "HPM Transform","distance_ke_pusatkota Transform","HPM","distance_ke_pusatkota","Peruntukan", "Kota/Kabupaten","Clusters","Hak Atas Properti","HPM"]

x_axis = dcc.Dropdown(id="x_axis", options=columns, value="HPM Transform", clearable=False)
y_axis = dcc.Dropdown(id="y_axis", options=columns, value="distance_ke_pusatkota Transform", clearable=False)

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    "X-Axis", x_axis, 
    "Y-Axis", y_axis,
    dcc.Graph(id="scatter")
])

####################### CALLBACKS ###############################
@callback(Output("scatter", "figure"), [Input("x_axis", "value"),Input("y_axis", "value"), ])
def update_scatter_chart(x_axis, y_axis):
    return create_scatter_chart(x_axis, y_axis)