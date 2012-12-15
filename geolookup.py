import urllib2
import json
from private import APIKEY
f = urllib2.urlopen('http://api.wunderground.com/api/'+ APIKEY + '/geolookup/conditions/q/95051.json')
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
print "Current temperature in %s is: %s" % (location, temp_f)
f.close()
