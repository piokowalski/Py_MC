import plotly.graph_objects as go


#basic pie chart
labels1= ['Oxygen', 'Hydrogen', 'Carbon_Dioxide', 'Nitrogen']
values1 = [4500, 2500, 1053, 500]

fig1 = go.Figure(data=[go.Pie(labels=labels1, values=values1)])
fig1.show()


#styled pie chart
colors2 = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']
fig2 = go.Figure(data=[go.Pie(labels=['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen'],
                             values=[4500,2500,1053,500])])
fig2.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors2, line=dict(color='#000000', width=2)))
fig2.show()

#donut shaped chart
labels3 = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
values3 = [4500, 2500, 1053, 500]
# Use `hole` to create a donut-like pie chart
fig3 = go.Figure(data=[go.Pie(labels=labels3, values=values3, hole=.3)])
fig3.show()