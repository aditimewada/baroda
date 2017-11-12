from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen as uReq,Request
import requests
import sys
import re

req = Request('https://www.99acres.com/property-rates-and-price-trends-in-mumbai/', headers={'User-Agent': 'Mozilla/5.0'})
html = uReq(req).read()
uReq(req).close()
bsObj = BeautifulSoup(html, "html.parser")
x = bsObj.find('table', class_='prTble')
y = x.findAll('tr')
# r = y.contents
# print(y[1])
lob_name = list()
lob_value = list()
i = 0
lobbying = {}
for element in y:
	name = element.find('td', class_='tl')
	value = element.find('td', {"class": None})
	if name == None and value == None:
		print("none")
		
	else:
		# lob_name.append(name.text)
		# lob_value[i] = value.text
		lobbying["name"] = name.text
		temp = value.text.replace(",","")
		number = re.findall('\d+', temp)
		if number == []:
			lobbying["value"] = 0
			lob_value.append(lobbying.copy())
		else:
			lobbying["value"] = number[1]
		# print(lobbying)
			lob_value.append(lobbying.copy())
		# lob_name.append()
	# i = i + 1	

newlist = sorted(lob_value, key=lambda k: int(k['value']))
land_value = newlist[::-1]
# print(newlist)
# str1 = lob_value[1]["value"].replace(",","") 
# print(str1)

# print(number[0]) if number[0]>number[1] else print(number[1])
# l = lob_value.sort()
# print(l)



# print("names------->", lob_name)