#!/usr/bin/env python3
# -*-coding:utf-8 -*-

import time
import re
import json
from random import choice
from threading import Thread

import pymysql
import requests
import bs4
from selenium import webdriver
from selenium.webdriver.common.by import By


class Net(object):

    def __init__(self):
        self.url = 'https://music.163.com/#/user/home'
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
        self.proxies = self.get_ip()

    #Retun a list contain playlist urls.
    def get_playlist(self, name_id):

        playlist_urls = []
        url = self.url + '?id=' + name_id
        browser = webdriver.Chrome()
        browser.get(url)
        browser.switch_to.frame('g_iframe')
        time.sleep(3)
        text = browser.find_elements(By.XPATH, '//ul[@class="m-cvrlst f-cb"]//a[@class="msk"]')  #Find where are the playlist urls
        for playlist in text:
            playlist_urls.append(playlist.get_attribute('href'))

        browser.close()
        return playlist_urls

    #Return a list contain song http://music.163.com/api/v1/resource/comments/R_SO_4_urls.
    def get_songlist(self, url):

        song_urls = []
        browser = webdriver.Chrome()
        browser.get(url)
        browser.switch_to.frame('g_iframe')
        time.sleep(3)
        songs = browser.find_elements(By.XPATH, '//table//td[2]/div/div/div/span/a')
        for song in songs:
            song_urls.append(song.get_attribute('href'))
        browser.close()
        return song_urls

    def get_data(self, song_id, params):

        url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_' + song_id
        try:
            proxies=choice(self.proxies)
            r = requests.get(url, headers=self.headers, proxies=proxies, params=params, timeout=1)
            if r.status_code == 200:
                return r.text
        except(requests.exceptions.Timeout, requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError):
            NETWORK_STATUS = False
            if NETWORK_STATUS is False:
                for i in range(1, 10):
                    print('请求超时，第%d次重复请求: ' % i)
                    proxies = choice(self.proxies)
                    r = requests.get(url, headers=self.headers, proxies=proxies, params=params, timeout=1)
                    if r.status_code == 200:
                        return r.text

    def get_ip(self):
        url = "http://www.xicidaili.com/nn"
        r = requests.get(url,headers=self.headers)
        soup = bs4.BeautifulSoup(r.text, 'html.parser')
        data = soup.table.find_all("td")
        ip_compile = re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td>')    # 匹配IP
        port_compile = re.compile(r'<td>(\d+)</td>')                # 匹配端口
        https_compile = re.compile(r'<td>(HTTP\w*)</td>')
        ip = re.findall(ip_compile, str(data))       # 获取所有IP
        port = re.findall(port_compile, str(data))   # 获取所有端口
        way = re.findall(https_compile,str(data))
        ip = [":".join(i) for i in zip(ip, port)]
        pros = []
        for i in range(len(way)):
            pro = {way[i]: ip[i]}
            pros.append(pro)
        return pros

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

    def create_song_table(self, song_id, conn):

        table_name = 'song_' + song_id
        sql = 'create table if not exists %s(`comment_id` int UNSIGNED AUTO_INCREMENT,`song_name` VARCHAR(20) ,`user_id`   varchar(100) ,`user_name` VARCHAR(100) ,`avatar_url` VARCHAR(100) ,`user_comment`   varchar(400) ,`like_count`  int(10) default 0,`be_replied`     int default 0,`reply_user_id` int(10)   default 0,`reply_user_name` varchar(100)   ,`reply_comment` VARCHAR(400) ,`is_hot_comment` int default 0,primary key (`comment_id`))ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;' % table_name
        conn.cursor().execute(sql)
        conn.commit()

    def save_song_url(self, conn, urls, table):
        sql = 'insert into %s (song_id, url) values(%s, %s)'
        for url in urls:
            song_id = re.search(r'id=(\d*)', url).group(1)
            sql = 'insert into %s (song_id, url) values(\'%s\', \'%s\')'%(table, song_id, url)
            print(sql)
            conn.cursor().execute(sql)
        conn.commit()

    def save_comments(self, page, conn, song_id):

        cursor = conn.cursor()
        comments = json.loads(page).get('comments')
        for comment in comments:
            user_id = comment.get('user').get('userId')
            user_name = comment.get('user').get('nickname')
            avatar_url = comment.get('user').get('avatarUrl')
            user_comment = comment.get('content')
            like_count = int(comment.get('likeCount', '0'))
            reply = comment.get('beReplied')

            be_replied = 0
            reply_user_id = 0
            reply_user_name = ''
            reply_comment = ''
            if reply:
                be_replied = 1
                reply_user_id = int(reply[0].get('user').get('userId'))
                reply_user_name = reply[0].get('user').get('nickname')
                reply_comment = reply[0].get('content')

            sql = 'insert into song_%s(user_id,user_name, avatar_url, user_comment, like_count, be_replied, reply_user_id, reply_user_name, reply_comment) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
            cursor.execute(sql, (song_id, user_id, user_name, avatar_url, user_comment, like_count, be_replied, reply_user_id, reply_user_name, reply_comment))
        conn.commit()
        cursor.close()


class Logic(object):

    def __init__(self, mysql):
        self.mysql = mysql

    def crawl_one(self, song_id):

        print(song_id)
        net = Net()
        conn = self.mysql.conn()
        data = {
            'limit': 100,
            'offset': 0
        }

        self.mysql.create_song_table(str(song_id), conn)
        text = net.get_data(str(song_id), data)
        offset = 0
        total = int(json.loads(text).get('total'))
        print(total)
        while offset < total:
            data['offset'] = offset
            print(song_id, offset)
            text = net.get_data(str(song_id), data)
            self.mysql.save_comments(text, conn, song_id)
            offset += data.get('limit')
        conn.close()

    def get_song_id(self):
        playlist_urls = Net().get_playlist('78443113')
        song_id_list = []
        for url in playlist_urls:
            song_list_urls = Net().get_songlist(url)
            for url in song_list_urls:
                song_id = re.search(r'id=(\d*)', url)
                print(song_id.group(1))
                song_id_list.append(song_id.group(1))
        return song_id_list

    def create_thread(self, song_id):

        t = Thread(target=self.crawl_one, args=(song_id,))
        t.start()


def main(user_id):

    mysql = Mysql()
    logic = Logic(mysql)
    conn = mysql.conn()
    cursor = conn.cursor()
    sql = 'select song_id from playlist_78443113'
    cursor.execute(sql)
    song_id_list = cursor.fetchall()
    for i in range(10):
        logic.create_thread(int(song_id_list[i][0]))


if __name__ == '__main__':
    main('78443113')
