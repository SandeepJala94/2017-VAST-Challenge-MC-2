
# coding: utf-8

# In[52]:

import functions as funcs
from matplotlib import pyplot as plt

import numpy as np
np.random.seed(0)
import math
import random 

from bokeh.io import curdoc
from bokeh.layouts import widgetbox, row, column, layout
from bokeh.models import ColumnDataSource, Select, Slider
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
    print(keyTriple, " ) ", combinedData[keyTriple])
    print()

print("len(combinedData) = ", len(combinedData))





