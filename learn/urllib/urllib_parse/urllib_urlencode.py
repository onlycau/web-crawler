from urllib.parse import urlencode

paramas={
	'name':'germy',
	'age':22
}
base_url='http://www.baidu.com?'
url=base_url+urlencode(paramas)
print(url)