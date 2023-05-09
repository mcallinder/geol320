import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

app.layout = html.Div([
    dbc.NavbarSimple(
        children=[
            html.Div([
                html.Div([
                    dcc.Link(
                        f"{page['name']}", href=page["relative_path"], style={'textDecoration': 'none', 'color': 'white'}
                    )
                ], style={'paddingLeft': '20px', 'display': 'inline-block'})
                for page in dash.page_registry.values()
            ]),
        ],
        brand="GEOL 320 / 330 App",
        brand_href="/",
        color="dark",
        dark=True,
    ),
    dbc.Row([
        dbc.Col(md=1, lg=1),
        dbc.Col([
            html.Br(),
            dash.page_container
        ], md=10, lg=10)
    ])
])


if __name__ == '__main__':
    app.run_server(debug=True)
