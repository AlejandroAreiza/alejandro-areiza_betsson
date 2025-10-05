from business.screens import AppiumBy, MobileDriver


class CartScreen:

    SCREEN_TITLE = (AppiumBy.XPATH, '//android.widget.TextView[@text="YOUR CART"]')
    CHECKOUT_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("CHECKOUT"))',
    )
    CART_ITEMS = (AppiumBy.ACCESSIBILITY_ID, "test-Cart Content")

    def __init__(self, driver: MobileDriver):
        self.driver = driver

    def tap_checkout(self):
        self.driver.click(self.CHECKOUT_BUTTON)
