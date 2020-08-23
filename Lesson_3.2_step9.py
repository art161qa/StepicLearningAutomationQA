from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome("C:\python\chromedriver.exe")
browser.maximize_window()

try:

    link = 'http://suninjuly.github.io/wait2.html'
    browser.get(link)
    name = 'My name is Artem'

    assert 'login' in browser.current_url, 'Login doee not exist in current url'


finally:
    time.sleep(5)
    browser.quit()