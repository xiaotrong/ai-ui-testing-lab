"""
Selenium 项目共享 fixtures
"""
import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")


@pytest.fixture(scope="function")
def driver():
    """每个测试用例独立 driver，用 Chrome"""
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(BASE_URL)
    yield driver
    driver.quit()
