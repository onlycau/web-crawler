import requests
from requests.auth import HTTPBasicAuth

r=requests.get('https://www.baidu.com/s?wd=%E4%BB%A3%E7%90%86%E6%9C%8D%E5%8A%A1%E5%99%A8&rsv_spt=1&rsv_iqid=0xe29c74b2000528dc&issp=1&f=3&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=1&oq=%25E4%25BB%25A3%25E7%2590%2586&rsv_t=119cdj6izvlFjeG%2FOOBtjhV26ELisxdlEF%2BBB0YYuOjceClmigB9HjlSKtxt8MUy4fYG&rsv_sug3=8&rsv_sug1=10&rsv_sug7=100&rsv_pq=e4190fb200051a18&rsv_sug2=1&prefixsug=%25E4%25BB%25A3%25E7%2590%2586&rsp=0&rsv_sug4=1308',auth=HTTPBasicAuth('15723084900','982074165'))
print(r.status_code)