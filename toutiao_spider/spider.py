#!/usr/bin/env python# -*-coding:utf-8 -*-

import requests
import re
import os

'''
A small spider crawling the focus images of today's headlines
'''

def get_page():

    url = 'https://www.toutiao.com/api/pc/focus/'
    headers = {
        'Host':'www.toutiao.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',}
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error',e.args)


def get_image_urls(json):

    urls=re.findall(r'image_url.*?//(.*?)\'',str(json),re.S)
    return urls


def save_image(urls):

    if not os.path.exists('images'):
        os.mkdir('images')
    os.chdir('images')
    for item in urls:
        try:
            response=requests.get('https://'+item)
            if response.status_code==200:
                with open(item[-20:],'wb') as f:
                    f.write(response.content)
        except requests.ConnectionError:
            print('Failed to save Image')

def main():


    page = get_page()
    urls = get_image_urls(page)
    save_image(urls)

main()
