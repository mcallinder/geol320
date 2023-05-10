from constants import co2_data1, co2_data2, colors, uhslc_list, psmsl_list
from dash import callback, dcc, html, Input, Output, register_page
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import statsmodels.api as sm

# CO2 Concentration data and figure
co2_df1 = pd.read_csv(co2_data1, skiprows=61, nrows=781, usecols=[3, 8])
co2_df2 = pd.read_csv(co2_data2, skiprows=55, usecols=[2, 3])
co2_df1.columns = ["Date", "CO2"]
co2_df2.columns = ["Date", "AVG"]
co2_fig = go.Figure()
co2_fig.add_trace(go.Scatter(x=co2_df1['Date'], y=co2_df1['CO2'], mode='lines', name='Mauna Loa CO2 Record'))
co2_fig.add_trace(go.Scatter(x=co2_df2['Date'], y=co2_df2['AVG'], mode='lines', name='Globally averaged marine surface'))
co2_fig.update_layout(title='Monthly CO2 Concentration', title_x = 0.5, xaxis_title='Date', yaxis_title='CO2 in ppm')

headers = ["year", "month", "day", "level"]
uhslc_dfs = []
for uhslc_station in uhslc_list:
    uhslc_df = pd.read_csv(uhslc_station[2], names=headers, na_values=-32767)
    uhslc_df['location'] = uhslc_station[1]
    uhslc_df['latitude'] = uhslc_station[3][0]
    uhslc_df['longitude'] = uhslc_station[3][1]
    uhslc_dfs.append(uhslc_df)
uhslc_df = pd.concat(uhslc_dfs, ignore_index=True)
uhslc_df['date'] = pd.to_datetime(uhslc_df[['year', 'month', 'day']])

psmsl_dfs = []
for psmsl_station in psmsl_list:
    psmsl_df = pd.read_csv(psmsl_station[2], sep=';', usecols=[0, 1], names=['year', 'level'], na_values=-99999)
    psmsl_df['location'] = psmsl_station[1]
    psmsl_df['latitude'] = psmsl_station[4][0]
    psmsl_df['longitude'] = psmsl_station[4][1]
    psmsl_dfs.append(psmsl_df)
psmsl_df = pd.concat(psmsl_dfs, ignore_index=True)

psmsl_dfs_an = []
for psmsl_station in psmsl_list:
    psmsl_df_an = pd.read_csv(psmsl_station[3], sep=';', usecols=[0, 1], names=['year', 'level'], na_values=-99999)
    psmsl_df_an['location'] = psmsl_station[1]
    psmsl_df_an['latitude'] = psmsl_station[4][0]
    psmsl_df_an['longitude'] = psmsl_station[4][1]
    psmsl_dfs_an.append(psmsl_df_an)
psmsl_df_an = pd.concat(psmsl_dfs_an, ignore_index=True)

register_page(__name__, path='/', name='Home')

layout = html.Div([
    html.H3('Data Dashboard'),
    html.Br(),
    dbc.Tabs([
        dbc.Tab([
            html.Br(),
            html.Br(),
            dbc.Row([
                dbc.Col(md=1, lg=1),
                dbc.Col([
                    dcc.Dropdown(id='station', multi=True, options=[{'label': location, 'value': location}
                                                                    for location in psmsl_df['location'].unique()], value=['San Francisco']),
                ], lg=6),
                dbc.Col([
                    dcc.Slider(id='year_slider', value=1980, min=1860, max=2022, step=5, marks=None, tooltip={"placement": "bottom", "always_visible": True})
                ], lg=4)
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    dcc.RadioItems([
                        {'label': html.Div(['Annual'],
                                           style={'margin-right': '20px'}),
                         'value': False},

                        {'label': html.Div(['Monthly'],
                                           style={'margin-right': '20px'}),
                         'value': True}

                    ], id='is_monthly', value=False, inline=True, style={}),
                ], lg=2),
                dbc.Col([
                    dcc.RadioItems([
                        {'label': html.Div(['Line'],
                                           style={'margin-right': '20px'}),
                         'value': 'lines'},

                        {'label': html.Div(['Scatter'],
                                           style={'margin-right': '20px'}),
                         'value': 'markers'}

                    ], id='mode', value='lines', inline=True, style={}),
                ], lg=2),
                dbc.Col([
                    dcc.RadioItems([
                        {'label': html.Div(['None'],
                                           style={'margin-right': '20px'}),
                         'value': 'none'},

                        {'label': html.Div(['OLS'],
                                           style={'margin-right': '20px'}),
                         'value': 'ols'},

                        {'label': html.Div(['Lowess'],
                                           style={'margin-right': '20px'}),
                         'value': 'lowess'}

                    ], id='trendline', value='none', inline=True, style={}),
                ], lg=2),
                dbc.Col([
                    dcc.RadioItems([
                        {'label': html.Div(['Trace'],
                                           style={'margin-right': '20px'}),
                         'value': 'trace'},

                        {'label': html.Div(['Overall'],
                                           style={'margin-right': '20px'}),
                         'value': 'overall'}

                    ], id='scope', value='trace', inline=True, style={}),
                ], lg=2)
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=1, lg=1),
                dbc.Col([
                    dcc.Graph(id='psmsl')
                ], md=10, lg=10)
            ]),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='location')
                ], md=6, lg=6),
                dbc.Col([
                    dcc.Graph(id='rate')
                ], md=6, lg=6)
            ])
        ], label='PSMSL Tide Gauge'),
        dbc.Tab([
            html.Br(),
            html.Br(),
            dbc.Row([
                dbc.Col(md=1, lg=1),
                dbc.Col([
                    dcc.Graph(id='uhslc_daily')
                ], md=10, lg=10)
            ]),
            dbc.Row([
                dbc.Col(md=4, lg=4),
                dbc.Col([
                    dcc.Dropdown(id='uhslc_station',
                                 options=[{'label': location, 'value': location} for location in
                                          uhslc_df['location'].unique()], value='San Francisco'),
                ], md=4, lg=4)
            ])
        ], label='UHSLC Daily Tide Gauge'),
        dbc.Tab([
            html.Br(),
            html.Br(),
            dcc.Graph(figure=co2_fig)
        ], label='CO2 Concentration'),

    ])
])


@callback(
    Output('psmsl', 'figure'),
    Input('station', 'value'),
    Input('year_slider', 'value'),
    Input('is_monthly', 'value'),
    Input('mode', 'value'),
    Input('trendline', 'value'),
    Input('scope', 'value'),
    suppress_callback_exceptions=True
)
def psmsl(locations, year, is_monthly, mode, trendline, scope):
    if is_monthly:
        df = psmsl_df.loc[psmsl_df['location'].isin(locations)]
    else:
        df = psmsl_df_an.loc[psmsl_df_an['location'].isin(locations)]
    df = df[df.year >= year]
    if trendline == 'none':
        fig = px.scatter(df, x="year", y="level", color="location", title=f'Annual Mean Tide, Overall Trend Since {year}', color_discrete_map=colors)
    else:
        fig = px.scatter(df, x="year", y="level", color="location", title=f'Annual Mean Tide, Overall Trend Since {year}',trendline=trendline, trendline_scope=scope, color_discrete_map=colors)
    if mode == 'lines':
        fig.update_traces(mode=mode)
        if trendline != 'none':
            fig.data[len(locations)].update(mode='lines')
    fig.update_layout(xaxis_title="Year", yaxis_title="Tide Level above RLR in mm", legend_title="Location",title_x = 0.5)
    fig.update_xaxes(showline=True, linewidth=.5, linecolor='black', mirror=True)
    fig.update_yaxes(showline=True, linewidth=.5, linecolor='black', mirror=True)
    return fig


@callback(
    Output('location', 'figure'),
    Input('station', 'value'),
    suppress_callback_exceptions=True
)
def station_location(locations):
    # https://plotly.com/python/reference/layout/geo/
    # https://plotly.com/python/reference/layout/
    # https://plotly.com/python/reference/scattergeo/

    fig = go.Figure(go.Scattergeo())
    fig.update_geos(lataxis_range=[32, 42], lonaxis_range=[-130, -112], resolution=50, scope='north america',
                    subunitcolor="Black", subunitwidth=0.2)
    fig.update_layout(title_text='Location of Tide Gauge Station', title_x=0.5)
    if locations:
        df = psmsl_df[psmsl_df['location'].isin(locations)]
        df = df[['location', 'latitude', 'longitude']].drop_duplicates()
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
            marker_color=colors[location],
            hoverinfo="skip"
            ))
    return fig


@callback(
    Output('uhslc_daily', 'figure'),
    Input('uhslc_station', 'value')
)
def uhslc_daily(location):
    if location is None:
        raise PreventUpdate
    df = uhslc_df.loc[uhslc_df['location'] == location]
    # https://plotly.com/python/reference/layout/
    # https://plotly.com/python/reference/scatter/
    fig = go.Figure(go.Scatter(x=df['date'], y=df['level'], mode='lines', marker_color=colors[location]))
    fig.update_layout(title_text='University of Hawaii Sea Level Center (UHSLC) Daily Tide Gauge',
                      title_x=0.5,
                      xaxis_title='Year',
                      yaxis_title='Tide Level above Datum in mm')
    fig.update_xaxes(showline=True, linewidth=.5, linecolor='black', mirror=True)
    fig.update_yaxes(showline=True, linewidth=.5, linecolor='black', mirror=True)
    return fig


@callback(
    Output('rate', 'figure'),
    Input('is_monthly', 'value'),
    Input('station', 'value'),
    suppress_callback_exceptions=True
)
def psmsl_rate(is_monthly, locations):
    rates_df = pd.DataFrame(columns=['location', 'rate'])
    for location in locations:
        if is_monthly:
            df = psmsl_df.loc[psmsl_df['location'] == location].dropna()
        else:
            df = psmsl_df_an.loc[psmsl_df_an['location'] == location].dropna()
        Y = df['level']
        X = sm.add_constant(df['year'])
        model = sm.OLS(Y, X)
        results = model.fit()
        print([location, results.params[1]])
        rates_df.loc[len(rates_df.index)] = [location, results.params[1]]
    fig = px.bar(rates_df, x="location", y="rate", color="location", color_discrete_map=colors, title="Rate of Sea-level Rise")
    fig.update(layout_showlegend=False)
    fig.update_layout(yaxis_title="Rate in mm per year", xaxis_title="", title_x=0.5)
    fig.update_xaxes(showline=True, linewidth=.5, linecolor='black', mirror=True)
    fig.update_yaxes(showline=True, linewidth=.5, linecolor='black', mirror=True)
    return fig
