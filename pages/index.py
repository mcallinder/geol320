from constants import co2_data1, co2_data2, colors, config, uhslc_list, psmsl_list, title
from dash import callback, dcc, html, Input, Output, register_page
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import statsmodels.api as sm

# Build CO2 Concentration DataFrame and figure
co2_df1 = pd.read_csv(co2_data1, nrows=781, skiprows=61, usecols=[3, 8])
co2_df2 = pd.read_csv(co2_data2, skiprows=55, usecols=[2, 3])
co2_df1.columns = ["Date", "CO2"]
co2_df2.columns = ["Date", "AVG"]
co2_fig = go.Figure()
co2_fig.add_trace(
    go.Scatter(
        mode='lines',
        name='Mauna Loa CO2 record (Scripps)',
        x=co2_df1['Date'],
        y=co2_df1['CO2']
    )
)
co2_fig.add_trace(
    go.Scatter(
        mode='lines',
        name='Globally averaged marine surface (NOAA)',
        x=co2_df2['Date'],
        y=co2_df2['AVG']
    )
)
co2_fig.update_layout(
    legend=dict(
        orientation='h',
        title=None,
        x=0.5,
        xanchor='center',
        y=-0.2
    ),
    title='Monthly Atmospheric CO2 Concentration',
    title_x=0.5,
    xaxis_title=None,
    yaxis_title='CO2 in ppm'
)

# Build UHSLC tide gauge daily research quality DataFrame and figure
df, dfs, headers = [], [], ["year", "month", "day", "level"]
for uhslc_station in uhslc_list:
    df = pd.read_csv(uhslc_station[2], na_values=-32767, names=headers)
    df['location'] = uhslc_station[1]
    df['latitude'] = uhslc_station[3][0]
    df['longitude'] = uhslc_station[3][1]
    dfs.append(df)
uhslc_df = pd.concat(dfs, ignore_index=True)
uhslc_df['date'] = pd.to_datetime(uhslc_df[['year', 'month', 'day']])
dfs.clear()

# Build PSMSL tide gauge monthly DataFrame and figure
for psmsl_station in psmsl_list:
    df = pd.read_csv(psmsl_station[2], na_values=-99999, names=['year', 'level'], sep=';', usecols=[0, 1])
    df['location'] = psmsl_station[1]
    df['latitude'] = psmsl_station[4][0]
    df['longitude'] = psmsl_station[4][1]
    dfs.append(df)
psmsl_mon_df = pd.concat(dfs, ignore_index=True)
dfs.clear()

# Build PSMSL tide gauge annual DataFrame and figure
for psmsl_station in psmsl_list:
    df = pd.read_csv(psmsl_station[3], na_values=-99999, names=['year', 'level'], sep=';', usecols=[0, 1])
    df['location'] = psmsl_station[1]
    df['latitude'] = psmsl_station[4][0]
    df['longitude'] = psmsl_station[4][1]
    dfs.append(df)
psmsl_ann_df = pd.concat(dfs, ignore_index=True)

# Register as home page
register_page(__name__, name='Home', path='/', title=f'{title}')

# Child container with link to data sources
reflink = dcc.Link(
    children='See references page for data source citations.',
    href='/references',
    style={'fontSize': 'small', 'marginTop': '15px', 'textDecoration': 'none'}
)

# Main layout container
layout = html.Div([
    html.H3('Data Dashboard'),
    html.Br(),
    dbc.Tabs([
        dbc.Tab([
            dbc.Card([
                dbc.CardHeader([
                    html.Br(),
                    dbc.Row([
                        html.P(
                            children='Note: The tide gauge stations represented here have data within variable ranges '
                                     'of time. Stations without data within the selected year range will not appear on '
                                     'the line or bar figures below.',
                            style={'fontStyle': 'italic'}
                        ),
                        dbc.Col([
                            html.P('Station Location:'),
                            dcc.Dropdown(
                                id='station-dropdown',
                                multi=True,
                                options=[{'label': location, 'value': location}
                                         for location in psmsl_mon_df['location'].unique()],
                                value=['San Francisco']),
                        ]),
                        dbc.Col([
                            html.P('Year Range:'),
                            dcc.RangeSlider(
                                id='year-range-slider',
                                marks={1860: '1860', 1880: '1880', 1900: '1900', 1920: '1920', 1940: '1940',
                                       1960: '1960', 1980: '1980', 2000: '2000', 2020: '2020'},
                                max=2023,
                                min=1855,
                                step=1,
                                tooltip={"placement": "top", "always_visible": True},
                                value=[1980, 2023]
                            )
                        ])
                    ]),
                    html.Hr(style={'margin': '20px auto', 'width': '80%'}),
                    dbc.Row([
                        dbc.Col(lg=1, md=1),
                        dbc.Col([
                            html.P('Recurrence:'),
                            dcc.RadioItems([
                                {'label': html.Div(['Annual'], style={'margin-right': '20px'}), 'value': True},
                                {'label': html.Div(['Monthly']), 'value': False}
                            ], id='recurrence-radio', inline=True, style={}, value=True),
                        ]),
                        dbc.Col([
                            html.P('Plot Type:'),
                            dcc.RadioItems([
                                {'label': html.Div(['Line'], style={'margin-right': '20px'}), 'value': 'lines'},
                                {'label': html.Div(['Scatter']), 'value': 'markers'}
                            ], id='line-mode-radio', inline=True, style={}, value='lines'),
                        ]),
                        dbc.Col([
                            html.P('Trend Line Type:'),
                            dcc.RadioItems([
                                {'label': html.Div(['None'], style={'margin-right': '20px'}), 'value': 'none'},
                                {'label': html.Div(['OLS'], style={'margin-right': '20px'}), 'value': 'ols'},
                                {'label': html.Div(['Lowess']), 'value': 'lowess'}
                            ], id='trend-type-radio', inline=True, style={}, value='none'),
                        ]),
                        dbc.Col([
                            html.P('Trend Line Scope:'),
                            dcc.RadioItems([
                                {'label': html.Div(['Trace'], style={'margin-right': '20px'}), 'value': 'trace'},
                                {'label': html.Div(['Overall']), 'value': 'overall'}
                            ], id='trend-scope-radio', inline=True, style={}, value='trace'),
                        ])
                    ]),
                    html.Br()
                ]),
                dbc.CardBody([
                    dbc.Row(
                        dbc.Col(
                            dcc.Graph(config=config, id='psmsl-tide-gauge-fig')
                        )
                    ),
                    dbc.Row([
                        dbc.Col(
                            dcc.Graph(config=config, id='psmsl-station-location-fig'), lg=6, md=6
                        ),
                        dbc.Col(
                            dcc.Graph(config=config, id='psmsl-rate-fig'), lg=6, md=6
                        )
                    ])
                ]),
                dbc.CardFooter(children=reflink, style={'textAlign': 'center'}),
            ])
        ], label='PSMSL Tide Gauge'),
        dbc.Tab([
            dbc.Card([
                dbc.CardHeader([
                    html.Br(),
                    dbc.Row([
                        dbc.Col(lg=4, md=4),
                        dbc.Col([
                            dcc.Dropdown(id='uhslc-station-dropdown',
                                         options=[{'label': location, 'value': location}
                                                  for location in uhslc_df['location'].unique()],
                                         value='San Francisco')
                        ], lg=4, md=4)
                    ]),
                    html.Br()
                ]),
                dbc.CardBody(
                    dcc.Graph(config=config, id='uhslc-tide-gauge-fig')
                ),
                dbc.CardFooter(children=reflink, style={'textAlign': 'center'})
            ])
        ], label='UHSLC Daily Tide Gauge'),
        dbc.Tab([
            dbc.Card([
                dbc.CardHeader(),
                dbc.CardBody(
                    dcc.Graph(config=config, figure=co2_fig)
                ),
                dbc.CardFooter(children=reflink, style={'textAlign': 'center'})
            ])
        ], label='CO2 Concentration')
    ])
])


# Callback for PSMSL tide gauge line graph functionality, returns figure based on inputs
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
    locations_with_data_in_range = df.location.unique()

    if locations_with_data_in_range.size and trend_type != 'none':
        fig = px.scatter(
            color="location",
            color_discrete_map=colors,
            data_frame=df,
            trendline=trend_type,
            trendline_scope=trend_scope,
            x="year",
            y="level"
        )
    else:
        fig = px.scatter(
            color="location",
            color_discrete_map=colors,
            data_frame=df,
            x="year",
            y="level"
        )

    if line_mode == 'lines':
        fig.update_traces(mode=line_mode)
        if trend_type != 'none' and locations_with_data_in_range.size:
            fig.data[len(locations_with_data_in_range)].update(mode='lines')

    fig.update_layout(
        legend=dict(
            orientation='h',
            title=None,
            x=0.5,
            xanchor='center',
            y=1.4),
        title=f'{"Annual" if annual else "Monthly"} Mean Tide as mm Above RLR, {years[0]}-{years[1]}',
        title_x=0.5,
        title_y=0.84,
        xaxis_title=None,
        yaxis_title="mm"
    )

    return fig


# Callback for PSMSL tide gauge location map functionality, returns figure based on inputs
@callback(
    Output('psmsl-station-location-fig', 'figure'),
    Input('station-dropdown', 'value'),
    suppress_callback_exceptions=True
)
def psmsl_station_location(locations):
    fig = go.Figure(
        go.Scattergeo()
    )
    fig.update_layout(
        geo=dict(
            lataxis_range=[32, 42],
            lonaxis_range=[-130, -112],
            resolution=50,
            scope='north america',
            subunitcolor="Black",
            subunitwidth=0.2
        ),
        showlegend=False,
        title_text='Location of Tide Gauge Station',
        title_x=0.5
    )

    if locations:
        df = psmsl_mon_df[psmsl_mon_df['location'].isin(locations)]
        df = df[['location', 'latitude', 'longitude']].drop_duplicates()

        for location in locations:
            fig.add_trace(
                go.Scattergeo(
                    hoverinfo="skip",
                    lat=df.loc[df['location'] == location, 'latitude'],
                    lon=df.loc[df['location'] == location, 'longitude'],
                    marker=dict(
                        color=colors[location],
                        size=8
                    ),
                    mode='markers+text',
                    text=df.loc[df['location'] == location, 'location'],
                    textposition="middle left"
                )
            )

    return fig


# Callback for PSMSL sea-level change rate bar graph functionality, returns figure based on inputs
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
        else:
            df = psmsl_mon_df.loc[psmsl_mon_df['location'] == location].dropna()

        df = df[(years[0] <= df['year']) & (df['year'] <= years[1])]

        if not df.empty:
            reg = sm.OLS(df['level'], sm.add_constant(df['year'])).fit()
            rates_df.loc[len(rates_df.index)] = [location, reg.params[1]]

    fig = px.bar(
        color='location',
        color_discrete_map=colors,
        data_frame=rates_df,
        text='rate',
        text_auto='.3f',
        x='location',
        y='rate'
    )
    fig.update_layout(
        showlegend=False,
        title_text=f'Rate of Change in mm Per Year, {years[0]}-{years[1]}',
        title_x=0.5,
        xaxis_title=None,
        yaxis_title='mm Per Year'
    )

    return fig


# Callback for UHSLC tide gauge line graph functionality, returns figure based on inputs
@callback(
    Output('uhslc-tide-gauge-fig', 'figure'),
    Input('uhslc-station-dropdown', 'value'),
    suppress_callback_exceptions=True
)
def uhslc_tide_gauge(location):
    if location is None:
        raise PreventUpdate

    df = uhslc_df.loc[uhslc_df['location'] == location]

    fig = go.Figure(
        go.Scatter(
            marker_color=colors[location],
            mode='lines',
            x=df['date'],
            y=df['level']
        )
    )
    fig.update_layout(
        title_text=f'University of Hawaii Sea Level Center (UHSLC) Tide Gauge, Daily, {location}',
        title_x=0.5,
        xaxis_title=None,
        yaxis_title='Tide Level above Datum in mm'
    )

    return fig
