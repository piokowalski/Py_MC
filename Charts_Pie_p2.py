import plotly.graph_objects as go
from plotly.subplots import make_subplots

labels5 = ['1st', '2nd', '3rd', '4th', '5th']
# Define color sets of paintings
night_colors = ['rgb(56, 75, 126)', 'rgb(18, 36, 37)', 'rgb(34, 53, 101)',
                'rgb(36, 55, 57)', 'rgb(6, 4, 4)']
sunflowers_colors = ['rgb(177, 127, 38)', 'rgb(205, 152, 36)', 'rgb(99, 79, 37)',
                     'rgb(129, 180, 179)', 'rgb(124, 103, 37)']
irises_colors = ['rgb(33, 75, 99)', 'rgb(79, 129, 102)', 'rgb(151, 179, 100)',
                 'rgb(175, 49, 35)', 'rgb(36, 73, 147)']
cafe_colors =  ['rgb(146, 123, 21)', 'rgb(177, 180, 34)', 'rgb(206, 206, 40)',
                'rgb(175, 51, 21)', 'rgb(35, 36, 21)']

# Create subplots, using 'domain' type for pie charts
specs = [[{'type':'domain'}, {'type':'domain'}], [{'type':'domain'}, {'type':'domain'}]]
fig5 = make_subplots(rows=2, cols=2, specs=specs)

# Define pie charts
fig5.add_trace(go.Pie(labels=labels5, values=[38, 27, 18, 10, 7], name='Starry Night',
                     marker_colors=night_colors), 1, 1)
fig5.add_trace(go.Pie(labels=labels5, values=[28, 26, 21, 15, 10], name='Sunflowers',
                     marker_colors=sunflowers_colors), 1, 2)
fig5.add_trace(go.Pie(labels=labels5, values=[38, 19, 16, 14, 13], name='Irises',
                     marker_colors=irises_colors), 2, 1)
fig5.add_trace(go.Pie(labels=labels5, values=[31, 24, 19, 18, 8], name='The Night Café',
                     marker_colors=cafe_colors), 2, 2)

# Tune layout and hover info
fig5.update_traces(hoverinfo='label+percent+name', textinfo='none')
fig5.update(layout_title_text='Van Gogh: 5 Most Prominent Colors Shown Proportionally',
           layout_showlegend=False)

fig5 = go.Figure(fig5)
fig5.show()