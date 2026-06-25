"""
SauceDemo 登录页面 — Selenium 版
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.username_input = (By.CSS_SELECTOR, "[data-test='username']")
        self.password_input = (By.CSS_SELECTOR, "[data-test='password']")
        self.login_button = (By.CSS_SELECTOR, "[data-test='login-button']")
        self.error_message = (By.CSS_SELECTOR, "[data-test='error']")

    def login(self, username: str, password: str):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.username_input)).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def get_error_text(self) -> str:
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.error_message)
        ).text
