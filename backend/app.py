from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pandas as pd
import asyncio
from time import sleep


options = Options()
options.headless = True
driver = webdriver.Chrome(options = options, service=ChromeService(ChromeDriverManager().install()))
driver.get("https://fuellabs.github.io/block-explorer-v2/beta-3/")
driver.implicitly_wait(15)

elems = driver.find_elements(by = By.CLASS_NAME, value = 'sc-oZIhv giyXjA')
elem_df = pd.DataFrame(elems)
for elem in elems:
    print(elem)

driver.save_screenshot('hn_homepage.png')
driver.quit()
elem_df.head()
