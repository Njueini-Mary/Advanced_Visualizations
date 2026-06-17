from dash import Dash, html
import dash_bootstrap_components as dbc


# Create an instance of the app
app = Dash(
	__name__,
	external_stylesheets=[dbc.themes.BOOTSTRAP],
)


BOX_STYLE = {
	"height": "100%",
	"borderRadius": "0px",
	"padding": "10px",
	"color": "black",
	"fontSize": "20px",
	"display": "flex",
	"justifyContent": "center",
	"alignItems": "center",
	"border": "2px solid black",
	"backgroundColor": "white",
}


# Create a layout
app.layout = dbc.Container(
	[
		html.Div(
			[
				dbc.Row(
					[
						dbc.Col(
							[
								html.Div(
									"Title",
									style={
										**BOX_STYLE,
										"height": "70px",
									},
								)
							]
						)
					],
					className="mb-4",
				),
				dbc.Row(
					[
						dbc.Col(
							[
								html.Div(
									"Chart 1",
									style={
										**BOX_STYLE,
										"height": "260px",
									},
								)
							],
							width=6,
						),
						dbc.Col(
							[
								html.Div(
									"Chart 2",
									style={
										**BOX_STYLE,
										"height": "260px",
									},
								)
							],
							width=6,
						),
					],
					className="mb-4",
				),
				dbc.Row(
					[
						dbc.Col(
							[
								html.Div(
									"Chart 3",
									style={
										**BOX_STYLE,
										"height": "160px",
									},
								)
							]
						)
					]
				),
			],
			style={
				"maxWidth": "800px",
				"margin": "0 auto",
				"border": "2px solid black",
				"borderRadius": "0px",
				"padding": "16px",
				"backgroundColor": "white",
			},
		)
	],
	fluid=True,
	style={
		"backgroundColor": "white",
		"padding": "40px",
		"minHeight": "100vh",
	},
)


if __name__ == "__main__":
	app.run(debug=True, port=8003)
