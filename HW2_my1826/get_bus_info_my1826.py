import json
import pandas as pd
import numpy as np
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import os
import sys

apikey = sys.argv[1]
bus_line = sys.argv[2]
VMDL = "calls"

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=%s&LineRef=%s&version=2"%(apikey, VMDL, bus_line)

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
dataDict = json.loads(data)

try:
	vehicleActivity = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
except KeyError:
	print(dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['ErrorCondition']['Description'])
	sys.exit()

numVehicle = len(vehicleActivity)

# print("Number of active buses: %s"%numVehicle)

header = ['Latitude','Longitude','Stop Name','Stop Status']
rows = []
count = 0
for vhc in vehicleActivity:
	vhc_location = vehicleActivity[count]['MonitoredVehicleJourney']['VehicleLocation']
	lon = vhc_location['Longitude']
	lat = vhc_location['Latitude']
	OnwardCalls = vehicleActivity[count]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall']
	stopName = OnwardCalls[0]['StopPointName'][0]
	stopStatus = OnwardCalls[0]['ArrivalProximityText']
	# row = np.array([lat,lon,stopName,stopStatus])
	rows.append([lat,lon,stopName,stopStatus])
	count += 1

df = pd.DataFrame(rows, columns = header)
print(df)