import dash_core_components as dcc
import dash_html_components as html
from dash import Dash

import plotly.graph_objs as go

import random as r

q = lambda i: r.randint(0,i)

a = [[q(10001) for i in range(1000)] for j in range(10)]
b = [[i-10001*2 for i in j] for j in a]
c = [[i+10001*2 for i in j] for j in a]

z=[go.Surface(z=a),
   go.Surface(z=b,showscale=False,opacity=0.9),
   go.Surface(z=c,showscale=False,opacity=0.3)]
layout= go.Layout(title="Surface",xaxis=dict(title="X"),yaxis=dict(title="Y"),hovermode="closest")

app=Dash()

app.layout = html.Div([
    dcc.Graph(id="Surface",figure=dict(data=z,layout=layout))
])
if __name__ == "__main__":
    app.run_server()