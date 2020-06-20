import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input,Output
from request_data import Data


filename = 'coviddata.pkl'
dataclass = Data()

external_stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
tickFont = {'size':10, 'color':"rgb(30,30,30)",'family':"Courier New, monospace"}

def load_global():
    data = {'state':None, 'District':None, 'Confirmed':dataclass.get_country_data()['totalconfirmed'],'Deaths':dataclass.get_country_data()['totaldeceased'],'Recovered':dataclass.get_country_data()['totalrecovered']}
    data = pd.DataFrame(data)
    '''
    when it is global all dropdowns must be <ALL> and teh entire should be shown in graph 1
    '''
    data['state'] = '<ALL>'
    data['District'] = '<ALL>'
    print(data)
    return data

load_global()

def load_states():
    pass


def load_district():
    pass


app = dash.Dash(__name__,external_stylesheets = external_stylesheet)



app.index_string = """<!DOCTYPE html>
<html>
    <head>
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=UA-161733256-2"></script>
        <script>
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());
          gtag('config', 'UA-161733256-2');
        </script>
        <meta name="keywords" content="COVID-19 India,Coronavirus,Dash,Python,Dashboard,Cases,Statistics">
        <title>COVID-19 Case History in India</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
       </footer>
    </body>
</html>"""

app.layout = html.Div(
    style={ 'font-family':"Courier New, monospace" },
    children=[
        html.H1('Coronavirus (COVID-19) cases in India'),
        html.Div(className="row", children=[
            html.Div(className="three columns", children=[
                html.H5('Country'),
                html.H4('India')
            ]),
            html.Div(className="three columns", children=[
                html.H5('State'),
                dcc.Dropdown(
                    id='state'
                )
            ]),
            html.Div(className="three columns", children=[
                html.H5('District'),
                dcc.Dropdown(
                    id='district'
                )
            ]),
            html.Div(className="two columns", children=[
                html.H5('Selected Metrics'),
                dcc.Checklist(
                    id='metrics',
                    options=[{'label':m, 'value':m} for m in ['Confirmed', 'Deaths','Recovered']],
                    value=['Confirmed', 'Deaths','Recovered']
                )
            ])
        ]),
        dcc.Graph(
            id="plot_country_metrics",
            config={ 'displayModeBar': False }
        ),
        dcc.Graph(
            id="plot_state_metrics",
            config={ 'displayModeBar': False }
        ),
        dcc.Graph(
            id = "plot_state_district_metrics",
            config = {'displayModeBar' : True}
        ),
        dcc.Interval(
            id='interval-component',
            interval=3600*1000, # Refresh data each hour.
            n_intervals=0
        )
    ]
)
'''
@app.callback(
    [Output('state','options'),Output('state','value')],
    [Output('district','options'),Output('district','value')],
    [Input('country','value')]
)

def update_states(country):
    states = list(Data.statedata)

'''
if __name__ == '__main__':
    app.run_server(debug = True )
