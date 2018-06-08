from urllib import error
from urllib.robotparser import RobotFileParser
from urllib.request import urlopen


rp=RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'http://www.jianshu.com'))
print(rp.can_fetch('*', "http://www.jianshu.com/serch?q=python&page=1&type=collections"))

#parser()

rp2=RobotFileParser()
try :
	rp2.parse(urlopen('http://www.jianshu.com/robots.txt').read().decode('utf-8').split('\n'))
except error.HTTPError as e:
	print(e.reason,e.code,e.headers)
except error.URLError as e:
	print(e.reason)
else:
	print('Request successfully')
print(rp2.can_fetch('*', 'http://www.jianshu.com'))
print(rp2.can_fetch('*', "http://www.jianshu.com/search?q=python&page=1&type=collections"))
