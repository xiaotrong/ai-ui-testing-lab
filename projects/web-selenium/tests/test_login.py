from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_standard_user_login(driver):
    """标准用户登录成功"""
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    title = driver.find_element(*inventory.title)
    assert title.is_displayed(), "商品列表标题应该可见"


def test_locked_out_user(driver):
    """锁定用户登录失败"""
    login_page = LoginPage(driver)
    login_page.login("locked_out_user", "secret_sauce")

    error = login_page.get_error_text()
    assert "locked out" in error.lower(), f"应该提示账号被锁，实际: {error}"


def test_add_to_cart(driver):
    """加商品到购物车"""
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_first_item_to_cart()

    assert inventory.get_cart_count() == 1, "购物车 badge 应该显示 1"
