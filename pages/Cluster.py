# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 23:27:42 2024

@author: daffa
"""
from dash import register_page,dash_table,dcc, html, callback
import pandas as pd 
import plotly.express as px
from dash.dependencies import Input, Output #, callback # If you need callbacks, import it here.

register_page(
    __name__,
    name='Cluster Count',
    top_nav=True,
    path='/Cluster'
)
####################### DATASET #############################
df = pd.read_excel("JawaBarat.xlsx")

####################### BAR CHART #############################
def create_bar_chart(col_name="Peruntukan"):
    fig =  px.histogram(data_frame=df, x="Clusters", color=col_name,
                        histfunc="count", barmode='group', height=600)
    fig = fig.update_layout(bargap=0.5)
    return fig

####################### WIDGETS ################################
columns = ["Kondisi Wilayah Sekitar", "Peruntukan", "Kota/Kabupaten"]
dd = dcc.Dropdown(id="sel_col", options=columns, value="Peruntukan", clearable=False)

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    dd, 
    dcc.Graph(id="bar_chart")
])

####################### CALLBACKS ################################
@callback(Output("bar_chart", "figure"), [Input("sel_col", "value"), ])
def update_bar_chart(sel_col):
    return create_bar_chart(sel_col)