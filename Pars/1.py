from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

driver=webdriver.Chrome()

driver.get("https://5element.by/products/830028-smartfon-apple-iphone-15-pro-1tb-belyy-titan-mtur3j-a")

data = []
time.sleep(2)
try:
        title = driver.find_element(By.CLASS_NAME, value="section-heading__title").text
        price = driver.find_element(By.CLASS_NAME, value="pp-price")
        print(title)
        driver.get(f'{'https://5element.by/products/830028-smartfon-apple-iphone-15-pro-1tb-belyy-titan-mtur3j-a'}#characteristics')
        time.sleep(2)
        try:
            brend = driver.find_element(By.XPATH, value='/html/body/div[2]/main/div[3]/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div[1]/div/table[1]/tbody/tr[1]/td[2]/b/a').text
            print(brend)
        except:
            print("brend crash")
            brend = None
        try:
            Gh = driver.find_element(By.XPATH, value="/html/body/div[2]/main/div[3]/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div[1]/div/table[2]/tbody/tr[7]/td[2]/b").text
            print(Gh)
        except:
            print("Gh crash")
            Gh = None
        try:
            memory = driver.find_element(By.XPATH, value="/html/body/div[2]/main/div[3]/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div[1]/div/table[3]/tbody/tr[4]/td[2]/b").text
            
            print(memory)
        except:
            memory = None
            print("memory crash")
except:
        title = None
data.append({
        "url": "https://5element.by/products/830028-smartfon-apple-iphone-15-pro-1tb-belyy-titan-mtur3j-a",
        "Название": title,
        "Бренд": brend,
        "Частота обновления экрана": Gh,
        "Объем встроенной памяти" : memory
    })

driver.quit()
df = pd.DataFrame(data)
df.to_csv("links.csv", index=False, encoding="utf-8-sig")