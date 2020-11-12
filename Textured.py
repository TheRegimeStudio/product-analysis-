#%% md

### Go to Url : ' https://www.target.com/c/textured-hair-care/-/N-4rsrf '
### Click the first product's title
### On the next page find where it says 'drug facts' and click
### Scrape 'Inactive Ingredients' body
#%%
import time
import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
import pandas as pd
import csv


#%%



driver_path = '/Users/Yan/Downloads/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)

df = pd.DataFrame(columns=['Brand', 'Name', 'Beauty_Purpose', 'Product_Form', 'Ingredients','Label', 'URL']) # creates master dataframe

def scrollDown(driver, n_scroll):
    body = driver.find_element_by_tag_name("body")
    while n_scroll >= 0:
        body.send_keys(Keys.PAGE_DOWN)
        n_scroll -= 1
    return driver



url = 'https://www.target.com/c/textured-hair-care/leave-in-conditioners/-/N-4rsrfZcrx6h?type=products&Nao='
driver.get(url)
time.sleep(10)

browser = scrollDown(driver, 5)
time.sleep(5)

browser = scrollDown(driver, 5)
time.sleep(5)

browser = scrollDown(driver, 5)
time.sleep(5)

browser = scrollDown(driver, 5)
time.sleep(5)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight= 23452)")  # 23452 - page height
time.sleep(10)



#%%
##code works to click  different pages

def links_list():
    links = []
    xpath = ('//*[@class="Row-uds8za-0 fMpYji h-padding-t-tight"]')
    elems = driver.find_elements_by_xpath('//*[@data-test="product-title"]')

    for elem in elems:
        href = elem.get_attribute('href')
        links.append(href)
        if href is None:
            print(None)
    return links
 list = links_list()
print (list)


for i in range(len(list) + 1):
    url = list[i]
    driver.get(url)
    time.sleep(5)

    Brand = driver.find_element_by_xpath('//*[@data-test="product-title"]').text
    Name = driver.find_element_by_xpath('//*[@class="Link-sc-1khjl8b-0 gMFbJt"]').text[9:]


#everything works above

    #print(Brand,Name)

    brands_list = []
    for b in range(len(Brand)):
        brands_list.append(Brand[b])

    name_list = []
    for n in range(len(Name)):
        name_list.append(Name[n])

    data_tuples = list(zip(brands_list[1:], name_list[1:]))  # list of each brand name and product's name paired together
    temp_df = pd.DataFrame(data_tuples, columns=['Brand', 'Name'])  # creates dataframe of each tuple in list
    df = df.append(temp_df)  # appends to master dataframe
print(df)
driver.close()
