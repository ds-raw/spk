from dash import html, register_page,dash_table
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import pandas as pd  #, callback # If you need callbacks, import it here.
from dash_table import DataTable
register_page(
    __name__,
    name='Dataset',
    top_nav=True,
    path='/Dataset'
)

# Load dataset
df = pd.read_excel("JawaBarat.xlsx")
def layout():
    # Create a DataTable with pagination
    table = DataTable(
        id='table',
        columns=[{'name': col, 'id': col} for col in df.columns],
        data=df.to_dict('records'),
        page_size=20,
        style_table={'overflowX': 'auto'},

    )

    # Create a loading spinner while data is being loaded
    loading_spinner = dcc.Loading(
        id="loading",
        type="circle",
        children=[table],
    )

    return html.Div([html.Br(), loading_spinner])
