from urllib import request,parse

values="username:'546359321@qq.com passwd:'123456"
data=values.encode(encoding="gb2312")
url='https://music.163.com/#/song?id=869785'
my_request=request.Request(url,data)
respense=request.urlopen(my_request)
print(respense.read())