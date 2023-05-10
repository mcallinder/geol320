from constants import co2_data1, co2_data2, colors, config, uhslc_list, psmsl_list
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
co2_fig.add_trace(go.Scatter(x=co2_df1['Date'], y=co2_df1['CO2'], mode='lines', name='Mauna Loa CO2 record (Scripps)'))
co2_fig.add_trace(go.Scatter(x=co2_df2['Date'], y=co2_df2['AVG'], mode='lines', name='Globally averaged marine surface (NOAA)'))
co2_fig.update_layout(title='Monthly Atmospheric CO2 Concentration', title_x=0.5, xaxis_title=None, yaxis_title='CO2 in ppm',
                      legend=dict(orientation='h', title=None, xanchor='center', x=0.5, y=-0.2))

df, dfs, headers = [], [], ["year", "month", "day", "level"]
for uhslc_station in uhslc_list:
    df = pd.read_csv(uhslc_station[2], names=headers, na_values=-32767)
    df['location'] = uhslc_station[1]
    df['latitude'] = uhslc_station[3][0]
    df['longitude'] = uhslc_station[3][1]
    dfs.append(df)
uhslc_df = pd.concat(dfs, ignore_index=True)
uhslc_df['date'] = pd.to_datetime(uhslc_df[['year', 'month', 'day']])

dfs.clear()
for psmsl_station in psmsl_list:
    df = pd.read_csv(psmsl_station[2], sep=';', usecols=[0, 1], names=['year', 'level'], na_values=-99999)
    df['location'] = psmsl_station[1]
    df['latitude'] = psmsl_station[4][0]
    df['longitude'] = psmsl_station[4][1]
    dfs.append(df)
psmsl_mon_df = pd.concat(dfs, ignore_index=True)

dfs.clear()
for psmsl_station in psmsl_list:
    df = pd.read_csv(psmsl_station[3], sep=';', usecols=[0, 1], names=['year', 'level'], na_values=-99999)
    df['location'] = psmsl_station[1]
    df['latitude'] = psmsl_station[4][0]
    df['longitude'] = psmsl_station[4][1]
    dfs.append(df)
psmsl_ann_df = pd.concat(dfs, ignore_index=True)

register_page(__name__, path='/', name='Home')

layout = html.Div([
    html.H3('Data Dashboard'),
    html.Br(),
    dbc.Tabs([
        dbc.Tab([
            dbc.Card([
                dbc.CardHeader([
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            html.P('Station Location:'),
                            dcc.Dropdown(id='station-dropdown', multi=True,
                                         options=[{'label': location, 'value': location} for location in psmsl_mon_df['location'].unique()],
                                         value=['San Francisco']),
                        ]),
                        dbc.Col([
                            html.P('Year Range:'),
                            dcc.RangeSlider(id='year-range-slider', value=[1980, 2023], min=1855, max=2023, step=1,
                                            marks={1860: '1860', 1880: '1880', 1900: '1900', 1920: '1920', 1940: '1940',
                                                   1960: '1960', 1980: '1980', 2000: '2000', 2020: '2020'},
                                            tooltip={"placement": "top", "always_visible": True})
                        ])
                    ]),
                    html.Hr(style={'margin': '20px auto', 'width': '80%'}),
                    dbc.Row([
                        dbc.Col(md=1, lg=1),
                        dbc.Col([
                            html.P('Recurrence:'),
                            dcc.RadioItems([
                                {'label': html.Div(['Annual'], style={'margin-right': '20px'}), 'value': True},
                                {'label': html.Div(['Monthly']), 'value': False}
                            ], id='recurrence-radio', value=True, inline=True, style={}),
                        ]),
                        dbc.Col([
                            html.P('Plot Type:'),
                            dcc.RadioItems([
                                {'label': html.Div(['Line'], style={'margin-right': '20px'}), 'value': 'lines'},
                                {'label': html.Div(['Scatter']), 'value': 'markers'}
                            ], id='line-mode-radio', value='lines', inline=True, style={}),
                        ]),
                        dbc.Col([
                            html.P('Trend Line Type:'),
                            dcc.RadioItems([
                                {'label': html.Div(['None'], style={'margin-right': '20px'}), 'value': 'none'},
                                {'label': html.Div(['OLS'], style={'margin-right': '20px'}), 'value': 'ols'},
                                {'label': html.Div(['Lowess']), 'value': 'lowess'}
                            ], id='trend-type-radio', value='none', inline=True, style={}),
                        ]),
                        dbc.Col([
                            html.P('Trend Line Scope:'),
                            dcc.RadioItems([
                                {'label': html.Div(['Trace'], style={'margin-right': '20px'}), 'value': 'trace'},
                                {'label': html.Div(['Overall']), 'value': 'overall'}
                            ], id='trend-scope-radio', value='trace', inline=True, style={}),
                        ])
                    ]),
                    html.Br()
                ]),
                dbc.CardBody([
                    dbc.Row(
                        dbc.Col(dcc.Graph(id='psmsl-tide-gauge-fig', config=config))
                    ),
                    dbc.Row([
                        dbc.Col(dcc.Graph(id='psmsl-station-location-fig', config=config), md=6, lg=6),
                        dbc.Col(dcc.Graph(id='psmsl-rate-fig', config=config), md=6, lg=6)
                    ])
                ]),
                dbc.CardFooter(),
            ])
        ], label='PSMSL Tide Gauge'),
        dbc.Tab([
            dbc.Card([
                dbc.CardHeader([
                    html.Br(),
                    dbc.Row([
                        dbc.Col(md=4, lg=4),
                        dbc.Col([
                            dcc.Dropdown(id='uhslc-station-dropdown',
                                         options=[{'label': location, 'value': location} for location in uhslc_df['location'].unique()],
                                         value='San Francisco')
                        ], md=4, lg=4)
                    ]),
                    html.Br()
                ]),
                dbc.CardBody(dcc.Graph(id='uhslc-tide-gauge-fig', config=config)),
                dbc.CardFooter()
            ])
        ], label='UHSLC Daily Tide Gauge'),
        dbc.Tab([
            dbc.Card([
                dbc.CardHeader(),
                dbc.CardBody(dcc.Graph(figure=co2_fig, config=config)),
                dbc.CardFooter()
            ])
        ], label='CO2 Concentration')
    ])
])


@callback(
    Output('psmsl-tide-gauge-fig', 'figure'),
    Input('station-dropdown', 'value'),
    Input('year-range-slider', 'value'),
    Input('recurrence-radio', 'value'),
    Input('line-mode-radio', 'value'),
    Input('trend-type-radio', 'value'),
    Input('trend-scope-radio', 'value'),
    suppress_callback_exceptions=True
)
def psmsl_tide_guage(locations, years, annual, line_mode, trend_type, trend_scope):
    if annual:
        df = psmsl_ann_df.loc[psmsl_ann_df['location'].isin(locations)]
    else:
        df = psmsl_mon_df.loc[psmsl_mon_df['location'].isin(locations)]

    df = df[(years[0] <= df['year']) & (df['year'] <= years[1])]

    if trend_type == 'none':
        fig = px.scatter(df, x="year", y="level", color="location", color_discrete_map=colors)
    else:
        fig = px.scatter(df, x="year", y="level", color="location", color_discrete_map=colors,
                         trendline=trend_type, trendline_scope=trend_scope)

    if line_mode == 'lines':
        fig.update_traces(mode=line_mode)
        if trend_type != 'none':
            fig.data[len(locations)].update(mode='lines')

    fig.update_layout(title=f'{"Annual" if annual else "Monthly"} Mean Tide as mm Above RLR, {years[0]}-{years[1]}',
                      title_x=0.5, title_y=0.84, xaxis_title=None, yaxis_title="mm",
                      legend=dict(orientation='h', title=None, xanchor='center', x=0.5, y=1.4))
    return fig


@callback(
    Output('psmsl-station-location-fig', 'figure'),
    Input('station-dropdown', 'value'),
    suppress_callback_exceptions=True
)
def psmsl_station_location(locations):
    fig = go.Figure(go.Scattergeo())
    fig.update_layout(title_text='Location of Tide Gauge Station', title_x=0.5, showlegend=False,
                      geo=dict(lataxis_range=[32, 42], lonaxis_range=[-130, -112], resolution=50,
                               scope='north america', subunitcolor="Black", subunitwidth=0.2))
    if locations:
        df = psmsl_mon_df[psmsl_mon_df['location'].isin(locations)]
        df = df[['location', 'latitude', 'longitude']].drop_duplicates()
        for location in locations:
            fig.add_trace(go.Scattergeo(
                hoverinfo="skip",
                lon=df.loc[df['location'] == location, 'longitude'],
                lat=df.loc[df['location'] == location, 'latitude'],
                marker=dict(size=8, color=colors[location]),
                mode='markers+text',
                text=df.loc[df['location'] == location, 'location'],
                textposition="middle left"
            ))
    return fig


@callback(
    Output('psmsl-rate-fig', 'figure'),
    Input('recurrence-radio', 'value'),
    Input('station-dropdown', 'value'),
    Input('year-range-slider', 'value'),
    suppress_callback_exceptions=True
)
def psmsl_rate(annual, locations, years):
    rates_df = pd.DataFrame(columns=['location', 'rate'])
    for location in locations:
        if annual:
            df = psmsl_ann_df.loc[psmsl_ann_df['location'] == location].dropna()
            df = df[(years[0] <= df['year']) & (df['year'] <= years[1])]
        else:
            df = psmsl_mon_df.loc[psmsl_mon_df['location'] == location].dropna()
            df = df[(years[0] <= df['year']) & (df['year'] <= years[1])]
        reg = sm.OLS(df['level'], sm.add_constant(df['year'])).fit()
        rates_df.loc[len(rates_df.index)] = [location, reg.params[1]]
    fig = px.bar(rates_df, x='location', y='rate', color='location', text='rate', text_auto='.3f', color_discrete_map=colors)
    fig.update_layout(title_text=f'Rate of Change in mm Per Year, {years[0]}-{years[1]}',
                      title_x=0.5,
                      xaxis_title=None,
                      yaxis_title='mm Per Year',
                      showlegend=False)
    return fig


@callback(
    Output('uhslc-tide-gauge-fig', 'figure'),
    Input('uhslc-station-dropdown', 'value'),
    suppress_callback_exceptions=True
)
def uhslc_tide_gauge(location):
    if location is None:
        raise PreventUpdate
    df = uhslc_df.loc[uhslc_df['location'] == location]
    fig = go.Figure(go.Scatter(x=df['date'], y=df['level'], mode='lines', marker_color=colors[location]))
    fig.update_layout(title_text=f'University of Hawaii Sea Level Center (UHSLC) Tide Gauge, Daily, {location}',
                      title_x=0.5,
                      xaxis_title=None,
                      yaxis_title='Tide Level above Datum in mm')
    return fig
