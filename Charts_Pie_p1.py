import plotly.graph_objects as go
#https://plot.ly/python/pie-charts/
#
#basic pie chart
#
labels1= ['Oxygen', 'Hydrogen', 'Carbon_Dioxide', 'Nitrogen']
values1 = [4500, 2500, 1053, 500]

fig1 = go.Figure(data=[go.Pie(labels=labels1, values=values1)])
fig1.show()

#
#styled pie chart
#
colors2 = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']
fig2 = go.Figure(data=[go.Pie(labels=['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen'],
                             values=[4500,2500,1053,500])])
fig2.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors2, line=dict(color='#000000', width=2)))
fig2.show()

#
#donut shaped chart
#
labels3 = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
values3 = [4500, 2500, 1053, 500]
# Use `hole` to create a donut-like pie chart
fig3 = go.Figure(data=[go.Pie(labels=labels3, values=values3, hole=.3)])
fig3.show()

#
#pie charts in subplots
#
from plotly.subplots import make_subplots
labels4 = ["US", "China", "European Union", "Russian Federation", "Brazil", "India",
          "Rest of World"]
# Create subplots: use 'domain' type for Pie subplot
fig4 = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
fig4.add_trace(go.Pie(labels=labels4, values=[16, 15, 12, 6, 5, 4, 42], name="GHG Emissions"),
              1, 1)
fig4.add_trace(go.Pie(labels=labels4, values=[27, 11, 25, 8, 1, 3, 25], name="CO2 Emissions"),
              1, 2)

# Use `hole` to create a donut-like pie chart
fig4.update_traces(hole=.4, hoverinfo="label+percent+name")

fig4.update_layout(
    title_text="Global Emissions 1990-2011",
    # Add annotations in the center of the donut pies.
    annotations=[dict(text='GHG', x=0.18, y=0.5, font_size=20, showarrow=False),
                 dict(text='CO2', x=0.82, y=0.5, font_size=20, showarrow=False)])
fig4.show()