#import dash
from dash import Dash, html

#create an instance of our app

app = Dash(__name__) # where dash() creates an instance of our app and __name__ is a special variable in Python that represents the name of the current module. When you run a Python script, __name__ is set to "__main__". This allows Dash to know where to look for resources like CSS and JavaScript files.App is the python object that represents our Dash application. We will use this object to define the layout and behavior of our app.

# define the layout of our app
app.layout = html.Div([
    html.H1("Main heading"),
    html.H2("Sub heading"),
    html.H3("Sub sub heading"),
    html.P("This is a paragraph of text"),

    html.Br(),
    html.P("This is another paragraph of text"),

    #Input and controls

    html.Button("Click me"),
    html.Br(),
    html.Textarea("This is a text area"),

    #List
    html.Ul([
        html.Li("Apples"),
        html.Li("Oranges"),
        html.Li("Bananas")
    
    ])
])

if __name__ == "__main__":
    app.run(debug=True, port=8050)