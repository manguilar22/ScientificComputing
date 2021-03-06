import dash_core_components as dcc
import dash_html_components as html
from dash import Dash

import plotly.graph_objs as go

import random as r

q = lambda i: r.randint(0,i)

a = [[q(10001) for i in range(1000)] for j in range(10)]
b = [[i-q(10001) for i in j] for j in a]
c = [[i+q(10001) for i in j] for j in a]
a,b,c = list(map(lambda e: sum(e,[]), [a,b,c])
trace00 = go.Scatter3d(x=a,y=b,z=c,mode="markers",
                       marker=dict(size=10,symbol="diamond",color="red"))
trace01 = go.Mesh3d(x=a,y=b,z=c,alphahull=10.0,color="#FFFFFF",opacity=.50)

layout = go.Layout(title="Alpha Shape")

app=Dash()

app.layout = html.Div(children=[
    dcc.Graph(id="my-graph", figure=dict(data=[trace00,trace01],layout=layout))
])

if __name__ == "__main__":
    app.run_server()
