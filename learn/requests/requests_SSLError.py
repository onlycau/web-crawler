import logging
import requests

logging.captureWarnings(True)
response=requests.get('https://www.12306.cn',verify=False)
print(response.status_code)

# add SSL certificate
# response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
