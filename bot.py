from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
from random import randint
from random import choice
import random
import sys
import emoji



#from selenium.webdriver.common.keys import Keys
import os
import time

class InstagramBot:
    username = ''
    password = ''

    hashtags = ['wrxnation', 'stancenation', 'boost', 'wrxdaily_', 'sweetsubies', 'awdarmy', 'wrx', 'jdm', 'subie']
    comments = [emoji.emojize('Dope shot! :thumbs_up'), 'This is heattttt', 'yo this is niceeeee', 'love this', 'this is a great picture', 'your stuff is flamee', 'this is a killer shot', 'so dopee', 'bringing the heatt']
    links = []
    price = 0.0

    # def __init__(self, username, password):
    #     self.username = username
    #     self.password = password
    def __init__(self):
        self.username = ''
        self.password = ''
        self.driver = webdriver.Chrome('./chromedriver')
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
        time.sleep(1)

        # nn_notification = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
        # nn_notification.click()
        # time.sleep(1)
        ui.WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()

    def hustle(self):
        self.explore()
        # self.getTopPosts()
        # self.execute()
        self.execute2()
        self.finalize()

    def explore(self): 
        self.driver.get('https://instagram.com/explore')
        time.sleep(2)

        links = self.driver.find_elements_by_tag_name('a')
        condition = lambda link: '.com/p/' in link.get_attribute('href')
        valid_links = list(filter(condition, links))
        print(valid_links)
        for i in range(0,9):
                link = valid_links[i].get_attribute('href')
                if link not in self.links:
                    self.links.append(link)

    
    def getTopPosts(self):
        for hashtag in self.hashtags:
            self.driver.get('https://instagram.com/explore/tags/' + hashtag + '/')
            time.sleep(2)

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
            print(taglist)

        

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
        #print (self.price)
        self.driver.close()
        sys.exit()

    


if __name__ == '__main__':
    ig_bot = InstagramBot()
    print(ig_bot.username)    
