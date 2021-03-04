# script to serach for given video title and play the video on youtube :)
# known issue: if there is an ad before video,
# timer calculations are messed up, and video cuts off prematurely

import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Firefox()

browser.get('https://www.youtube.com/')

elem = browser.find_element_by_class_name('ytd-searchbox-spt')
elem.click()

actions = ActionChains(browser)
actions.send_keys('Postman Pat intro theme' + Keys.RETURN)
actions.perform()
time.sleep(2)

vid = browser.find_element_by_class_name('title-and-badge')
vidstring = vid.find_element_by_id('video-title')
aria_label = vidstring.get_attribute("aria-label")
timeser=re.search("years ago ([0-9]) [a-zA-Z]{0,}, ([0-9]{0,})", aria_label)

timemin=int(timeser.group(1))
timesec=int(timeser.group(2))

timetot=timemin*60+timesec

print("Seconds of vid: " + str(timetot))

vid.click()
time.sleep(timetot+8)

browser.quit()
