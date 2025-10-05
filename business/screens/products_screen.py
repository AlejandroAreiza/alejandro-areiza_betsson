from business.screens import AppiumBy, MobileDriver


class ProductsScreen:

    SCREEN_TITLE = (AppiumBy.XPATH, '//android.widget.TextView[@text="PRODUCTS"]')
    PRODUCTS_CONTAINER = (AppiumBy.ACCESSIBILITY_ID, "test-PRODUCTS")
    CART_BADGE = (AppiumBy.ACCESSIBILITY_ID, "test-Cart")

    def __init__(self, driver: MobileDriver):
        self.driver = driver

    def get_screen_title(self) -> str:
        """Get the products screen title text."""
        return self.driver.get_text(self.SCREEN_TITLE)

    def is_cart_icon_visible(self) -> bool:
        """Check if cart icon is visible."""
        return self.driver.is_element_visible(self.CART_BADGE)

    def is_products_catalog_visible(self) -> bool:
        """Check if products catalog container is visible."""
        return self.driver.is_element_visible(self.PRODUCTS_CONTAINER)

    def is_products_screen_visible(self) -> bool:
        """Check if products screen is visible."""
        return self.driver.is_element_visible(self.SCREEN_TITLE)
