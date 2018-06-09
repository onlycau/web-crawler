import requests
import re

r=requests.get('http://httpbin.org/get')
print(type(r.text))
print(r.json())
print(type(r.json()))

#
headers={
	    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
	    }
r=requests.get("https://www.zhihu.com/explore", headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles=re.findall(pattern,r.text)
print(titles)