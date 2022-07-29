from selenium.webdriver.common.by import By



class HandleReimb:

    def __init__(self, driver):
        self.driver = driver

    def get_filter_select_element(self):
        return self.driver.find_element(By.ID, 'filter')

    def find_first_pending_request_on_pending_filtered_list(self):
        return self.driver.find_element(By.XPATH, '//tbody/tr[1]/td[4]/select[1]')

    def get_logout_btn(self):
        return self.driver.find_element(By.ID, 'login-status')

    def get_my_reimbursement_btn(self):
        return self.driver.find_element(By.ID, 'header3')

