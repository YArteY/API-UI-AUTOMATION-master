from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class InventoryPage:
    backpack_add_to_cart = (By.ID, 'add-to-cart-sauce-labs-backpack')
    backpack_remove = (By.ID, 'remove-sauce-labs-backpack')
    burger_menu = (By.ID, 'react-burger-menu-btn')
    shopping_cart = (By.CLASS_NAME, 'shopping_cart_link')
    shopping_cart_badge = (By.CLASS_NAME, 'shopping_cart_badge')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_backpack_add_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.backpack_add_to_cart)).click()

    def click_remove_backpack_add_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.backpack_remove)).click()

    def get_cart_badge_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.shopping_cart_badge)).text

    def is_cart_badge_displayed(self):
        # find_elements no lanza excepción si no existe: devuelve [] -> False.
        return len(self.driver.find_elements(*self.shopping_cart_badge)) > 0

    def is_remove_backpack_displayed(self):
        return self.wait.until(EC.visibility_of_element_located(self.backpack_remove)).is_displayed()
