import pandas as pd
import datetime as dt
import os
import sys

def main():
    names = ["activity", "basal", "basal", "cgm", "hr", "meal", "smbg"]
    #T1 import
    activity = pd.read_csv("smallData/activity_small.csv")
    basal = pd.read_csv("smallData/basal_small.csv")
    bolus = pd.read_csv("smallData/bolus_small.csv")
    cgm = pd.read_csv("smallData/cgm_small.csv")
    hr = pd.read_csv("smallData/hr_small.csv")
    meal = pd.read_csv("smallData/meal_small.csv")
    smbg = pd.read_csv("smallData/smbg_small.csv")

    files = [activity, basal, basal, cgm, hr, meal, smbg]

    i = 0

    for file in files:
    	file['time'] = pd.to_datetime[file['time']] # convert time col type to datetime type
    	file.set_index("time", inplace = "True")
    	file['value'] = file['value'].astype(float)
    	file['value'].rename(columns={'value': names[i]})

    	i = i + 1

    #merge

    joined = cgm
    for file in files:
    	if(file is not cgm):
    		joined = joined.merge(file, on="time", how="left")

    joined = joined.fillna(value=0)

    joined.insert(joined.shape[1], "time5", joined.time.round('5min'))
    joined.insert(joined.shape[1], "time15", joined.time.round('15min'))
    sums = joined[['activity', 'bolus', 'meal','time5',]]
    means = joined[['smbg', 'hr', "basal", "cgm"]]

    mus5 = joined.groupby(['time5'])['activity', 'bolus', 'meal'].sum()
    mus15 = joined.groupby(['time15'])['activity', 'bolus', 'meal'].sum()
    mean5 = means.groupby(['time5'])['smbg', 'hr', "basal", "cgm"].mean()
    mean15 = means.groupby(['time15'])['smbg', 'hr', "basal", "cgm"].mean()

    joined5 = merge(mus5, mean5)
    joined15 = merge(mus15, mean15)

    joined5.to_csv('pandas_5min.csv')
    joined15.to_csv("pandas_15min.csv")






