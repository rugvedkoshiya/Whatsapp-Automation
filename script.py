import csv
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import time
from urllib.parse import urlencode

# link = "https://web.whatsapp.com/"
msg = {"text": "Hii \n why *ggs*"}
print(urlencode(msg))
# link = "https://web.whatsapp.com/send?phone=919876543210&text=hehe&app_absent=0"
link = "https://web.whatsapp.com/send?phone=919876543210&%s&app_absent=0"
link = link%urlencode(msg)

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\DELL\\AppData\\Local\\Google\\Chrome\\User Data")
# options.add_argument("disable-infobars");
options.add_argument("--start-maximized");
driver = webdriver.Chrome(executable_path='./chromedriver', options=options)


# driver = webdriver.Chrome('./chromedriver')
driver.get(link)
try:
    print("hehe")
    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "_4sWnG")))
    # element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "_1Jn3C")))
    print("huhu")
    # a = driver.find_elements_by_class_name("content")
    element.click()
except:
    pass

time.sleep(100)
# driver.get("https://google.com")