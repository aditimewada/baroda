
import bs4
from urllib.request import urlopen as uReq,Request
from bs4 import BeautifulSoup as soup
import re

req=Request('https://www.99acres.com/search/project/buy/residential/mumbai?search_type=QS&search_location=SH&lstAcn=NPSEARCH&lstAcnId=8649040819546363&src=CLUSTER&preference=S&city=12&res_com=R&np_search_type=NP&selected_tab=3&isvoicesearch=N&keyword=mumbai&strEntityMap=IiI%3D&refine_results=Y&Refine_Localities=Refine%20Localities&action=%2Fdo%2Fquicksearch%2Fsearch&searchform=1&price_min=null&price_max=null',headers={'User-Agent':'Mozilla/5.0'})
html_page=uReq(req).read()
uReq(req).close()
page_soup = soup(html_page,"html.parser")
container=page_soup.findAll("td",{"class":"npsrp_head"})
subhead=page_soup.findAll("tr",{"class":"subHead"})
h=len(container)
i=0
res_areas = {}
lob_value = list()
resArea = list()
# print("places \t residential under construction")
while i<h:
 	place=container[i].span.text.strip()
 	res_areas["places"] = place
 	# print(place)
 	count=subhead[i].findAll("td",{"class":"npsrp_tip"})
 	if(len(count)>1):
 		res = count[1].text
 		temp = re.findall('\d+', res)
 		res_areas["price"] = temp[0]
 		# print(res_areas["price"])
 		lob_value.append(res_areas.copy())
 	else:
 		res_areas["price"] = 0
 		# print(res_areas["price"])
 		lob_value.append(res_areas.copy())
 
 	i=i+1

# print(lob_value)
newlist = sorted(lob_value, key=lambda k: int(k['price']))
results = newlist[::-1]
# print(results)
for i in range(10):
	resArea.append(results[i])
# print("________", resArea) 	