from selenium.webdriver.common.by import By



class ReimbView:

    def __init__(self, driver):
        self.driver = driver

    def get_filter_select_element(self):
        return self.driver.find_element(By.ID, 'filter')

    def get_add_reimbursement(self):
        return self.driver.find_element(By.LINK_TEXT, 'Add Reimbursement')

    def get_amount_input(self):
        return self.driver.find_element(By.ID, 'amount')

    def get_description_input(self):
        return self.driver.find_element(By.ID, 'description')

    def get_category_input(self):
        return self.driver.find_element(By.ID, 'category')

    def get_receipt_input(self):
        return self.driver.find_element(By.ID, 'receipt')

    def get_submit_btn(self):
        return self.driver.find_element(By.ID, 'submit-btn')

    def get_last_receipt_link(self):
        return self.driver.find_element(By.XPATH, '//tr[last()]/td/a')

    def get_logout_btn(self):
        return self.driver.find_element(By.ID, 'login-status')

    def get_handle_reimbursement_btn(self):
        return self.driver.find_element(By.ID, 'header3')

