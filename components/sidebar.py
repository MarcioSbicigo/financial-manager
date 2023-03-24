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
    ]),
    
        # ========== Modal de Receitas ========== #
        dbc.Modal([
            
            dbc.ModalHeader(dbc.ModalTitle('Adicionar Receita')),
            
            dbc.ModalBody([
                dbc.Row([
                    dbc.Col([
                        dbc.Label('Descrição: '),
                        dbc.Input(placeholder="Ex.: Dividendos, Salário, etc...", id="txt-receita"),
                    ], width=6),
                    
                    dbc.Col([
                        dbc.Label('Valor: '),
                        dbc.Input(placeholder="R$ 0,00", id="valor_receita", value=""),
                    ], width=6)
                ]),
                
                dbc.Row([
                    dbc.Col([
                       dbc.Label("Data: "),
                       dcc.DatePickerSingle(id='date-receitas',
                                            min_date_allowed=date(2000, 1, 1),
                                            max_date_allowed=date(2050, 12, 31),
                                            date=datetime.today(),
                                            display_format='DD/MM/YYYY',
                                            first_day_of_week=1,
                                            style={"width": "100%"})
                    ], width=4),
                    
                    dbc.Col([
                        dbc.Label("Extras"),
                        dbc.Checklist(options=[],
                                      value=[],
                                      id='switches-input-receita',
                                      switch=True
                        )
                    ], width=4),
                    
                    dbc.Col([
                        html.Label('Categoria'),
                        dbc.Select(id='select_receita',
                                   options=[],
                                   value=[])
                    ], width=4)
                ], style={'margin-top': '25px'}),
                
                dbc.Row([
                    dbc.Accordion([
                        dbc.AccordionItem(children=[
                            dbc.Row([
                                dbc.Col([
                                    html.Legend('Adicionar categoria', style={'color': 'green'}),
                                    dbc.Input(type="text", placeholder="Nova categoria...", id='input-add-receita', value=""),
                                    html.Br(),
                                    dbc.Button("Adicionar", className="btn btn-success", id="add-category-receita", style={"margin-top": "20px"}),
                                    html.Br(),
                                    html.Div(id="category-div-add-receita", style={}),
                                ], width=6),
                                
                                dbc.Col([
                                    html.Legend('Excluir categorias', style={'color': 'red'}),
                                    dbc.Checklist(id='checklist-selected-style-receita',
                                                  options=[],
                                                  value=[],
                                                  label_checked_style={'color': 'red'},
                                                  input_checked_style={'backgroundColor': 'blue', 'borderColor': 'orange'}),
                                    dbc.Button('Remover', color='warning', id='remove-category-receita', style={'margin-top': '20px'}),
                                    
                                ], width=6)
                            ])
                        ], title='Adicionar/Remover Categorias')
                    ], flush=True, start_collapsed=True, id='accordion-receita'),
                    
                    html.Div(id='id_teste_receita', style={'padding-top': '20px'}),
                    
                    dbc.ModalFooter([
                        dbc.Button("Adicionar Receita", id='salvar_receita', color='success'),
                        dbc.Popover(dbc.PopoverBody("Receita Salva"), target="salvar_receita", placement="left", trigger="click")
                    ])
                ], style={'margint-top': '25px'})
            ])
        ],  id='modal-novo-receita',
            style={"background-color": "rgba(17, 140, 79, 0.05)"},
            size="lg",
            is_open=False,
            centered=True,
            backdrop=True),
        
        # ========== Modal de Despesas ========== #
        dbc.Modal([
            
            dbc.ModalHeader(dbc.ModalTitle('Adicionar Despesa')),
            
            dbc.ModalBody([
                dbc.Row([
                    dbc.Col([
                        dbc.Label('Descrição: '),
                        dbc.Input(placeholder="Ex.: Supermercado, Remédios, etc...", id="txt-despesa"),
                    ], width=6),
                    
                    dbc.Col([
                        dbc.Label('Valor: '),
                        dbc.Input(placeholder="R$ 0,00", id="valor_despesa", value=""),
                    ], width=6)
                ]),
                
                dbc.Row([
                    dbc.Col([
                       dbc.Label("Data: "),
                       dcc.DatePickerSingle(id='date-despesa',
                                            min_date_allowed=date(2000, 1, 1),
                                            max_date_allowed=date(2050, 12, 31),
                                            date=datetime.today(),
                                            display_format='DD/MM/YYYY',
                                            first_day_of_week=1,
                                            style={"width": "100%"})
                    ], width=4),
                    
                    dbc.Col([
                        dbc.Label("Extras"),
                        dbc.Checklist(options=[],
                                      value=[],
                                      id='switches-input-despesa',
                                      switch=True
                        )
                    ], width=4),
                    
                    dbc.Col([
                        html.Label('Categoria'),
                        dbc.Select(id='select_receita',
                                   options=[],
                                   value=[])
                    ], width=4)
                ], style={'margin-top': '25px'}),
                
                dbc.Row([
                    dbc.Accordion([
                        dbc.AccordionItem(children=[
                            dbc.Row([
                                dbc.Col([
                                    html.Legend('Adicionar categoria', style={'color': 'green'}),
                                    dbc.Input(type="text", placeholder="Nova categoria...", id='input-add-despesa', value=""),
                                    html.Br(),
                                    dbc.Button("Adicionar", className="btn btn-success", id="add-category-despesa", style={"margin-top": "20px"}),
                                    html.Br(),
                                    html.Div(id="category-div-add-despesa", style={}),
                                ], width=6),
                                
                                dbc.Col([
                                    html.Legend('Excluir categorias', style={'color': 'red'}),
                                    dbc.Checklist(id='checklist-selected-style-despesa',
                                                  options=[],
                                                  value=[],
                                                  label_checked_style={'color': 'red'},
                                                  input_checked_style={'backgroundColor': 'blue', 'borderColor': 'orange'}),
                                    dbc.Button('Remover', color='warning', id='remove-category-despesa', style={'margin-top': '20px'}),
                                    
                                ], width=6)
                            ])
                        ], title='Adicionar/Remover Categorias')
                    ], flush=True, start_collapsed=True, id='accordion-despesa'),
                    
                    html.Div(id='id_teste_despesa', style={'padding-top': '20px'}),
                    
                    dbc.ModalFooter([
                        dbc.Button("Adicionar Despesa", id='salvar_despesa', color='success'),
                        dbc.Popover(dbc.PopoverBody("Despesa Salva"), target="salvar_despesa", placement="left", trigger="click")
                    ])
                ], style={'margint-top': '25px'})
            ])
        ],  id='modal-novo-despesa',
            style={"background-color": "rgba(17, 140, 79, 0.05)"},
            size="lg",
            is_open=False,
            centered=True,
            backdrop=True),

# ========== Seção de navegação ========== #
    html.Hr(),
    
    dbc.Nav(
        [
        dbc.NavLink("Dashboard", href="/dashboards", active="exact"),
        dbc.NavLink("Extratos", href="/extratos", active="exact")
    ], vertical=True, pills=True, id='nav_buttons', style={"margin-bottom": "50px"})

], id='sidebar_completa')

# ========== FIM LAYOUT SIDEBAR ========== #

# =========  CALLBACKS  =========== #

#Pop-up de receitas
@app.callback(
    Output('modal-novo-receita', 'is_open'),
    Input('open-novo-receita', 'n_clicks'),
    State('modal-novo-receita', 'is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    
#Pop-up de despesas
@app.callback(
    Output('modal-novo-despesa', 'is_open'),
    Input('open-novo-despesa', 'n_clicks'),
    State('modal-novo-despesa', 'is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
