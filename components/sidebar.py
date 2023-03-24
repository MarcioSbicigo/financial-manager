import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd

# ========== INÍCIO LAYOUT SIDEBAR ========== #

src = {'img_home': 'static\img_home.png',
       'img_house': 'static\img_house.png',
       'img_man': 'static\img_man.png',
       'img_money_bank': 'static\img_money_bank.png',
       'img_money_down': 'static\img_money_down.png',
       'img_money_up': 'static\img_money_up.png',
       'img_plus': 'static\img_plus.png',
       'img_woman': 'static\img_woman.png',
       'img_woman2': 'static\img_woman2.png'       
       }

# ========== Definindo layout coluna lateral ========== #
layout = dbc.Col([
    html.H1("Minhas Finanças", className="text-primary"),
    html.P("By Marcio Jr", className="text-info"),
    html.Hr(),

# ========== Seleção de Perfil ========== #
    dbc.Button(id='botao_avatar',
               children=[html.Img(src=src['img_man'], id='avatar_change', alt='Avatar', style={'margin-left': 'auto', 'margin-right': 'auto', 'width': '150px', 'background-color': 'rgba(0, 0, 0, 0)',})],
               style={'backgroundColor': 'transparent', 'borderColor': 'transparent'}
               ),
    
# ========== Criação dos botões ========== #
    dbc.Row([
        
        dbc.Col([
            dbc.Button(color='success', id='open-novo-receita', children=['Receita'])
        ], width=6),
        
        dbc.Col([
            dbc.Button(color='danger', id='open-novo-despesa', children=['Despesa'])
        ], width=6)
    ]
    ),

# ========== Seção de navegação ========== #
    html.Hr(),
    
    dbc.Nav(
        [
        dbc.NavLink("Dashboard", href="/dashboards", active="exact"),
        dbc.NavLink("Extratos", href="/extracts", active="exact")
    ], vertical=True, pills=True, id='nav_buttons', style={"margin-bottom": "50px"})

], id='sidebar_completa')

# ========== FIM LAYOUT SIDEBAR ========== #

# =========  CALLBACKS  =========== #

