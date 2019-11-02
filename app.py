import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import plotly.figure_factory as ff
import pandas as pd
import dash_daq as daq

########### Define a few variables ######

tabtitle = 'Dash DAQ'
sourceurl = 'https://dash.plot.ly/dash-daq'
githublink = 'https://github.com/austinlasseter/dash-daq-state'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Layout

app.layout = html.Div(children=[
    html.H1('This is the header'),


    # Footer
    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)


############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
