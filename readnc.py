#!/usr/bin/python

import netCDF4
import numpy as np

from netCDF4 import Dataset  # http://code.google.com/p/netcdf4-python/

#Dataset is the type

y=60
x=90
filein = netCDF4.Dataset('gfdl-cm3.2098090100.nc')         #Reads in specific file gfdl-cm3.2098090100.nc
mint = filein.variables['T2MIN']                               #Stores individual variable
data = mint[:,y,x]

for t in range(0,mint.shape[0]) :
    print([data[t]])

#print(mint.shape)
#print(mint.dimensions)


#ticker = 0
#datenew = 0
#
#Loop -> Data Point Exists
#for ()
#ticker=ticker+1
#datanew=data+datanew
#Exit Loop

#average=(datanew)/ticker
#print(average)


