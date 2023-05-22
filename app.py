from constants import title
from dash import Dash, dcc, html, page_container, page_registry
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Gunicorn server, see gunicorn.conf.py
server = app.server

# Set up navigation bar and main container for all pages
app.layout = html.Div([
    dbc.NavbarSimple([
        html.Div([
            html.Div([
                dcc.Link(
                    f"{page['name']}",
                    href=page["relative_path"],
                    style={'textDecoration': 'none', 'color': 'white'}
                )
            ], style={'paddingLeft': '20px', 'display': 'inline-block'}) for page in page_registry.values()
        ]),
    ], brand=title, brand_href='/', color='dark', dark=True),
    dbc.Row([
        dbc.Col(md=1, lg=1),
        dbc.Col([
            html.Br(),
            page_container
        ], md=10, lg=10)
    ]),
    html.Br()
])


if __name__ == '__main__':
    app.run_server()
