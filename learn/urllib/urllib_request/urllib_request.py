from urllib import request,parse

url1='http://httpbin.org/post'
headers={
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict={'name':'Germey'}
data=bytes(parse.urlencode(dict),encoding='utf8')
my_request=request.Request(url=url1,data=data,headers=headers,method='POST')
response=request.urlopen(my_request)
print(response.read().decode('utf-8'))
