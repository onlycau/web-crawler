from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
from urllib.error import URLError

username='username'
password='password'
url='https://passport.csdn.net/account/login'

p=HTTPPasswordMgrWithDefaultRealm()
p.add_password(None,url,username,password)
auth_handler=HTTPBasicAuthHandler(p)
opener=build_opener(auth_handler)


try:
	result=opener.open(url)
	html=result.read().decode('utf-8')
	f=open('csdn.html','w')
	f.write(html)
	f.close()
except URLError as e :
	print(e.reasn)