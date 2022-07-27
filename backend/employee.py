import time
import autoit
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

from pom.login import Login

c_options = webdriver.ChromeOptions()
c_options.add_argument("start-maximized")

driver = webdriver.Chrome('./chromedriver.exe', options=c_options)
driver.implicitly_wait(4)
driver.get("http://127.0.0.1:5500/")

login = Login(driver)
action_chain = ActionChains(driver)

time.sleep(1)
driver.find_element(By.LINK_TEXT, 'Login').click()

# Successful Login
login.get_username_input().send_keys("JohnD80")
time.sleep(1)
login.get_password_input().send_keys("password")
time.sleep(1)

# navigate to view reimbursement page
login.get_login_button().click()

# wait for page to load

# demonstrate filter

filter_element = Select(driver.find_element(By.ID, 'filter'))
time.sleep(1)
for choice in ("Pending", "Approved", "Denied", "Any Status"):
    filter_element.select_by_visible_text(choice)
    time.sleep(3)

# add reimbursement
driver.find_element(By.LINK_TEXT, 'Add Reimbursement').click()
time.sleep(1)
driver.find_element(By.ID, 'amount').send_keys('50')
time.sleep(2)
driver.find_element(By.ID, 'description').send_keys('Lunch - Bond with new team member')
time.sleep(2)
file = driver.find_element(By.ID, 'receipt')


# use autoit - install -  pip install pyautoit
action_chain.move_to_element(file).click().perform()
time.sleep(2)
handle = "[CLASS:#32770; TITLE:Open]"
autoit.win_wait(handle, 60)
autoit.control_set_text(handle, "Edit1", "C:\\Users\\Valentin\\Downloads\\receipt2.jpeg")
autoit.control_click(handle, "Button1")
time.sleep(4)
select_add = Select(driver.find_element(By.ID, 'category'))
select_add.select_by_visible_text('Food')
time.sleep(4)

driver.find_element(By.ID, 'submit-btn').click()
time.sleep(7)

filter_element.select_by_visible_text("Pending")

driver.find_element(By.XPATH, '//tr[last()]/td/a').click()
other_tab = driver.window_handles[1]
driver.switch_to.window(other_tab)
time.sleep(10)
driver.switch_to.window(driver.window_handles[0])

time.sleep(10)
driver.quit()
