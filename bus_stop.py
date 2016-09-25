import requests
import json

# import the base url from Constants class
from constants import Constants

class BusStop:
	# Nearest stop uing Latitude and Longitude, with a default radius of 2
	def nearest_stop(self, latitude, longitude, radius = 2):
		NEAREST_STOP_URL = Constants.BASE_URL + \
			"/busstops/stopnearby/lat/{0}/lon/{1}/rad/{2}".format(
				latitude, longitude, radius)
		r = requests.get(NEAREST_STOP_URL)

		if r.status_code is 200:
			return r.json()
		else:
			return

	# Search for bus stop 
	def search_stop(self, query):

		SEARCH_STOP_URL = Constants.BASE_URL + \
			"/busstops/stopsearch/name/{}".format(query)
		r = requests.get(SEARCH_STOP_URL)

		if r.status_code is 200:
			return r.json()
		else:
			return

	# Search for bus in a particular Bus Stop
	def buses_in_stop(self, stop_id):
		STOP_DETAILS_URL = Constants.BASE_URL + "/itsstopwise/details"

		r = requests.post(STOP_DETAILS_URL, data=stop_id)

		if r.status_code is 200:
			return r.json()
		else:
			return