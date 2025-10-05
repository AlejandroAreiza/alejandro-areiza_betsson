from business.screens import AppiumBy, MobileDriver


class ProductsScreen:

    SCREEN_TITLE = (AppiumBy.XPATH, '//android.widget.TextView[@text="PRODUCTS"]')
    CART_ICON = (AppiumBy.ACCESSIBILITY_ID, "test-Cart")
    PRODUCTS_CONTAINER = (AppiumBy.ACCESSIBILITY_ID, "test-PRODUCTS")
    CART_BADGE = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Cart"]/android.widget.TextView')

    def __init__(self, driver: MobileDriver):
        self.driver = driver

    def get_screen_title(self) -> str:
        """Get the products screen title text."""
        return self.driver.get_text(self.SCREEN_TITLE)

    def is_cart_icon_visible(self) -> bool:
        """Check if cart icon is visible."""
        return self.driver.is_element_visible(self.CART_ICON)

    def is_products_catalog_visible(self) -> bool:
        """Check if products catalog container is visible."""
        return self.driver.is_element_visible(self.PRODUCTS_CONTAINER)

    def is_products_screen_visible(self) -> bool:
        """Check if products screen is visible."""
        return self.driver.is_element_visible(self.SCREEN_TITLE)
