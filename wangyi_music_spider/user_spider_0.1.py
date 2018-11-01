#!/usr/bin/env python
# -*-coding:utf-8 -*-

import re
import time
import json
import requests
import pymysql
from random import choice

from lxml import etree
from bs4 import BeautifulSoup


class Mysql(object):

    def __init__(self):
        self.host = 'localhost'
        self.user = 'music_163'
        self.password = 'password'
        self.db = 'music_163_users'
        self.charset = 'utf8mb4'  # To save emoji

    def conn(self):

        conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, charset=self.charset)
        return conn


class Ip(object):

    def __init__(self):

        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/67.0.3396.87 Safari/537.36'}

    # Return a list with ip(dict) from net.
    def get_proxies_net(self):
        proxies = []
        url = "http://www.xicidaili.com"
        response = requests.get(url, headers=self.headers)
        html = etree.HTML(response.text)
        ip = html.xpath(r'//table//tr/td[2]')
        port = html.xpath(r'//table//tr/td[3]')
        http_s = html.xpath(r'//table//tr/td[6]')
        for i in range(len(ip)):
            ip_port = ip[i].text + ':' + port[i].text
            if http_s[i].text != 'socks4/5':
                pro = {http_s[i].text: ip_port}
                proxies.append(pro)
        return proxies

    # Return a list with ip(dict) from mysql.
    def get_proxies_mysql(self, conn):
        cursor = conn.cursor()
        sql = 'select * from proxies'
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        proxies = []
        for item in data:
            proxies.append({item[1]: item[2]})
        return proxies

    def save_proxies(self, conn, proxies):
        cursor = conn.cursor()
        sql_1 = 'create table if not exists proxies(`id` int UNSIGNED AUTO_INCREMENT,`http_s` varchar(20),`ip` varchar(50),primary key (`id`));'
        cursor.execute(sql_1)
        sql_2 = 'insert into proxies(http_s, ip) values(%s, %s)'
        for item in proxies:
            cursor.execute(sql_2, (list(item.keys())[0], list(item.values())[0]))
        cursor.close()
        conn.commit()
        return 1


class Net(object):

    def __init__(self):

        self.url = 'https://music.163.com/user/home'
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML,\
        like Gecko) Chrome/67.0.3396.87 Safari/537.36'}

    def get_page(self, id, proxies):
        params = {'id': id}
        try:
            proxies = choice(proxies)
            response = requests.get(self.url, headers=self.headers,proxies=proxies, params=params)
            if response.status_code == 200:
                return response.text
        except requests.exceptions.ConnectionError:
            response = requests.get(self.url, headers=self.headers, proxies=proxies, params=params)
            if response.status_code == 200:
                return response.text

    def handle_page(self, id, page):
        soup = BeautifulSoup(page, 'lxml')
        text = soup.select('dd')[0]
        user_id = id
        user_name = text.select('span')[0].text
        user_lv = text.select('span')[2].text
        follow_count = text.select('strong')[1].text
        fan_count = text.select('strong')[2].text
        area = text.select('span')[6].text[5:-1]
        sex = text.select('i')[2].attrs['class'][-1][-1]
        listen_number = soup.select('h4')[0].text[4:-1]
        print(listen_number)




conn = Mysql().conn()
proxies = Ip().get_proxies_mysql(conn)
net = Net()
page = net.get_page(39002, proxies)
net.handle_page(39002, page)
'''proxies = Ip().get_proxies_net()
page = Net().get_page(39002,proxies)
soup = BeautifulSoup(page, 'lxml')
body = soup.find_all(attrs={'id': 'fan_count'})
print(body[0].text)'''
