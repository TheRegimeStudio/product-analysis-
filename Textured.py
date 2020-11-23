# %%
"""
Created on Sat Nov 22 3:55 PM 2020
@author: Yan Lawrence

"""
# %%
import time
import re
import operator
from functools import reduce
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
import pandas as pd
import csv

# %%

driver_path = '/Users/Yan/Downloads/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)

df = pd.DataFrame(
    columns=['Links', 'Brand', 'Name', 'Ingredients'])


def scrollDown(driver, n_scroll):  # we wants to scroll function
    body = driver.find_element_by_tag_name("body")
    while n_scroll >= 0:
        body.send_keys(Keys.PAGE_DOWN)
        n_scroll -= 1
    return driver


# %%#

## function to get all the product pages from each category

def num_pages():
    pages = []
    category = [
        [f'https://www.target.com/c/textured-hair-care/leave-in-conditioners/-/N-4rsrfZcrx6h?type=products&Nao={i * 24}'
         for i in range(0, 3)],
        ['https://www.target.com/c/textured-hair-care/deep-conditioners/-/N-4rsrfZtq8xq?type=products&Nao=0'],
        [f'https://www.target.com/c/textured-hair-care/hair-shampoos/-/N-4rsrfZlga4c?type=products&Nao={i * 24}' for i
         in
         range(0, 4)],
        [f'https://www.target.com/c/textured-hair-care/hair-gels/-/N-4rsrfZ3e8i8?type=products&Nao={i * 24}' for i in
         range(0, 4)],
        [f'https://www.target.com/c/textured-hair-care/curl-enhancers/-/N-4rsrfZ1g47h?type=products&Nao={i * 24}' for i
         in range(0, 3)],
        ['https://www.target.com/c/textured-hair-care/co-washes/-/N-4rsrfZao1w6?type=products&Nao=0']]

    for links in category:
        pages.append(links)
    return (pages)


func = num_pages()
# print(func)
newlist = reduce(operator.add, func)

# function to get all the hrefs from each page of the pages in [newList]

for x in newlist:
    driver.get(x)

    browser = scrollDown(driver, 5)
    time.sleep(2)

    browser = scrollDown(driver, 5)
    time.sleep(2)

    browser = scrollDown(driver, 5)
    time.sleep(2)

    browser = scrollDown(driver, 5)
    time.sleep(2)

    browser = scrollDown(driver, 5)
    time.sleep(2)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight= 23452)")  # 23452 - page height
    time.sleep(2)

    get_links = []
    xpath = ('//*[@class="Row-uds8za-0 fMpYji h-padding-t-tight"]')
    elems = driver.find_elements_by_xpath('//*[@data-test="product-title"]')

    for elem in elems:
        href = str(elem.get_attribute('href'))
        get_links.append(href)
        if href is None:
            print(None)

    # print (len(get_links))
    # print(get_links)

    # for each of the hrefs click and get the ingredients, brand and name
    for url in get_links:
        driver.get(url)
        time.sleep(5)

        # brand and Name
        Brand = driver.find_element_by_xpath('//*[@class="Link-sc-1khjl8b-0 gMFbJt"]').text[9:]
        Name = driver.find_element_by_xpath('//*[@data-test="product-title"]').text

        # print (Brand,Name)
        browser = scrollDown(driver, 2)
        time.sleep(5)

        # ingredients
        try:
            Ingredients = driver.find_element_by_xpath('//a[@data-test="tabDrugFacts"]')
            Ingredients.click()
            time.sleep(5)
            Ingredients = driver.find_element_by_xpath("//*[@class='h-text-transform-caps']").text
        except NoSuchElementException:
            Ingredients = 'No Info'
            time.sleep(5)
        df2 = pd.DataFrame([[x, Brand, Name, Ingredients]], columns=['Links', 'Brand', 'Name', 'Ingredients'])
        df = df.append(df2, ignore_index=True)

df.to_csv('textured-hair.csv', encoding='utf-8-sig', index=False)
driver.close()

# %%
