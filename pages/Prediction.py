# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 11:51:36 2024

@author: daffa
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 23:27:42 2024

@author: daffa
"""
from dash import register_page,dash_table,dcc, html, callback
import pandas as pd 
import plotly.express as px
from dash.dependencies import Input, Output, State #, callback # If you need callbacks, import it here.
import joblib
import numpy as np

register_page(
    __name__,
    name='Prediction',
    top_nav=True,
    path='/Prediction'
)
####################### DATASET #############################
# Load the model from the file
loaded_model = joblib.load("random_forest_model fixed with sc.joblib")

####################### PAGE LAYOUT #############################
# Updated layout with dropdown options based on one-hot encoding
layout = html.Div([
    html.H1("Random Forest Regressor Prediction App"),
    dcc.Input(id='lt-input', type='number', placeholder='Enter LT (m2)'),
    dcc.Input(id='distance-input', type='number', placeholder='Enter distance_ke_pusatkota'),
    dcc.Input(id='lebar-jalan-input', type='number', placeholder='Enter Lebar Jalan Depan (m)'),
    dcc.Dropdown(
        id='kota-kabupaten-dropdown',
        options=[
            {'label': 'Kabupaten Bandung', 'value': 'Kota/Kabupaten_Kabupaten Bandung'},
            {'label': 'Kabupaten Bandung Barat', 'value': 'Kota/Kabupaten_Kabupaten Bandung Barat'},
            {'label': 'Kabupaten Bekasi', 'value': 'Kota/Kabupaten_Kabupaten Bekasi'},
            {'label': 'Kabupaten Bogor', 'value': 'Kota/Kabupaten_Kabupaten Bogor'},
            {'label': 'Kabupaten Ciamis', 'value': 'Kota/Kabupaten_Kabupaten Ciamis'},
            {'label': 'Kabupaten Cianjur', 'value': 'Kota/Kabupaten_Kabupaten Cianjur'},
            {'label': 'Kabupaten Cirebon', 'value': 'Kota/Kabupaten_Kabupaten Cirebon'},
            {'label': 'Kabupaten Garut', 'value': 'Kota/Kabupaten_Kabupaten Garut'},
            {'label': 'Kabupaten Indramayu', 'value': 'Kota/Kabupaten_Kabupaten Indramayu'},
            {'label': 'Kabupaten Karawang', 'value': 'Kota/Kabupaten_Kabupaten Karawang'},
            {'label': 'Kabupaten Kuningan', 'value': 'Kota/Kabupaten_Kabupaten Kuningan'},
            {'label': 'Kabupaten Majalengka', 'value': 'Kota/Kabupaten_Kabupaten Majalengka'},
            {'label': 'Kabupaten Pangandaran', 'value': 'Kota/Kabupaten_Kabupaten Pangandaran'},
            {'label': 'Kabupaten Purwakarta', 'value': 'Kota/Kabupaten_Kabupaten Purwakarta'},
            {'label': 'Kabupaten Subang', 'value': 'Kota/Kabupaten_Kabupaten Subang'},
            {'label': 'Kabupaten Sukabumi', 'value': 'Kota/Kabupaten_Kabupaten Sukabumi'},
            {'label': 'Kabupaten Sumedang', 'value': 'Kota/Kabupaten_Kabupaten Sumedang'},
            {'label': 'Kabupaten Tasikmalaya', 'value': 'Kota/Kabupaten_Kabupaten Tasikmalaya'},
            {'label': 'Kota Bandung', 'value': 'Kota/Kabupaten_Kota Bandung'},
            {'label': 'Kota Banjar', 'value': 'Kota/Kabupaten_Kota Banjar'},
            {'label': 'Kota Bekasi', 'value': 'Kota/Kabupaten_Kota Bekasi'},
            {'label': 'Kota Bogor', 'value': 'Kota/Kabupaten_Kota Bogor'},
            {'label': 'Kota Cimahi', 'value': 'Kota/Kabupaten_Kota Cimahi'},
            {'label': 'Kota Cirebon', 'value': 'Kota/Kabupaten_Kota Cirebon'},
            {'label': 'Kota Depok', 'value': 'Kota/Kabupaten_Kota Depok'},
            {'label': 'Kota Sukabumi', 'value': 'Kota/Kabupaten_Kota Sukabumi'},
            {'label': 'Kota Tasikmalaya', 'value': 'Kota/Kabupaten_Kota Tasikmalaya'},
        ],
        placeholder='Select Kota/Kabupaten'
    ),
    dcc.Dropdown(
        id='clusters-dropdown',
        options=[
            {'label': f'Cluster {i}', 'value': i} for i in range(3)
        ],
        placeholder='Select Clusters'
    ),
    dcc.Dropdown(
        id='peruntukan-dropdown',
        options=[
            {'label': 'Fasilitas Umum', 'value': 'Peruntukan_Fasilitas Umum'},
            {'label': 'Kawasan Industri', 'value': 'Peruntukan_Kawasan Industri'},
            {'label': 'Kawasan Perdagangan dan Jasa', 'value': 'Peruntukan_Kawasan Perdagangan dan Jasa'},
            {'label': 'Kawasan Peruntukan Perkebunan', 'value': 'Peruntukan_Kawasan Peruntukan Perkebunan'},
            {'label': 'Pemukiman Perkotaan', 'value': 'Peruntukan_Pemukiman Perkotaan'},
            {'label': 'Perikanan (Tambak, Kolam, Perairan Umum)', 'value': 'Peruntukan_Perikanan (Tambak, Kolam, Perairan Umum)'},
        ],
        placeholder='Select Peruntukan'
    ),
    dcc.Dropdown(
        id='hap-dropdown',
        options=[
            {'label': 'Hak Atas Properti_AJB', 'value': 'Hak Atas Properti_AJB'},
            {'label': 'Hak Atas Properti_Girik', 'value': 'Hak Atas Properti_Girik'},
            {'label': 'Hak Atas Properti_Gross Akte', 'value': 'Hak Atas Properti_Gross Akte'},
            {'label': 'Hak Atas Properti_HGB diatas HPL', 'value': 'Hak Atas Properti_HGB diatas HPL'},
            {'label': 'Hak Atas Properti_HP', 'value': 'Hak Atas Properti_HP'},
            {'label': 'Hak Atas Properti_PPJB', 'value': 'Hak Atas Properti_PPJB'},
            
            {'label': 'Hak Atas Properti_SHGB', 'value': 'Hak Atas Properti_SHGB'},
            {'label': 'Hak Atas Properti_SHGU', 'value': 'Hak Atas Properti_SHGU'},
            {'label': 'Hak Atas Properti_SHM', 'value': 'Hak Atas Properti_SHM'},
            
            {'label': 'Hak Atas Properti_SHMSRS ', 'value': 'Hak Atas Properti_SHMSRS '},
            {'label': 'Hak Atas Properti_SIPPT', 'value': 'Hak Atas Properti_SIPPT'},
            {'label': 'Hak Atas Properti_SPH', 'value': 'Hak Atas Properti_SPH'},
        ],
        placeholder='Select Hak Atas Properti'
    ),
    dcc.Dropdown(
        id='bentuk-tapak-dropdown',
        options=[
            {'label': 'Kipas', 'value': 'Bentuk Tapak_Kipas'},
            {'label': 'Letter L', 'value': 'Bentuk Tapak_Letter L'},
            {'label': 'Ngantong', 'value': 'Bentuk Tapak_Ngantong'},
            {'label': 'Persegi', 'value': 'Bentuk Tapak_Persegi'},
            {'label': 'Persegi Panjang', 'value': 'Bentuk Tapak_Persegi Panjang'},
            {'label': 'Tidak Beraturan', 'value': 'Bentuk Tapak_Tidak Beraturan'},
            {'label': 'Trapesium', 'value': 'Bentuk Tapak_Trapesium'},
        ],
        placeholder='Select Bentuk Tapak'
    ),
    dcc.Dropdown(
        id='kualitas-wilayah-dropdown',
        options=[
            {'label': 'Bawah', 'value': 'Kualitas Wilayah Sekitar_Bawah'},
            {'label': 'Kumuh', 'value': 'Kualitas Wilayah Sekitar_Kumuh'},
            {'label': 'Menengah', 'value': 'Kualitas Wilayah Sekitar_Menengah'},
            {'label': 'Mewah', 'value': 'Kualitas Wilayah Sekitar_Mewah'},
        ],
        placeholder='Select Kualitas Wilayah Sekitar'
    ),
    dcc.Dropdown(
        id='kondisi-wilayah-dropdown',
        options=[
            {'label': 'Campuran', 'value': 'Kondisi Wilayah Sekitar_Campuran'},
            {'label': 'Hijau', 'value': 'Kondisi Wilayah Sekitar_Hijau'},
            {'label': 'Industri', 'value': 'Kondisi Wilayah Sekitar_Industri'},
            {'label': 'Komersial', 'value': 'Kondisi Wilayah Sekitar_Komersial'},
            {'label': 'Pemerintahan', 'value': 'Kondisi Wilayah Sekitar_Pemerintahan'},
            {'label': 'Perumahan', 'value': 'Kondisi Wilayah Sekitar_Perumahan'},
        ],
        placeholder='Select Kondisi Wilayah Sekitar'
    ),
    dcc.Dropdown(
        id='kondisi-tapak-dropdown',
        options=[
            {'label': 'Darat / Kering', 'value': 'Kondisi Tapak_Darat / Kering'},
            {'label': 'Tanah Mentah', 'value': 'Kondisi Tapak_Tanah Mentah'},
            {'label': 'Tanah Rawa', 'value': 'Kondisi Tapak_Tanah Rawa'},
            {'label': 'Tanah Siap Dikembangkan (Tanah Matang)', 'value': 'Kondisi Tapak_Tanah Siap Dikembangkan (Tanah Matang)'},
            {'label': 'Tanah dalam Pengembangan', 'value': 'Kondisi Tapak_Tanah dalam Pengembangan'},
        ],
        placeholder='Select Kondisi Tapak'
    ),
    html.Button('Predict', id='predict-button', n_clicks=0),
    html.Div(id='output-predictions')
])


####################### CALLBACKS ################################
# Updated callback function
@callback(
    Output('output-predictions', 'children'),
    Input('predict-button', 'n_clicks'),
    State('lt-input', 'value'),
    State('distance-input', 'value'),
    State('lebar-jalan-input', 'value'),
    State('clusters-dropdown', 'value'),
    State('peruntukan-dropdown', 'value'),
    State('hap-dropdown', 'value'),  # Include Hak Atas Properti value
    State('kota-kabupaten-dropdown', 'value') , # Include Kondisi Tapak value
    State('bentuk-tapak-dropdown', 'value'),  # Include Bentuk Tapak value
    State('kualitas-wilayah-dropdown', 'value'),  # Include Kualitas Wilayah Sekitar value
    State('kondisi-wilayah-dropdown', 'value'),  # Include Kondisi Wilayah Sekitar value
    State('kondisi-tapak-dropdown', 'value') , # Include Kondisi Tapak value
    
)
def update_output_predictions(n_clicks, lt_input, distance_input, lebar_jalan_input, clusters_dropdown, peruntukan_dropdown, hap_dropdown, bentuk_tapak_dropdown, kualitas_wilayah_dropdown, kondisi_wilayah_dropdown, 
                              kondisi_tapak_dropdown,kota_kabupaten_dropdown):
    if n_clicks == 0 or None in [lt_input, distance_input, lebar_jalan_input, clusters_dropdown, peruntukan_dropdown, hap_dropdown, kota_kabupaten_dropdown,bentuk_tapak_dropdown, kualitas_wilayah_dropdown, kondisi_wilayah_dropdown, 
                                  kondisi_tapak_dropdown]:
        return None

    user_input = [
        float(lt_input),
        float(distance_input),
        float(lebar_jalan_input),
        clusters_dropdown,
        peruntukan_dropdown,
        hap_dropdown,
        kota_kabupaten_dropdown,
        bentuk_tapak_dropdown,
        kualitas_wilayah_dropdown,
        kondisi_wilayah_dropdown,
        kondisi_tapak_dropdown,
        
    ]

    prediction = make_predictions(loaded_model, user_input)

    return html.Div([
        html.H2("Prediction:"),
        html.H4(f"{prediction}")
    ])




# Function to make predictions using the loaded model
def make_predictions(model, new_data):
    lt, distance, lebar_jalan, cluster, peruntukan, hap, bentuk_tapak, kualitas_wilayah, kondisi_wilayah, kondisi_tapak,kota_kabupaten_dropdown = new_data
    
# Create a DataFrame with the input features
    input_df = pd.DataFrame([[float(lt), float(distance), float(lebar_jalan)] +  [0]*70], 
                        columns=['LT (m2)', 'distance_ke_pusatkota', 'Lebar Jalan Depan (m)', 'Clusters_0', 'Clusters_1', 'Clusters_2', 
                                 'Peruntukan_Fasilitas Umum', 'Peruntukan_Kawasan Industri', 'Peruntukan_Kawasan Perdagangan dan Jasa', 'Peruntukan_Kawasan Peruntukan Perkebunan', 
                                 'Peruntukan_Pemukiman Perkotaan', 'Peruntukan_Perikanan (Tambak, Kolam, Perairan Umum)', 'Hak Atas Properti_AJB', 'Hak Atas Properti_Girik',
                                 'Hak Atas Properti_Gross Akte', 'Hak Atas Properti_HGB diatas HPL', 'Hak Atas Properti_HP', 'Hak Atas Properti_PPJB', 'Hak Atas Properti_SHGB', 
                                 'Hak Atas Properti_SHGU', 'Hak Atas Properti_SHM', 'Hak Atas Properti_SHMSRS ', 'Hak Atas Properti_SIPPT', 'Hak Atas Properti_SPH', 'Kota/Kabupaten_Kabupaten Bandung', 
                                 'Kota/Kabupaten_Kabupaten Bandung Barat', 'Kota/Kabupaten_Kabupaten Bekasi', 'Kota/Kabupaten_Kabupaten Bogor', 'Kota/Kabupaten_Kabupaten Ciamis', 
                                 'Kota/Kabupaten_Kabupaten Cianjur', 'Kota/Kabupaten_Kabupaten Cirebon', 'Kota/Kabupaten_Kabupaten Garut', 'Kota/Kabupaten_Kabupaten Indramayu', 
                                 'Kota/Kabupaten_Kabupaten Karawang', 'Kota/Kabupaten_Kabupaten Kuningan', 'Kota/Kabupaten_Kabupaten Majalengka', 'Kota/Kabupaten_Kabupaten Pangandaran', 
                                 'Kota/Kabupaten_Kabupaten Purwakarta', 'Kota/Kabupaten_Kabupaten Subang', 'Kota/Kabupaten_Kabupaten Sukabumi', 'Kota/Kabupaten_Kabupaten Sumedang', 
                                 'Kota/Kabupaten_Kabupaten Tasikmalaya', 'Kota/Kabupaten_Kota Bandung', 'Kota/Kabupaten_Kota Banjar', 'Kota/Kabupaten_Kota Bekasi', 'Kota/Kabupaten_Kota Bogor', 
                                 'Kota/Kabupaten_Kota Cimahi', 'Kota/Kabupaten_Kota Cirebon', 'Kota/Kabupaten_Kota Depok', 'Kota/Kabupaten_Kota Sukabumi', 'Kota/Kabupaten_Kota Tasikmalaya', 
                                 'Bentuk Tapak_Kipas', 'Bentuk Tapak_Letter L', 'Bentuk Tapak_Ngantong', 'Bentuk Tapak_Persegi', 'Bentuk Tapak_Persegi Panjang', 'Bentuk Tapak_Tidak Beraturan', 
                                 'Bentuk Tapak_Trapesium', 'Kualitas Wilayah Sekitar_Bawah', 'Kualitas Wilayah Sekitar_Kumuh', 'Kualitas Wilayah Sekitar_Menengah', 'Kualitas Wilayah Sekitar_Mewah', 
                                 'Kondisi Wilayah Sekitar_Campuran', 'Kondisi Wilayah Sekitar_Hijau', 'Kondisi Wilayah Sekitar_Industri', 'Kondisi Wilayah Sekitar_Komersial', 
                                 'Kondisi Wilayah Sekitar_Pemerintahan', 'Kondisi Wilayah Sekitar_Perumahan', 'Kondisi Tapak_Darat / Kering', 'Kondisi Tapak_Tanah Mentah', 
                                 'Kondisi Tapak_Tanah Rawa', 'Kondisi Tapak_Tanah Siap Dikembangkan (Tanah Matang)', 'Kondisi Tapak_Tanah dalam Pengembangan'])
    
    # Set the corresponding features to 1
    input_df[f'Clusters_{cluster}'] = 1
    input_df[peruntukan] = 1
    input_df[hap] = 1
    input_df[kota_kabupaten_dropdown] = 1
    input_df[bentuk_tapak] = 1
    input_df[kualitas_wilayah] = 1
    input_df[kondisi_wilayah] = 1
    input_df[kondisi_tapak] = 1
    
    
    prediction = model.predict(input_df)
    
    formatted_prediction = "{:,.2f}".format(prediction[0])
    
    return formatted_prediction