#!/usr/bin/env python
# -*-coding:utf-8 -*-

import time
import re

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


class Net(object):

    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}

    def get_playlist(self, name_id):

        song_list_urls = []
        url = self.url + '?id=' + name_id
        browser = webdriver.Chrome()
        browser.get(url)
        browser.switch_to.frame('g_iframe')
        time.sleep(3)
        song_lists = browser.find_elements(By.XPATH, '//ul[@class="m-cvrlst f-cb"]//a[@class="msk"]')
        for song_list in song_lists:
            song_list_urls.append(song_list.get_attribute('href'))

        browser.close()
        return song_list_urls

    def get_song_list(self, url):

        song_urls = []
        browser = webdriver.Chrome()
        browser.get(url)
        browser.switch_to.frame('g_iframe')
        time.sleep(3)
        songs = browser.find_elements(By.XPATH, '//table//td[2]/div/div/div/span/a')
        print(songs)
        for song in songs:
            song_urls.append(song.get_attribute('href'))
        browser.close()
        return song_urls

        def get_comments(self, song_id, data):

                url = api_address + song_id
                try:
                    r = requests.get(url, headers=self.headers, params=data, timeout=1)
                    if r.status_code == 200:
                        return r.text
                except(requests.exceptions.Timeout, requests.exceptions.ConnectionError):
                    global NETWORK_STATUS
                    NETWORK_STATUS = False 

                    if NETWORK_STATUS == False:
                        for i in range(1, 10):
                            print('请求超时，第%d次重复请求: ' % i)
                            r = requests.get(url, headers=headers, params=data, timeout=1)
                            if r.status_code == 200:
                                return r.text

class Mysql(object):

    def __init__(self):
        self.host = 'localhost'
        self.user = 'music_163'
        self.password = 'password'
        self.db = 'music_163_comments'
        self.charset = 'utf8mb4'

    def conn(self):
        conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, charset=self.charset)
        return conn





a = Net('https://music.163.com/#/user/home')
song_list_urls = a.get_playlist('78443113')
song_id_list = []
for url in song_list_urls:
    print(url)
    song_id = re.search(r'id=(\d*)', url)
    print(song_id.group(1))
    song_id_list.append(song_id.group(1))
print(song_id_list)