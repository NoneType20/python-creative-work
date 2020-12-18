from selenium import webdriver
import time
from bs4 import BeautifulSoup
chrome_driver = "chromedriver.exe"
driver = webdriver.Chrome(chrome_driver)
url_ = 'https://corona-live.com/'
URL = "https://corona-live.com/"
driver.get(URL)
time.sleep(5)

while True :
    try : 
        html = driver.page_source 
        soup = BeautifulSoup(html , 'html.parser')
    
    
        nn = soup.select('div.Layout__SBox-c6bc3z-0.ekTmfG.Layout__SFlex-c6bc3z-1.iDxwnx.Layout__SRow-c6bc3z-2.Maibk > div.Layout__SBox-c6bc3z-0.kiyQoo.Layout__SFlex-c6bc3z-1.YyXdR.Layout__SRow-c6bc3z-2.Maibk')
        nnnd = nn.find_all('div')
        print(nn)
        a = int(nnnd[1].get_text())
        if a >= 1000 : 
           driver.get(url_)
           break
        print(a)
        time.sleep(180)
    except : 
        print("크롤링 실패")


