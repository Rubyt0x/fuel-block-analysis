from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.options import Options
import asyncio
from time import sleep


options = Options()
options.headless = True
chrome_driver = webdriver.Chrome(options=options)
chrome_driver.get("https://fuellabs.github.io/block-explorer-v2/beta-3/")
chrome_driver.maximize_window()
sleep(8)

chrome_driver.save_screenshot('hn_homepage.png')
chrome_driver.quit()
