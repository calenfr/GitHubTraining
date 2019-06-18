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

#!/usr/bin/python

import netCDF4
import numpy as np
from netCDF4 import Dataset  # http://code.google.com/p/netcdf4-python/   #Dataset is the type
import  utils_date
import datetime
from datetime import timedelta

#Coordinate Points (~Pendleton~)
y=60
x=90

YearAverages=[]

startdate = '2096080100'
num_months = 2       #Change back to 30

#print(time_increment(2096080100, 35, "%Y%m%d%H"))

for m in range(0,num_months):
    
    thisdate=(startdate)+datetime.timedelta(days=35)#days 35 & startdate
    print(thisdate)
    yyyy=thisdate[0,4]   
    mm=thisdate[4,6]
    newdate = str(yyyy)+str(mm)+"0100"
    newfile = "gfdl-cm3."+newdate+".nc"

    mmm=mm-1
    
    ticker=0
    datanew=0
    
    filein=netCDF4.Dataset(newfile)
    mint = filein.variables['T2MIN']                           #Stores individual variable
    data = mint[:,y,x]                                         #Files into a month long array
    
    
   # for t in range(0,mint.shape[0]) :
  #      datanew=data[ticker]+datanew
   #     ticker=ticker+1                      
        
    #    average=datanew/ticker
  #  YearAverages=YearAverages.append('The average TMin for {mmm} is: {average}')
    #print(f'The average minimum temperature is: " average)
        


#print(YearAverages)
