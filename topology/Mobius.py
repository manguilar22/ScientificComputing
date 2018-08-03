import dash_core_components as dcc
import dash_html_components as html
from dash import Dash

import plotly.graph_objs as go
import plotly.figure_factory as FF
import numpy as np
from scipy.spatial import Delaunay

u= np.linspace(0,2*np.pi,100)
v= np.linspace(-1,8,8)
u,v= np.meshgrid(u,v)
u=u.flatten()
v=v.flatten()

tp=1+0.5*v*np.cos(u/2.0)
x=tp*np.cos(u)
y=tp*np.sin(u)
z=0.5*v*np.sin(u/2.0)
points2D=np.vstack([u,v]).T
tri = Delaunay(points2D)
simplices=tri.simplices

fig=FF.create_trisurf(x=x,y=y,z=z,simplices=simplices,colormap="Portland",title="Mobius Strip")
layout=go.Layout(title="Mobius Strip")

app = Dash()

app.layout = html.Div(children=[
    dcc.Graph(id="strip",figure=dict(data=fig))
])

if __name__ == "__main__":
    app.run_server()
