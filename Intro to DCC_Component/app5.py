#Import packages 
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import seaborn as sns
import plotly.express as px

# Create an instance of the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

box_style = {
    "height": "100%",
    "borderRadius": "0px",
    "padding": "10px",
    "color": "black",
    "fontSize": "20px",
    "display": "flex",
    "justifyContent": "center",
    "alignItems": "center",
    "border": "2px solid black",
    "backgroundColor": "white"
}

#Layout

app.layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col([html.H1("Dashboard Title", style={"backgroundColor": "lightblue", "textAlign": "center"})], width=12)
        ]),
        dbc.Row([
            dbc.Col("Chart 1", style={**box_style, "height": "260px"}, width=6),
            dbc.Col("Chart 2", style={**box_style, "height": "260px"}, width=6)
        ], className="mb-4"),
        dbc.Row([
            dbc.Col("Chart 3", style={**box_style, "height": "160px"}, width=4),
            dbc.Col([], width=4),
            dbc.Col([], width=4)
        ])
    ],
    fluid=True  # stretch the container to full width of the screen
)
#Run the app
if __name__ == "__main__":
    app.run(debug=True, port=8003)