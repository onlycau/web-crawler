from urllib import request,parse

values={}
values['username']='sjdfsdj@qq.com'
values['password']='xxx'
data=parse.urlencode(values,encoding="gb2312")
url="https://passport.csdn.net/account/login"
geturl=url+"?"+data
my_request=request.Request(geturl)
respanse=request.urlopen(my_request)
print(respanse.read())