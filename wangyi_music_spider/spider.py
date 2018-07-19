#!/usr/bin/env python
# -*-coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By


# Get songs' id from page.
def get_songs_id(url):

    songs_id = ['']
    browser = webdriver.Chrome()
    browser.get(url)
    browser.switch_to.frame('g_iframe')
    pages = browser.find_elements(By.XPATH, '//ul/li//span[@class="ply "]')
    for page in pages:
        song_id = page.get_attribute('data-res-id')
        print(song_id)
        songs_id.append(song_id)
    browser.close()
    return songs_id


def get_comments(songs_id):



def main():

    url = 'https://music.163.com/#/user/songs/rank?id=78443113'
    songs_id = get_songs_id(url)