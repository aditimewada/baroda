from residential_loc.first import resArea
import requests
import json
# print(resArea)
lat = {}
listlat = list()
for i in resArea:
	# print("------",i);
	data = i["places"].replace(" ","+")
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
	# print(url)
# url = 'https://maps.googleapis.com/maps/api/geocode/json?address=Infinity+Mall+Mumbai&key=AIzaSyBwHgotLbWEXP4VM_KAM7gc0icK28wAxgo'
# resp = requests.get(url)
# res = json.loads(resp.text)
