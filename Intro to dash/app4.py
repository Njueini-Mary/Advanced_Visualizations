from dash import Dash ,html 
import dash_bootstrap_components as dbc  


# Create an instance of the app

app = Dash(__name__, 
           external_stylesheets=[dbc.themes.BOOTSTRAP]
           )



BOX_STYLE = {
    
    "height":"100%",
    "borderRadius":"20px",
    "padding":"10px",
    "color":"white",
    "fontSize":"20px",
    "display":"flex",
    "justifyContent":"center",
    "alignItems":"center"
    
}


# Create a Layout

app.layout = dbc.Container([
    
    
    
    dbc.Row([
        
        
        dbc.Col([
            
            html.Div("Navigation Bar",style={**BOX_STYLE,"backgroundColor":"#47699F","height":"70px"})
            
              ],)
        ],className="mb-4"),
    
    
    
    dbc.Row([
        
        
        dbc.Col([
            
            html.Div('INPUT PANEL',style={**BOX_STYLE,"backgroundColor":"#3B82F6","height":"300px"})
            
            
            ],width=4),
        dbc.Col([
            
            
           html.Div('MAIN CHART AREA',style={**BOX_STYLE,"backgroundColor":"#3B82F6","height":"300px"})

            
        
            ],width=8),
        
        
        ],className="mb-4"),
    
    dbc.Row([
        
        dbc.Col([
            
            html.Div('CHART 1',style={**BOX_STYLE,"backgroundColor":"#3ECE92","height":"250px"})
            
            
            
            ],width=4),
        
        
        dbc.Col([
            
            
            html.Div('CHART 2',style={**BOX_STYLE,"backgroundColor":"#497653","height":"250px"})
            
            
            ],width=4),
        
        
        dbc.Col([
            
            
            html.Div('CHART 3',style={**BOX_STYLE,"backgroundColor":"#879235","height":"250px"})
            
            
            
            ],width=4)
        
         
        
    ],className="mb-4")
    





],fluid=True,style={
    "backgroundColor":"#EAE5E4",
    "padding":"40px",
    "minHeight":"100vh"
    
})



if __name__==  "__main__":
    app.run(debug=True,port=8002)