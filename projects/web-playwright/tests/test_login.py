from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_standard_user_login(page):
    """标准用户登录成功并看到商品列表"""
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    assert inventory.title.is_visible(), "商品列表标题应该可见"


def test_locked_out_user(page):
    """锁定用户登录失败并显示错误信息"""
    login_page = LoginPage(page)
    login_page.login("locked_out_user", "secret_sauce")

    error = login_page.get_error_text()
    assert "locked out" in error.lower(), f"应该提示账号被锁，实际: {error}"


def test_add_to_cart(page):
    """加商品到购物车，badge 数量更新"""
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.add_first_item_to_cart()

    assert inventory.get_cart_count() == 1, "购物车 badge 应该显示 1"
