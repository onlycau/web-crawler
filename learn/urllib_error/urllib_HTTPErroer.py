from urllib import request,error

try:
	response=request.urlopen('http://aawww.google.com')
except error.HTTPError as e:
	print(e.reason,e.code,e.headers)
except error.URLError as e:
	print(e.reason)
else:
	print('Request successfully')