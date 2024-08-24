from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import os
import time
import pandas as pd
from intro import *

def openweb():
    if search_value:
        try:
            options = webdriver.ChromeOptions()
            options.add_experimental_option("excludeSwitches", ['enable-automation']) 
            driver = webdriver.Chrome(options=options)
            driver.get(lang)
            time.sleep(1)
            search_input = driver.find_element(By.CLASS_NAME, "nav-input").send_keys(search_value)
            driver.find_element(By.XPATH, "//div[@class = 'nav-right']//input").click()
        except Exception as err:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Something went wrong! Try again....")

        url = driver.current_url
        user_agent = str(driver.execute_script("return navigator.userAgent;"))
        time.sleep(3)
        driver.quit()
    return url

def database():
    request = requests.get(url) 
    soup = BeautifulSoup(request.content, 'html.parser')
    pages = int(soup.find("span", attrs={'class': 's-pagination-item s-pagination-disabled'}).find(string=True))
    for i in range(1, pages+1):
        syb_first = url.index("&")
        syb_last = len(url) - url[::-1].index("&")
        url2 = url[0: syb_first+1] + "page=" + str(i) + "&" + url[syb_first+1:syb_last] + "ref=sr_pg_" + str(i)
        requestt = requests.get(url2) 
        soup = BeautifulSoup(requestt.content, 'html.parser')

        price = soup.find_all("div", attrs={'data-component-type': 's-search-result'})
        print(url)

        for i in range(3, len(price)+3):
            try:
                d['title'].append(soup.find("div", attrs={'data-index': i}).find_next("span", attrs={'class': 'a-size-base-plus a-color-base a-text-normal'}).find(string=True))
            except AttributeError as err:
                continue
            d['link'].append(soup.find("div", attrs={'data-index': i}).find_next("a", attrs={'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'}).get('href'))
            try:
                d['rating'].append(soup.find("div", attrs={'data-index': i}).find_next("span", attrs={'class': 'a-icon-alt'}).find(string=True))
            except AttributeError as err:
                continue
            try:
                d['price'].append(soup.find("div", attrs={'data-index': i}).find_next("span", attrs={'class': 'a-offscreen'}).find(string=True))
            except AttributeError as err:
                continue

search_value = intro()
lang = region()

url = openweb()
d = {"title":[], "price":[], "rating":[], "link":[]}

database()

df = pd.DataFrame(d)
df.to_excel(search_value + '.xlsx')