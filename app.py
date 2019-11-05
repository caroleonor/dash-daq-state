import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import plotly.figure_factory as ff
import pandas as pd
import dash_daq as daq

########### Define a few variables ######

tabtitle = 'Visitors Data'
sourceurl = 'https://dash.plot.ly/dash-daq'
sourceurl2 = 'https://dash.plot.ly/state'
githublink = 'https://github.com/caroleonor/dash-daq-state/edit/master/app.py'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

######### Define the figure

colorlist=['Magic Kingdom', 'Hollywood Studio', 'Epcot',  'Animal Kingdom ']
palette=['#F4D03F',  '#CD6155', '#85C1E9', '#73C6B6']

def make_my_cool_figure(input1, input2, drop1, drop2, knob1, knob2):
    drop1=int(drop1)
    drop2=int(drop2)
    myfavoritecolors=[palette[drop1], palette[drop2]]
    x_list=[input1, input2]
    y_list=[knob1, knob2]
    mytitle=f"Compare visiter number of {input1} and {input2}"
    mydata = [go.Bar(x=x_list,
                    y=y_list,
                    marker=dict(color=myfavoritecolors))]
    mylayout = go.Layout(
        title = mytitle,
        xaxis = dict(title = 'Attraction'),
        yaxis = dict(title = 'Visitor Number'))
    myfigure = go.Figure(data=mydata, layout=mylayout)
    return myfigure

########### Layout

app.layout = html.Div(children=[
    html.Div([
        html.H4(['Compare the attraction'], className='six columns'),
        html.Div([html.Button(id='submit-button', n_clicks=0, children='Submit')], className='six columns'),
    ], className='twelve columns'),


    html.Div([
        # Input 1
        html.Div([
            html.H6('Attraction Name and Park'),
                html.Div([
                    dcc.Input(id='input-1', type='text', value='Space Mountain'),
                    dcc.RadioItems(
                        id='drop-1',
                        options=[{'label': j, 'value': k} for j, k in zip(colorlist, range(0,4))],
                        value=2
                    ),
                ], className='four columns'),
                html.Div([
                    daq.Knob(
                          id='knob-1',
                          max=1000,
                          value=500,
                          min=0
                        ),
                ], className='two columns'),
        ], className='six columns', style={'padding': '12px','border': 'thin black solid',}),

        # Input 2
        html.Div([
            html.H6('Attraction Name and Park'),
                html.Div([
                    dcc.Input(id='input-2', type='text', value='Avatar'),
                    dcc.RadioItems(
                        id='drop-2',
                        options=[{'label': j, 'value': k} for j, k in zip(colorlist, range(0,4))],
                        value=1
                    ),
                ], className='four columns'),
                html.Div([
                    daq.Knob(
                          id='knob-2',
                          max=1000,
                          value=500,
                          min=0
                        ),
                ], className='two columns'),
        ], className='six columns', style={'padding': '12px','border': 'thin black solid',}),
    ], className='twelve columns'),


        # Output
    html.Div(
        [dcc.Graph(id='my-graph'),
        # Footer
        html.Br(),
        html.A('Code on Github', href=githublink),
        html.Br(),
        html.A("Data Source", href=sourceurl),
        html.Br(),
        html.A("Data Source", href=sourceurl2),
    ], className='twelve columns'),



    ]
)

########### Callback

@app.callback(Output('my-graph', 'figure'),
              [Input('submit-button', 'n_clicks')],
              [State('input-1', 'value'),
               State('input-2', 'value'),
               State('drop-1', 'value'),
               State('drop-2', 'value'),
               State('knob-1', 'value'),
               State('knob-2', 'value'),
               ])
def update_output(n_clicks, input1, input2, drop1, drop2, knob1, knob2):
    return make_my_cool_figure(input1, input2, drop1, drop2, knob1, knob2)

############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
