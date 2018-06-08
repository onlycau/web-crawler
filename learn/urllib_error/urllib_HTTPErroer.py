from urllib import request,error

try:
	response=request.urlopen('http://www.yangqq.com/jstst/')
except error.HTTPError as e:
	print(e.reason,e.code,e.headers,seq='\n')