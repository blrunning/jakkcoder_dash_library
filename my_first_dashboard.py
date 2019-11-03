



#### lib required for dashboard
import plotly.graph_objects as go
import dash
import dash_html_components as html
import dash_core_components as dcc

import plotly.offline as pyo

from dash.dependencies import State, Input, Output

import numpy as np
import pandas as pd


############################################################################################################################################

## Lets create a dataFrame generating data with help of numpy

def datagen():
    my_sample_data = np.random.random_sample([100,3])
    cat_g = ["good","bad","worst"] 
    sample_Cat = [cat_g[np.random.randint(0,3)] for i in range(100)]
    Base_Data = pd.DataFrame(my_sample_data,columns=["val_1","val_2","val_3"])
    Base_Data["sample_Cat"] = sample_Cat
    
    
    
    return(Base_Data)



cat_g = ["good","bad","worst"] 



## Creating values and lables for dropdown

options_list = []
for i in cat_g:
    options_list.append({'label': i, 'value': i})
    


###############################################################################################################################################



def fig_generator(sample_data):
    sample_data = sample_data.reset_index(drop=True)
    sample_data.head()
    plot_data =[]

    for i in range(1,4):
        plot_data.append(go.Scatter(x=sample_data.index, y=sample_data['val_'+ str(i)], name = 'val_'+ str(i) ))
    plot_layout = go.Layout(title = " This plot is generated using plotly  ")

    fig = go.Figure( data = plot_data ,layout = plot_layout)

    return(fig.data,fig.layout)
        


    
### Dash board code 
    
app = dash.Dash()

### defining the HTML component


app.layout = html.Div(children=[html.Div("Welcome to the dashboard",style= {   "color": "white",
                                                      "text-align": "center","background-color": "blue",
                                                      "border-style": "dotted","display":"inline-block","width":"80%"
                                                      
                                                    }),
                       html.Div(dcc.Dropdown(id = "drop_down_1" ,options= options_list , value= 'good'
                                                       ),style= {
                                                      "color": "green",
                                                      "text-align": "center","background-color": "darkorange",
                                                      "border-style": "dotted","display":"inline-block","width":"20%"
                                                      
                                                    }),
                       html.Div(children=[html.P(
                            id="map-title",
                            children = "Forecast and validation for Facility ",
                        ), html.Div(dcc.Graph(id ="plot_area"))
                                                       ],style= {
                                                      "color": "black",
                                                      "text-align": "center","background-color": "yellow",
                                                      "border-style": "dotted","display":"inline-block","width":"75%",
                                                                                                            
                                                    })],style={"width":"100%",'paffing':10})

## Creating callback buttons

@app.callback(Output("plot_area", 'figure'),
              
              [Input("drop_down_1", "value")])

def updateplot(input_cat):
    
    df= datagen()
    sample_data = df[df["sample_Cat"] == input_cat ]
    
    trace,layout = fig_generator(sample_data)
    
    return {
        'data': trace,
        'layout':layout
    }
    
    
    
if __name__=='__main__':
    app.run_server()
	
	
###################################################################################################################################