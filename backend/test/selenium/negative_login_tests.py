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

login.get_username_input().send_keys("JohnD80")
time.sleep(2)
login.get_password_input().send_keys("password")
time.sleep(2)
login.get_login_button().click()
# demonstrate filter
time.sleep(2)
# add reimbursement without amount
reimb.get_add_reimbursement().click()
time.sleep(1)
#reimb.get_amount_input().send_keys('50')
time.sleep(2)
reimb.get_description_input().send_keys('Lunch - Bond with new team member')
time.sleep(2)
file = reimb.get_receipt_input()


# use autoit - install -  pip install pyautoit
action_chain.move_to_element(file).click().perform()
time.sleep(2)
handle = "[CLASS:#32770; TITLE:Open]"
autoit.win_wait(handle, 60)
autoit.control_set_text(handle, "Edit1", "C:\\Users\\Valentin\\Downloads\\receipt2.jpeg")
autoit.control_click(handle, "Button1")
time.sleep(4)
select_add = Select(reimb.get_category_input())
select_add.select_by_visible_text('Food')
time.sleep(4)

reimb.get_submit_btn().click()
time.sleep(7)
driver.find_element(By.ID, 'cancel-btn').click()


# add reimbursement without description
reimb.get_add_reimbursement().click()
time.sleep(1)
reimb.get_amount_input().send_keys('50')
time.sleep(2)
# reimb.get_description_input().send_keys('Lunch - Bond with new team member')
time.sleep(2)
file = reimb.get_receipt_input()


# use autoit - install -  pip install pyautoit
action_chain.move_to_element(file).click().perform()
time.sleep(2)
handle = "[CLASS:#32770; TITLE:Open]"
autoit.win_wait(handle, 60)
autoit.control_set_text(handle, "Edit1", "C:\\Users\\Valentin\\Downloads\\receipt2.jpeg")
autoit.control_click(handle, "Button1")
time.sleep(4)
select_add = Select(reimb.get_category_input())
select_add.select_by_visible_text('Food')
time.sleep(4)

reimb.get_submit_btn().click()
time.sleep(7)
driver.find_element(By.ID, 'cancel-btn').click()


# add reimbursement without choosing a category
reimb.get_add_reimbursement().click()
time.sleep(1)
reimb.get_amount_input().send_keys('50')
time.sleep(2)
reimb.get_description_input().send_keys('Lunch - Bond with new team member')
time.sleep(2)
file = reimb.get_receipt_input()


# use autoit - install -  pip install pyautoit
action_chain.move_to_element(file).click().perform()
time.sleep(2)
handle = "[CLASS:#32770; TITLE:Open]"
autoit.win_wait(handle, 60)
autoit.control_set_text(handle, "Edit1", "C:\\Users\\Valentin\\Downloads\\receipt2.jpeg")
autoit.control_click(handle, "Button1")
time.sleep(4)
select_add = Select(reimb.get_category_input())
# select_add.select_by_visible_text('Food')
time.sleep(4)

reimb.get_submit_btn().click()
time.sleep(7)
driver.find_element(By.ID, 'cancel-btn').click()

# add reimbursement without loading a file
reimb.get_add_reimbursement().click()
time.sleep(1)
reimb.get_amount_input().send_keys('50')
time.sleep(2)
reimb.get_description_input().send_keys('Lunch - Bond with new team member')
time.sleep(2)
file = reimb.get_receipt_input()


# use autoit - install -  pip install pyautoit
#action_chain.move_to_element(file).click().perform()
time.sleep(2)
handle = "[CLASS:#32770; TITLE:Open]"
autoit.win_wait(handle, 60)
autoit.control_set_text(handle, "Edit1", "C:\\Users\\Valentin\\Downloads\\receipt2.jpeg")
autoit.control_click(handle, "Button1")
time.sleep(4)
select_add = Select(reimb.get_category_input())
select_add.select_by_visible_text('Food')
time.sleep(4)

reimb.get_submit_btn().click()
time.sleep(7)
driver.find_element(By.ID, 'cancel-btn').click()


time.sleep(4)
driver.quit()
