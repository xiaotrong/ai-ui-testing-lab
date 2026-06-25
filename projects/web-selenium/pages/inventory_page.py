"""
SauceDemo 商品列表页 — Selenium 版
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.title = (By.CSS_SELECTOR, ".title")
        self.add_to_cart_buttons = (By.XPATH, "//button[contains(text(),'Add to cart')]")
        self.cart_badge = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
        self.cart_link = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")

    def add_first_item_to_cart(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.add_to_cart_buttons)).click()

    def get_cart_count(self) -> int:
        try:
            badge = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(self.cart_badge)
            )
            return int(badge.text)
        except:
            return 0

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()
