
import bs4
from urllib.request import urlopen as uReq,Request
from bs4 import BeautifulSoup as soup
from land_value import *

req=Request('https://www.99acres.com/search/project/buy/commercial/mumbai?search_type=QS&search_location=SH&lstAcn=NPSEARCH&lstAcnId=8649067396399739&src=CLUSTER&preference=S&city=12&res_com=C&np_search_type=NP&selected_tab=3&isvoicesearch=N&keyword=mumbai&area_unit=1&strEntityMap=IiI%3D&refine_results=Y&Refine_Localities=Refine%20Localities&action=%2Fdo%2Fquicksearch%2Fsearch&searchform=1&price_min=null&price_max=null',headers={'User-Agent':'Mozilla/5.0'})
html_page=uReq(req).read()
uReq(req).close()
page_soup = soup(html_page,"html.parser")
container=page_soup.findAll("td",{"class":"npsrp_head"})
subhead=page_soup.findAll("tr",{"class":"subHead"})

h=len(container)
i=0
lobbying = {}
lob_value = list()
print("places \t commercial under construction")
while i<h:
 	place=container[i].span.text.strip()
 	count=subhead[i].findAll("td",{"class":"npsrp_tip"})
 	poss=subhead[i].find("td",{"class":"_poss"})
 	price=subhead[i].find("td",{"class":"_price"})
 	phase=subhead[i].find("td",{"class":"_phase"})
 	lobbying["name"] = place
 	lobbying["poss"] = poss.text
 	lob_value.append(lobbying.copy())
 	# print("place"+place)
 	# print(poss.text)
 	# if price == None:
 	# 	print(price)
 	# else:
 	# 	print(price.text)

		 
 	# print(phase)
 	# for c in count:
 		# print(c);
 
 
 	i=i+1
print(lob_value)
# print(land_value[100])  	