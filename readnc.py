#!/usr/bin/python

import netCDF4
import numpy as np
from netCDF4 import Dataset  # http://code.google.com/p/netcdf4-python/  
import  utils_date
from utils_date import time_increment          #Uses Jeff's function time_increment Important to reference
import datetime
from datetime import timedelta
#
import matplotlib
import matplotlib.pyplot as plt




mintempaverages=[]
monthsofyear=[]

#Coordinate Points (~Pendleton~)
y=60
x=90

startdate = '2098080100'                       #Start at a date just prior to the month you want to calculate the average 
num_months = 4                                 #Number of months incremented in the future. The num you want
num_days = 35                                  #Days to increment forward to reach the next month

for m in range(0,num_months):

    new_date=(time_increment(startdate, num_days, "%Y%m%d%H"))  #Jeff's function. Passes the date, increment step, & format. Returns date
    #print(new_date)
    newYYYYMM=new_date[0:6]+'0100'                              #Cuts off extraneous day & hours
    newfile='gfdl-cm3.'+newYYYYMM+'.nc'                         #Puts in actual file form needed
    #print(newfile)
    ticker=0                                                    #Reset
    datanew=0                                                   #Reset
    
    mm=int(new_date[4:6])                                       #Makes the month a number
    monthsofyear.append(mm)                                     #Creates an array with the months 
    
    filein=netCDF4.Dataset(newfile)                            #Calls file of desirec month & year
    mint = filein.variables['T2MIN']                           #Stores individual variable
    data = mint[:,y,x]                                         #Files into a month long array
    
    
    for t in range(0,mint.shape[0]) :
        datanew=data[ticker]+datanew                           #Updates data count within month
        ticker=ticker+1                                        #Updates days passed
        
    average=datanew/ticker                                     #Calculation
        
    print('The average minimum temperature for '+ newYYYYMM +' is: '+str(average))
    startdate=new_date                                         #Start date must get updated to continue looping forward in time
    mintempaverages.append(average)

print(mintempaverages)
fig, linepl = plt.subplots()
#monthsofyear=[9, 10, 11, 12]
linepl.plot(monthsofyear, mintempaverages)
linepl.set(xlabel='Month', ylabel='Min Temp Avg (K)', title='Min Avg Temps of 2098 near Pendleton')
linepl.grid()
fig.savefig("test.png")
plt.show()
