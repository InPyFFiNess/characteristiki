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

driver.get("https://5element.by/catalog/377-smartfony")

def get_links_on_page():
    elements = driver.find_elements(By.CLASS_NAME, value = 'c-text')
    #"#container > div > div > div > div > div.catalog-content > div.catalog-wrapper > div > div > div.catalog-form__tabs > div > div > div > div > div.catalog-form__filter-part.catalog-form__filter-part_2 > div.catalog-form__offers > div > div:nth-child(1) > div > div > div.catalog-form__offers-part.catalog-form__offers-part_data > div.catalog-form__description.catalog-form__description_primary.catalog-form__description_base-additional.catalog-form__description_font-weight_semibold.catalog-form__description_condensed-other > a"
    ads_list = []
    for element in elements:
        ads_list.append(element.get_attribute('href'))
    return ads_list

links = get_links_on_page()

df = pd.DataFrame(links, columns=["Link"])
df.to_csv("links.csv", index=False, encoding="utf-8-sig")
print("Ссылки сохранены")
print(len(links))

