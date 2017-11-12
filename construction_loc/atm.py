from construction_loc.const import result
import requests
import json
import webbrowser


# from latitude import lat
from construction_loc.latitude import listlat
place = list()
length = list()
print("--------------TOP CONSTUCTION AREAS---------------")
for i in listlat:
	data1 = repr(i["lat"]["lat"])
	data2 = repr(i["lat"]["lng"])
	# print(data1, data2)
# url= 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+data1+','+data2+'&radius=100&type=atm&key=AIzaSyCUj1RJqTJPbvFxwUv6XR7SQnfJB0hdoyU'


# uncomment the above url and comment the below url to get top location conatining lesser number of ATMs


	url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+data1+','+data2+'&radius=100&type=bank&key=AIzaSyCUj1RJqTJPbvFxwUv6XR7SQnfJB0hdoyU'
	resp = requests.get(url)
	res = json.loads(resp.text)
	demo = res.get('results')
	length = len(demo)
	# print(length)
	if length<1:
		place.append(i)
		print(" >> ",i["places"])
data = place[0]["places"].replace(" ","+")
# print(data)
url1 = 'https://www.google.co.in/maps/search/'+data+'/data=!3m2!1e3!4b1?hl=en'
resp = requests.get(url1)
webbrowser.open(url1)