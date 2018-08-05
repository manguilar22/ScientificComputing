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
                        colormap="Portland",
                        aspectratio=dict(x=1,y=1,z=0.3))
fig2 =FF.create_trisurf(x=x,y=y,z=z,simplices=simplices,
                        title="Torus V. 2",
                        colormap="Earth",
                        aspectratio=dict(x=1,y=1,z=1))
fig3 =FF.create_trisurf(x=x,y=y,z=z,simplices=simplices,
                        title="Torus V. 3",
                        colormap="RdBu",
                        aspectratio=dict(x=.2,y=.2,z=1))
fig4=go.Scatter3d(x=x,y=y,z=z,mode="markers",marker=dict(size=.5,symbol="square",colorscale="polar"))

trace01=go.Scatter(x=x,y=z,mode="markers",name="(X-Axis,Z-Axis)",marker=dict(size=.5,symbol="circle-open"))
trace02=go.Scatter(x=x,y=y,mode="lines",name="(X-Axis,Y-Axis)",marker=dict(size=.3))

layout2D=go.Layout(title="Scatter-2D Torus",yaxis=dict(title="Y-axis"),
                 xaxis=dict(title="X-axis"),hovermode="closest")

layout=go.Layout(title="Scatter-3D Torus",yaxis=dict(title="Y-axis"),
                 xaxis=dict(title="X-axis"),hovermode="closest")

app.layout = html.Div([
    dcc.Markdown("""# Torus"""),
    dcc.Graph(id="Torus-Graph",figure=dict(data=fig,layout=layout)),
    dcc.Graph(id="Torus-Scatter",figure=dict(data=[fig4],layout=layout)),
    html.H2("Version 2"),
    dcc.Graph(id="Torus-V2",figure=dict(data=fig2)),
    dcc.Graph(id="Torus-2D",figure=dict(data=[trace01,trace02],layout=layout2D)),
    html.H2("Version 3"),
    dcc.Graph(id="Torus-V3",figure=dict(data=fig3))
])

if __name__ == "__main__":
    app.run_server()
