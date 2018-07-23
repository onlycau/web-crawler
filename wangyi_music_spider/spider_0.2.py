#!/usr/bin/env python
# -*-coding:utf-8 -*-

import time
import json
import requests
import pymysql


api_address = 'http://music.163.com/api/v1/resource/comments/R_SO_4_'
data = {'limit': 100, 'offset': 0}
offset = 117900
total = 2113122
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}

db = pymysql.connect(host = 'localhost', user = 'music_163', password = 'password' ,db = 'music_163_comments', charset='utf8mb4')
cursor = db.cursor()


def get_data(song_id, data):

        url = api_address + song_id
        try :
            r = requests.get(url, headers=headers, params=data, timeout=1)
            if r.status_code == 200:
                return r.text
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            global NETWORK_STATUS
            NETWORK_STATUS = False # 请求超时改变状态

            if NETWORK_STATUS == False:
                for i in range(1, 10):
                    print('请求超时，第%d次重复请求: ' % i)
                    r = requests.get(url, headers=headers, params=data, timeout=1)
                    if r.status_code == 200:
                        return r.text


def analytical_data(page):

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

        sql = 'insert into song_186016(user_id,user_name, avatar_url, user_comment, like_count, be_replied, reply_user_id, reply_user_name, reply_comment) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(sql, (user_id, user_name, avatar_url, user_comment, like_count, be_replied, reply_user_id, reply_user_name, reply_comment))
    db.commit()


while offset<total:
    data['offset'] = offset
    time.sleep(1)
    print(offset)
    text = get_data('186016', data)
    analytical_data(text)
    offset += data.get('limit')

db.close()
