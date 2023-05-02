from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

# San Francisco Daily https://uhslc.soest.hawaii.edu/data/
data = "https://uhslc.soest.hawaii.edu/data/csv/rqds/pacific/daily/d551a.csv"
headers = ["year", "month", "day", "level"]
df = pd.read_csv(data, names=headers, na_values=-32767)

years = df.year.unique()

app = Dash(__name__)

server = app.server

app.layout = html.Div([
    html.H1(children='GEOL 320 App', style={'textAlign': 'center'}),
    dcc.Slider(
        min=years[0],
        max=years[-1],
        step=1,
        value=years[0],
        id='years',
        marks=None,
        tooltip={"placement": "bottom", "always_visible": True},
    ),
    dcc.Graph(id='graph')
])


@callback(
    Output('graph', 'figure'),
    Input('years', 'value')
)
def update_graph(value):
    dff = df[df.year == value]
    return px.scatter(dff, x='day', y='level')


if __name__ == '__main__':
    app.run_server(debug=True)
