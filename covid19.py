from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time
# 디버그 모드인 크롬에 접속 
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
chrome_driver = "chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
print(" start url ")
# driver.get("https://corona-live.com/")
driver.get('https://apiv2.corona-live.com/stats.json?timestamp=1608254279953')

page_s = driver.page_source
print(page_s)

