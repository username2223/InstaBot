from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import pandas as pd
from random import randint
from random import choice
import random
import sys

import requests
import json
import re



#from selenium.webdriver.common.keys import Keys
import os
import time

class InstagramBot:
    username = 'blu_baru'
    password = 'TestPass'
    hashtagList = []

    hashtags = ['wrxnation', 'stancenation', 'boost', 'wrxdaily_', 'sweetsubies', 'awdarmy', 'wrx', 'jdm', 'subie']
    # comments = [emoji.emojize('Dope shot! :thumbs_up'), 'This is heattttt', 'yo this is niceeeee', 'love this', 'this is a great picture', 'your stuff is flamee', 'this is a killer shot', 'so dopee', 'bringing the heatt']
    links = []
    price = 0.0

    # def __init__(self, username, password):
    #     self.username = username
    #     self.password = password
    def __init__(self):
        self.username = 'blu_baru'
        self.password = 'TestPass'
        # self.driver = webdriver.Chrome('./chromedriver')
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.login()
        self.hustle()

    
    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)

        un_field = self.driver.find_element_by_name('username')
        un_field.clear()
        un_field.send_keys(self.username)
        time.sleep(1)

        pw_field = self.driver.find_element_by_name('password')
        pw_field.clear()
        pw_field.send_keys(self.password)
        time.sleep(1)
        "//input[@name='password']"
        #//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button
        # /html/body/div[4]/div/div/div[3]/button[2]
        lg_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        lg_button.click()
        time.sleep(10)

        # nn_notification = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
        # nn_notification.click()
        # time.sleep(1)
        nn_button = self.driver.find_element_by_xpath("//button[text()='Not Now']")
        nn_button.click()
        time.sleep(5)
        ui.WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()
        # sqdOP yWX7d    y3zKF     

    def hustle(self):
        # self.getLinks()
        self.explore()
        # self.getTopPosts()
        # self.execute()
        self.execute2()
        self.finalize()
   
    def getLinks(self):
        url = 'https://www.instagram.com/explore/tags/beans/'
        
        page = requests.get(url)
        print(page)
        time.sleep(2)
        data = BeautifulSoup(page.text, 'html.parser')
        print('data is next')
        print(data)
        
        links = []
        edges = tagpage[0].get('graphql',{}).get('hashtag',{}).get('edge_hashtag_to_media',{}).get('edges',[])
        for e in edges:
            links.append("https://www.instagram.com/p/"+e.get('node',{}).get('shortcode','')+'/')

        print(links)
    
    def explore(self): 
        self.driver.get('https://instagram.com/explore')
        time.sleep(2)

        # links = self.driver.find_elements_by_tag_name('a')
        # links = self.driver.find_element(By.TAG_NAME, '//a')
        # links = self.driver.find_element_by_class_name('QzzMF.Igw0E.IwRSH.eGOV_._4EzTm')

        # hrefDiv = BeautifulSoup.find_all('div', attrs={'class' : 'QzzMF.Igw0E.IwRSH.eGOV_._4EzTm'})
        print("ran explore")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        
        soup = BeautifulSoup(self.driver.execute_script('return document.documentElement.outerHTML'), 'lxml')
        newLinks =[]
        for tag in soup.find_all('a', href=True):
            newLinks.append(tag['href'])

        print(newLinks)

        #links = soup.findAll(lambda tag: len(tag.attrs) == 4)
        #print(links)
        # validAtag=[]
        # for link in links:
        #     validAtag.append(link.get('href'))

        # print(validAtag)                
                                                                                                 
        # # print(links)
        condition = lambda link: '/p/' in link
        valid_links = list(filter(condition, newLinks))
        print(valid_links)
        time.sleep(1)
        
        return valid_links

        # automate truck owner and truck and sending correct emails at correct time to correct people and  vendor sign up form.  
        # for i in range(0,9):
        #     link = valid_links[i].get_attribute('href')
        #     if link not in self.links:
        #         self.links.append(link)
        #     if i == 8:
        #         self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # link = valid_links[1].get_attribute('href')
        # print(link)
       

    def makeDict(self,tl):
        flat_list = []
        _ = [flat_list.extend(item) if isinstance(item, list) else flat_list.append(item) for item in tl if item]
        count = dict((x,flat_list.count(x)) for x in set(flat_list))
        tl = count
        return tl
        # print(count)


    def getTopPosts(self):
        for hashtag in self.hashtags:
            self.driver.get('https://instagram.com/explore/tags/' + hashtag + '/')
            # time.sleep(2)

            links = self.driver.find_elements_by_tag_name('a')
            condition = lambda link: '.com/p/' in link.get_attribute('href')
            valid_links = list(filter(condition, links))
            #print(valid_links)
            # rand = [randint(0, 9) for p in range(0, 9)]
            for i in range(0,9):
                link = valid_links[i].get_attribute('href')
                if link not in self.links:
                    self.links.append(link)
    def execute(self):
        for link in self.links:
            self.driver.get(link)
            time.sleep(1)

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)

            # self.comment()
            # time.sleep(2)

            self.like()
            time.sleep(2)
            
            # self.price += 0.02
            sleeptime = randint(18,28)
            time.sleep(sleeptime)

    def execute2(self):
        for link in self.links:
            self.driver.get(link)
            time.sleep(1)

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)

            soup = BeautifulSoup(self.driver.page_source, "lxml")
            desc = " "
            time.sleep(1)

            for item in soup.findAll("a"):
                desc = desc + " " + str(item.string)

            taglist = desc.split()
            taglist = [x for x in taglist if x.startswith('#')]
            index = 0
            while index < len(taglist):
                taglist[index] = taglist[index].strip('#')
                index += 1
            # self.hashtagList.append(taglist)
            for tag in taglist:
                self.hashtagList.append(tag)

            # print(taglist)

        

            # self.comment()
            # time.sleep(2)

            # self.like()
            # time.sleep(2)
            
            # self.price += 0.02
            sleeptime = randint(18,28)
            time.sleep(sleeptime)

    def comment(self):
        comment_input = lambda: self.driver.find_element_by_tag_name("textarea")
        comment_input().click()
        comment_input().clear()

        comment = choice(self.comments)
        for letter in comment:
            comment_input().send_keys(letter)
            delay = randint(1, 7) / 30
            time.sleep(delay)
        #//*[@id="react-root"]/section/main/div/div/article/div[2]/section[3]/div/form/button
        # //*[@id="react-root"]/section/main/div/div/article/div[2]/section[1]/span[1]/button
        comment_input().send_keys(Keys.RETURN)

    def like(self):
        like_button = lambda: self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[1]/span[1]/button')
        time.sleep(1)
        like_button().click()
        time.sleep(1)

    def finalize(self):
        print(self.makeDict(self.hashtagList))
        # print (self.price)
        # print(self.hashtagList)
        self.driver.close()
        sys.exit()

    


if __name__ == '__main__':
    ig_bot = InstagramBot()
    print(ig_bot.username)    
