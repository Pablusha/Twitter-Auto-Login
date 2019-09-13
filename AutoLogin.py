from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import LoginInfo

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://twitter.com/")

login = browser.find_element_by_xpath("//*[@id='doc']/div/div[1]/div[1]/div[2]/div[2]/div/a[2]")
login.click()
time.sleep(3)

username = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input")
password = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input")

username.send_keys(LoginInfo.username)
password.send_keys(LoginInfo.password)

loginButton = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/div[2]/button")
loginButton.click()

time.sleep(10)
browser.close()