# -*- coding: utf-8 -*-
"""Data_mining_selenium.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16jQ1rGA7wSotNlrgsqkqwEQoNebkjFY1

#Initialization
"""

from google.colab import drive

drive.mount("/content/drive")

!pip install selenium
!apt-get update # to update ubuntu to correctly run apt install
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np

driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
driver.get("https://s.cafef.vn/Lich-su-giao-dich-vna-1.chn")
print(driver.back)

"""#Get data have dict"""

#Get data next page
def next():
    nextpage = driver.find_element(By.XPATH, "(//a[contains(text(),'>')])[2]")
    nextpage.click()

for i in range(3):
    tables = driver.find_elements('xpath', '//tr[starts-with(@id, "ctl00_ContentPlaceHolder1_ctl03_rptData")]')
    for number_table in tables:
          
            data = number_table.find_elements(By.XPATH, 'td')
            data_table = {'Ngày': data[0].text,
                          'Giá điều chỉnh': data[1].text,
                          'Giá đóng cửa': data[2].text,
                          'Giá bình quân': data[3].text,
                          'Thay đổi': data[4].text,
                          'KL1': data[6].text,
                          'GT1': data[7].text,
                          'KL2': data[8].text,
                          'GT2': data[9].text,
                          'Giá tham chiếu': data[10].text,
                          'Giá mở cửa': data[11].text,
                          'Giá cao nhất': data[12].text,
                          'Giá thấp nhất': data[13].text }
        
            print(data_table)
    next()
  
        # df = list(data_table.values())
        #print(df)
        # df = pd.DataFrame([data_table])
        # df.to_csv("VNA.csv", index = False)

