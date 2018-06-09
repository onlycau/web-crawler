# -*- coding:utf-8 -*-
import requests

r=requests.get('https://music.163.com/#/song?id=869785')
with open('reviews.txt','wb') as f:
	f.write(r.content)