import requests
import json
import sys

# query = sys.argv[1]
# url = 'https://api.duckduckgo.com/?q='+ query +'&format=json&pretty=1'
# resp = requests.get(url)
# res = json.loads(resp.text)
# result = res.get('RelatedTopics')
# cell = result[0]
# print(cell.get('Text'))
payload = {"Customer_Id" : 440728117}

headers = {'Accept-Encoding': 'gzip,deflate',
'apikey': '00testapikey1',
'Content-Type': 'application/json',
'Content-Length': '31',
'Host': '104.211.176.248:8080',
'Connection': 'Keep-Alive',
'User-Agent': 'Apache-HttpClient/4.1.1'}

res_cust = requests.post('http://104.211.176.248:8080/bob/bobuat/api/GetCustAccList', headers=headers, json=payload)

res = json.loads(res_cust.text)
print(res)

wanted_keys = ['Account_Number']

for i in res:
	temp = i
	cell = {k: temp[k] for k in set(wanted_keys) & set(temp.keys())}
	acc = json.dumps(cell)
	headers_acc = {'Accept-Encoding': 'gzip,deflate',
	'apikey': '00testapikey1',
	'Content-Type': 'application/json',
	'Content-Length': '35',
	'Host': '104.211.176.248:8080',
	'Connection': 'Keep-Alive',
	'User-Agent': 'Apache-HttpClient/4.1.1'}
	res_acc = requests.post('http://104.211.176.248:8080/bob/bobuat/api/GetAccDetails', headers=headers_acc, json=acc)
	jsonAcc = json.loads(res_acc.text)
	print(jsonAcc)
