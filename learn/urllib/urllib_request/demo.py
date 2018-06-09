import urllib.request

response=urllib.request.urlopen('https://www.python.org')
print(response.status,response.getheaders(),'\n',response.getheader('Server'))