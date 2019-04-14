from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('C:\\Users\\saurabh\\Desktop\\chromedriver.exe')  # give the path of the chrome driver, which need to be download from the googlechromedrivers website as per the os 
browser.get('https://gabrielecirulli.github.io/2048/')
html_elem = browser.find_element_by_tag_name('html')

while True:
    html_elem.send_keys(Keys.UP)
    html_elem.send_keys(Keys.RIGHT)
    html_elem.send_keys(Keys.DOWN)
    html_elem.send_keys(Keys.LEFT)