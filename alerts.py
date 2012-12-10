#!/usr/local/bin/python
# coding: latin-1
"""
alerts.py -- Display weather alerts for 95051 using Weather Underground's API
"""
# MLPrince 2012 ｡◕ ‿ ◕｡ 

import urllib2
import json
from wunderapi import WUNDERKEY

def get_alert():
	""" 
	Makes a call to wunderground's API and displays weather alerts 
	if there are any. 
	"""
	# Open url, make call to the API using an API key.
	f = urllib2.urlopen('http://api.wunderground.com/api/' + WUNDERKEY + '/alerts/q/95051.json')
	json_string = f.read() # Save response as a json string.
	parsed_json = json.loads(json_string) # Parse the json string.

	# If there are alerts...
	if parsed_json['alerts']:

		# Print the date, expiration date, and message to the console.
		for alert in parsed_json['alerts']:
	    	print "Date: %s" % alert['date']
	    	print "Expires: %s" % alert['expires']
	    	print alert['message']

	# Otherwise...
	else:

		# Print the following string.
		print "There are no alerts today."

	# Hang up the phone.
	f.close()

def main():
	get_alert()

if __name__ == '__main__':
	main()
