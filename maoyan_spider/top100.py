#-*- coding:utf-8 -*-
#!/usr/bin/env python3


'Crawl MaoYan net tope100 movies  by python3'

import requests

import re

def get_one_page(url):

	headers={
			'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
	}
	response=requests.get(url,headers=headers)
	if response.status_code==200:
		print(response.status_code)
		return response.text
	return None

def extract_info(html):

	result=re.findall('<p\sclass="name".*?title="(.*?)".*?star">\s+(.*?)\s+</p.*?time">(.*?)<',html,re.S)
	return result


def main():
	top100=''
	for page in range(10):  #crawl 10 pages
		url='http://maoyan.com/board/4?offset=%d'%(page*10)
		html=get_one_page(url)
		top100_10=extract_info(html)  #get wanted information in one page
		print(page)
		for row in top100_10:  #save  wanted information from every page
			row_new='{}{:<30}{:>}'.format(row[0]+' '*(30-2*len(row[0])), row[1], row[2])+'\n'
			top100+=row_new
	with open('top100.txt','w') as f:  #save  data in file
		f.write(top100)


main()