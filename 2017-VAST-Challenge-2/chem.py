import pandas 
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, BoxZoomTool, WheelZoomTool,PanTool
from bokeh.palettes import Category10 as palette
from bokeh.models import (
    ColumnDataSource,
    HoverTool,
    LogColorMapper,
    LinearColorMapper
)
color_mapper = LinearColorMapper(palette=palette[9])

df = pandas.read_excel('Sensor Data.xlsx')
p = figure(plot_width=800, plot_height=800,x_axis_type='datetime')
tempdf = df.loc[df['Monitor'] == 1]
source = ColumnDataSource(data=dict(
    x=df['Date Time '],
    y=df['Monitor'],
))

p.circle('x', 'y',color={'field': 'y', 'transform': color_mapper}, size=5, source=source)
show(p)