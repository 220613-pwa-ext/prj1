import time
import autoit
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

from pom.login import Login
from pom.reimb_view import ReimbView

c_options = webdriver.ChromeOptions()
c_options.add_argument("start-maximized")

driver = webdriver.Chrome('../../chromedriver.exe', options=c_options)
driver.implicitly_wait(4)
driver.get("http://127.0.0.1:5500/")

login = Login(driver)
reimb = ReimbView(driver)
action_chain = ActionChains(driver)

time.sleep(1)
driver.find_element(By.LINK_TEXT, 'Login').click()

# unsuccessful login attempt
login.get_username_input().send_keys("JohnD80")
time.sleep(2)
login.get_password_input().send_keys("passwor")
time.sleep(2)

# attempt navigate to view reimbursement page
login.get_login_button().click()

time.sleep(2)
driver.quit()
