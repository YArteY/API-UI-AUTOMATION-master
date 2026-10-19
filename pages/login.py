from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    username_field = (By.ID, 'user-name')
    password_field = (By.ID, 'password')
    login_button = (By.ID, 'login-button')

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        wait_from_input = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.username_field))
        wait_from_input.send_keys(username)

    def set_password(self, password):
        wait_from_input = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.password_field))
        wait_from_input.send_keys(password)

    def get_username(self):
        return self.driver.find_element(*self.username_field).get_property('value')

    def click_login_button(self):
        wait_login_button = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.login_button))
        wait_login_button.click()

    def login(self, username, password):
        """Acción completa de login reutilizable por cualquier fixture o prueba."""
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()
