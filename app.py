import data
from dash import Dash, html, dcc, Output, Input
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from dash.exceptions import PreventUpdate

# Header styles
h1_style = {'textAlign': 'center'}
h2_style = {'textAlign': 'left'}

# CO2 Concentration data and figure
co2_df1 = pd.read_csv(data.co2_data1, skiprows=61, nrows=781, usecols=[3, 8])
co2_df2 = pd.read_csv(data.co2_data2, skiprows=55, usecols=[2, 3])
co2_df1.columns = ["Date", "CO2"]
co2_df2.columns = ["Date", "AVG"]
co2_fig = go.Figure()
co2_fig.add_trace(go.Scatter(x=co2_df1['Date'], y=co2_df1['CO2'], mode='lines', name='Mauna Loa CO2 Record'))
co2_fig.add_trace(go.Scatter(x=co2_df2['Date'], y=co2_df2['AVG'], mode='lines', name='Globally averaged marine surface'))
co2_fig.update_layout(title='Monthly CO2 Concentration', xaxis_title='Date', yaxis_title='CO2 in ppm')

headers = ["year", "month", "day", "level"]
uhslc_dfs = []
for uhslc_station in data.uhslc_list:
    uhslc_df = pd.read_csv(uhslc_station[2], names=headers, na_values=-32767)
    uhslc_df['location'] = uhslc_station[1]
    uhslc_df['latitude'] = uhslc_station[3][0]
    uhslc_df['longitude'] = uhslc_station[3][1]
    uhslc_dfs.append(uhslc_df)
uhslc_df = pd.concat(uhslc_dfs, ignore_index=True)
uhslc_df['date'] = pd.to_datetime(uhslc_df[['year', 'month', 'day']])

psmsl_dfs = []
for psmsl_station in data.psmsl_list:
    psmsl_df = pd.read_csv(psmsl_station[2], sep=';', usecols=[0, 1], names=['year', 'level'], na_values=-99999)
    psmsl_df['location'] = psmsl_station[1]
    psmsl_df['latitude'] = psmsl_station[4][0]
    psmsl_df['longitude'] = psmsl_station[4][1]
    psmsl_dfs.append(psmsl_df)
psmsl_df = pd.concat(psmsl_dfs, ignore_index=True)

psmsl_dfs_an = []
for psmsl_station in data.psmsl_list:
    psmsl_df_an = pd.read_csv(psmsl_station[3], sep=';', usecols=[0, 1], names=['year', 'level'], na_values=-99999)
    psmsl_df_an['location'] = psmsl_station[1]
    psmsl_df_an['latitude'] = psmsl_station[4][0]
    psmsl_df_an['longitude'] = psmsl_station[4][1]
    psmsl_dfs_an.append(psmsl_df_an)
psmsl_df_an = pd.concat(psmsl_dfs_an, ignore_index=True)

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

app.layout = html.Div([
    html.H1('GEOL 320 App', style=h1_style),
    html.Br(),
    dbc.Row([
        dbc.Col(md=0, lg=1),
        dbc.Col([
            dbc.Tabs([
                dbc.Tab([
                    html.Br(),
                    html.H2('Tide Gauge', style=h2_style),
                    html.Br(),
                    dbc.Row([
                        dbc.Col(md=1, lg=1),
                        dbc.Col([
                            dcc.Dropdown(id='station', multi=True, options=[{'label': location, 'value': location} for location in psmsl_df['location'].unique()],value=['San Francisco']),
                        ], lg=6),
                        dbc.Col([
                            dcc.Slider(id='year_slider', value=1980, min=1860, max=2022, step=5, marks=None, tooltip={"placement": "bottom", "always_visible": True})
                        ], lg=4)
                    ]),
                    html.Br(),
                    dbc.Row([
                        dbc.Col(md=1, lg=1),
                        dbc.Col([
                            dcc.RadioItems([
                                {'label': html.Div(['Monthly'],
                                                   style={'margin-right': '20px', 'display': 'inline-block'}),
                                 'value': True},

                                {'label': html.Div(['Annually'],
                                                   style={'margin-right': '20px', 'display': 'inline-block'}),
                                 'value': False}

                            ], id='is_monthly', value=True, inline=True, style={}),
                        ], lg=3),
                        dbc.Col([
                            dcc.RadioItems([
                                {'label': html.Div(['Line'],
                                                   style={'margin-right': '20px', 'display': 'inline-block'}),
                                 'value': 'lines'},

                                {'label': html.Div(['Scatter'],
                                                   style={'margin-right': '20px', 'display': 'inline-block'}),
                                 'value': 'markers'}

                            ], id='mode', value='lines', inline=True, style={}),
                        ], lg=2),
                        dbc.Col([
                            dcc.RadioItems([
                                {'label': html.Div(['OLS'],
                                                   style={'margin-right': '20px', 'display': 'inline-block'}),
                                 'value': 'ols'},

                                {'label': html.Div(['Lowess'],
                                                   style={'margin-right': '20px', 'display': 'inline-block'}),
                                 'value': 'lowess'}

                            ], id='trendline', value='ols', inline=True, style={}),
                        ], lg=2),
                        dbc.Col([
                            dcc.RadioItems([
                                {'label': html.Div(['Trace'],
                                                   style={'margin-right': '20px', 'display': 'inline-block'}),
                                 'value': 'trace'},

                                {'label': html.Div(['Overall'],
                                                   style={'margin-right': '20px', 'display': 'inline-block'}),
                                 'value': 'overall'}

                            ], id='scope', value='trace', inline=True, style={}),
                        ], lg=2)
                    ]),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id='location')
                        ], lg=6),
                        dbc.Col([
                            dcc.Graph(id='psmsl')
                        ], lg=6)
                    ])
                ], label='Tide Gauge'),
                dbc.Tab([
                    html.Br(),
                    html.H2('CO2 Concentration', style=h2_style),
                    html.Br(),
                    dcc.Graph(figure=co2_fig)
                ], label='CO2 Concentration'), dbc.Tab([
                    html.Br(),
                    html.H2('About', style=h2_style)
                ], label='About')
            ])
        ], md=12, lg=10)
    ])
])


@app.callback(
    Output('psmsl', 'figure'),
    Input('station', 'value'),
    Input('year_slider', 'value'),
    Input('is_monthly', 'value'),
    Input('mode', 'value'),
    Input('trendline', 'value'),
    Input('scope', 'value')
)
def psmsl(locations, year, is_monthly, mode, trendline, scope):

    if is_monthly:
        df = psmsl_df.loc[psmsl_df['location'].isin(locations)]
    else:
        df = psmsl_df_an.loc[psmsl_df_an['location'].isin(locations)]

    df = df[df.year >= year]
    fig = px.scatter(df, x="year", y="level", color="location", title=f'Annual Mean Tide, Overall Trend Since {year}',
               trendline=trendline, trendline_scope=scope, color_discrete_map=data.colors)
    if mode == 'lines':
        fig.update_traces(mode=mode)
        fig.data[len(locations)].update(mode='lines')
    fig.update_layout(xaxis_title="Year", yaxis_title="Tide Level above RLR in mm", legend_title="Location")
    return fig


# @app.callback(
#     Output('uhslc_daily', 'figure'),
#     Input('uhslc_station', 'value')
# )
# def uhslc_daily(locations):
#     fig = go.Figure()
#     # https://plotly.com/python/reference/layout/
#     fig.update_layout(title_text='Daily Tide Gauge', xaxis_title='Date', yaxis_title='Tide Level above Datum in mm', showlegend=True)
#     fig.update_xaxes(showline=True, linewidth=.5, linecolor='black', mirror=True)
#     fig.update_yaxes(showline=True, linewidth=.5, linecolor='black', mirror=True)
#     if locations:
#         for location in locations:
#             df = uhslc_df.loc[uhslc_df['location'] == location]
#             # https://plotly.com/python/reference/scatter/
#             fig.add_trace(go.Scatter(x=df['date'], y=df['level'], mode='lines', name=location, marker_color=data.colors[location]))
#     return fig


@app.callback(
    Output('location', 'figure'),
    Input('station', 'value')
)
def station_location(locations):
    fig = go.Figure(go.Scattergeo())

    # https://plotly.com/python/reference/layout/geo/
    fig.update_geos(lataxis_range=[32, 42], lonaxis_range=[-130, -112], resolution=50, scope='north america',
                    subunitcolor="Black", subunitwidth=0.2)

    # https://plotly.com/python/reference/layout/
    fig.update_layout(title_text='Location of Tide Gauge Station')

    if locations:
        df = psmsl_df[psmsl_df['location'].isin(locations)]
        df = df[['location', 'latitude', 'longitude']].drop_duplicates()
        # https://plotly.com/python/reference/scattergeo/

        for location in locations:
            fig.add_trace(go.Scattergeo(
            lon=df.loc[df['location'] == location, 'longitude'],
            lat=df.loc[df['location'] == location, 'latitude'],
            text=df.loc[df['location'] == location, 'location'],
            textposition="middle left",
            mode='markers+text',
            marker_size=8,
            showlegend=False,
            name=location,
            marker_color=data.colors[location],
            hoverinfo="skip"
            ))
    return fig


if __name__ == '__main__':
    app.run_server()
