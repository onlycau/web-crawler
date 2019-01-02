#!/usr/bin/env python
# -*-coding:utf-8 -*-

import re
import time
import json
import requests
import pymysql
from random import choice
from threading import Thread

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

    def save_inf(self, list, cursor):

        sql_1 = 'create table if not exists users(`id` int UNSIGNED AUTO_INCREMENT,`user_id` varchar(20),`user_name` varchar(50),`user_lv` varchar(20), `sex` varchar(20), `fan_count` varchar(20), primary key (`id`))ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;'
        sql_2 = 'insert into users(user_id, user_name, user_lv, sex, fan_count) values(%s, %s, %s, %s, %s)'
        cursor.execute(sql_1)
        cursor.executemany(sql_2, list)

#ip from https://github.com/qiyeboy/IPProxyPool
class Ip(object):

    def __init__(self):

        self.url = 'http://127.0.0.1:8000/?types=0&protocol=1&count=30&country=%E5%9B%BD%E5%86%85'

    def get_proxies(self):

        proxies = []
        r = requests.get(self.url)
        ip_ports = json.loads(r.text)
        for ip_port in ip_ports:
            proxies.append({'https':'https://%s:%s'%(ip_port[0], ip_port[1])})
        return proxies

class Net(object):

    def __init__(self):

        self.url = 'https://music.163.com/user/home'
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36','Referer': 'https://music.163.com/'}

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
        try:
            dd = soup.select('dd')[0]
        except IndexError:
            print(id, 'wrong')
            return 0
        inf = []
        inf.append(str(id))
        inf.append(dd.select('span.tit.f-ff2.s-fc0.f-thide')[0].text)
        inf.append(dd.select('span.lev.u-lev.u-icn2.u-icn2-lev')[0].text)
        inf.append(dd.select('#j-name-wrap > i')[0]['class'][-1][-1])
        inf.append(dd.select('#fan_count')[0].text)
        return inf


class Logic(object):

    def __init__(self, mysql, proxies):
        self.mysql = mysql
        self.proxies = proxies

    def crawl_one(self, net, user_begin):

        list = []
        conn = self.mysql.conn()
        for i in range(10):
            page = net.get_page(user_begin+i*1000, self.proxies)
            inf = net.handle_page(user_begin+i*1000,page)
            if inf:
                print(inf)
                list.append(tuple(inf))
        self.mysql.save_inf(list, conn.cursor())
        conn.commit()
        conn.close()


'''conn = Mysql().conn()
net = Net()
proxies = Ip().get_proxies()
print(proxies)
logic = Logic(Mysql(), proxies)

for user_begin in range(39002,39003):
    t = Thread(target=logic.crawl_one, args=(net,user_begin))
    t.start()'''
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36','Referer': 'https://music.163.com/',
'X-Forwarded-For': '127.0.0.1, 225.226.337.29'}
response = requests.get('http://httpbin.org/get', headers = headers)
print(response.text)