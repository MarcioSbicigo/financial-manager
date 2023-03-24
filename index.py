from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from app import *

#Importando os componentes da pasta 'components'
from components import sidebar, dashboards, extracts

# ========== INÍCIO LAYOUT ========== #

content = html.Div(id="page-content")

app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([dcc.Location(id='url'), sidebar.layout], md=2),
        dbc.Col([content], md=10)
    ])
    
], fluid=True,)

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])

def render_page(pathname):
    if pathname == '/' or pathname == '/dashboards':
        return dashboards.layout
    
    if pathname == '/extratos':
        return extracts.layout

if __name__ == '__main__':
    app.run_server(port=9090, debug=True)