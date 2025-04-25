from selenium.webdriver.common.by import By
from .base_page import BasePage

class OrderPage(BasePage):
    SEARCH_INPUT = (By.ID, "searchinput_products")
    PRODUCT = (By.XPATH, "//div[@id='searchResults_products']/div")
    QUANTITY = (By.ID, "quantity")
    ADD_BTN = (By.ID, "add")
    CONFIRM_BTN = (By.ID, "saveOrderBtn")
    
    def create_order(self, product_ref, quantity):
        self.enter_text(self.SEARCH_INPUT, product_ref)
        self.click(self.PRODUCT)
        self.enter_text(self.QUANTITY, str(quantity))
        self.click(self.ADD_BTN)
        self.click(self.CONFIRM_BTN)