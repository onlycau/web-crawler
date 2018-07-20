#!/usr/bin/env python
# -*-coding:utf-8 -*-

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Get songs' id from rank's page.
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

# Get and save comment.
def get_comments(song_id):

    url = 'https://music.163.com/#/song?id=%s' % song_id
    browser = webdriver.Chrome()
    browser.get(url)
    browser.implicitly_wait(10)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'g_iframe')))
    browser.switch_to.frame('g_iframe')
    page_number = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="m-cmmt"]/div[3]//a[last()-1]')))
    for i in range(int(page_number.text)):

        time.sleep(3)
        elements = browser.find_elements(By.XPATH, '//*[@class="itm"]')
        with open('comments', 'a') as f:
            for element in elements:
                f.write(element.text)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="m-cmmt"]/div[3]//a[last()]')))
        time.sleep(3)
        button.click()


def main():

    url = 'https://music.163.com/#/user/songs/rank?id=361666960' 
    songs_id = get_songs_id(url)
    for song_id in songs_id:
        get_comments(song_id)