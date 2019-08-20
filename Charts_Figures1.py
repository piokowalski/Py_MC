import plotly.graph_objects as go
#
## Basic Figure
#

fig1 = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="A Figure Displayed with fig.show()"
)
fig1.show()
# Displaying yourself
fig2 = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="A Figure Displaying Itself"
)
fig2.show()

#
png_renderer = pio.renderers["png"]
png_renderer.width = 500
png_renderer.height = 500
pio.renderers.default = "png"
fig3 = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="A Figure Displayed with the 'png' Renderer"
)
fig3.show()

#
#
import plotly.express as px

data_canada = px.data.gapminder().query("country == 'Canada'")
fig4 = px.bar(data_canada, x='year', y='pop')
fig4.show()