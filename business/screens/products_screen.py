from business.screens import AppiumBy, MobileDriver


class ProductsScreen:

    SCREEN_TITLE = (AppiumBy.XPATH, '//android.widget.TextView[@text="PRODUCTS"]')
    PRODUCTS_CONTAINER = (AppiumBy.ACCESSIBILITY_ID, "test-PRODUCTS")
    CART_BADGE = (AppiumBy.ACCESSIBILITY_ID, "test-Cart")
    CART_BADGE_COUNT = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@content-desc="test-Cart"]//android.widget.TextView',
    )

    def __init__(self, driver: MobileDriver):
        self.driver = driver

    def get_screen_title(self) -> str:
        return self.driver.get_text(self.SCREEN_TITLE)

    def is_cart_icon_visible(self) -> bool:
        return self.driver.is_element_visible(self.CART_BADGE)

    def is_products_catalog_visible(self) -> bool:
        return self.driver.is_element_visible(self.PRODUCTS_CONTAINER)

    def is_products_screen_visible(self) -> bool:
        return self.driver.is_element_visible(self.SCREEN_TITLE)

    def get_cart_badge_count(self) -> str:
        return self.driver.get_text(self.CART_BADGE_COUNT)

    def is_cart_badge_empty(self) -> bool:
        try:
            count = int(self.get_cart_badge_count())
            return count == 0
        except Exception:
            return True

    def go_to_cart(self):
        self.driver.click(self.CART_BADGE)

    def add_product_to_cart(self, product_name: str):
        add_to_cart_button = (
            AppiumBy.XPATH,
            f'//android.widget.TextView[@text="{product_name}"]/../..//android.widget.TextView[@text="ADD TO CART"]',
        )
        self.driver.click(add_to_cart_button)
