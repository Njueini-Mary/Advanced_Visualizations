# Import packages

from dash import Dash, html, dcc, dash_table
import dash_bootstrap_components as dbc

import plotly.express as px


# Data

df_iris = px.data.iris()


# KPIs

total_records = len(df_iris)

species_count = df_iris['species'].nunique()

avg_petal_length = round(
    df_iris['petal_length'].mean(),
    2
)


# Charts

# Scatter Plot

fig_scatter = px.scatter(
    data_frame=df_iris,
    x='sepal_width',
    y='sepal_length',
    color='species',
    title='Sepal Width vs Sepal Length'
)


# Histogram

fig_hist = px.histogram(
    data_frame=df_iris,
    x='petal_length',
    color='species',
    title='Petal Length Distribution'
)


# Create an instance

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)


# Card Style

CARD_STYLE = {

    "color": "white",
    "padding": "15px",

}


# Layout

app.layout = dbc.Container([

    # Dashboard Title

    html.H1("Iris Analytics Dashboard"),

    html.P(
        "Simple interactive dashboard built with Dash + Bootstrap + Plotly"
    ),

    html.Br(),

    # KPI Cards

    dbc.Row([

        dbc.Col([

            dbc.Card(

                dbc.CardBody([

                    html.H4("Total Records"),

                    html.H1(total_records)

                ]),

                style={
                    **CARD_STYLE,
                    "backgroundColor": "#2E4057"
                }

            )

        ], width=4),

        dbc.Col([

            dbc.Card(

                dbc.CardBody([

                    html.H4("Species Count"),

                    html.H1(species_count)

                ]),

                style={
                    **CARD_STYLE,
                    "backgroundColor": "#40B89D"
                }

            )

        ], width=4),

        dbc.Col([

            dbc.Card(

                dbc.CardBody([

                    html.H4("Avg Petal Length"),

                    html.H1(avg_petal_length)

                ]),

                style={
                    **CARD_STYLE,
                    "backgroundColor": "#E8A11C"
                }

            )

        ], width=4)

    ]),

    html.Br(),

    # Charts

    dbc.Row([

        dbc.Col([

            dcc.Graph(
                id='scatter_chart',
                figure=fig_scatter
            )

        ], width=6),

        dbc.Col([

            dcc.Graph(
                id='hist_chart',
                figure=fig_hist
            )

        ], width=6)

    ]),

    html.Br(),

    # Dataset Preview

    html.H2("Dataset Preview"),

    dash_table.DataTable(

        data=df_iris.head(10).to_dict('records'),

        columns=[
            {
                "name": col,
                "id": col
            }
            for col in df_iris.columns
        ],

        page_size=10

    )

], fluid=True)


# Run App

if __name__ == "__main__":
    app.run(debug=True, port=8004)