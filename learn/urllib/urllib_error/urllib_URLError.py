from urllib import request,error

try:
	response=request.urlopen('http://www.aaaabaidu.com')
except error.URLError as e:
	print(e.reason)