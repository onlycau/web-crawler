import requests

r=requests.get('https://www.taobao.com',timeout=(0.01,1))
print(r.status_code)