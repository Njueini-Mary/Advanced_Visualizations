#Import packages 
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc


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
            dbc.col([
                dbc.card([
                    dbc.cardbody([
                        html.label("Filters"),
                        dcc.Dropdown(
                            options=[
                                {"label": "Option 1", "value": "1"},
                                {"label": "Option 2", "value": "2"},
                                {"label": "Option 3", "value": "3"}
                            ],
                            value="1"
                        )
                    ])
                ])
            ])
        ])
    ]
)

if __name__ == "__main__":
    app.run(debug=True, port=8003)