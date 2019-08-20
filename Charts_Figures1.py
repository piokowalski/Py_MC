import plotly.graph_objects as go

#
## Basic Figure
#

fig1 = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="A Figure Displayed with fig.show()"
)
fig1.show()