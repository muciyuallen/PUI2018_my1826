import json
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

vehicleActivity = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

numVehicle = len(vehicleActivity)

print("Number of active buses: %s"%numVehicle)
count = 0
for vhc in vehicleActivity:
	vhc_location = vehicleActivity[count]['MonitoredVehicleJourney']['VehicleLocation']
	lon = vhc_location['Longitude']
	lat = vhc_location['Latitude']
	print('Bus %s is at latitude %s and longitude %s '%(count, lat, lon))
	count += 1