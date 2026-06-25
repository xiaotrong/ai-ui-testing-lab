"""
SauceDemo 商品列表页
"""
from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")
        self.inventory_items = page.locator("[data-test='inventory-item']")
        self.add_to_cart_buttons = page.locator("button:has-text('Add to cart')")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.cart_link = page.locator("[data-test='shopping-cart-link']")

    def add_first_item_to_cart(self):
        self.add_to_cart_buttons.first.click()

    def get_cart_count(self) -> int:
        if self.cart_badge.is_visible():
            return int(self.cart_badge.inner_text())
        return 0

    def go_to_cart(self):
        self.cart_link.click()
