import requests

proxies={
	'http':'106.111.243.113:9000',
	'https':'http://10.10.1.10:1080',
}

requests.get('http://www.taobao.com',proxies=proxies)