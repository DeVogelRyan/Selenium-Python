from selenium import webdriver
import time

searchIput = input("Search: ")

PATH = "/usr/bin/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get('https://www.youtube.com/')

time.sleep(1)

button = driver.find_element_by_xpath('/html/body/div/c-wiz/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button/div[2]')
button.click()

time.sleep(1)

searchbox = driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/yt-upsell-dialog-renderer/div/div[3]/div[1]/yt-button-renderer/a/paper-button/yt-formatted-string')
searchbox.click()

password = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
password.send_keys(searchIput)

button = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button')
button.click()