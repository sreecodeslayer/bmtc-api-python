import requests
import json

# import functions from child class : BusStop
from bus_stop import BusStop

# import functions from child class : Route 
from route import Route 

# import the base url from Constants class
from constants import Constants


class Bmtc(BusStop, Route):
	# Get trip fare
	def trip_fare(self, source, destination, service_type, adults_count):
		TRIP_FARE_URL = Constants.BASE_URL + "/tripfare/details"
		x = service_type if service_type in Constants.SERVICE_TYPE else None
		print x

		if x is not None:
			PARAMS = {'source': source, 'destination': destination,
				  'servieType': x, 'adults': adults_count}
			r = requests.post(TRIP_FARE_URL, data=PARAMS)

			if r.status_code is 200:
				return r.json()
			else:
				return

bmtc = Bmtc()