"""
Playwright 项目共享 fixtures — 使用本地 Chrome 浏览器
"""
import os
import pytest
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """使用本地 Chrome 浏览器，不下载 chromium"""
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "locale": "en-US",
    }


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    """使用本地 Chrome channel，headless 模式跑"""
    return {
        **browser_type_launch_args,
        "channel": "chrome",  # 用本地 Chrome
        "headless": True,
    }


@pytest.fixture(scope="session")
def base_url() -> str:
    return BASE_URL


@pytest.fixture(autouse=True)
def _auto_navigate(page, base_url):
    """每个测试自动导航到首页"""
    page.goto(base_url)
    yield
