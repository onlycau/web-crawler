import requests

r=requests.get('https://www.baidu.com')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)

#params

data={
	'name':'germy',
	'age':22
	}
r=requests.get("http://httpbin.org/get",params=data)
print(r.text)