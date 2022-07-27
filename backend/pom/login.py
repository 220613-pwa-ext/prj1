from selenium.webdriver.common.by import By


class Login:

    def __init__(self, driver):
        self.driver = driver

    def get_username_input(self):
        return self.driver.find_element(By.XPATH, "//input")

    def get_password_input(self):
        return self.driver.find_element(By.XPATH, "(//input)[2]")

    def get_login_button(self):
        return self.driver.find_element(By.XPATH, "//button")
