from bokeh.io import show, curdoc
from bokeh.models import (
    ColumnDataSource,
    HoverTool,
    LogColorMapper,
    LinearColorMapper
)
from bokeh.palettes import OrRd9 as palette
from bokeh.plotting import figure
from bokeh.layouts import widgetbox, row, column
from time import sleep
from bokeh.sampledata.us_counties import data as counties
from bokeh.sampledata.unemployment import data as unemployment
import pandas
from bokeh.models.widgets import Button
import numpy 
from bokeh.models import Arrow, OpenHead, NormalHead, VeeHead



coor = pandas.read_csv('points.csv')
facs = pandas.read_csv('factories.csv')

# data = pandas.read_csv('sensorData.csv')
# print(data.keys())
palette.reverse()
color_mapper = LinearColorMapper(palette=palette)

sensorSource = ColumnDataSource(data=dict(
    xSen=list(coor['x']),
    ySen=list(coor['y']),
    voldata = [1]*len(coor['x']),
    # address = list(coor['location']),
))
windSource = ColumnDataSource(data=dict(
    x_start=[.75],
    y_start=[0.1],
    x_end=[.75], 
    y_end=[.2]
    # address = list(coor['location']),
))
# print(source.data['address'])
TOOLS = "pan,wheel_zoom,reset,hover,save"
p = figure(
    title="Emissions",
    x_axis_location=None, y_axis_location=None, tools = TOOLS, x_axis_label='Map', y_axis_label='Map'
)
p.circle(x='xSen',y='ySen',
    fill_color={'field': 'voldata', 'transform': color_mapper}, 
    size = 15, source=sensorSource)
p.circle(x = facs['x'], y = facs['y'], color = 'blue', size = 15)
p.circle(x=.75, y=.15, fill_alpha = 0, size = 110)
p.add_layout(Arrow(end=VeeHead(size=35), line_color="red",
                   x_start='x_start', y_start='y_start', x_end='x_end', y_end='y_end', source = windSource))
p.image_url(url=['https://i.imgur.com/Lz7D8KN.jpg'], x=0, y=1, w = 1, h= 1.03, global_alpha = 0.5)
show(p)
