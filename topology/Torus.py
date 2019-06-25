import dash_core_components as dcc
import dash_html_components as html
from dash import Dash

import plotly.graph_objs as go
import plotly.figure_factory as FF
import numpy as np
from scipy.spatial import Delaunay

app = Dash()

u=np.linspace(0,2*np.pi,100)
v=np.linspace(0,2*np.pi,100)
u,v = np.meshgrid(u,v)
u = u.flatten()
v = v.flatten()

x=(3+np.cos(v))*np.cos(u)
y=(3+np.cos(v))*np.sin(u)
z=np.sin(v)

points2D=np.vstack([u,v]).T
tri=Delaunay(points2D)
simplices=tri.simplices

fig = FF.create_trisurf(x=x,y=y,z=z,simplices=simplices,
                        title="Torus",
                        colormap="Earth",
                        aspectratio=dict(x=1,y=1,z=0.3))
scatter00 = go.Scatter3d(x=x,y=y,z=z,mode="markers",name="Outline",
                         marker=dict(size=5.0,symbol="circle-open",color="black"))
scatter01=go.Scatter3d(x=x,y=y,z=z,mode="markers",name="Outline",
                        marker=dict(size=.70,symbol="square",color="red"))

mesh00 = go.Mesh3d(x=x,y=y,z=z,opacity=.1,color="orange",name="Mesh")


layout=go.Layout(title="Scatter-3D Torus",yaxis=dict(title="Y-axis"),
                 xaxis=dict(title="X-axis"),hovermode="closest",
                 plot_bgcolor="#FFFFFF",
                 paper_bgcolor="#FFFFFF")
layoutS=go.Layout(title="Torus",yaxis=dict(title="Y-axis"),
                 xaxis=dict(title="X-axis"),hovermode="closest",
                 font=dict(family='Courier New, monospace', size=13, color="white"),
                 plot_bgcolor="black",
                 paper_bgcolor="black")

app.layout = html.Div(children=[
    dcc.Markdown("""# Torus"""),
    dcc.Graph(id="Torus",figure=go.Figure(data=fig,layout=go.Layout(title="Torus"))),
    dcc.Graph(id="Torus-Scatter", figure=go.Figure(data=[scatter01], layout=layoutS)),
    dcc.Graph(id="Torus-Graph",figure=go.Figure(data=[scatter00,mesh00],layout=layout))
        ],
    style={
        "width":"80%",
        "vertical-align": "middle",
    })

if __name__ == "__main__":
    app.run_server(host="0.0.0.0",port=5000,debug=True)
