
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time

# Set a "base" URL to append onto
base_url = "https://www.grailed.com/designers/acne-studios"

# open up chrome. Don't use headless otherwise the feed-item doesn't fully load all the way
chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=chrome_options)
driver.get(base_url)
# wait 30 sec
timeout = 30
