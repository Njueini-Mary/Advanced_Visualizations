#122380 Njueini Mary Michelle
# 1. IMPORT LIBRARIES

from dash import Dash, html, dcc, dash_table
import dash_bootstrap_components as dbc
import seaborn as sns
import plotly.express as px

# 2. LOAD IRIS DATASET

df = sns.load_dataset("iris")

# 3. CREATE KPI VALUES

total_records = len(df)

species_count = df["species"].nunique()

avg_petal_length = round(df["petal_length"].mean(), 2)


# 4. CREATE CHARTS

# Scatter Plot

fig_scatter = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="species",
    title="Sepal Width vs Sepal Length"
)

# Histogram

fig_hist = px.histogram(
    df,
    x="petal_length",
    color="species",
    title="Petal Length Distribution"
)


# 5. CREATE DASH APP

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

# 6. CARD STYLE

CARD_STYLE = {
    "color": "white",
    "padding": "15px",
    "borderRadius": "5px"
}

# 7. LAYOUT

app.layout = dbc.Container([

    html.H1("Iris Analytics Dashboard"),

    html.P(
        "Simple interactive dashboard built with Dash + Bootstrap + Plotly"
    ),

    html.Br(),

    # KPI CARDS
   
    dbc.Row([

        dbc.Col(

            dbc.Card(
                dbc.CardBody([

                    html.H4("Total Records"),
                    html.H1(total_records)

                ]),
                style={
                    **CARD_STYLE,
                    "backgroundColor": "#2E4057"
                }
            ),

            width=4
        ),

        dbc.Col(

            dbc.Card(
                dbc.CardBody([

                    html.H4("Species Count"),
                    html.H1(species_count)

                ]),
                style={
                    **CARD_STYLE,
                    "backgroundColor": "#40B89D"
                }
            ),

            width=4
        ),

        dbc.Col(

            dbc.Card(
                dbc.CardBody([

                    html.H4("Avg Petal Length"),
                    html.H1(avg_petal_length)

                ]),
                style={
                    **CARD_STYLE,
                    "backgroundColor": "#E8A11C"
                }
            ),

            width=4
        )

    ]),

    html.Br(),
    html.Br(),

    # CHARTS

    dbc.Row([

        dbc.Col([

            dcc.Graph(
                figure=fig_scatter
            )

        ], width=6),

        dbc.Col([

            dcc.Graph(
                figure=fig_hist
            )

        ], width=6)

    ]),

    html.Br(),
# DATA TABLE
    html.H2("Dataset Preview"),

    dash_table.DataTable(

        data=df.head(10).to_dict("records"),

        columns=[
            {"name": col, "id": col}
            for col in df.columns
        ],

        page_size=10,

        style_table={
            "overflowX": "auto"
        }

    )

], fluid=True)

# 8. RUN APP

if __name__ == "__main__":
    app.run(debug=True, port=8004)