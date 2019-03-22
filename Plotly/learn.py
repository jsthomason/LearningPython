#!/usr/bin/python3

import plotly
import plotly.graph_objs as go
import time
from bfile import BFile

#da_file = "testbin.dat"
da_file = "10.246.5.22.dat"
da_sfmt = "dfff"

bf = BFile(da_file, da_sfmt)

icmp_time = 0.0
icmp_min = 0.0
icmp_avg = 0.0
icmp_max = 0.0
x = []
y_min = []
y_avg = []
y_max = []
for record in bf.readit():
    icmp_time, icmp_min, icmp_avg, icmp_max = tuple(record)
    x.append(time.strftime("%H:%M:%S", time.localtime(icmp_time)))
    y_min.append(icmp_min)
    y_avg.append(icmp_avg)
    y_max.append(icmp_max)

# Create traces
trace0 = go.Scatter(
    x = x,
    y = y_min,
    mode = 'lines',
    name = 'Min'
)
trace1 = go.Scatter(
    x = x,
    y = y_avg,
    mode = 'lines',
    name = 'Avg'
)
trace2 = go.Scatter(
    x = x,
    y = y_max,
    mode = 'lines',
    name = 'Max'
)
# Consolidate data traces
data = [trace0, trace1, trace2]

# Edit the layout
layout = dict(title = 'Monitor Stats',
              xaxis = dict(title = 'Time Sample'),
              yaxis = dict(title = 'ICMP RTT(ms)'),
              )

# Create a Figure Dictionary
fig = dict(data=data, layout=layout)

# Plot It...
plotly.offline.plot(fig, filename='learn.html', show_link=False)

