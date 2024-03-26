from dash import html, register_page,dash_table
import pandas as pd 
from dash import dcc, html, callback
import plotly.express as px
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output #, callback # If you need callbacks, import it here.

register_page(
    __name__,
    name='Distribution',
    top_nav=True,
    path='/Distribution'
)

# Load dataset
df = pd.read_excel("JawaBarat.xlsx")
# Distribution chart function
# set average score and row id
df['Provinsi'] = df.index
avg_lt = round(df['LT (m2)'].mean(), 2)
avg_hpm = round(df['HPM'].mean(), 2)
avg_distance = round(df['distance_ke_pusatkota'].mean(), 2)
# create reusable card component
def get_card_component(title, data):
    component = dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            html.H4(title),
                            html.H4(data)
                        ]), 
                        color="dark", 
                        outline=True,
                        className = 'text-dark',
                        style={'textAlign': 'center', 'margin-bottom': '20px'}
                    ),
                )
    return component



# Dropdown widget
columns = ["Kondisi Wilayah Sekitar", "Peruntukan", "Kota/Kabupaten", "Clusters", "Hak Atas Properti"]
dd = dcc.Dropdown(id="dist_column", options=[{'label': col, 'value': col} for col in columns], value="Peruntukan", clearable=False)
# create color palette
color_discrete_sequence = ['#0a9396','#94d2bd','#e9d8a6','#ee9b00', '#ca6702', '#bb3e03', '#ae2012']
# Page layout
layout = html.Div([
    
    html.H1(children='Explore Data', style={'textAlign':'center', 'padding-bottom': '20px'}),
    dbc.Row([
        get_card_component('Total Data', '{:,}'.format(len(df.index))),
        get_card_component('Avg Luas Tanah', str(avg_lt)),
        get_card_component('Avg Harga Per Meter', str(avg_hpm)),
        get_card_component('Avg Ke Pusat Kota', str(avg_distance)),
        
    ]),
    dbc.Row(
        dbc.Col([
            html.H4("Distribusi Data Numerikal"),
            html.Div(
                dbc.RadioItems(
                    id="score-distribution-radios",
                    className="btn-group",
                    inputClassName="btn-check",
                    labelClassName="btn btn-outline-dark",
                    labelCheckedClassName="active",
                    options=[
                        {'label': 'Luas Tanah', 'value': 'LT (m2)'},
                        {'label': 'Harga Per Meter', 'value': 'HPM'},
                        {'label': 'Jarak Pusat Kota', 'value': 'distance_ke_pusatkota'},
                        ],
                    value='LT (m2)',
                ),
                className ="radio-group",
                style = {'margin-top': '20px'}
            ),
            dcc.Graph(figure={}, id="score-distribution-histogram")
        ])
    ),
    dbc.Row([
        html.H4("Each Score Relationship"),
        dbc.Col(
            dcc.Graph(figure=px.scatter(df, x="LT (m2)", y="HPM", color_discrete_sequence=['#94d2bd'])),
        ),
        dbc.Col(
            dcc.Graph(figure=px.scatter(df, x="distance_ke_pusatkota", y="LT (m2)", color_discrete_sequence=['#e9d8a6'])),
        ),
        dbc.Col(
            dcc.Graph(figure=px.scatter(df, x="HPM", y="distance_ke_pusatkota", color_discrete_sequence=['#ee9b00'])),
        )
    ]),
    dbc.Row(
        dbc.Col([
            html.H4("Explore Categorical Data"),
            html.Div(
                dbc.RadioItems(
                    id="student-categorical-radios",
                    className="btn-group",
                    inputClassName="btn-check",
                    labelClassName="btn btn-outline-dark",
                    labelCheckedClassName="active",
                    options=[
                        {'label': 'Peruntukan', 'value': 'Peruntukan'},
                        {'label': 'Kondisi Wilayah Sekitar', 'value': 'Kondisi Wilayah Sekitar'},
                        {'label': 'Kota/Kabupaten', 'value': 'Kota/Kabupaten'},
                        {'label': 'Kualitas Wilayah Sekitar', 'value': 'Kualitas Wilayah Sekitar'},
                    ],
                    value='Peruntukan',
                ),
                className ="radio-group",
                style = {'margin-top': '20px'}
            ),
            dcc.Graph(figure={}, id="student-categorical-summary"),
            dbc.Row([
                dbc.Col(dcc.Graph(figure={}, id="student-categorical-math-score-distribution")),
                dbc.Col(dcc.Graph(figure={}, id="student-categorical-writing-score-distribution")),
                dbc.Col(dcc.Graph(figure={}, id="student-categorical-reading-score-distribution")),
            ]),
        ])
    ),
])
@callback(
    Output("score-distribution-histogram", "figure"),
    [Input("score-distribution-radios", "value")]
)
def update_histogram(selected_column):
    # Create histogram based on the selected column
    fig = px.histogram(df, x=selected_column, color_discrete_sequence=color_discrete_sequence)
    fig.update_layout(title=f"Distribution of {selected_column}", xaxis_title=selected_column, yaxis_title="Count")
    return fig

@callback(
    Output("student-categorical-summary", "figure"),
    Output("student-categorical-math-score-distribution", "figure"),
    Output("student-categorical-writing-score-distribution", "figure"),
    Output("student-categorical-reading-score-distribution", "figure"),
    [Input("student-categorical-radios", "value")]
)
def update_categorical_component(value):
    grouped_df = pd.DataFrame({'count': df.groupby([value]).size()}).reset_index()
    figure = px.bar(grouped_df, x=value, y='count', color=value, color_discrete_sequence=color_discrete_sequence, title='Summary')

    HPM_figure = px.box(df, x=value, y="HPM", color_discrete_sequence=['#0a9396'], title='HPM Distribution')
    LT_figure = px.box(df, x=value, y="LT (m2)", color_discrete_sequence=['#ee9b00'], title='LT (m2) Distribution')
    kota_figure = px.box(df, x=value, y="distance_ke_pusatkota", color_discrete_sequence=['#bb3e03'],
                         title='distance_ke_pusatkota Distribution')

    return figure, HPM_figure, LT_figure, kota_figure



