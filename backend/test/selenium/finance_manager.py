import time
import autoit
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

from pom.handle_reimb import HandleReimb
from pom.login import Login
from pom.reimb_view import ReimbView

c_options = webdriver.ChromeOptions()
c_options.add_argument("start-maximized")

driver = webdriver.Chrome('../../chromedriver.exe', options=c_options)
driver.implicitly_wait(4)
driver.get("http://127.0.0.1:5500/")

login = Login(driver)
reimb = ReimbView(driver)
handle_reimb = HandleReimb(driver)
action_chain = ActionChains(driver)

time.sleep(1)
driver.find_element(By.LINK_TEXT, 'Login').click()

# Successful Login
login.get_username_input().send_keys("valiv9")
time.sleep(1)
login.get_password_input().send_keys("password")
time.sleep(1)

# navigate to view reimbursement page
login.get_login_button().click()

# wait for page to load

# demonstrate filter

filter_element = Select(reimb.get_filter_select_element())
time.sleep(1)
for choice in ("Pending", "Approved", "Denied", "Any Status"):
    filter_element.select_by_visible_text(choice)
    time.sleep(3)

# add reimbursement
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
select_add.select_by_visible_text('Food')
time.sleep(4)

reimb.get_submit_btn().click()
time.sleep(7)

filter_element.select_by_visible_text("Pending")

reimb.get_last_receipt_link().click()
other_tab = driver.window_handles[1]
driver.switch_to.window(other_tab)
time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)

reimb.get_handle_reimbursement_btn().click()

# demonstrate filter

filter_element = Select(handle_reimb.get_filter_select_element())
time.sleep(1)
# for choice in ("Pending", "Approved", "Denied", "Any Status"):
#     filter_element.select_by_visible_text(choice)
#     time.sleep(3)

filter_element.select_by_visible_text("Pending")
time.sleep(3)
handle_first_pending_request = Select(handle_reimb.find_first_pending_request_on_pending_filtered_list())

handle_reimb.find_first_pending_request_on_pending_filtered_list().click()
handle_first_pending_request.select_by_visible_text('Approved')
time.sleep(5)
filter_element.select_by_visible_text("Approved")
time.sleep(3)
filter_element.select_by_visible_text("Pending")
time.sleep(3)
handle_reimb.find_first_pending_request_on_pending_filtered_list().click()
handle_first_pending_request = Select(handle_reimb.find_first_pending_request_on_pending_filtered_list())
handle_first_pending_request.select_by_visible_text('Denied')
time.sleep(3)

filter_element.select_by_visible_text("Denied")
time.sleep(5)

reimb.get_logout_btn().click()

time.sleep(4)
driver.quit()
