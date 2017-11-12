from construction_loc.const import result
import requests
import json
# print(resArea)
lat = {}
listlat = list()
for i in result:
	# print("------",i);
	data = i["name"].replace(" ","+")
	url = 'https://maps.googleapis.com/maps/api/geocode/json?address='+data+'&key=AIzaSyBwHgotLbWEXP4VM_KAM7gc0icK28wAxgo'
	resp = requests.get(url)
	res = json.loads(resp.text)
	demo = res.get('results')
	# print(demo)
	if demo != []:
		# lat.append(demo[0]['formatted_address'],demo[0]['geometry']['location'])
		lat["places"]=demo[0]['formatted_address']
		lat["lat"]=demo[0]['geometry']['location']
		listlat.append(lat.copy())
# print(listlat)