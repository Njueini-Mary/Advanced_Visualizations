#import dash
from dash import Dash, html

#create an instance of our app

app = Dash(__name__) # where dash() creates an instance of our app and __name__ is a special variable in Python that represents the name of the current module. When you run a Python script, __name__ is set to "__main__". This allows Dash to know where to look for resources like CSS and JavaScript files.App is the python object that represents our Dash application. We will use this object to define the layout and behavior of our app.

# define the layout of our app
app.layout = html.Div(
    [
       #Header section
       html.Header([
           html.H1("Company Dashboard", style={"color": "Pink"}),
           html.P("Real Time Analytics", style={"color": "Green"})
       ]),

       #Navigation section
         html.Nav([
              html.A("Home", href="#"),
              html.Span(" | "),
                html.A("Report", href="#"),
                html.Span(" | "),
                html.A("Settings", href="#")
         ]),

         #Main content section
            html.Main([
                #Section 1
                html.Section([
                    html.H2("Sales Overview"),
                    html.P("This section contains sales data and charts."),
                    html.Button("Refresh Data")
                ]),

                html.Hr(),

                #Section 2
                html.Section([
                    html.H2("Key Metrics"),
                    html.Ul([
                        html.Li("Total Sales: $1,000,000"),
                        html.Li("New Customers: 500"),
                        html.Li("Customer Satisfaction: 95%")
                    ])

                ]),

                html.Hr(),

                #Section 3





            ]),




    ]
)

#run my code

if __name__ == "__main__":
    app.run(debug=True, port=8050)