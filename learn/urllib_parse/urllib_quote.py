from urllib.parse import quote,unquote

keyword='photo'
url='http://www.baidu.com/s?wd='+quote(keyword)
print(quote(url))
print(unquote(url))