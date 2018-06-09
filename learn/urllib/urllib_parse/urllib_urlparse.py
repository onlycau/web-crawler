from urllib.parse import urlparse

#urllib.parse.urlparse(urlstring,scheme='',allow_fragments=True)

result=urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result),result)
