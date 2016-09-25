import requests
import json

# import the base url from Constants class
from constants import Constants

class Route:
	# Get route wise details
	def route_wise(self, direction, route_no):
		ROUTE_WISE_URL = Constants.BASE_URL + "/itsroutewise/details"
		PARAMS = {'direction': direction, 'routeNO': route_no}
		r = requests.post(ROUTE_WISE_URL, data=PARAMS)

		if r.status_code is 200:
			return r.json()
		else:
			return

	# Route map details
	def route_map(self, direction, route_no):
		ROUTE_MAP_URL = Constants.BASE_URL + "/routemap/details"
		PARAMS = {'direction': direction, 'routeNO': route_no}
		r = requests.post(ROUTE_MAP_URL, data=PARAMS)

		if r.status_code is 200:
			return r.json()
		else:
			return