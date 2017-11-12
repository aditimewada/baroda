from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen as uReq,Request
import requests
import sys
import re

req = Request('https://m.magicbricks.com//mbs/property-for-sale/office-space-real-estate-mumbai?from=submit&amp;possessionYears=10081&amp;ageOfConstruction=11651&amp;ageOfConstruction=11651&amp;filter=Y&amp;pageOption=B/Page-2', headers={'User-Agent': 'Mozilla/5.0'})
html = uReq(req).read()
uReq(req).close()
const = {}
listConst = list()
final = {}
listfinal = list()
constArea = list()
bsObj = BeautifulSoup(html, "html.parser")
# a = bsObj.find("div",  {"id": "container"})
# print(a)
x = bsObj.find('div', class_='resultContainer srp-card-container')
# z = x.find('div', id_='resultContainerData')
# print()
y = x.findAll('div', class_='resultBox srp-card-opt-2')
# print(x)
for element in y:
	value = element.find('span', class_='c2-price fw-semi-bold')
	name = element.find('div', class_='c2-locailty text-truncate' )
	# print(name.text, value.text)
	const["name"]= name.text
	const["price"] = value.text
	listConst.append(const.copy())
	# temp = re.findall('\d+', value.text)
	# print(temp[0])
for i in listConst:
	if('Cr' in i["price"]):
		# print(i)
		final["name"] = i["name"]
		temp = re.findall('\d+', i["price"])
		final["value"] = temp[0]
		listfinal.append(final.copy())
newlist = sorted(listfinal, key=lambda k: int(k['value']))
result = newlist[::-1]
# print(result)
# print(results)
# for i in range(10):
# 	constArea.append(results[i])
# https://m.magicbricks.com/mbs/property-for-sale/office-space-real-estate-mumbai?from=submit&possessionYears=10081&ageOfConstruction=11651&ageOfConstruction=11651&filter=Y&pageOption=B/Page-2
# 