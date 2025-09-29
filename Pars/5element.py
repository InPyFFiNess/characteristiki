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
import random
from concurrent.futures import ThreadPoolExecutor
import threading

chrome_version = random.randint(110, 140)
windows_version = random.randint(10, 11)
opts = Options()
opts.add_argument(f"user-agent=Mozilla/5.0 (Windows NT {windows_version}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=opts)

#driver.get("https://5element.by/catalog/377-smartfony")

def get_links_on_page():
    elements = driver.find_elements(By.CLASS_NAME, value = 'c-text')
    #"#container > div > div > div > div > div.catalog-content > div.catalog-wrapper > div > div > div.catalog-form__tabs > div > div > div > div > div.catalog-form__filter-part.catalog-form__filter-part_2 > div.catalog-form__offers > div > div:nth-child(1) > div > div > div.catalog-form__offers-part.catalog-form__offers-part_data > div.catalog-form__description.catalog-form__description_primary.catalog-form__description_base-additional.catalog-form__description_font-weight_semibold.catalog-form__description_condensed-other > a"
    ads_list = []
    for element in elements:
        ads_list.append(element.get_attribute('href'))
    return ads_list

links = []

for i in range(3):
    driver.get(f"https://5element.by/catalog/377-smartfony?page={i+1}")
    time.sleep(2)
    links += get_links_on_page()

driver.quit()

print(len(links))
data = []
lock = threading.Lock()

def parse_link(link):
    chrome_version = random.randint(110, 140)
    windows_version = random.randint(10, 11)
    opts = Options()
    opts.add_argument(f"user-agent=Mozilla/5.0 (Windows NT {windows_version}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/537.36")

    local_driver = webdriver.Chrome(options=opts)
    try:
        local_driver.get(link)
        time.sleep(2)
        title = local_driver.find_element(By.CLASS_NAME, "section-heading__title").text
        price = local_driver.find_element(By.CLASS_NAME, "pp-price").text

        local_driver.get(f'{link}#characteristics')
        time.sleep(2)

        try:
            brend = local_driver.find_element(By.XPATH, '/html/body/div[2]/main/div[3]/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div[1]/div/table[1]/tbody/tr[1]/td[2]/b/a').text
        except:
            brend = None
        try:
            Gh = local_driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div[1]/div/table[2]/tbody/tr[7]/td[2]/b").text
        except:
            Gh = None
        try:
            memory = local_driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div[1]/div/table[3]/tbody/tr[4]/td[2]/b/a").text
        except:
            memory = None

        with lock:
            data.append({
                "url": link,
                "Название": title,
                "Бренд": brend,
                "Частота обновления экрана": Gh,
                "Объем встроенной памяти": memory,
                "Цена": price
            })
    except Exception as e:
        print(f"Ошибка при обработке {link}: {e}")
    finally:
        local_driver.quit()

with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(parse_link, links)

df = pd.DataFrame(data)
df.to_csv("links.csv", index=False, encoding="utf-8-sig")
