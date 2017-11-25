import xlrd
import numpy as np




def openSensorFile():
    file_location = "Sensor_Data.xlsx"
    sensorFile = xlrd.open_workbook(file_location)
    sensorInfo = sensorFile.sheet_by_index(0)        
    
    v = []
    
    for r in range(1, sensorInfo.nrows):
        sensorTuple = ( sensorInfo.cell_value(r, 0), sensorInfo.cell_value(r, 1), sensorInfo.cell_value(r, 2), sensorInfo.cell_value(r, 3) )                       
        v.append(sensorTuple)
    
    return v



def openMeteorFile():
    file_location = "Meteorological_Data.xlsx"
    file = xlrd.open_workbook(file_location)
    meteorFile = file.sheet_by_index(0)        
    
    v = []
    
    for r in range(1, meteorFile.nrows):
        sensorTuple = ( meteorFile.cell_value(r, 0), meteorFile.cell_value(r, 1), meteorFile.cell_value(r, 2) )                       
        v.append(sensorTuple)
    
    return v


def addMeteorDataToDict(timeDict, m):
    print("len(m) = ", len(m))
    uniqueMTime = []
    allMTime = []
    for row in m:
        allMTime.append(row[0])
        if row[0] not in uniqueMTime:
            uniqueMTime.append(row[0])
    print("len(uniqueM) = ", len(uniqueMTime))
    
    
    allTime = []
    for keyTriple in timeDict.keys():
        if keyTriple[0] not in uniqueMTime:
            allTime.append(keyTriple[0])
            
    print("len(allTime) = ", len(allTime))
    
    for keyTriple in timeDict.keys():
        print(type(keyTriple), " ) ", type(timeDict[keyTriple]))
    
    numOfTimesMatched = 1
    for time in uniqueMTime:
        for keyTriple in timeDict.keys():
            if time == keyTriple[0]:
                index = allMTime.index(time)
                direction = m[index][1]
                speed = m[index][2]
                timeDict[keyTriple].append(direction)
                timeDict[keyTriple].append(speed)
                print(keyTriple, " ) ", timeDict[keyTriple])
                
                
    #for keyTriple in timeDict.keys():
    #    print(keyTriple, " ) ", timeDict[keyTriple])
                

            
    
    
    


def combineData(s, m):
    print("went into combineData")
    
    timeDict = {}
    for i in range(0, len(s)):
        timeDict[s[i][2], s[i][1], s[i][0]] = [ s[i][3] ]
        
    for keyTriple in timeDict.keys():
        print(keyTriple, " ) ", timeDict[keyTriple])
        
        
    print("len(timeDict) = ",  len(timeDict))
        
    newTimeDict = addMeteorDataToDict(timeDict, m)
    
    
    
    
    
    
    
    
    
    
    
    