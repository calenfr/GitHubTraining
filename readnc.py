#!/usr/bin/python

import netCDF4
import numpy as np
from netCDF4 import Dataset  # http://code.google.com/p/netcdf4-python/   #Dataset is the type

#Coordinate Points (~Pendleton~)
y=60
x=90
#!/usr/bin/python

import netCDF4
import numpy as np
from netCDF4 import Dataset  # http://code.google.com/p/netcdf4-python/   #Dataset is the type

#Coordinate Points (~Pendleton~)
y=60
x=90

ticker=0
datanew=0

filein = netCDF4.Dataset('gfdl-cm3.2098090100.nc')         #Reads in specific file gfdl-cm3.2098090100.nc
mint = filein.variables['T2MIN']                           #Stores individual variable
data = mint[:,y,x]                                         #Files into a month long array
#print(data)                                               #Use to check data points
#print(mint.shape)                                         #Use to check array size
#print(mint.dimensions)

#for t in range(0,4) :                                     #Use for a smaller range than entire month

for t in range(0,mint.shape[0]) :
    datanew=data[ticker]+datanew
    ticker=ticker+1                      

average=datanew/ticker
print(average)

ticker=0
datanew=0

filein = netCDF4.Dataset('gfdl-cm3.2098090100.nc')         #Reads in specific file gfdl-cm3.2098090100.nc
mint = filein.variables['T2MIN']                           #Stores individual variable
data = mint[:,y,x]                                         #Files into a month long array
#print(data)                                               #Use to check data points
#print(mint.shape)                                         #Use to check array size
#print(mint.dimensions)

#for t in range(0,4) :                                     #Use for a smaller range than entire month

for t in range(0,mint.shape[0]) :
    datanew=data[ticker]+datanew
    ticker=ticker+1                      

average=datanew/ticker
print(average)
