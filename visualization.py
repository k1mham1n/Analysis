#!/usr/bin/env python
# coding: utf-8

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.font_manager
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import json
from csv import reader
import seaborn as sns

df = pd.read_csv('/home/tan/Desktop/Python/BB_finaloutput.csv')
df

car = int(df.vehicle_car.sum())
bus = int(df.vehicle_bus_s.sum()) + int(df.vehicle_bus_l.sum())
truck = int(df.vehicle_truck_s.sum()) + int(df.vehicle_truck_l.sum())
yellow_vehicle = int(df.yellow_vehicle.sum())
pedestrian = int(df.pedestrian.sum())
bicycle = int(df.ptw_bicycle.sum())
motorcycle = int(df.ptw_motorcycle.sum())
rider = int(df.rider.sum())
police = int(df.police.sum())
emergency = int(df.emergency.sum())
fire = int(df.fire.sum())

x = np.arange(11) 

# 막대명  
Class = ['Car' , 
         'Bus' , 
         'Truck',
         'Yellow_vehicle' , 
         'Pedestrian' , 
         'Bicycle' ,
         'Motorcycle' ,
         'Rider' ,
         'Police',
         'Emergency' ,
         'Fire']


# Instance 수량
Instance = [car, bus, truck, yellow_vehicle, pedestrian, bicycle, motorcycle, rider, police, emergency, fire]



plt.figure(figsize=(20,10), dpi=300)
colors = sns.color_palette('hls',len(Class))
plt.bar(x, Instance, color=colors, edgecolor=colors, alpha=0.7, linewidth=2)

for i, v in enumerate(x):
    plt.text(v, Instance[i], format(Instance[i],',d'),
              fontsize = 12,
              color='black',
              horizontalalignment='center',
              verticalalignment='bottom',
              weight = 'bold' 
              )
    
plt.xticks(x, Class)
current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])
plt.xlabel('Class', labelpad=20, fontdict={'weight':'bold'}, size=20)
plt.ylabel('Instance', labelpad=20, fontdict={'weight':'bold'}, size=20)
plt.title('BB_10K', pad=20, fontdict={'weight':'bold'}, size=20)
plt.savefig('BB_10K.png', dpi=100)
plt.show()



