from datetime import datetime

from dash import Dash, html
import dash_bootstrap_components as dbc

#Create an instance of the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
BUILD_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@app.server.after_request
def disable_cache(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

#Create the layout of the app
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Analysis", href="#")),
        dbc.NavItem(dbc.NavLink("Data", href="#")),
        dbc.NavItem(dbc.NavLink("About", href="#")),
    ],
    brand="AI Job Replacement Dashboard",
    brand_href="#",
    color="primary",
    dark=True,
)
        )
    ]),
    dbc.Row([]),
    dbc.Row([]),
    dbc.Row([]),
    dbc.Row([]),
    dbc.Row([]),
], fluid=True)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8050,
        use_reloader=True,
        dev_tools_hot_reload=True,
        dev_tools_hot_reload_interval=1000,
        dev_tools_hot_reload_watch_interval=0.5,
    )