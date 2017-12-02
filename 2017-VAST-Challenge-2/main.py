
# coding: utf-8

# In[52]:

import functions as funcs
from matplotlib import pyplot as plt
import time as timeLib

import numpy as np
np.random.seed(0)
import math
import random 

from bokeh.io import curdoc
from bokeh.layouts import widgetbox, row, column, layout
from bokeh.models import ColumnDataSource, Select, Slider, Button
from bokeh.palettes import Spectral6
from bokeh.io import output_notebook, show
from bokeh.plotting import figure, output_file, show
from sklearn import tree
from sklearn.cross_validation import train_test_split

from sklearn import neighbors, datasets
from sklearn.neighbors import NearestNeighbors
from sklearn import cluster, datasets
from sklearn.neighbors import kneighbors_graph
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import cross_val_score


from sklearn.cluster import KMeans
from bokeh.plotting import figure
from bokeh.models import HoverTool
from bokeh.models import BoxZoomTool
from bokeh.models import WheelZoomTool
from bokeh.models import PanTool




sensorData = funcs.openSensorFile()
meteorData = funcs.openMeteorFile()




for i in range(0, len(sensorData)):
    print(sensorData[i])

#print("len(sensorData) = ", len(sensorData))
#print("len(meteorData) = ", len(meteorData))



#for i in range(0, len(meteorData)):
#    print(meteorData[i])




combinedData = funcs.combineData(sensorData, meteorData)
plt.plot([0,1,2],[0,1,2])
plt.show()
for keyTriple in combinedData.keys():
    print(keyTriple, " ) ", len(combinedData[keyTriple]))
    print()

print("len(combinedData) = ", len(combinedData))







def findRanksBasedOnChemicalMeasurement(combinedData, chemical, time):
    currentTimeData = combinedData[time]
    
    #print("currentTimeData[len(currentTimeData)-1] = ", currentTimeData[len(currentTimeData)-1])
    #print()
    sensor_measurements = []
    for i in range(0, len(currentTimeData)-2):
        if currentTimeData[i][1] == chemical:
            sensor_measurements.append((currentTimeData[i][0], currentTimeData[i][2]))
            
    #print("sensor_measurements = ", sensor_measurements)
    #print()
    sensor_measurements.sort(key=lambda tup: tup[1])
    #print("sensor_measurements = ", sensor_measurements)
    return sensor_measurements
            








def drawGasPlot(combinedData, chemical, time):
    p = figure(plot_width=600, plot_height=600, title= "Gas Measure of " + chemical,  tools=[PanTool(), BoxZoomTool(), WheelZoomTool()]) 
    
    sensor_measurements = findRanksBasedOnChemicalMeasurement(combinedData, chemical, time)
    rankSize = 10
    
    for pair in sensor_measurements:
        if pair[0] == 1.0:
            p.circle(61, 21, size=rankSize, line_color="green", fill_color="green", fill_alpha=0.5)
        elif pair[0] == 2.0:
            p.circle(66, 35, size=rankSize, line_color="green", fill_color="green", fill_alpha=0.5)
        elif pair[0] == 3.0:
            p.circle(76, 41, size=rankSize, line_color="green", fill_color="green", fill_alpha=0.5)
        elif pair[0] == 4.0:
            p.circle(88, 45, size=rankSize, line_color="green", fill_color="green", fill_alpha=0.5)
        elif pair[0] == 5.0:
            p.circle(103, 43, size=rankSize, line_color="green", fill_color="green", fill_alpha=0.5)
        elif pair[0] == 6.0:
            p.circle(102, 22, size=rankSize, line_color="green", fill_color="green", fill_alpha=0.5)
        elif pair[0] == 7.0:
            p.circle(89, 3, size=rankSize, line_color="green", fill_color="green", fill_alpha=0.5)
        elif pair[0] == 8.0:
            p.circle(74, 7, size=rankSize, line_color="green", fill_color="green", fill_alpha=0.5)
        elif pair[0] == 9.0:
            p.circle(119, 42, size=rankSize, line_color="green", fill_color="green", fill_alpha=0.5)
            
        rankSize += 10
            
    #show(p)
    return p
    

plt.plot([0,1,2],[0,1,2])
plt.show()




#first time = 42461.0
currGasPlot = drawGasPlot(combinedData, "Methylosmolene", 42461.0)

timePeriods = []
for time in combinedData.keys():
    timePeriods.append(str(time))
    
sensors = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
chemicals = ["Methylosmolene", "Chlorodinine", "AGOC-3A", "Appluimonia"]







#Selections and Sliders
time_select = Select(title = "Time",
                     value = str(42461.0),
                     width=200,
                     options = timePeriods)

chemical_select = Select(title = "Chemical",
                     value = "Methylosmolene",
                     width=200,
                     options = chemicals)
scan_button = Button(label="Scan", button_type="success")
scan_30_button = Button(label="Scan Next 30", button_type="success")







#functions when selectors and sliders are used
def update(attrname, old, new):
    currTime = time_select.value
    currChemical = chemical_select.value
    newGasPlot = drawGasPlot(combinedData, currChemical, float(currTime))
    layout.children[1] = newGasPlot
    
    
    
    
def scanAllTime():
    print("Went into scanAllTime method")
    for timeFrame in timePeriods:
        time_select.value = timeFrame
        timeLib.sleep(3.0)

    
def scanNext30():
    print("Went into scanNext30 method")
    timeIndex = timePeriods.index(time_select.value)
    for i in range(timeIndex, timeIndex+30):
        time_select.value = timePeriods[i]
        timeLib.sleep(3.0)
    print("Done with scanNext30")
    
    
    
    
#execute these functions when any inputs are changed
time_select.on_change('value', update)
chemical_select.on_change('value', update)
scan_button.on_click(scanAllTime)
scan_30_button.on_click(scanNext30)

inputs = column(widgetbox(time_select, chemical_select, scan_button, scan_30_button, sizing_mode="scale_both"))
layout = row(inputs, currGasPlot)
curdoc().add_root(layout)
curdoc().title = "Gas Plot"





