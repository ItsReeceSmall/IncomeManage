import time, os, sys, glob, math, threading

null = 0
#=====PERSONAL====#
livingKeep = 150
moneySave = 150
phoneBill = 18
perTotal = (livingKeep + moneySave + phoneBill)
#=======CAR=======#
carTax = null
carIns = null
carFuel = null
carTotal = (carTax + carIns + carFuel)
#=================#

allTotal = (perTotal + carTotal)

funds = int(input('Earnings £:'))
remFunds = (funds - allTotal)
weeklyFunds = round((remFunds / 4), 2)
dailyFunds = round((remFunds / 28), 2)
print('TOTAL £' + str(remFunds))
print('WEEKLY £' + str(weeklyFunds))
print('DAILY £' +  str(dailyFunds))
