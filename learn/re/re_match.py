import re

content='Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result=re.match('^Hello\s(\d+)\s(\d+)\sWorld',content)
print(result)
print(result.group())
for i in result.group():
	print(i)

content2='http://weibo.com/comment/KRraCN'
result1=re.match('http.*?comment/(.*?)',content2)
result2=re.match('http.*?comment/(.*)',content2)
print('result1', result1.group(1))
print('result2', result2.group(1))