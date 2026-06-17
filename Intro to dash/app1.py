#import dash
from dash import Dash, html

#create an instance of our app

app = Dash(__name__) # where dash() creates an instance of our app and __name__ is a special variable in Python that represents the name of the current module. When you run a Python script, __name__ is set to "__main__". This allows Dash to know where to look for resources like CSS and JavaScript files.App is the python object that represents our Dash application. We will use this object to define the layout and behavior of our app.

# define the layout of our app
app.layout = html.Div(
    [
        html.H1("My first dash app!"),
        html.P("Welcome to dash, I love Python")
    ]
)

#run my code

if __name__ == "__main__":
    app.run()