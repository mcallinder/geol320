from constants import title
from dash import Dash, dcc, html, page_container, page_registry
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True)

# Gunicorn server
server = app.server

# Set up navigation bar and main container for all pages
app.layout = html.Div([
    dbc.NavbarSimple([
        html.Div([
            html.Div([
                dcc.Link(
                    children=f"{page['name']}",
                    href=page["relative_path"],
                    style={'color': 'white', 'textDecoration': 'none'}
                )
            ], style={'display': 'inline-block', 'paddingLeft': '20px'}) for page in page_registry.values()
        ]),
    ], brand=title, brand_href='/', color='dark', dark=True),
    dbc.Row([
        dbc.Col(lg=1, md=1),
        dbc.Col([
            html.Br(),
            page_container
        ], lg=10, md=10)
    ]),
    html.Br()
])


if __name__ == '__main__':
    app.run_server()
